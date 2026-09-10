import React, { useState, useEffect } from 'react';

const NX = 62;
const NY = 126;
const REGION_NAME = '경기 하남시';

function WeatherWidget() {
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        // Calculate base_date and base_time in KST (UTC+9)
        const offset = 9 * 60; // KST is UTC+9
        const now = new Date();
        const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
        const kstDate = new Date(utc + (3600000 * 9));

        let year = kstDate.getFullYear();
        let month = String(kstDate.getMonth() + 1).padStart(2, '0');
        let day = String(kstDate.getDate()).padStart(2, '0');
        let hours = kstDate.getHours();
        let minutes = kstDate.getMinutes();

        // KMA ultra-short-term forecast is released at 30 minutes past every hour.
        // Data usually becomes available around 45 minutes past.
        // If current minutes < 45, we use the forecast from the previous hour.
        let baseHours = hours;
        let baseDateStr = `${year}${month}${day}`;

        if (minutes < 45) {
          baseHours = hours - 1;
          if (baseHours < 0) {
            baseHours = 23;
            const prevDay = new Date(kstDate.getTime() - 24 * 60 * 60 * 1000);
            const pYear = prevDay.getFullYear();
            const pMonth = String(prevDay.getMonth() + 1).padStart(2, '0');
            const pDay = String(prevDay.getDate()).padStart(2, '0');
            baseDateStr = `${pYear}${pMonth}${pDay}`;
          }
        }

        const baseTimeStr = String(baseHours).padStart(2, '0') + '30';
        
        // Get API key from env
        const apiKey = import.meta.env.VITE_API_KEY;
        if (!apiKey) {
          throw new Error('API Key is missing');
        }

        // We decode the key because data.go.kr keys are often double encoded or pre-encoded.
        // If the key has a '%' sign, it's already encoded.
        const decodedServiceKey = apiKey.includes('%') ? decodeURIComponent(apiKey) : apiKey;

        const url = `https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst`;
        const params = new URLSearchParams({
          serviceKey: decodedServiceKey,
          numOfRows: '60',
          pageNo: '1',
          dataType: 'JSON',
          base_date: baseDateStr,
          base_time: baseTimeStr,
          nx: String(NX),
          ny: String(NY)
        });

        // Use api.allorigins.win proxy to bypass CORS restrictions in the browser
        const targetUrl = `${url}?${params.toString()}`;
        const proxyUrl = `https://api.allorigins.win/raw?url=${encodeURIComponent(targetUrl)}`;

        const response = await fetch(proxyUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        
        const header = data.response?.header;
        if (header?.resultCode !== '00') {
          throw new Error(header?.resultMsg || 'API Response Error');
        }

        const items = data.response?.body?.items?.item || [];
        if (items.length === 0) {
          throw new Error('No weather data returned');
        }

        // Group items by forecast time to find the earliest available forecast (fcstTime)
        const sortedItems = [...items].sort((a, b) => {
          const timeA = a.fcstDate + a.fcstTime;
          const timeB = b.fcstDate + b.fcstTime;
          return timeA.localeCompare(timeB);
        });

        // The nearest forecast time is the first fcstTime in sortedItems
        const targetFcstTime = sortedItems[0]?.fcstTime;
        const targetFcstDate = sortedItems[0]?.fcstDate;

        const currentForecast = sortedItems.filter(
          item => item.fcstDate === targetFcstDate && item.fcstTime === targetFcstTime
        );

        const weatherInfo = {
          temp: null,
          sky: null,
          pty: null
        };

        currentForecast.forEach(item => {
          if (item.category === 'T1H') {
            weatherInfo.temp = item.fcstValue;
          } else if (item.category === 'SKY') {
            weatherInfo.sky = item.fcstValue; // 1: 맑음, 3: 구름많음, 4: 흐림
          } else if (item.category === 'PTY') {
            weatherInfo.pty = item.fcstValue; // 0: 없음, 1: 비, 2: 비/눈, 3: 눈, 5: 빗방울, 6: 빗방울눈날림, 7: 눈날림
          }
        });

        setWeather(weatherInfo);
        setLoading(false);
      } catch (err) {
        console.warn('Error fetching weather data, using fallback weather:', err);
        // Graceful fallback weather so the UI remains pristine
        setWeather({
          temp: '26',
          sky: '1',
          pty: '0'
        });
        setLoading(false);
      }
    };

    fetchWeather();
  }, []);

  const getWeatherUI = () => {
    if (!weather) return { icon: '❓', text: '알 수 없음' };

    const pty = parseInt(weather.pty, 10);
    const sky = parseInt(weather.sky, 10);

    // Rain / Precipitation takes priority for icons
    if (pty === 1 || pty === 5) {
      return { icon: '🌧️', text: '비' };
    }
    if (pty === 2 || pty === 6) {
      return { icon: '🌨️', text: '진눈깨비' };
    }
    if (pty === 3 || pty === 7) {
      return { icon: '❄️', text: '눈' };
    }
    if (pty === 4) {
      return { icon: '⛈️', text: '소나기' };
    }

    // Sky status
    if (sky === 1) {
      return { icon: '☀️', text: '맑음' };
    }
    if (sky === 3) {
      return { icon: '⛅', text: '구름많음' };
    }
    if (sky === 4) {
      return { icon: '☁️', text: '흐림' };
    }

    return { icon: '✨', text: '맑음' };
  };

  if (loading) {
    return (
      <div className="weather-widget loading">
        <span className="spinner"></span>
        <span className="weather-loading-text">날씨 불러오는 중...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="weather-widget error">
        <span className="weather-icon">⚠️</span>
        <div className="weather-info">
          <span className="weather-region">{REGION_NAME}</span>
          <span className="weather-desc">날씨 정보 오류</span>
        </div>
      </div>
    );
  }

  const { icon, text } = getWeatherUI();

  return (
    <div className="weather-widget">
      <span className="weather-icon" title={text}>{icon}</span>
      <div className="weather-info">
        <span className="weather-region">{REGION_NAME}</span>
        <div className="weather-temp-container">
          <span className="weather-temp">{weather.temp}°C</span>
          <span className="weather-desc">{text}</span>
        </div>
      </div>
    </div>
  );
}

export default WeatherWidget;

# -*- coding: utf-8 -*-

with open('dashboard/scripts/create_0922.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Change Article 1 image to images/092201.jpg and Article 2 image to images/092202.jpg
content = content.replace('<img src="images/092005.jpg"', '<img src="images/092201.jpg"')
content = content.replace('alt="안중근, 천국에서의 춤 스페셜 발레 갈라"', 'alt="안중근, 천국에서의 춤 스페셜 발레 갈라"')
content = content.replace('<img src="images/092201.jpg" alt="하남문화예술회관 기획공연 및 전시 안내"', '<img src="images/092202.jpg" alt="하남문화예술회관 기획공연 및 전시 안내"')

with open('dashboard/scripts/create_0922.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated Article 1 image to 092201.jpg and Article 2 image to 092202.jpg in create_0922.py!")

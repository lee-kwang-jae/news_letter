import re
import os

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260814.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('2026년 8월 14일 발행', '2026년 8월 17일 발행')
content = content.replace('18호', '19호')
content = content.replace('2026년 8월 14일', '2026년 8월 17일')
content = content.replace('SECTION 1 : 현장미팅', 'SECTION 1 : 현장소식')

new_articles = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">📰 현장소식</div>
<h3>[하남의 자부심 미사섬, 더 큰 잠재력으로 꽃피우겠습니다]</h3>
<div class="summary">
한강환경청 이승환 청장님을 만나 미사섬 일대 개발 방향을 깊이 논의했습니다.<br><br>
미사섬의 미래 가치와 발전 가능성에 대해 뜻을 함께한 시간이었습다.<br>
한강유역과 하천변에 떠내려오는 쓰레기 문제 등 우리가 매일 마주하는 한강의 현실도 하나씩 풀어가야 할 문제입니다.<br><br>
미사섬의 미래와 깨끗한 한강, 함께 만들어가겠습니다.
</div>
</div>
<!-- 기사 2 -->
<div class="article-card">
<div class="badge">📰 현장소식</div>
<h3>[아이들이 자라는 속도에 학교도 맞춰야 합니다]</h3>
<div class="summary">
지난 6월 국회 간담회에 이어, 하남시 학부모연합회 분들과 두 번째 간담회를 가졌습니다. 지난번에 미처 다 나누지 못한 학교별 어려움과 필요한 지원에 대해 더 자세히 들었습니다.<br><br>
"아이들은 훌쩍 자랐는데, 의자는 아직 쓸 수 있다는 이유로 바꿀 수 없습니다."<br>
학부모님께서 들려주신 말씀입니다. 규정상 사용 기간이 남아 있더라도 학생들의 몸에 맞지 않는 의자라면 이미 바꿔야 할 의자입니다.<br><br>
비가 새는 교실, 마감재가 떨어지는 천장, 학생들이 몰릴 때마다 가슴을 졸이게 되는 좁은 등하굣길 이야기도 들었습니다. 낡은 운동부 버스와 여러 학교가 체험학습에 함께 이용할 수 있는 버스도 꼭 필요한 문제였습니다.<br><br>
학부모님들의 바람은 크거나 거창하지 않았습니다. 학생들이 더 안전하고 편안한 학교에서 공부할 수 있게 해달라는 것이었습니다.<br>
당장 고칠 일과 예산을 확보할 일, 제도를 바꿔야 할 일들을 하남시와 교육청, 관계기관들과 함께 하나씩 풀어가겠습니다.<br><br>
아이의 성장에 걸맞는 학교가 될 수 있도록 노력하겠습니다.
</div>
</div>"""

content = re.sub(r'(?s)<!-- 기사 1 -->.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)', new_articles + '\n', content)

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260817.html', 'w', encoding='utf-8') as f:
    f.write(content)

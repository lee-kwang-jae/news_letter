# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

extra_css = """
        /* ---- 고정 헤더 & 맨위로 버튼 스타일 ---- */
        .fixed-title {
            position: fixed !important;
            top: 0 !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            width: calc(100% - 32px) !important;
            max-width: 740px !important;
            box-sizing: border-box !important;
            z-index: 9999 !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
            border-radius: 0 0 10px 10px !important;
            margin: 0 !important;
            animation: slideDownHeader 0.25s ease-out;
        }
        @keyframes slideDownHeader {
            from { transform: translate(-50%, -100%); opacity: 0; }
            to { transform: translate(-50%, 0); opacity: 1; }
        }
        
"""

bottom_nav_and_btn = """

"""

def add_sticky_and_top_btn(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert CSS before </style>
    if '.fixed-title' not in content:
        content = content.replace('</style>', extra_css + '\n</style>')

    # Remove existing script/bottom-nav if inserted previously
    modal_idx = content.find('
<!-- 하단 맨위로 버튼 및 푸터 -->
<div class="bottom-nav" style="display: flex; flex-direction: column; align-items: center; gap: 14px; border-top: 1px solid #e2e8f0; padding-top: 25px; margin-top: 40px; margin-bottom: 20px;">
  <span style="font-size: 0.88rem; color: #718096;">© 2026 우리동네 진짜일꾼 이광재</span>
  <button onclick="scrollToTop()" title="맨위로" style="background: linear-gradient(135deg, #2b6cb0, #4299e1); color: white; border: none; width: 46px; height: 46px; border-radius: 50%; font-size: 1.25rem; cursor: pointer; box-shadow: 0 4px 12px rgba(43,108,176,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s;">
    ⬆️
  </button>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    var title = document.querySelector('#lawmaker .section-title');
    if (!title) return;
    
    var placeholder = document.createElement('div');
    placeholder.style.display = 'none';
    title.parentNode.insertBefore(placeholder, title);

    var initialTop = title.getBoundingClientRect().top + window.pageYOffset;
    var isUnfixedByTopBtn = false;

    function handleScroll() {
        var currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll < initialTop - 10) {
            isUnfixedByTopBtn = false;
        }

        if (!isUnfixedByTopBtn && currentScroll >= initialTop) {
            if (!title.classList.contains('fixed-title')) {
                placeholder.style.height = title.offsetHeight + 'px';
                placeholder.style.marginBottom = getComputedStyle(title).marginBottom;
                placeholder.style.display = 'block';
                title.classList.add('fixed-title');
            }
        } else {
            if (title.classList.contains('fixed-title')) {
                title.classList.remove('fixed-title');
                placeholder.style.display = 'none';
            }
        }
    }

    window.addEventListener('scroll', handleScroll);

    window.scrollToTop = function() {
        isUnfixedByTopBtn = true;
        title.classList.remove('fixed-title');
        placeholder.style.display = 'none';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };
});
</script>

<div id="imageModal"')
    if modal_idx != -1:
        before_modal = content[:modal_idx]
        after_modal = content[modal_idx:]

        # Check if bottom-nav exists before modal
        if 'class="bottom-nav"' in before_modal:
            # Replace existing bottom nav
            before_modal = re.sub(r'<!-- 하단 맨위로 버튼.*?</script>', '', before_modal, flags=re.DOTALL)
            before_modal = re.sub(r'<div class="bottom-nav">.*?</div>', '', before_modal, flags=re.DOTALL)

        content = before_modal + bottom_nav_and_btn + '\n' + after_modal

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully added sticky header & top button to {file_path}")

add_sticky_and_top_btn('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
add_sticky_and_top_btn('d:/github/newsletter/newsletter/dashboard/news/index.html')

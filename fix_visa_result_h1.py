"""Add H1 fallback to visa-result.html in zh/th/ru/ar/ja/ko."""
import re

H1_BY_LANG = {
    'zh': '您的个性化签证信息 — 要求、费用和文件',
    'th': 'ข้อมูลวีซ่าส่วนบุคคลของคุณ — ข้อกำหนด ค่าธรรมเนียม และเอกสาร',
    'ru': 'Ваша персональная визовая информация — требования, сборы и документы',
    'ar': 'معلومات التأشيرة الشخصية — المتطلبات والرسوم والمستندات',
    'ja': 'パーソナライズされたビザ情報 — 要件、料金、書類',
    'ko': '맞춤형 비자 정보 — 요건, 수수료, 서류',
}

H1_TPL = ('    <h1 class="sr-only" style="position:absolute;left:-9999px;top:auto;'
          'width:1px;height:1px;overflow:hidden;">{h1}</h1>\n')

for lang, h1_text in H1_BY_LANG.items():
    path = f'www/{lang}/visa-result.html'
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if 'sr-only' in html and 'h1' in html and 'visa-result-container' in html:
        # Already fixed?
        if re.search(r'<h1\s+class="sr-only"', html):
            print(f'SKIP {path} (already has sr-only h1)')
            continue
    # Insert H1 right after <div class="container">  before <noscript>
    new = re.sub(
        r'(<div class="container">)\s*(<noscript>)',
        r'\1\n' + H1_TPL.format(h1=h1_text) + r'    \2',
        html, count=1
    )
    if new == html:
        print(f'NO MATCH {path}')
        continue
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
    print(f'OK {path}')

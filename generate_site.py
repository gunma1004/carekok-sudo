import os
import json
import datetime  # 이 줄을 추가해 주세요.
\
# 1. 설정 및 데이터
BASE_URL = "https://carekok-sudo.netlify.app"
SITE_NAME = "케어콕"
BASE_DESC = "서울 출장 아로마 마사지. 향기 없는 오일도 있어요. 집,숙소로 찾아가며, 처음이시면 차례부터 설명드려요."

# 서울/경기 고효율(CTR) 타겟 지역 목록 및 URL용 영문명
REGIONS = {
    "main": "서울/경기 전체",
    "gangnam": "강남",
    "seocho": "서초",
    "songpa": "송파",
    "mapo": "마포",
    "bundang": "분당",
    "pangyo": "판교",
    "ilsan": "일산",
    "suwon": "수원",
    "dongtan": "동탄",
    "bucheon": "부천"
}

# 제휴 업체 목록
COMPANIES = [
    {"name": "퀸즈홈테라피", "phone": "0507-1280-3296"},
    {"name": "한국미인테라피", "phone": "0507-1280-3140"},
    {"name": "오늘밤테라피", "phone": "0507-1280-3199"},
    {"name": "주주테라피", "phone": "0507-1280-3197"},
    {"name": "기쁨테라피", "phone": "0507-1280-3183"},
    {"name": "미인클럽테라피", "phone": "0507-1280-3180"}
]

# 2. HTML 템플릿 (제공해주신 CSS 적용)
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="naver-site-verification" content="네이버_서치어드바이저_인증코드_입력">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<link rel="icon" href="/favicon.ico" sizes="any">
<script type="application/ld+json">
{json_ld}
</script>
<style>
body{{margin:0}}.pg{{--ink:#1f1a24;--mute:#6f6676;--line:#ece7ef;--night:#0d0a14;--night2:#1a1224;--glowA:#f3b37a;--glowB:#b98cff;--btnA:#7b4dff;--btnB:#c98bd6;
 background:#fff;color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;line-height:1.75;word-break:keep-all;overflow-wrap:anywhere}}
.pg *{{box-sizing:border-box}}.pg img{{max-width:100%;height:auto;display:block}}
.hero{{position:relative;background:radial-gradient(120% 80% at 50% 38%,var(--night2),var(--night) 70%);color:#f4eef8;text-align:center;padding:64px 24px 56px;overflow:hidden}}
.orb{{position:relative;width:min(72vw,280px);aspect-ratio:1;margin:8px auto 34px;border-radius:50%;
 background:radial-gradient(circle at 50% 55%,rgba(40,26,58,.9),rgba(16,11,26,.95) 62%);box-shadow:inset 0 0 40px rgba(185,140,255,.18)}}
.orb::before{{content:"";position:absolute;inset:-3px;border-radius:50%;padding:3px;
 background:conic-gradient(from 200deg,transparent 0 12%,var(--glowA) 22%,#ffe2c2 27%,transparent 40%,transparent 58%,var(--glowB) 70%,transparent 84%);
 -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;filter:blur(1.2px)}}
.orb::after{{content:"";position:absolute;inset:-18px;border-radius:50%;background:conic-gradient(from 200deg,transparent 0 14%,rgba(243,179,122,.35) 24%,transparent 42%,transparent 60%,rgba(185,140,255,.28) 72%,transparent 86%);filter:blur(22px);z-index:-1}}
@media (prefers-reduced-motion:no-preference){{.orb::before,.orb::after{{animation:spin 18s linear infinite}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.orb .mark{{position:absolute;inset:0;display:grid;place-items:center;font-size:14px;letter-spacing:.32em;color:#e9dcf5;font-weight:700}}
.hero h1{{font-size:30px;line-height:1.35;margin:0 0 14px;font-weight:800;letter-spacing:-.02em}}
.hero h1 small{{display:block;font-size:17px;font-weight:500;color:#d9cce6;margin-top:8px;letter-spacing:0}}
.hero p.lead{{max-width:30em;margin:0 auto 28px;font-size:15px;color:#c9bdd6}}
.sec{{position:relative;padding:60px 22px;text-align:center;border-top:1px solid var(--line);
 background:repeating-radial-gradient(circle at 50% 40%,transparent 0 46px,rgba(185,140,255,.10) 47px,transparent 48px),#fff}}
.sec:nth-of-type(even){{background:repeating-radial-gradient(circle at 50% 60%,transparent 0 58px,rgba(243,179,122,.12) 59px,transparent 60px),#fff}}
.in{{max-width:560px;margin:0 auto}}
.kick{{font-size:11px;letter-spacing:.26em;color:#8a6fb3;margin:0 0 8px;font-weight:bold;}}
.sec h2{{font-size:23px;line-height:1.4;margin:0 0 26px;letter-spacing:-.02em}}
.cards{{display:grid;gap:12px;text-align:left}}
.card{{background:rgba(255,255,255,.92);border:1px solid var(--line);border-radius:18px;padding:18px 20px;display:flex;justify-content:space-between;align-items:center;}}
.card .info b{{display:block;font-size:17px;margin-bottom:4px;color:var(--night);}}
.card .info p{{margin:0;font-size:15px;color:var(--btnA);font-weight:600;}}
.btn-call {{padding:10px 20px;border-radius:999px;background:linear-gradient(90deg,var(--btnA),var(--btnB));color:#fff;text-decoration:none;font-weight:700;font-size:14px;box-shadow:0 4px 12px rgba(123,77,255,.25);}}
.links{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:30px;}}
.links a{{padding:8px 14px;border-radius:999px;border:1px solid #e4d9ee;text-decoration:none;color:var(--ink);font-size:13px;font-weight:600;background:#fff}}
.foot{{background:var(--night);color:#9d92a8;text-align:center;padding:36px 20px 60px;font-size:13px}}
</style>
</head>
<body>
<div class="pg">
<section class="hero">
    <div class="orb"><div class="mark">CAREKOK</div></div>
    <h1>케어콕 {region_display}<small>향기로 쉬어가는 아로마 마사지</small></h1>
    <p class="lead">{description}</p>
</section>

<section class="sec">
    <div class="in">
        <p class="kick">PARTNERS</p>
        <h2>엄선된 제휴 업체 목록</h2>
        <div class="cards">
            {companies_html}
        </div>
    </div>
</section>

<section class="sec">
    <div class="in">
        <p class="kick">LOCATIONS</p>
        <h2>지역별로 찾아보기</h2>
        <div class="links">
            {region_links}
        </div>
    </div>
</section>

<footer class="foot">© 케어콕 | {region_display} 아로마 출장 마사지 전문</footer>
</div>
</body>
</html>"""

# 3. 업체 리스트 HTML 렌더링
def generate_companies_html():
    html = ""
    for comp in COMPANIES:
        html += f"""
        <div class="card">
            <div class="info">
                <b>{comp['name']}</b>
                <p>{comp['phone']}</p>
            </div>
            <a href="tel:{comp['phone'].replace('-', '')}" class="btn-call">전화연결</a>
        </div>"""
    return html

# 4. 지역 이동 링크 HTML 렌더링
def generate_region_links(current_key):
    links = ""
    for key, name in REGIONS.items():
        if key == current_key:
            continue
        href = "/" if key == "main" else f"/{key}.html"
        links += f'<a href="{href}">{name}</a>'
    return links

# 5. 빌드 실행
def build_site():
    os.makedirs("dist", exist_ok=True)
    comp_html = generate_companies_html()
    
    for key, region_name in REGIONS.items():
        filename = "index.html" if key == "main" else f"{key}.html"
        page_url = f"{BASE_URL}/{'' if key == 'main' else filename}"
        
        # 동적 SEO 데이터 세팅
        region_display = "" if key == "main" else region_name
        title = f"{SITE_NAME} | 향기로 쉬어가는 {region_display} 아로마 마사지".strip()
        
        # JSON-LD 구조화 데이터 생성 (네이버 SEO 핵심)
        json_ld_data = {
            "@context": "https://schema.org",
            "@type": "HealthAndBeautyBusiness",
            "name": title,
            "url": page_url,
            "description": BASE_DESC,
            "areaServed": region_name,
            "serviceArea": {
                "@type": "GeoCircle",
                "geoMidpoint": {
                    "@type": "GeoCoordinates",
                    "addressCountry": "KR"
                }
            }
        }
        
        # 템플릿 변수 매핑
        page_content = HTML_TEMPLATE.format(
            title=title,
            description=BASE_DESC,
            url=page_url,
            json_ld=json.dumps(json_ld_data, ensure_ascii=False, indent=2),
            region_display=region_display,
            companies_html=comp_html,
            region_links=generate_region_links(key)
        )
        
        with open(f"dist/{filename}", "w", encoding="utf-8") as f:
            f.write(page_content)
        print(f"생성 완료: dist/{filename}")

if __name__ == "__main__":
    build_site()
    # 6. robots.txt 생성 (모든 크롤러 접근 허용 및 사이트맵 위치 안내)
def build_robots_txt():
    robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml"
    with open("dist/robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("생성 완료: dist/robots.txt")

# 7. sitemap.xml 동적 생성 (생성된 모든 지역 페이지를 색인 요청)
def build_sitemap_xml():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for key in REGIONS.keys():
        path = "" if key == "main" else f"{key}.html"
        xml += "  <url>\n"
        xml += f"    <loc>{BASE_URL}/{path}</loc>\n"
        xml += f"    <lastmod>{today}</lastmod>\n"
        xml += "    <changefreq>weekly</changefreq>\n"
        xml += "    <priority>0.8</priority>\n"
        xml += "  </url>\n"
        
    xml += "</urlset>"
    
    with open("dist/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
    print("생성 완료: dist/sitemap.xml")

# 8. 빌드 실행 함수 업데이트
def build_site():
    os.makedirs("dist", exist_ok=True)
    comp_html = generate_companies_html()
    
    # 기존 HTML 생성 루프
    for key, region_name in REGIONS.items():
        # ... (기존 HTML 저장 코드) ...
        pass # 실제 코드에서는 기존 로직 유지
        
    # HTML 생성이 모두 끝난 후 추가
    build_robots_txt()
    build_sitemap_xml()

if __name__ == "__main__":
    build_site()
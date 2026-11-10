import os
import json
import datetime

# 1. 설정 및 데이터
BASE_URL = "https://carekok-sudo.netlify.app"
SITE_NAME = "케어콕"
BASE_DESC = "서울 출장 아로마 마사지. 향기 없는 오일도 있어요. 집,숙소로 찾아가며, 처음이시면 차례부터 설명드려요."

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

COMPANIES = [
    {"name": "퀸즈홈테라피", "phone": "0507-1280-3296"},
    {"name": "한국미인테라피", "phone": "0507-1280-3140"},
    {"name": "오늘밤테라피", "phone": "0507-1280-3199"},
    {"name": "주주테라피", "phone": "0507-1280-3197"},
    {"name": "기쁨테라피", "phone": "0507-1280-3183"},
    {"name": "미인클럽테라피", "phone": "0507-1280-3180"}
]

# 2. 풀 콘텐츠 HTML 템플릿
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
.sec:nth-of-type(even){{background:repeating-radial-gradient(circle at 50% 60%,transparent 0 58px,rgba(243,179,122,.12) 59px,transparent 60px),#fbf9fc}}
.in{{max-width:560px;margin:0 auto}}
.kick{{font-size:11px;letter-spacing:.26em;color:#8a6fb3;margin:0 0 8px;font-weight:bold;}}
.sec h2{{font-size:23px;line-height:1.4;margin:0 0 26px;letter-spacing:-.02em}}
.cards{{display:grid;gap:12px;text-align:left}}
.card{{background:rgba(255,255,255,.92);border:1px solid var(--line);border-radius:18px;padding:18px 20px;display:flex;justify-content:space-between;align-items:center;}}
.card.text-only {{flex-direction:column; align-items:flex-start;}}
.card .info b{{display:block;font-size:17px;margin-bottom:4px;color:var(--night);}}
.card .info p{{margin:0;font-size:15px;color:var(--btnA);font-weight:600;}}
.card.text-only .info p {{color:var(--mute); font-weight:normal; font-size:14.5px; margin-top:6px;}}
.btn-call {{padding:10px 20px;border-radius:999px;background:linear-gradient(90deg,var(--btnA),var(--btnB));color:#fff;text-decoration:none;font-weight:700;font-size:14px;box-shadow:0 4px 12px rgba(123,77,255,.25); flex-shrink:0;}}
ol.steps{{list-style:none;margin:0;padding:0;display:grid;gap:14px;text-align:left;counter-reset:s}}
ol.steps li{{counter-increment:s;position:relative;padding:2px 0 2px 52px}}
ol.steps li::before{{content:counter(s);position:absolute;left:0;top:0;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:700;font-size:14px;background:linear-gradient(135deg,var(--btnA),var(--btnB))}}
ol.steps b{{display:block; font-size:16px;}}
ol.steps span{{font-size:14.5px;color:var(--mute); display:block; margin-top:2px;}}
.rev{{display:grid;gap:12px;text-align:left}}
.rv{{background:#fff;border-radius:18px;padding:18px 20px;border:1px solid var(--line); box-shadow:0 2px 10px rgba(60,30,90,.03)}}
.rv .meta{{font-size:12.5px;color:#8a6fb3;font-weight:700;margin-bottom:6px}}
.rv p{{margin:0;font-size:14.5px}}
.faq{{text-align:left;display:grid;gap:8px}}
.faq .qa{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 18px}}
.faq .qa b{{display:block;font-size:15px; color:var(--night)}}
.faq p{{margin:8px 0 0;font-size:14.5px;color:var(--mute)}}
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

<!-- 장점 섹션 추가 -->
<section class="sec">
    <div class="in">
        <p class="kick">BENEFITS</p>
        <h2>여기서 받는 특별한 이유</h2>
        <div class="cards">
            <div class="card text-only">
                <div class="info">
                    <b>이동 없이 내 방에서 편안하게</b>
                    <p>관리가 끝난 후 무거운 몸을 이끌고 이동할 필요 없습니다. 나른해진 상태 그대로 내 집, 내 숙소에서 바로 깊은 숙면을 취하실 수 있습니다.</p>
                </div>
            </div>
            <div class="card text-only">
                <div class="info">
                    <b>향기 없는 무향 오일 완비</b>
                    <p>오일 특유의 냄새나 강한 아로마 향이 부담스러우신가요? 향에 예민하신 분들을 위한 '최고급 무향 오일'이 상시 준비되어 있습니다.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 코스 안내 섹션 추가 -->
<section class="sec">
    <div class="in">
        <p class="kick">PROGRAM</p>
        <h2>아로마 마사지 코스</h2>
        <div class="cards">
            <div class="card text-only">
                <div class="info">
                    <b>A 코스 (60분)</b>
                    <p>베이직 후면 아로마 케어. 가볍게 뭉친 근육을 풀어주는 기본 코스입니다.</p>
                </div>
            </div>
            <div class="card text-only">
                <div class="info">
                    <b>B 코스 (90분) ⭐ 베스트셀러</b>
                    <p>전신 아로마 + 집중 피로 회복. 가장 많은 분들이 찾으시는 시그니처 코스입니다.</p>
                </div>
            </div>
            <div class="card text-only">
                <div class="info">
                    <b>C 코스 (120분)</b>
                    <p>전신 아로마 + 스페셜 릴렉싱. 전신을 꼼꼼하게 관리하는 VIP 힐링 코스입니다.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 진행 순서 섹션 추가 -->
<section class="sec">
    <div class="in">
        <p class="kick">PROCESS</p>
        <h2>마사지 진행 순서</h2>
        <p style="font-size:14px; color:var(--mute); margin-bottom:24px;">출장 마사지가 처음이셔도 안심하세요. 친절히 안내해 드립니다.</p>
        <ol class="steps">
            <li><b>예약 및 편안한 대기</b><span>원하시는 시간과 장소로 관리사가 필요한 모든 비품을 챙겨 방문합니다.</span></li>
            <li><b>코스 안내 및 오일 선택</b><span>처음이신 분들을 위해 진행 차례를 설명하고, 취향에 맞게 향/무향 오일을 선택합니다.</span></li>
            <li><b>전신 아로마 케어</b><span>부드럽고 꼼꼼한 손길로 굳어있던 몸의 피로와 스트레스를 풀어드립니다.</span></li>
            <li><b>마무리 및 휴식</b><span>관리가 끝나면 개운해진 몸으로 편안하게 휴식을 취하시면 됩니다.</span></li>
        </ol>
    </div>
</section>

<!-- 업체 목록 -->
<section class="sec">
    <div class="in">
        <p class="kick">PARTNERS</p>
        <h2>엄선된 제휴 업체 목록</h2>
        <p style="font-size:14px; color:var(--mute); margin-bottom:24px;">원하시는 업체를 선택하여 바로 전화로 문의해 보세요.</p>
        <div class="cards">
            {companies_html}
        </div>
    </div>
</section>

<!-- 후기 섹션 추가 -->
<section class="sec">
    <div class="in">
        <p class="kick">REVIEWS</p>
        <h2>고객 리얼 생생 후기</h2>
        <div class="rev">
            <div class="rv">
                <div class="meta">{region_display} 자택 방문 고객님</div>
                <p>"출장은 처음 불러봐서 걱정했는데, 오셔서 순서부터 차근차근 설명해주시고 너무 시원하게 잘 받았습니다. 끝나고 바로 잘 수 있어서 최고네요."</p>
            </div>
            <div class="rv">
                <div class="meta">{region_display} 출장 숙소 방문 고객님</div>
                <p>"제가 오일 냄새를 진짜 싫어해서 고민하다가 무향 오일이 있다는 글 보고 불렀습니다. 냄새 하나도 안 나고 마사지 실력도 훌륭해서 꿀잠 잤습니다."</p>
            </div>
        </div>
    </div>
</section>

<!-- FAQ 섹션 추가 -->
<section class="sec">
    <div class="in">
        <p class="kick">Q&A</p>
        <h2>자주 묻는 질문</h2>
        <div class="faq">
            <div class="qa">
                <b>처음인데 제가 따로 준비할 게 있나요?</b>
                <p>아닙니다. 고객님은 편안한 복장으로 계시기만 하면 됩니다. 마사지에 필요한 최고급 오일과 수건 등 모든 물품은 저희가 꼼꼼히 챙겨서 방문합니다.</p>
            </div>
            <div class="qa">
                <b>원룸이나 작은 오피스텔에서도 가능한가요?</b>
                <p>네, 물론입니다. 매트를 깔 수 있는 최소한의 공간만 있다면 어디든 편안하게 관리를 받으실 수 있습니다.</p>
            </div>
            <div class="qa">
                <b>향기 없는 오일은 추가 비용이 있나요?</b>
                <p>아닙니다. 추가 비용 없이 고객님의 취향에 따라 무향 오일을 선택하실 수 있습니다. 예약 시 미리 말씀해 주시면 더욱 좋습니다.</p>
            </div>
        </div>
    </div>
</section>

<!-- 하단 지역 링크 -->
<section class="sec">
    <div class="in">
        <p class="kick">LOCATIONS</p>
        <h2>다른 지역 찾아보기</h2>
        <div class="links">
            {region_links}
        </div>
    </div>
</section>

<footer class="foot">© {site_name} | {region_display} 아로마 출장 마사지 전문</footer>
</div>
</body>
</html>"""

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

def generate_region_links(current_key):
    links = ""
    for key, name in REGIONS.items():
        if key == current_key:
            continue
        href = "/" if key == "main" else f"/{key}.html"
        links += f'<a href="{href}">{name}</a>'
    return links

def build_robots_txt():
    robots_content = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml"
    with open("dist/robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("생성 완료: dist/robots.txt")

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

def build_site():
    os.makedirs("dist", exist_ok=True)
    comp_html = generate_companies_html()
    
    for key, region_name in REGIONS.items():
        filename = "index.html" if key == "main" else f"{key}.html"
        page_url = f"{BASE_URL}/{'' if key == 'main' else filename}"
        
        region_display = "서울/경기" if key == "main" else region_name
        title = f"{SITE_NAME} | 향기로 쉬어가는 {region_display} 아로마 마사지".strip()
        
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
        
        page_content = HTML_TEMPLATE.format(
            title=title,
            description=BASE_DESC,
            url=page_url,
            json_ld=json.dumps(json_ld_data, ensure_ascii=False, indent=2),
            region_display=region_display,
            companies_html=comp_html,
            region_links=generate_region_links(key),
            site_name=SITE_NAME
        )
        
        with open(f"dist/{filename}", "w", encoding="utf-8") as f:
            f.write(page_content)
        print(f"생성 완료: dist/{filename}")

    build_robots_txt()
    build_sitemap_xml()

if __name__ == "__main__":
    build_site()
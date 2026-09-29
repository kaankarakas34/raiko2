from html import escape
import json
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape
from guides import GUIDES

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
SITE_URL = "https://www.raiko.tech"


def item(href, title, description):
    return f'<a class="mega-link" href="{href}"><strong>{title}</strong><span>{description}</span></a>'


menus = {
    "cozumler": {
        "label": "Ã‡Ã¶zÃ¼mler",
        "intro": "KonuÅŸan, dÃ¼ÅŸÃ¼nen ve iÅŸi ilerleten sistemler.",
        "columns": [
            ("MÃ¼ÅŸteri iletiÅŸimi", [
                ("/ai-call-agent/", "AI Call Agent", "Yapay zekÃ¢ Ã§aÄŸrÄ± merkezi"),
                ("/ai-call-agent/#gelen", "Gelen Ã§aÄŸrÄ± ajanÄ±", "AramalarÄ± karÅŸÄ±layÄ±n ve yÃ¶nlendirin"),
                ("/ai-call-agent/#giden", "Giden Ã§aÄŸrÄ± ajanÄ±", "TanÄ±mlÄ± takip gÃ¶rÃ¼ÅŸmeleri"),
                ("/ai-chatbot/", "AI Chatbot", "Web ve mesajlaÅŸma sohbetleri"),
                ("/ai-chatbot/#whatsapp", "WhatsApp AI Agent", "Mesajdan iÅŸ akÄ±ÅŸÄ±na"),
            ]),
            ("SatÄ±ÅŸ ve bÃ¼yÃ¼me", [
                ("/akilli-crm/", "AkÄ±llÄ± CRM", "MÃ¼ÅŸteri kaydÄ±nÄ± tek yerde toplayÄ±n"),
                ("/ai-satis-ajani/", "AI SatÄ±ÅŸ AjanÄ±", "Lead nitelendirme ve takip"),
                ("/b2b-outreach/", "B2B Outreach", "Hedefleme ve satÄ±ÅŸ iletiÅŸimi"),
                ("/b2b-outreach/#musteri-bulma", "Lead Generation", "DoÄŸru ÅŸirketleri araÅŸtÄ±rÄ±n"),
            ]),
            ("Operasyon", [
                ("/otomasyonlar/", "Ä°ÅŸ akÄ±ÅŸÄ± otomasyonlarÄ±", "Tekrarlanan adÄ±mlarÄ± baÄŸlayÄ±n"),
                ("/otomasyonlar/#ozel-ajanlar", "Ã–zel AI agent", "Åirketinize gÃ¶re kurgulayÄ±n"),
            ]),
        ],
    },
    "sektorler": {
        "label": "SektÃ¶rler",
        "intro": "Her sektÃ¶rÃ¼n konuÅŸmasÄ± ve iÅŸ akÄ±ÅŸÄ± farklÄ±dÄ±r.",
        "columns": [
            ("Ã–ne Ã§Ä±kan kullanÄ±m alanlarÄ±", [
                ("/saglik-turizmi/", "SaÄŸlÄ±k turizmi", "Ã‡ok dilli ilk temas ve randevu"),
                ("/ihracat-uretim/", "Ä°hracat ve Ã¼retim", "Hedef ÅŸirket araÅŸtÄ±rmasÄ± ve takip"),
                ("/b2b-hizmetler/", "B2B hizmetler", "Talep toplama ve satÄ±ÅŸ sÃ¼reci"),
                ("/emlak/", "Emlak", "Ä°lan talepleri ve portfÃ¶y takibi"),
                ("/otomotiv/", "Otomotiv", "AraÃ§ talepleri ve test sÃ¼rÃ¼ÅŸÃ¼"),
            ]),
        ],
    },
    "kaynaklar": {
        "label": "Kaynaklar",
        "intro": "Karar vermeden Ã¶nce sorulmasÄ± gerekenler.",
        "columns": [
            ("Rehberler", [
                ("/rehberler/ai-call-agent-nedir/", "AI Call Agent nedir?", "KullanÄ±m ve kurulum adÄ±mlarÄ±"),
                ("/rehberler/ai-sdr-nedir/", "AI SDR nedir?", "SatÄ±ÅŸ sÃ¼recindeki rolÃ¼"),
            ]),
            ("KarÅŸÄ±laÅŸtÄ±rmalar", [
                ("/rehberler/chatbot-ai-agent-canli-destek/", "Chatbot, ajan, canlÄ± destek", "Hangi iÅŸi kim Ã¼stlenmeli?"),
            ]),
            ("KullanÄ±m senaryolarÄ±", [
                ("/rehberler/telefon-crm-satis-takibi/", "UÃ§tan uca Ã¶rnek akÄ±ÅŸ", "Telefon, CRM ve satÄ±ÅŸ takibi"),
                ("/rehberler/emlak-yapay-zeka-asistani/", "Emlakta AI asistan", "Ä°lan talebinden gÃ¶sterime"),
                ("/rehberler/otomotiv-test-surusu-takibi/", "Otomotivde AI asistan", "AraÃ§ talebinden test sÃ¼rÃ¼ÅŸÃ¼ne"),
            ]),
        ],
    },
}


def header():
    triggers = []
    for key, menu in menus.items():
        groups = "".join(
            f'<div class="mega-group"><p class="mega-heading">{heading}</p>'
            + "".join(item(*link) for link in links) + "</div>"
            for heading, links in menu["columns"]
        )
        triggers.append(
            f'<div class="nav-group" data-menu="{key}">'
            f'<button class="nav-trigger" type="button" aria-expanded="false" aria-controls="menu-{key}">{menu["label"]}<span aria-hidden="true">âŒ„</span></button>'
            f'<div class="mega" id="menu-{key}" hidden><div class="wrap mega-inner">'
            f'<div class="mega-intro"><span class="mega-mark">RAIKO / {menu["label"].upper()}</span><p>{menu["intro"]}</p></div>'
            f'<div class="mega-columns">{groups}</div></div></div></div>'
        )
    return (
        '<header class="header"><div class="wrap nav">'
        '<a class="brand" href="/" aria-label="Raiko ana sayfa"><img src="/raiko-logo.webp" alt="Raiko" width="144" height="48"><small>AI Techs</small></a>'
        '<button class="menu" type="button" aria-expanded="false" aria-controls="nav-links">MenÃ¼</button>'
        '<nav class="links" id="nav-links" aria-label="Ana menÃ¼">'
        + "".join(triggers)
        + '<a class="nav-simple" href="/#sistemler">NasÄ±l Ã§alÄ±ÅŸÄ±r?</a>'
        '</nav></div></header>'
    )


def shell(title, description, main, path="/"):
    escaped_title = escape(title)
    escaped_description = escape(description)
    canonical = SITE_URL + path
    schema = ""
    if path == "/":
        schema = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "Organization",
            "name": "Raiko", "url": SITE_URL, "logo": SITE_URL + "/raiko-logo.webp",
        }, ensure_ascii=False) + "</script>"
    elif path.strip("/") in pages:
        schema = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "Service",
            "name": pages[path.strip("/")]["title"],
            "description": pages[path.strip("/")]["summary"],
            "url": canonical,
            "provider": {"@type": "Organization", "name": "Raiko", "url": SITE_URL},
        }, ensure_ascii=False) + "</script>"
    return f'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#11110f">
  <meta name="description" content="{escaped_description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Raiko">
  <meta property="og:locale" content="tr_TR">
  <meta property="og:title" content="{escaped_title}">
  <meta property="og:description" content="{escaped_description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}/social-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <title>{escaped_title}</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%2311110f'/%3E%3Cpath d='M37 4 10 36h19l-5 24 30-36H35z' fill='%23ffc400'/%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Space+Grotesk:wght@400;500;600;700&amp;display=swap">
  <link rel="stylesheet" href="/style.css">
  <script src="/site.js" defer></script>
  {schema}
</head>
<body id="ust">
  <a class="skip" href="#icerik">Ä°Ã§eriÄŸe geÃ§</a>
  {header()}
  <main id="icerik">{main}</main>
</body>
</html>'''


def contact_link(subject):
    return "mailto:info@raiko.tech?subject=" + quote(subject)


pages = {
    "ai-call-agent": {
        "category": "MÃ¼ÅŸteri iletiÅŸimi / Sesli ajan",
        "title": "AI Call Agent: yapay zekÃ¢ Ã§aÄŸrÄ± merkezi",
        "summary": "Gelen aramalarÄ± karÅŸÄ±layan, ihtiyacÄ± anlayan ve tanÄ±mladÄ±ÄŸÄ±nÄ±z sonraki adÄ±mÄ± baÅŸlatan sesli yapay zekÃ¢ ajanlarÄ±.",
        "lead": "Telefon hÃ¢lÃ¢ birÃ§ok mÃ¼ÅŸteri iÃ§in ilk temas noktasÄ±. Raiko, Ã§aÄŸrÄ± akÄ±ÅŸÄ±nÄ± ÅŸirketinizin bilgisi, yÃ¶nlendirme kurallarÄ± ve CRM sÃ¼reÃ§leriyle birlikte tasarlar.",
        "steps": [
            ("ArayanÄ± anlar", "Sorunun veya talebin konusunu belirler; gerekli bilgileri konuÅŸma iÃ§inde toplar."),
            ("Bilgiye dayanÄ±r", "OnaylanmÄ±ÅŸ bilgi kaynaklarÄ±ndan yararlanarak sÄ±k sorulara yanÄ±t verir."),
            ("Ä°ÅŸi ilerletir", "Randevu, kayÄ±t, geri arama veya ekip yÃ¶nlendirmesi gibi tanÄ±mlÄ± adÄ±mÄ± baÅŸlatÄ±r."),
        ],
        "sections": [
            ("gelen", "Gelen Ã§aÄŸrÄ± ajanÄ±", "AramalarÄ± yanÄ±tlayan yapay zekÃ¢ telefon asistanÄ±, yoÄŸun anlarda ilk temasÄ± karÅŸÄ±lar. SÄ±k sorularÄ± ele alÄ±r, mÃ¼ÅŸterinin amacÄ±nÄ± belirler ve insan gÃ¶rÃ¼ÅŸmesi gereken konuyu doÄŸru ekibe taÅŸÄ±r."),
            ("giden", "Giden Ã§aÄŸrÄ± ajanÄ±", "Geri arama, randevu hatÄ±rlatma veya daha Ã¶nce izin verilmiÅŸ takip gÃ¶rÃ¼ÅŸmeleri iÃ§in senaryolar kurulabilir. GÃ¶rÃ¼ÅŸmenin kapsamÄ± ve insana devredilecek noktalar Ã¶nceden tanÄ±mlanÄ±r."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir mÃ¼ÅŸteri randevu iÃ§in arar. Ajan uygun bilgileri toplar, mevcut takvim veya CRM baÄŸlantÄ±sÄ± varsa uygun adÄ±mÄ± baÅŸlatÄ±r. Belirsiz ya da hassas bir konu ortaya Ã§Ä±ktÄ±ÄŸÄ±nda gÃ¶rÃ¼ÅŸmeyi ekibe aktarÄ±r."),
        "questions": [
            ("Yapay zekÃ¢ Ã§aÄŸrÄ± merkezi insan temsilcinin yerini tamamen alÄ±r mÄ±?", "SÃ¼reÃ§ tasarÄ±mÄ±na baÄŸlÄ±dÄ±r. Tekrarlanan ve aÃ§Ä±k kurallÄ± gÃ¶rÃ¼ÅŸmeler otomatik ilerleyebilir; karmaÅŸÄ±k veya hassas konular iÃ§in insan devri tanÄ±mlanmalÄ±dÄ±r."),
            ("CRM baÄŸlantÄ±sÄ± zorunlu mu?", "HayÄ±r. Temel Ã§aÄŸrÄ± karÅŸÄ±lama ayrÄ± kurgulanabilir. Ancak kayÄ±t ve takip sÃ¼recini birleÅŸtirmek iÃ§in CRM entegrasyonu faydalÄ± olabilir."),
        ],
        "related": [("/ai-chatbot/", "AI Chatbot"), ("/akilli-crm/", "AkÄ±llÄ± CRM")],
    },
    "ai-chatbot": {
        "category": "MÃ¼ÅŸteri iletiÅŸimi / YazÄ±lÄ± ajan",
        "title": "AI Chatbot ve WhatsApp AI Agent",
        "summary": "Web ve mesajlaÅŸma kanallarÄ±ndaki sorularÄ± karÅŸÄ±layan, mÃ¼ÅŸteri adaylarÄ±nÄ± nitelendiren ve gÃ¶rÃ¼ÅŸmeyi doÄŸru akÄ±ÅŸa taÅŸÄ±yan yapay zekÃ¢ sohbet ajanlarÄ±.",
        "lead": "Kurumsal AI chatbot, yalnÄ±zca hazÄ±r yanÄ±t gÃ¶steren bir pencere deÄŸildir. Åirketinizin bilgi kaynaklarÄ±yla ve gerektiÄŸinde iÅŸ sistemleriyle baÄŸlantÄ±lÄ± bir konuÅŸma akÄ±ÅŸÄ± olarak kurgulanÄ±r.",
        "steps": [
            ("KarÅŸÄ±lar", "ZiyaretÃ§inin sorusunu ve niyetini doÄŸal dilde anlar."),
            ("YanÄ±tlar", "OnaylÄ± Ã¼rÃ¼n, hizmet ve sÃ¼reÃ§ bilgisini kullanÄ±r; belirsizlikte insan desteÄŸine yÃ¶nlendirir."),
            ("AktarÄ±r", "Toplanan baÄŸlamÄ± uygun satÄ±ÅŸ veya destek sÃ¼recine taÅŸÄ±r."),
        ],
        "sections": [
            ("web", "Web sitesi chatbotu", "ZiyaretÃ§iler hizmetler hakkÄ±nda soru sorarken onlarÄ± doÄŸru bilgiye ve sonraki adÄ±ma yÃ¶nlendirebilir. SatÄ±ÅŸ ekibine aktarÄ±lacak talepte gÃ¶rÃ¼ÅŸme baÄŸlamÄ± korunur."),
            ("whatsapp", "WhatsApp yapay zekÃ¢ asistanÄ±", "WhatsApp Ã¼zerinden gelen sorular iÃ§in bilgi verme, Ã¶n deÄŸerlendirme ve randevu talebi toplama akÄ±ÅŸlarÄ± tasarlanabilir. KullanÄ±lacak kanal ve entegrasyonlarÄ±n kapsamÄ± kurulumda belirlenir."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir ziyaretÃ§i web sitesinde hizmet kapsamÄ±nÄ± sorar. Ajan ilgili bilgiyi verir, ihtiyacÄ±nÄ± birkaÃ§ soruyla netleÅŸtirir ve uygun ekip iÃ§in bir talep oluÅŸturur."),
        "questions": [
            ("Åirket verileriyle eÄŸitilmiÅŸ chatbot yanlÄ±ÅŸ cevap verirse ne olur?", "YanÄ±tlarÄ±n kullanÄ±lacaÄŸÄ± kaynaklar, sÄ±nÄ±rlar ve insan devri Ã¶nceden tanÄ±mlanÄ±r. Kritik konular iÃ§in otomatik yanÄ±t yerine yÃ¶nlendirme tercih edilir."),
            ("Chatbot ile canlÄ± destek birlikte Ã§alÄ±ÅŸabilir mi?", "Evet. Tekrarlanan sorular ajan tarafÄ±ndan ele alÄ±nÄ±rken karmaÅŸÄ±k gÃ¶rÃ¼ÅŸmeler insan ekibe aktarÄ±lacak biÃ§imde tasarlanabilir."),
        ],
        "related": [("/ai-call-agent/", "AI Call Agent"), ("/akilli-crm/", "AkÄ±llÄ± CRM")],
    },
    "akilli-crm": {
        "category": "SatÄ±ÅŸ ve bÃ¼yÃ¼me / MÃ¼ÅŸteri verisi",
        "title": "AkÄ±llÄ± CRM ve otomatik lead yÃ¶netimi",
        "summary": "Telefon, sohbet ve satÄ±ÅŸ temaslarÄ±ndan gelen bilgiyi dÃ¼zenleyen; ekibin sonraki adÄ±mÄ± gÃ¶rmesini kolaylaÅŸtÄ±ran CRM odaklÄ± yapay zekÃ¢ akÄ±ÅŸlarÄ±.",
        "lead": "Yapay zekÃ¢ destekli CRM yaklaÅŸÄ±mÄ±, yeni bir ekran eklemekten Ã§ok mÃ¼ÅŸteri kaydÄ±nÄ±n doÄŸru anda gÃ¼ncel kalmasÄ±nÄ± ve satÄ±ÅŸ fÄ±rsatÄ±nÄ±n kaybolmamasÄ±nÄ± hedefler.",
        "steps": [
            ("TemasÄ± toplar", "Form, Ã§aÄŸrÄ± veya sohbetten gelen bilgileri tanÄ±mlÄ± alanlara aktarÄ±r."),
            ("BaÄŸlamÄ± dÃ¼zenler", "Talebin konusu, aÅŸamasÄ± ve sonraki aksiyon iÃ§in anlaÅŸÄ±lÄ±r bir Ã¶zet oluÅŸturur."),
            ("Takibi destekler", "Ekip iÃ§in gÃ¶rev, yÃ¶nlendirme veya hatÄ±rlatma adÄ±mlarÄ±nÄ± iÅŸ akÄ±ÅŸÄ±na baÄŸlar."),
        ],
        "sections": [
            ("lead-yonetimi", "Lead yÃ¶netimi", "Potansiyel mÃ¼ÅŸterinin kaynaÄŸÄ±, ihtiyacÄ± ve gÃ¶rÃ¼ÅŸme geÃ§miÅŸi aynÄ± kayÄ±tta bir araya geldiÄŸinde satÄ±ÅŸ ekibi Ã¶nceliklendirmeyi daha saÄŸlÄ±klÄ± yapabilir."),
            ("entegrasyon", "Mevcut CRM ile Ã§alÄ±ÅŸma", "Kurulum mevcut CRM'inizi temel alabilir. Veri alanlarÄ±, yetkiler ve hangi adÄ±mlarÄ±n otomatik iÅŸleyeceÄŸi sisteminize gÃ¶re planlanÄ±r."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir mÃ¼ÅŸteri web sohbetinden teklif talep eder. Talep Ã¶zetlenir, CRM'de ilgili kayda eklenir ve satÄ±ÅŸ ekibinin takip edeceÄŸi adÄ±m belirlenir."),
        "questions": [
            ("Yeni bir CRM kullanmak zorunda mÄ±yÄ±z?", "HayÄ±r. Ä°lk adÄ±m mevcut sistemlerin ve veri akÄ±ÅŸÄ±nÄ±n deÄŸerlendirilmesidir."),
            ("AI lead scoring nasÄ±l ele alÄ±nÄ±r?", "Ã–nceliklendirme iÃ§in kullanÄ±lacak iÅŸaretler ÅŸirketinizin satÄ±ÅŸ sÃ¼recine gÃ¶re belirlenir; nihai karar ve Ã¶nemli aksiyonlar iÃ§in insan onayÄ± korunabilir."),
        ],
        "related": [("/ai-satis-ajani/", "AI SatÄ±ÅŸ AjanÄ±"), ("/b2b-outreach/", "B2B Outreach")],
    },
    "ai-satis-ajani": {
        "category": "SatÄ±ÅŸ ve bÃ¼yÃ¼me / AI SDR",
        "title": "AI SatÄ±ÅŸ AjanÄ± ile daha dÃ¼zenli satÄ±ÅŸ takibi",
        "summary": "Potansiyel mÃ¼ÅŸteri bilgisini araÅŸtÄ±ran, gelen talepleri nitelendiren ve satÄ±ÅŸ temsilcisinin doÄŸru gÃ¶rÃ¼ÅŸmeye hazÄ±rlanmasÄ±na yardÄ±mcÄ± olan AI SDR akÄ±ÅŸlarÄ±.",
        "lead": "AI sales agent, satÄ±ÅŸ ekibine baÄŸlam hazÄ±rlar ve tanÄ±mlÄ± takip adÄ±mlarÄ±nÄ± yÃ¼rÃ¼tÃ¼r. Ä°liÅŸki kurma, teklif kararÄ± ve hassas iletiÅŸim noktalarÄ±nda insan kontrolÃ¼ Ã¶nemini korur.",
        "steps": [
            ("AraÅŸtÄ±rÄ±r", "Hedef mÃ¼ÅŸteri profiline uygun ÅŸirket ve talep bilgisini toplar."),
            ("Nitelendirir", "Ä°htiyaÃ§, zamanlama ve uygunluk gibi iÅŸaretleri dÃ¼zenler."),
            ("Takibi hazÄ±rlar", "CRM kaydÄ±nÄ± ve satÄ±ÅŸ temsilcisi iÃ§in bir sonraki adÄ±mÄ± netleÅŸtirir."),
        ],
        "sections": [
            ("nitelendirme", "Lead nitelendirme", "Her talep aynÄ± aÅŸamada deÄŸildir. AI satÄ±ÅŸ ajanÄ±, Ã¶nceden belirlenmiÅŸ Ã¶lÃ§Ã¼tlere gÃ¶re gÃ¶rÃ¼ÅŸme baÄŸlamÄ±nÄ± oluÅŸturabilir."),
            ("insan-onayi", "Ä°nsan onayÄ± nerede gerekir?", "DÄ±ÅŸarÄ±ya gÃ¶nderilecek kiÅŸiselleÅŸtirilmiÅŸ mesajlar, teklif ve Ã¶nemli satÄ±ÅŸ kararlarÄ± iÃ§in onay noktalarÄ± belirlenir. Otomasyonun sÄ±nÄ±rlarÄ± aÃ§Ä±k olur."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir ÅŸirket demo ilgisi gÃ¶sterir. Ajan talebin konusunu ve ÅŸirket bilgisini toplar, CRM kaydÄ±nÄ± gÃ¼nceller, ekibe kÄ±sa bir Ã¶zet sunar ve uygun takip adÄ±mÄ±nÄ± Ã¶nerir."),
        "questions": [
            ("AI SDR klasik satÄ±ÅŸ otomasyonundan nasÄ±l ayrÄ±lÄ±r?", "Klasik otomasyon Ã¶nceden tanÄ±mlÄ± tetikleyicileri iÅŸler. AI SDR akÄ±ÅŸÄ±, gelen bilgiyi yorumlayarak nitelendirme ve Ã¶zetleme gibi adÄ±mlara katkÄ± saÄŸlar."),
            ("ToplantÄ±larÄ± otomatik ayarlayabilir mi?", "Takvim ve onay sÃ¼reÃ§leri uygun biÃ§imde baÄŸlandÄ±ÄŸÄ±nda toplantÄ± talebi toplama veya planlama adÄ±mlarÄ± kurgulanabilir."),
        ],
        "related": [("/b2b-outreach/", "B2B Outreach"), ("/akilli-crm/", "AkÄ±llÄ± CRM")],
    },
    "b2b-outreach": {
        "category": "SatÄ±ÅŸ ve bÃ¼yÃ¼me / Outbound",
        "title": "B2B Outreach ve otonom satÄ±ÅŸ sistemleri",
        "summary": "Hedef ÅŸirket araÅŸtÄ±rmasÄ±, mÃ¼ÅŸteri adayÄ± nitelendirme, kiÅŸiselleÅŸtirilmiÅŸ iletiÅŸim ve CRM takibini tek bir satÄ±ÅŸ akÄ±ÅŸÄ±nda birleÅŸtirin.",
        "lead": "B2B mÃ¼ÅŸteri bulma sistemi, yalnÄ±zca toplu mesaj gÃ¶ndermek deÄŸildir. DoÄŸru mÃ¼ÅŸteri profilini seÃ§mek, baÄŸlamÄ± araÅŸtÄ±rmak ve iletiÅŸimi kontrollÃ¼ biÃ§imde yÃ¼rÃ¼tmek gerekir.",
        "steps": [
            ("Hedefler", "Ä°deal mÃ¼ÅŸteri profiline gÃ¶re uygun ÅŸirketleri ve karar verici rollerini araÅŸtÄ±rÄ±r."),
            ("HazÄ±rlar", "Åirkete ve ihtiyaca uygun iletiÅŸim taslaÄŸÄ± ile takip planÄ±nÄ± oluÅŸturur."),
            ("Ä°zler", "YanÄ±tlarÄ±, fÄ±rsatlarÄ± ve sonraki aksiyonlarÄ± CRM sÃ¼recinde dÃ¼zenler."),
        ],
        "sections": [
            ("musteri-bulma", "Yapay zekÃ¢ ile mÃ¼ÅŸteri bulma", "Hedef ÅŸirket listesi, sektÃ¶r, Ã¶lÃ§ek, coÄŸrafya ve ihtiyaÃ§ iÅŸaretlerine gÃ¶re oluÅŸturulabilir. AraÅŸtÄ±rmanÄ±n kalitesi, kullanÄ±lan veri kaynaklarÄ±na baÄŸlÄ±dÄ±r."),
            ("iletisim", "Ã‡ok kanallÄ± satÄ±ÅŸ iletiÅŸimi", "E-posta, telefon ve uygun diÄŸer temas noktalarÄ± ortak bir plan iÃ§inde ele alÄ±nabilir. KanallarÄ±n kurallarÄ±, izinler ve insan onayÄ± iletiÅŸim tasarÄ±mÄ±na dahil edilir."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Ä°hracat yapan bir Ã¼retici hedef pazarÄ±nÄ± tanÄ±mlar. Sistem uygun ÅŸirketleri araÅŸtÄ±rÄ±r, satÄ±ÅŸ ekibinin incelemesi iÃ§in kÄ±sa baÄŸlam ve iletiÅŸim taslaÄŸÄ± hazÄ±rlar. Onaylanan temaslar CRM'de takip edilir."),
        "questions": [
            ("Full outreach sistemi tamamen kendi baÅŸÄ±na Ã§alÄ±ÅŸÄ±r mÄ±?", "AraÅŸtÄ±rma ve takip adÄ±mlarÄ± otomatikleÅŸtirilebilir. DÄ±ÅŸ iletiÅŸim, veri kullanÄ±mÄ± ve Ã¶nemli kararlar iÃ§in onay ve kontrol noktalarÄ± tanÄ±mlanmalÄ±dÄ±r."),
            ("LinkedIn hesap etkinliklerini otomatikleÅŸtiriyor musunuz?", "Hedefleme ve araÅŸtÄ±rma akÄ±ÅŸlarÄ± platform kurallarÄ±na uygun biÃ§imde planlanmalÄ±dÄ±r. Ä°zinsiz hesap etkinliÄŸi otomasyonu vaat edilmez."),
        ],
        "related": [("/ai-satis-ajani/", "AI SatÄ±ÅŸ AjanÄ±"), ("/ihracat-uretim/", "Ä°hracat ve Ã¼retim")],
    },
    "otomasyonlar": {
        "category": "Operasyon / Ã–zel sistemler",
        "title": "Yapay zekÃ¢ otomasyonlarÄ± ve Ã¶zel AI agent sistemleri",
        "summary": "Uygulamalar arasÄ±nda kalan tekrarlÄ± iÅŸleri, ÅŸirketinizin veri kaynaklarÄ± ve onay sÃ¼reÃ§leriyle uyumlu otomasyonlara dÃ¶nÃ¼ÅŸtÃ¼rÃ¼n.",
        "lead": "HazÄ±r bir araÃ§ her iÅŸ akÄ±ÅŸÄ±nÄ± Ã§Ã¶zmez. Raiko, gÃ¶revin nerede baÅŸladÄ±ÄŸÄ±nÄ±, hangi veriye ihtiyaÃ§ duyduÄŸunu ve ne zaman insana dÃ¶nmesi gerektiÄŸini birlikte tasarlar.",
        "steps": [
            ("SÃ¼reci haritalar", "Tekrarlanan adÄ±mlarÄ±, karar noktalarÄ±nÄ± ve kullanÄ±lan araÃ§larÄ± belirler."),
            ("BaÄŸlantÄ±larÄ± kurar", "Gerekli veri kaynaklarÄ± ve uygulamalar arasÄ±ndaki akÄ±ÅŸÄ± tanÄ±mlar."),
            ("KontrolÃ¼ korur", "Hata, belirsizlik ve insan onayÄ± gereken durumlar iÃ§in aÃ§Ä±k sÄ±nÄ±rlar oluÅŸturur."),
        ],
        "sections": [
            ("is-akislari", "Ä°ÅŸ akÄ±ÅŸÄ± otomasyonlarÄ±", "MÃ¼ÅŸteri kaydÄ±, destek talebi, bildirim, rapor Ã¶zeti ve benzeri adÄ±mlar uygulamalar arasÄ±nda taÅŸÄ±nabilir. Otomasyonun kapsamÄ± mevcut sistemlere gÃ¶re belirlenir."),
            ("ozel-ajanlar", "Ã–zel AI agent geliÅŸtirme", "Åirkete Ã¶zel ajan, belirli gÃ¶revi yerine getirmek iÃ§in kendi bilgi kaynaklarÄ±, araÃ§larÄ± ve yetki sÄ±nÄ±rlarÄ±yla tasarlanÄ±r. Ã‡oklu ajan yaklaÅŸÄ±mÄ± ancak iÅŸin gerÃ§ekten gerektirdiÄŸi durumlarda kullanÄ±lÄ±r."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir destek talebi geldiÄŸinde sistem konuyu sÄ±nÄ±flandÄ±rÄ±r, ilgili kaynaÄŸÄ± bulur, taslak yanÄ±t hazÄ±rlar ve gerekli ise ekip onayÄ±na sunar."),
        "questions": [
            ("Kurulum maliyeti nasÄ±l belirlenir?", "Kapsam, entegrasyon sayÄ±sÄ±, veri hazÄ±rlÄ±ÄŸÄ± ve kullanÄ±m hacmi maliyeti etkiler. Net teklif iÃ§in gerÃ§ek sÃ¼reÃ§ deÄŸerlendirilmelidir."),
            ("Her adÄ±mÄ± otonomlaÅŸtÄ±rmak gerekir mi?", "HayÄ±r. TekrarlÄ± ve aÃ§Ä±k kurallÄ± adÄ±mlar Ã¶ncelikli olabilir; riskli veya belirsiz kararlar insanda kalmalÄ±dÄ±r."),
        ],
        "related": [("/akilli-crm/", "AkÄ±llÄ± CRM"), ("/ai-chatbot/", "AI Chatbot")],
    },
}


sectors = {
    "saglik-turizmi": {
        "category": "SektÃ¶rler / SaÄŸlÄ±k turizmi",
        "title": "SaÄŸlÄ±k turizmi iÃ§in Ã§ok dilli ilk temas",
        "summary": "Yurt dÄ±ÅŸÄ±ndan gelen hasta adayÄ±nÄ±n sorusunu karÅŸÄ±layan, talebini dÃ¼zenleyen ve uygun ekibe taÅŸÄ±yan yapay zekÃ¢ iletiÅŸim akÄ±ÅŸlarÄ±.",
        "lead": "SaÄŸlÄ±k turizminde hÄ±z kadar doÄŸru yÃ¶nlendirme de Ã¶nemlidir. Ajan, onaylÄ± operasyonel bilgiyle ilk temasÄ± yÃ¶netir; tÄ±bbi deÄŸerlendirme ve kararlar yetkili insan ekibinde kalÄ±r.",
        "steps": [
            ("Talebi karÅŸÄ±lar", "Dil, iletiÅŸim kanalÄ± ve talep konusunu belirler."),
            ("Bilgiyi dÃ¼zenler", "Randevu, ulaÅŸÄ±m ve sÃ¼reÃ§ gibi onaylÄ± genel bilgileri paylaÅŸÄ±r."),
            ("Ekibe aktarÄ±r", "Klinik veya hasta koordinasyon ekibine gerekli baÄŸlamÄ± iletir."),
        ],
        "sections": [("sinirlar", "Klinik sÄ±nÄ±rlarÄ±", "Ajan tÄ±bbi teÅŸhis veya tedavi Ã¶nerisi Ã¼retmek iÃ§in konumlandÄ±rÄ±lmaz. Hasta verisi ve iletiÅŸim izinleri tasarÄ±mÄ±n baÅŸÄ±nda ele alÄ±nÄ±r.")],
        "example": ("Ã–rnek akÄ±ÅŸ", "Yurt dÄ±ÅŸÄ±ndaki bir kiÅŸi WhatsApp'tan sÃ¼reÃ§ ve uygunluk sorar. Ajan genel sÃ¼reÃ§ bilgisini paylaÅŸÄ±r, iletiÅŸim tercihlerini toplar ve tÄ±bbi deÄŸerlendirme gerektiren soruyu koordinasyon ekibine aktarÄ±r."),
        "questions": [("Sesli ajan randevu talebi alabilir mi?", "Uygun takvim ve ekip akÄ±ÅŸÄ± kurulursa randevu talebini toplayÄ±p ilgili birime yÃ¶nlendirebilir.")],
        "related": [("/ai-call-agent/", "AI Call Agent"), ("/ai-chatbot/#whatsapp", "WhatsApp AI Agent")],
    },
    "ihracat-uretim": {
        "category": "SektÃ¶rler / Ä°hracat ve Ã¼retim",
        "title": "Ä°hracatÃ§Ä± ve Ã¼reticiler iÃ§in B2B mÃ¼ÅŸteri araÅŸtÄ±rmasÄ±",
        "summary": "Hedef pazardaki ÅŸirketleri araÅŸtÄ±ran, satÄ±ÅŸ temasÄ±nÄ± hazÄ±rlayan ve fÄ±rsatlarÄ± CRM sÃ¼recine taÅŸÄ±yan kontrollÃ¼ B2B outreach akÄ±ÅŸlarÄ±.",
        "lead": "FarklÄ± Ã¼lkelerde doÄŸru ÅŸirketi ve doÄŸru ihtiyacÄ± bulmak zaman alÄ±r. AI destekli araÅŸtÄ±rma, ekibin inceleyeceÄŸi hedefleri daha dÃ¼zenli oluÅŸturmasÄ±na yardÄ±mcÄ± olur.",
        "steps": [
            ("PazarÄ± tanÄ±mlar", "ÃœrÃ¼n, Ã¼lke ve ideal mÃ¼ÅŸteri profiline gÃ¶re araÅŸtÄ±rma sÄ±nÄ±rlarÄ±nÄ± belirler."),
            ("Hedefleri inceler", "Potansiyel ÅŸirketlere iliÅŸkin aÃ§Ä±k ve kullanÄ±labilir baÄŸlamÄ± toplar."),
            ("SatÄ±ÅŸa taÅŸÄ±r", "Ä°ncelenen hedefler iÃ§in iletiÅŸim taslaÄŸÄ± ve CRM takip adÄ±mÄ± oluÅŸturur."),
        ],
        "sections": [("insan-onayi", "KontrollÃ¼ dÄ±ÅŸ iletiÅŸim", "Yurt dÄ±ÅŸÄ± iletiÅŸimde dil, yerel beklentiler, veri kullanÄ±mÄ± ve ekip onayÄ± sÃ¼recin bir parÃ§asÄ±dÄ±r.")],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir Ã¼retici hedef Ã¼lke ve alÄ±cÄ± profilini belirler. Sistem uygun ÅŸirketleri araÅŸtÄ±rÄ±r, her biri iÃ§in kÄ±sa gerekÃ§e sunar; satÄ±ÅŸ ekibi seÃ§tikleri hedeflerle iletiÅŸime geÃ§er."),
        "questions": [("Sistem otomatik e-posta gÃ¶nderir mi?", "Ä°letiÅŸim akÄ±ÅŸÄ± teknik ve hukuki koÅŸullara gÃ¶re planlanÄ±r. Onay gerektiren adÄ±mlar ÅŸirket politikasÄ±na gÃ¶re belirlenir.")],
        "related": [("/b2b-outreach/", "B2B Outreach"), ("/ai-satis-ajani/", "AI SatÄ±ÅŸ AjanÄ±")],
    },
    "b2b-hizmetler": {
        "category": "SektÃ¶rler / B2B hizmetler",
        "title": "B2B hizmet ÅŸirketleri iÃ§in satÄ±ÅŸ akÄ±ÅŸÄ±",
        "summary": "Web, telefon ve satÄ±ÅŸ temaslarÄ±ndan gelen talepleri nitelendiren; gÃ¶rÃ¼ÅŸme baÄŸlamÄ±nÄ± satÄ±ÅŸ ekibine taÅŸÄ±yan AI agent sistemleri.",
        "lead": "Uzun karar sÃ¼reÃ§lerinde ilk gÃ¶rÃ¼ÅŸmeden sonraki takip kolayca kopabilir. Raiko, mÃ¼ÅŸteri iletiÅŸimini ve CRM adÄ±mlarÄ±nÄ± aynÄ± sÃ¼reÃ§te ele alÄ±r.",
        "steps": [
            ("Ä°lk temasÄ± alÄ±r", "Hizmet, ihtiyaÃ§ ve ÅŸirket baÄŸlamÄ±nÄ± toplar."),
            ("UygunluÄŸu deÄŸerlendirir", "TanÄ±mlanmÄ±ÅŸ kriterlere gÃ¶re talebi dÃ¼zenler ve eksik bilgiyi belirler."),
            ("Devreder", "SatÄ±ÅŸ ekibine konuÅŸma Ã¶zeti ve Ã¶nerilen takip adÄ±mÄ±nÄ± sunar."),
        ],
        "sections": [("uzun-satis", "Uzun satÄ±ÅŸ dÃ¶ngÃ¼sÃ¼", "Birden fazla gÃ¶rÃ¼ÅŸme ve karar verici olduÄŸunda mÃ¼ÅŸteri geÃ§miÅŸinin tek kayÄ±tta korunmasÄ± Ã¶nem kazanÄ±r.")],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir ÅŸirket hizmet kapsamÄ±nÄ± sorar. Ajan temel bilgiyi paylaÅŸÄ±r, ihtiyaÃ§ ve zamanlamayÄ± netleÅŸtirir; ekip gÃ¶rÃ¼ÅŸmeye hazÄ±rlanÄ±rken bu Ã¶zet CRM kaydÄ±nda yer alÄ±r."),
        "questions": [("SatÄ±ÅŸ temsilcisi hangi noktada devreye girer?", "GÃ¶rÃ¼ÅŸme karmaÅŸÄ±klaÅŸtÄ±ÄŸÄ±nda, Ã¶zel teklif gerektiÄŸinde veya iliÅŸki yÃ¶netimi Ã¶nem kazandÄ±ÄŸÄ±nda insan devri tasarlanÄ±r.")],
        "related": [("/akilli-crm/", "AkÄ±llÄ± CRM"), ("/ai-satis-ajani/", "AI SatÄ±ÅŸ AjanÄ±")],
    },
    "emlak": {
        "category": "SektÃ¶rler / Emlak",
        "title": "Emlak danÄ±ÅŸmanlarÄ± iÃ§in yapay zekÃ¢ mÃ¼ÅŸteri asistanÄ±",
        "summary": "Ä°lan, telefon ve WhatsApp Ã¼zerinden gelen alÄ±cÄ± veya kiracÄ± taleplerini dÃ¼zenleyen; portfÃ¶y ilgisini ve gÃ¶rÃ¼ÅŸme takibini ekip iÃ§in gÃ¶rÃ¼nÃ¼r kÄ±lan AI akÄ±ÅŸlarÄ±.",
        "lead": "Emlakta aynÄ± ilan iÃ§in farklÄ± kanallardan gelen sorular, hÄ±zlÄ± ve doÄŸru geri dÃ¶nÃ¼ÅŸ gerektirir. Ajan, onaylÄ± ilan bilgisiyle ilk sorularÄ± karÅŸÄ±layabilir; mÃ¼ÅŸterinin aradÄ±ÄŸÄ± Ã¶zellikleri ve iletiÅŸim tercihini danÄ±ÅŸmana aktarabilir.",
        "steps": [
            ("Talebi toplar", "Ä°lan kaynaÄŸÄ±nÄ±, ilgili mÃ¼lkÃ¼ ve alÄ±m veya kiralama niyetini kaydeder."),
            ("Ä°htiyacÄ± netleÅŸtirir", "Konum, bÃ¼tÃ§e, oda sayÄ±sÄ± ve uygun gÃ¶rÃ¼ÅŸme zamanÄ± gibi bilgileri sorar."),
            ("DanÄ±ÅŸmana devreder", "Talebi ilgili portfÃ¶yle eÅŸleÅŸtirir; gÃ¶sterim isteÄŸini ve sonraki adÄ±mÄ± CRM'de takip edilecek hÃ¢le getirir."),
        ],
        "sections": [
            ("ilan-bilgisi", "GÃ¼ncel portfÃ¶y bilgisi", "Fiyat, mÃ¼saitlik ve ilan durumu deÄŸiÅŸebilir. Ajan yalnÄ±zca gÃ¼ncel ve onaylÄ± kaynaÄŸa baÄŸlÄ± bilgiyi paylaÅŸmalÄ±; doÄŸrulayamadÄ±ÄŸÄ± durumda danÄ±ÅŸmana yÃ¶nlendirmelidir."),
            ("gorusme-takibi", "GÃ¶sterim ve takip akÄ±ÅŸÄ±", "Portaldan, siteden veya WhatsApp'tan gelen talepler aynÄ± mÃ¼ÅŸteri kaydÄ±nda birleÅŸtirilebilir. GÃ¶sterim sonrasÄ± geri bildirim ve sonraki temas ekibin kontrolÃ¼nde kalÄ±r."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir alÄ±cÄ± ilan baÄŸlantÄ±sÄ±yla WhatsApp'tan yazar. Asistan ilanÄ± ve aranan Ã¶zellikleri netleÅŸtirir, gÃ¶sterim iÃ§in uygun zamanlarÄ± toplar. DanÄ±ÅŸman ilan durumunu doÄŸrular, randevuyu onaylar ve gÃ¶rÃ¼ÅŸme sonucunu CRM'e iÅŸler."),
        "questions": [
            ("Portaldan gelen talepler CRM'e aktarÄ±labilir mi?", "KullanÄ±lan portalÄ±n eriÅŸim ve entegrasyon olanaklarÄ± incelendikten sonra uygun kayÄ±t akÄ±ÅŸÄ± tasarlanabilir."),
            ("Asistan fiyat pazarlÄ±ÄŸÄ± yapar mÄ±?", "PazarlÄ±k ve baÄŸlayÄ±cÄ± teklifler danÄ±ÅŸmana bÄ±rakÄ±lÄ±r. Asistan talebi ve gÃ¶rÃ¼ÅŸme baÄŸlamÄ±nÄ± dÃ¼zenleyebilir."),
        ],
        "related": [("/ai-chatbot/", "AI Chatbot"), ("/akilli-crm/", "AkÄ±llÄ± CRM"), ("/ai-call-agent/", "AI Call Agent")],
    },
    "otomotiv": {
        "category": "SektÃ¶rler / Otomotiv",
        "title": "Otomotiv satÄ±ÅŸÄ±nda yapay zekÃ¢ ile talep ve randevu takibi",
        "summary": "AraÃ§ ilanÄ±, web sitesi, telefon ve mesajlaÅŸmadan gelen talepleri karÅŸÄ±layan; model ilgisini, test sÃ¼rÃ¼ÅŸÃ¼ isteÄŸini ve satÄ±ÅŸ takibini dÃ¼zenleyen AI akÄ±ÅŸlarÄ±.",
        "lead": "AraÃ§ satÄ±n almak isteyen kiÅŸi stok, donanÄ±m, finansman seÃ§enekleri veya takas hakkÄ±nda farklÄ± kanallardan soru sorabilir. Ajan ilk temasÄ± ve bilgi toplamayÄ± destekler; gÃ¼ncel stok, fiyat ve satÄ±ÅŸ koÅŸullarÄ± yetkili ekip tarafÄ±ndan doÄŸrulanÄ±r.",
        "steps": [
            ("Ä°lgiyi belirler", "AraÃ§, model veya ilan bilgisini ve mÃ¼ÅŸterinin satÄ±n alma zamanlamasÄ±nÄ± kaydeder."),
            ("SorularÄ± ayÄ±rÄ±r", "OnaylÄ± araÃ§ bilgisini paylaÅŸÄ±r; stok, fiyat, takas ve finansman sorularÄ±nÄ± uygun uzmana yÃ¶nlendirir."),
            ("Takibi baÅŸlatÄ±r", "Test sÃ¼rÃ¼ÅŸÃ¼ veya gÃ¶rÃ¼ÅŸme talebini satÄ±ÅŸ ekibine aktarÄ±r ve sonraki adÄ±mÄ± CRM'de izlenebilir kÄ±lar."),
        ],
        "sections": [
            ("stok-ve-fiyat", "Stok ve fiyat doÄŸruluÄŸu", "AraÃ§ mÃ¼saitliÄŸi, kampanya ve fiyatlar deÄŸiÅŸebilir. CanlÄ± sistem baÄŸlantÄ±sÄ± yoksa ajan kesin teyit vermek yerine gÃ¼ncel bilgiyi satÄ±ÅŸ temsilcisinden istemelidir."),
            ("test-surusu", "Test sÃ¼rÃ¼ÅŸÃ¼nden satÄ±ÅŸ gÃ¶rÃ¼ÅŸmesine", "Test sÃ¼rÃ¼ÅŸÃ¼ iÃ§in tercih edilen model, lokasyon ve zaman toplanabilir. Randevu ancak bayi takvimi ve ekip onayÄ±yla kesinleÅŸir; gÃ¶rÃ¼ÅŸme sonucu aynÄ± mÃ¼ÅŸteri kaydÄ±nda izlenir."),
        ],
        "example": ("Ã–rnek akÄ±ÅŸ", "Bir mÃ¼ÅŸteri web sitesinde belirli bir model iÃ§in test sÃ¼rÃ¼ÅŸÃ¼ ister. Asistan iletiÅŸim bilgisini ve uygun zamanÄ±nÄ± alÄ±r, talebi satÄ±ÅŸ ekibine iletir. Temsilci stok ve takvimi doÄŸrulayÄ±p randevuyu kesinleÅŸtirir; takip gÃ¶revi CRM'e kaydedilir."),
        "questions": [
            ("Ä°kinci el araÃ§ ilanlarÄ± iÃ§in de kullanÄ±labilir mi?", "Evet, ilan ve araÃ§ bilgilerinin gÃ¼ncel tutulduÄŸu bir kaynak varsa ilk sorular ve gÃ¶rÃ¼ÅŸme talepleri iÃ§in akÄ±ÅŸ tasarlanabilir."),
            ("Takas veya kredi teklifi oluÅŸturur mu?", "Bu konularda baÄŸlayÄ±cÄ± sonuÃ§ Ã¼retmez. Ä°lgili bilgileri toplayÄ±p yetkili satÄ±ÅŸ veya finansman ekibine aktarabilir."),
        ],
        "related": [("/ai-call-agent/", "AI Call Agent"), ("/ai-chatbot/", "AI Chatbot"), ("/akilli-crm/", "AkÄ±llÄ± CRM")],
    },
}


decision_sections = {
    "ai-call-agent": [
        ("Kurulumda hangi bilgiler gerekir?", "Ã–nce Ã§aÄŸrÄ± tÃ¼rleri, sÄ±k sorulan sorular, mesai saatleri, yÃ¶nlendirme kurallarÄ± ve kullanÄ±lacak telefon altyapÄ±sÄ± belirlenir. Randevu veya CRM kaydÄ± isteniyorsa takvim, alanlar ve eriÅŸim yetkileri ayrÄ±ca incelenir. Pilot akÄ±ÅŸ, gerÃ§ek gÃ¶rÃ¼ÅŸmelerden seÃ§ilen Ã¶rneklerle test edilmelidir."),
        ("Ä°nsana devir ve Ã§Ä±ktÄ±", "Ajan doÄŸrulayamadÄ±ÄŸÄ± bilgi, ÅŸikÃ¢yet veya Ã¶zel teklif talebinde ilgili kiÅŸiye aktarÄ±m yapar. Ekip iÃ§in beklenen Ã§Ä±ktÄ±; arama nedeni, toplanan iletiÅŸim bilgisi, kÄ±sa gÃ¶rÃ¼ÅŸme Ã¶zeti ve aÃ§Ä±k sonraki adÄ±mdÄ±r. KayÄ±t ve aktarÄ±m kapsamÄ± kurulumda kararlaÅŸtÄ±rÄ±lÄ±r."),
    ],
    "ai-chatbot": [
        ("Web ve WhatsApp akÄ±ÅŸlarÄ± nasÄ±l ayrÄ±lÄ±r?", "Web sohbeti, ziyaretÃ§inin baktÄ±ÄŸÄ± sayfaya gÃ¶re Ã¼rÃ¼n veya hizmet sorusunu karÅŸÄ±layabilir. WhatsApp akÄ±ÅŸÄ±nda iÅŸletme hesabÄ±, kanal izinleri, mesaj kurallarÄ± ve ekip devri ayrÄ±ca planlanÄ±r. Her iki kanalda da onaylÄ± bilgi kaynaÄŸÄ± ve gÃ¼ncelleme sorumlusu tanÄ±mlanmalÄ±dÄ±r."),
        ("SatÄ±ÅŸ ekibine ne aktarÄ±lÄ±r?", "GÃ¶rÃ¼ÅŸmenin tamamÄ± yerine talep konusu, kaynak kanal, mÃ¼ÅŸterinin verdiÄŸi bilgiler ve cevaplanmamÄ±ÅŸ soru Ã¶zetlenebilir. MÃ¼ÅŸteri bir temsilci istediÄŸinde veya konu bilgi kaynaÄŸÄ±nÄ± aÅŸtÄ±ÄŸÄ±nda konuÅŸma insan ekibe yÃ¶nlendirilir. CRM baÄŸlantÄ±sÄ± varsa alan eÅŸleÅŸtirmesi ve mÃ¼kerrer kayÄ±t kontrolÃ¼ yapÄ±lÄ±r."),
    ],
    "akilli-crm": [
        ("Mevcut sistemle baÅŸlangÄ±Ã§", "Ã–nce mÃ¼ÅŸteri, ÅŸirket, fÄ±rsat ve gÃ¶rev kayÄ±tlarÄ±nÄ±n nerede tutulduÄŸu belirlenir. Form, telefon ve sohbetten gelen aynÄ± kiÅŸiyi tanÄ±mak iÃ§in alan eÅŸleÅŸtirmesi yapÄ±lÄ±r. Yazma yetkisi verilmeden Ã¶nce Ã¶rnek kayÄ±tlar ve hatalÄ± veri senaryolarÄ± birlikte gÃ¶zden geÃ§irilir."),
        ("Ã–rnek takip Ã§Ä±ktÄ±sÄ±", "Bir talep iÃ§in kaynak, ihtiyaÃ§, gÃ¶rÃ¼ÅŸme Ã¶zeti, sorumlu kiÅŸi ve takip tarihi tek kayÄ±tta gÃ¶rÃ¼lebilir. Otomasyon eksik bilgiyi iÅŸaretleyebilir; Ã¶ncelik puanÄ± ve satÄ±ÅŸ kararÄ± ÅŸirketin Ã¶lÃ§Ã¼tlerine gÃ¶re insan tarafÄ±ndan doÄŸrulanmalÄ±dÄ±r."),
    ],
    "ai-satis-ajani": [
        ("AjanÄ±n yetki sÄ±nÄ±rÄ±", "Åirket araÅŸtÄ±rmasÄ±, talep Ã¶zeti ve takip Ã¶nerisi otomatik hazÄ±rlanabilir. DÄ±ÅŸarÄ± gÃ¶nderilen kiÅŸiselleÅŸtirilmiÅŸ mesaj, indirim, taahhÃ¼t veya teklif iÃ§in insan onayÄ± gerekecek noktalar ayrÄ±ca tanÄ±mlanÄ±r. KaynaklarÄ±n doÄŸruluÄŸu ve eski kayÄ±tlarÄ±n temizliÄŸi sonucun kalitesini belirler."),
        ("Pilot nasÄ±l Ã¶lÃ§Ã¼lÃ¼r?", "Ä°lk pilotta nitelikli talep tanÄ±mÄ±, gÃ¶rÃ¼ÅŸmeye dÃ¶nÃ¼ÅŸen aday ve satÄ±ÅŸ temsilcisinin dÃ¼zeltme ihtiyacÄ± izlenir. YalnÄ±zca Ã¼retilen mesaj veya lead sayÄ±sÄ±na bakmak, satÄ±ÅŸa katkÄ±yÄ± gÃ¶stermez. CRM'deki fÄ±rsat aÅŸamalarÄ± pilot Ã¶ncesinde netleÅŸtirilmelidir."),
    ],
    "b2b-outreach": [
        ("AraÅŸtÄ±rmadan ilk temasa", "Hedef sektÃ¶r, ÅŸirket Ã¶lÃ§eÄŸi, bÃ¶lge ve hariÃ§ tutulacak profiller birlikte tanÄ±mlanÄ±r. Her hedef iÃ§in kamuya aÃ§Ä±k ve izinli kaynaklardan bir gerekÃ§e hazÄ±rlanÄ±r; belirsiz ÅŸirket bilgisi otomatik mesajda kesin gerÃ§ek gibi kullanÄ±lmaz. SatÄ±ÅŸ ekibi listeyi ve iletiÅŸim taslaÄŸÄ±nÄ± onaylar."),
        ("Ä°letiÅŸim ve Ã¶lÃ§Ã¼m sÄ±nÄ±rlarÄ±", "Kanal kurallarÄ±, veri kullanÄ±mÄ±, durdurma koÅŸullarÄ± ve yanÄ±t geldiÄŸinde insan devri planlanÄ±r. YanÄ±t oranÄ±na ek olarak olumlu yanÄ±t, gerÃ§ekleÅŸen toplantÄ± ve nitelikli fÄ±rsat takip edilir. AynÄ± kiÅŸiye birden Ã§ok kanaldan Ã§eliÅŸkili veya tekrarlÄ± mesaj gitmesi engellenmelidir."),
    ],
    "otomasyonlar": [
        ("Teslimat kapsamÄ± nasÄ±l belirlenir?", "Tetikleyici, kullanÄ±lan uygulamalar, okunacak ve yazÄ±lacak alanlar, hata bildirimi ve bakÄ±m sorumlusu baÅŸlangÄ±Ã§ta yazÄ±lÄ± hÃ¢le getirilir. Ã–nce tek bir tekrarlÄ± sÃ¼reÃ§te pilot yapÄ±lmasÄ±, istisnalarÄ±n gÃ¶rÃ¼lmesini saÄŸlar. Entegrasyon yetkileri ve veri akÄ±ÅŸÄ± kurumun sistemlerine baÄŸlÄ±dÄ±r."),
        ("Hata durumunda ne olur?", "YanlÄ±ÅŸ veya eksik veri, eriÅŸim kesintisi ve beklenmeyen yanÄ±t iÃ§in gÃ¼venli durma ve insan incelemesi adÄ±mlarÄ± tanÄ±mlanÄ±r. Her iÅŸlemin sonucu izlenebilir olmalÄ±; kritik kayÄ±tlarÄ±n sessizce deÄŸiÅŸmesi Ã¶nlenmelidir."),
    ],
    "saglik-turizmi": [
        ("Ã‡ok dilli ilk temas", "Talebin dili, Ã¼lkesi, tercih ettiÄŸi iletiÅŸim kanalÄ± ve operasyonel sorusu kaydedilebilir. Randevu, ulaÅŸÄ±m ve sÃ¼reÃ§ yanÄ±tlarÄ± yalnÄ±zca kurumun onayladÄ±ÄŸÄ± bilgilere dayanÄ±r. TÄ±bbi uygunluk veya tedavi sonucuna iliÅŸkin sorular yetkili klinik ekibe aktarÄ±lÄ±r."),
    ],
    "ihracat-uretim": [
        ("Hedef araÅŸtÄ±rmasÄ±nÄ±n doÄŸrulanmasÄ±", "Ãœlke, alÄ±cÄ± tipi ve Ã¼rÃ¼n kullanÄ±mÄ±na gÃ¶re ÅŸirketler araÅŸtÄ±rÄ±labilir. Listenin gÃ¼ncelliÄŸi, kaynak baÄŸlantÄ±larÄ± ve satÄ±ÅŸ ekibinin deÄŸerlendirmesi korunur; yalnÄ±zca ÅŸirket adÄ± eÅŸleÅŸmesine bakÄ±larak uygun mÃ¼ÅŸteri kabul edilmez."),
    ],
    "b2b-hizmetler": [
        ("Birden fazla karar verici", "Ä°lk talepte ÅŸirket ihtiyacÄ±, proje kapsamÄ± ve zamanlama ayrÄ± alanlarda tutulabilir. GÃ¶rÃ¼ÅŸmeye farklÄ± kiÅŸiler katÄ±ldÄ±ÄŸÄ±nda rolleri ve karar konularÄ± CRM kaydÄ±na eklenir. Teklif, kapsam ve pazarlÄ±k adÄ±mlarÄ± insan ekibin kontrolÃ¼nde kalÄ±r."),
    ],
    "emlak": [
        ("Kurulum iÃ§in gerekenler", "GÃ¼ncel portfÃ¶y kaynaÄŸÄ±, ilan kimliÄŸi, danÄ±ÅŸman atama kuralÄ± ve gÃ¶sterim takvimi belirlenir. Portal entegrasyonu varsa izinleri incelenir; yoksa web formu ve mesajlaÅŸma gibi mevcut kanallardan baÅŸlanabilir."),
    ],
    "otomotiv": [
        ("Bayi sistemleriyle Ã§alÄ±ÅŸma", "AraÃ§ kataloÄŸu, stok kaynaÄŸÄ±, lokasyon ve test sÃ¼rÃ¼ÅŸÃ¼ takvimi birlikte incelenir. CanlÄ± baÄŸlantÄ±sÄ± olmayan stok veya kampanya bilgisi kesinleÅŸtirilmez. GÃ¶rÃ¼ÅŸme sonrasÄ± teklif ve takas sÃ¼reci satÄ±ÅŸ temsilcisine bÄ±rakÄ±lÄ±r."),
    ],
}

guide_links = {
    "ai-call-agent": "ai-call-agent-nedir",
    "ai-chatbot": "chatbot-ai-agent-canli-destek",
    "akilli-crm": "telefon-crm-satis-takibi",
    "ai-satis-ajani": "ai-sdr-nedir",
    "b2b-outreach": "ai-sdr-nedir",
    "otomasyonlar": "telefon-crm-satis-takibi",
    "emlak": "emlak-yapay-zeka-asistani",
    "otomotiv": "otomotiv-test-surusu-takibi",
}


def page_body(data):
    steps = "".join(f'<li><span>0{i}</span><div><h3>{title}</h3><p>{copy}</p></div></li>' for i, (title, copy) in enumerate(data["steps"], 1))
    sections = "".join(f'<section class="detail-section" id="{sid}"><div class="wrap detail-columns"><p class="eyebrow">{data["category"]}</p><div><h2>{heading}</h2><p>{copy}</p></div></div></section>' for sid, heading, copy in data["sections"])
    questions = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in data["questions"])
    related = "".join(f'<a href="{href}">{label}<span aria-hidden="true">â†—</span></a>' for href, label in data["related"])
    slug = next(key for key, value in {**pages, **sectors}.items() if value is data)
    decision = "".join(f'<section class="detail-section"><div class="wrap detail-columns"><p class="eyebrow">Karar rehberi</p><div><h2>{heading}</h2><p>{copy}</p></div></div></section>' for heading, copy in decision_sections.get(slug, []))
    guide_slug = guide_links.get(slug)
    guide_ref = f'<section class="guide-ref"><div class="wrap"><p class="eyebrow">Daha ayrÄ±ntÄ±lÄ± okuyun</p><a href="/rehberler/{guide_slug}/">{GUIDES[guide_slug]["title"]} <span aria-hidden="true">â†—</span></a></div></section>' if guide_slug else ""
    example_title, example_copy = data["example"]
    contact = contact_link(data["category"].split(" / ")[-1] + " hakkÄ±nda gÃ¶rÃ¼ÅŸme talebi")
    page_slug = data["category"].split(" / ")[-1].lower().replace(" ", "-")
    return f'''
    <section class="detail-hero"><div class="wrap"><a class="back-link" href="/">â† Ana sayfa</a><p class="hero-kicker">{data["category"]}</p><h1>{data["title"]}</h1><p class="detail-summary">{data["summary"]}</p><a class="raiko-button raiko-button--shine" href="#is-akisi" aria-label="Ä°ÅŸ akÄ±ÅŸÄ±nÄ± gÃ¶r"><span class="raiko-button__surface">Ä°ÅŸ akÄ±ÅŸÄ±nÄ± gÃ¶r <span aria-hidden="true">â†˜</span></span></a></div></section>
    <section class="detail-lead"><div class="wrap detail-columns"><p class="eyebrow">YaklaÅŸÄ±m</p><p>{data["lead"]}</p></div></section>
    <section class="detail-process" id="is-akisi"><div class="wrap detail-columns"><div><p class="eyebrow">Ä°ÅŸ akÄ±ÅŸÄ±</p><h2>NasÄ±l Ã§alÄ±ÅŸÄ±r?</h2></div><ol>{steps}</ol></div></section>
    {sections}
    {decision}
    {guide_ref}
    <section class="example-band"><div class="wrap detail-columns"><p class="eyebrow">{example_title}</p><p>{example_copy}</p></div></section>
    <section class="detail-faq"><div class="wrap detail-columns"><div><p class="eyebrow">SÄ±k sorulanlar</p><h2>AÃ§Ä±k yanÄ±tlar.</h2></div><div>{questions}</div></div></section>
    {contact_form(page_topic=data["category"].split(" / ")[-1])}
    <section class="related"><div class="wrap"><p class="eyebrow">Ä°lgili Ã§Ã¶zÃ¼mler</p><div>{related}</div></div></section>
    {footer(show_cta=True)}
    '''



def contact_form(page_topic=""):
    topic_value = page_topic if page_topic else ""
    return f'''<section class="raiko-contact-section" id="iletisim-formu">
  <div class="wrap raiko-contact-inner">
    <div class="raiko-contact-copy">
      <p class="eyebrow" style="color:var(--yellow)">Sonraki adÄ±m</p>
      <h2 class="raiko-contact-heading">Kendi sÃ¼recinizi<br><span>konuÅŸalÄ±m.</span></h2>
      <p class="raiko-contact-desc">SektÃ¶rÃ¼nÃ¼zÃ¼ ve Ã§Ã¶zmek istediÄŸiniz sorunu kÄ±saca yazÄ±n. Birlikte deÄŸerlendirelim.</p>
      <div class="raiko-contact-trust">
        <div class="raiko-trust-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>24 saat iÃ§inde dÃ¶nÃ¼ÅŸ</span></div>
        <div class="raiko-trust-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>Ãœcretiz ilk gÃ¶rÃ¼ÅŸme</span></div>
        <div class="raiko-trust-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>BaÄŸlayÄ±cÄ± taahhÃ¼t yok</span></div>
      </div>
    </div>
    <div class="raiko-contact-form-wrap">
      <form class="raiko-form" data-topic="{topic_value}" novalidate>
        <div class="raiko-field">
          <input class="raiko-input" type="text" id="rf-name" name="name" required placeholder=" " autocomplete="name">
          <label class="raiko-label" for="rf-name">AdÄ±nÄ±z</label>
        </div>
        <div class="raiko-field">
          <input class="raiko-input" type="email" id="rf-email" name="email" required placeholder=" " autocomplete="email">
          <label class="raiko-label" for="rf-email">E-posta adresiniz</label>
        </div>
        <div class="raiko-field">
          <input class="raiko-input" type="text" id="rf-company" name="company" placeholder=" " autocomplete="organization">
          <label class="raiko-label" for="rf-company">Åirket / SektÃ¶r</label>
        </div>
        <div class="raiko-field">
          <textarea class="raiko-input raiko-textarea" id="rf-message" name="message" required placeholder=" " rows="4"></textarea>
          <label class="raiko-label" for="rf-message">Ne hakkÄ±nda gÃ¶rÃ¼ÅŸmek istersiniz?</label>
        </div>
        <button class="raiko-submit" type="submit">
          <span class="raiko-submit-text">Mesaj gÃ¶nder</span>
          <span class="raiko-submit-arrow" aria-hidden="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </span>
        </button>
        <p class="raiko-form-note">veya doÄŸrudan yazÄ±n: <a href="mailto:info@raiko.tech">info@raiko.tech</a></p>
        <div class="raiko-form-success" hidden>
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="20 6 9 17 4 12"/></svg>
          <p>MesajÄ±nÄ±z alÄ±ndÄ±. En kÄ±sa sÃ¼rede size dÃ¶nÃ¼ÅŸ yapacaÄŸÄ±z.</p>
        </div>
      </form>
    </div>
  </div>
</section>'''


def footer(show_cta=False):
    cta_html = ""
    if show_cta:
        cta_html = '''
    <div class="footer-cta-card">
      <div class="footer-cta-content">
        <div class="footer-status-pill">
          <span class="status-dot"></span>
          <span>Ä°ÅŸletmenize Ã¶zel yapay zekÃ¢ akÄ±ÅŸlarÄ±</span>
        </div>
        <h3 class="footer-cta-title">Yapay zekÃ¢ Ã§alÄ±ÅŸanlarÄ±nÄ±zla iÅŸinizi bir adÄ±m Ã¶ne taÅŸÄ±yÄ±n.</h3>
        <p class="footer-cta-desc">TelefonlarÄ± yanÄ±tlayan, mesajlarÄ± karÅŸÄ±layan ve CRM sÃ¼recini ilerleten sistemleri bugÃ¼n hayata geÃ§irin.</p>
      </div>
      <div class="footer-cta-actions">
        <a class="raiko-button raiko-button--shine" href="mailto:info@raiko.tech?subject=Raiko%20demo%20talebi" aria-label="Demo talep et">
          <span class="raiko-button__surface">Demo talep et <span aria-hidden="true">â†—</span></span>
        </a>
        <a class="footer-contact-link" href="mailto:info@raiko.tech">
          <span>info@raiko.tech</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
        </a>
      </div>
    </div>'''

    status_pill_home = ""
    if not show_cta:
        status_pill_home = '''
        <div class="footer-status-pill">
          <span class="status-dot"></span>
          <span>Åirketinize gÃ¶re tasarlanan AI sistemleri</span>
        </div>'''

    return f'''<footer class="site-footer" role="contentinfo">
  <div class="wrap">
    {cta_html}
    <div class="footer-main">
      <div class="footer-col footer-col--brand">
        <a class="brand" href="/" aria-label="Raiko ana sayfa">
          <img src="/raiko-logo.webp" alt="Raiko" width="144" height="48">
          <small>AI Techs</small>
        </a>
        <p class="footer-brand-desc">
          TelefonlarÄ± yanÄ±tlayan, mesajlarÄ± karÅŸÄ±layan, mÃ¼ÅŸteri adaylarÄ±nÄ± nitelendiren ve CRM sÃ¼recini ilerleten yapay zekÃ¢ Ã§alÄ±ÅŸanlarÄ± kuruyoruz.
        </p>
        {status_pill_home}
        <div class="footer-contact-info">
          <div class="footer-info-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            <a href="mailto:info@raiko.tech">info@raiko.tech</a>
          </div>
          <div class="footer-info-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
            <span>Ä°stanbul, TÃ¼rkiye</span>
          </div>
        </div>
      </div>

      <div class="footer-col">
        <p class="footer-heading">Ã‡Ã¶zÃ¼mler</p>
        <ul class="footer-nav-list">
          <li><a href="/ai-call-agent/">AI Call Agent <span class="footer-sub">Sesli Ajan</span></a></li>
          <li><a href="/ai-chatbot/">AI Chatbot <span class="footer-sub">WhatsApp & Web</span></a></li>
          <li><a href="/akilli-crm/">AkÄ±llÄ± CRM <span class="footer-sub">SatÄ±ÅŸ Takibi</span></a></li>
          <li><a href="/ai-satis-ajani/">AI SatÄ±ÅŸ AjanÄ± <span class="footer-sub">Lead SDR</span></a></li>
          <li><a href="/b2b-outreach/">B2B Outreach <span class="footer-sub">Ä°letiÅŸim AkÄ±ÅŸÄ±</span></a></li>
          <li><a href="/otomasyonlar/">Ã–zel Otomasyonlar <span class="footer-sub">Entegrasyon</span></a></li>
        </ul>
      </div>

      <div class="footer-col">
        <p class="footer-heading">SektÃ¶rler</p>
        <ul class="footer-nav-list">
          <li><a href="/saglik-turizmi/">SaÄŸlÄ±k Turizmi</a></li>
          <li><a href="/ihracat-uretim/">Ä°hracat ve Ãœretim</a></li>
          <li><a href="/b2b-hizmetler/">B2B Hizmetler</a></li>
          <li><a href="/emlak/">Emlak</a></li>
          <li><a href="/otomotiv/">Otomotiv</a></li>
          <li><a href="/#kullanim">MÃ¼ÅŸteri DesteÄŸi</a></li>
          <li><a href="/#sistemler">NasÄ±l Ã‡alÄ±ÅŸÄ±r?</a></li>
          <li><a href="/#sorular">SÄ±k Sorulan Sorular</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <p class="footer-heading">Kaynaklar</p>
        <ul class="footer-nav-list">
          <li><a href="/rehberler/">TÃ¼m Rehberler</a></li>
          <li><a href="/rehberler/ai-call-agent-nedir/">AI Call Agent Nedir?</a></li>
          <li><a href="/rehberler/ai-sdr-nedir/">AI SDR SatÄ±ÅŸ SÃ¼reci</a></li>
          <li><a href="/rehberler/chatbot-ai-agent-canli-destek/">Chatbot vs AI Agent</a></li>
          <li><a href="/rehberler/telefon-crm-satis-takibi/">Ã–rnek AkÄ±ÅŸ Modeli</a></li>
          <li><a href="/#ust">Ekosistem PlatformlarÄ±</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-divider"></div>

    <div class="footer-bottom">
      <div class="footer-copy">
        <span>Â© <span class="year">2026</span> Raiko AI Technologies Inc. TÃ¼m haklarÄ± saklÄ±dÄ±r.</span>
      </div>
      <a class="footer-back-to-top" href="#ust" aria-label="SayfanÄ±n baÅŸÄ±na dÃ¶n">
        <span>BaÅŸa dÃ¶n</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m18 15-6-6-6 6"/></svg>
      </a>
    </div>
  </div>
</footer>'''


def resources_body():
    articles = "".join(
        f'<article class="resource-article"><div class="wrap detail-columns"><p class="eyebrow">{i:02d} / Rehber</p><div><h2><a href="/rehberler/{slug}/">{guide["title"]}</a></h2><p>{guide["description"]}</p><a class="text-link" href="/rehberler/{slug}/">Rehberi oku <span aria-hidden="true">â†—</span></a></div></div></article>'
        for i, (slug, guide) in enumerate(GUIDES.items(), 1)
    )
    return '''<section class="detail-hero resource-hero"><div class="wrap"><a class="back-link" href="/">â† Ana sayfa</a><p class="hero-kicker">Kaynaklar / Rehberler</p><h1>DoÄŸru sistemi seÃ§mek iÃ§in aÃ§Ä±k rehberler.</h1><p class="detail-summary">Ã‡aÄŸrÄ± ajanÄ±, AI SDR, chatbot, CRM ve sektÃ¶r akÄ±ÅŸlarÄ± hakkÄ±nda Ã¶rneklerle hazÄ±rlanmÄ±ÅŸ karar rehberleri.</p></div></section>''' + articles + footer(show_cta=True)


def guide_body(guide):
    sections = "".join(
        f'<section class="resource-article"><div class="wrap detail-columns"><p class="eyebrow">Rehber</p><div><h2>{heading}</h2><p>{copy}</p></div></div></section>'
        for heading, copy in guide["sections"]
    )
    related = "".join(f'<a href="{href}">{label}<span aria-hidden="true">â†—</span></a>' for href, label in guide["related"])
    return f'''<section class="detail-hero resource-hero"><div class="wrap"><a class="back-link" href="/rehberler/">â† TÃ¼m rehberler</a><p class="hero-kicker">Raiko / Rehber</p><h1>{guide["title"]}</h1><p class="detail-summary">{guide["description"]}</p></div></section>
    <section class="detail-lead"><div class="wrap detail-columns"><p class="eyebrow">KÄ±sa yanÄ±t</p><p>{guide["intro"]}</p></div></section>
    {sections}
    <section class="related"><div class="wrap"><p class="eyebrow">Ä°lgili Ã§Ã¶zÃ¼mler</p><div>{related}</div></div></section>
    {footer(show_cta=True)}'''


ai_platforms = [
    ("ChatGPT", "https://chatgpt.com/", "https://cdn.oaistatic.com/assets/favicon-miwirzcw.ico"),
    ("Gemini", "https://gemini.google.com/", "https://www.gstatic.com/images/branding/product/2x/gemini_48dp.png"),
    ("Perplexity", "https://www.perplexity.ai/", "https://www.perplexity.ai/favicon.svg"),
    ("Hugging Face", "https://huggingface.co/", "https://huggingface.co/favicon.ico"),
    ("Claude", "https://claude.ai/", "https://www.anthropic.com/favicon.ico"),
    ("DeepSeek", "https://www.deepseek.com/", "https://www.deepseek.com/favicon.ico"),
    ("Kimi", "https://www.kimi.ai/", "https://www.kimi.ai/favicon.ico"),
    ("Manus", "https://manus.im/", "https://manus.im/icon.svg?icon.2kbcs13ndm9it.svg"),
    ("Grok", "https://grok.com/", "https://grok.com/images/favicon.svg"),
    ("Qwen", "https://qwen.ai/", "https://img.alicdn.com/imgextra/i4/O1CN01OXv3EM1FN8t9W4P79_!!6000000000474-2-tps-80-80.png"),
    ("Meta AI", "https://www.meta.ai/", "https://www.meta.ai/favicon.ico"),
    ("Copilot", "https://copilot.microsoft.com/", "https://copilot.microsoft.com/static/cmc/favicon.svg"),
    ("Muse", "https://ai.meta.com/muse/", "https://static.xx.fbcdn.net/rsrc.php/yf/r/-7pQO6hUGK_.svg"),
    ("Agent Zero", "https://www.agent-zero.ai/", "https://www.agent-zero.ai/res/favicon_round.png"),
    ("Cursor", "https://cursor.com/", "https://cursor.com/marketing-static/favicon.svg"),
    ("Mistral", "https://mistral.ai/", "https://mistral.ai/favicon.ico"),
    ("Cohere", "https://cohere.com/", "https://cohere.com/apple-touch-icon.png"),
    ("Runway", "https://runway.com/", "https://runway.com/icon.png"),
    ("Suno", "https://suno.com/", "https://cdn-o.suno.com/favicon-192x192.png"),
    ("ElevenLabs", "https://elevenlabs.io/", "https://elevenlabs.io/icon.svg"),
    ("Stability AI", "https://stability.ai/", "https://images.squarespace-cdn.com/content/v1/6213c340453c3f502425776e/804f0e8b-0028-4262-a8b0-b9f1c5de72c0/favicon.ico?format=100w"),
    ("Adobe Firefly", "https://firefly.adobe.com/", "https://firefly.adobe.com/releases/cba597300be0f8eb20d4095720ff38a1e910dc43/assets/fi_touch_icon_80-CYMZMllL.png"),
    ("Notion AI", "https://www.notion.so/product/ai", "https://www.notion.com/front-static/logo-ios.png"),
    ("Poe", "https://poe.com/", "https://poe.com/favicon.ico"),
    ("Gamma", "https://gamma.app/", "https://static.gamma.app/favicons/favicon_dark.svg"),
    ("Ideogram", "https://ideogram.ai/", "https://ideogram.ai/favicon.ico"),
    ("Pika", "https://pika.art/", "https://pika.art/icon.svg?icon.3bty87qirfeg8.svg"),
    ("Luma", "https://lumalabs.ai/", "https://lumalabs.ai/favicons/favicon-black.ico"),
    ("Genspark", "https://www.genspark.ai/", "https://www.genspark.ai/favicon.ico"),
    ("Bolt", "https://bolt.new/", "https://bolt.new/static/favicon-96x96.png"),
    ("v0", "https://v0.app/", "https://v0.app/assets/icon.svg"),
]


def ai_slider():
    def card(name, website, logo, duplicate=False):
        icon = f'<span class="ai-logo-mark"><span aria-hidden="true">{escape(name[0])}</span><img src="{escape(logo, quote=True)}" alt="" width="36" height="36" decoding="async" loading="lazy"></span>'
        contents = f'{icon}<span class="ai-logo-name">{escape(name)}</span>'
        if duplicate:
            return f'<span class="ai-logo">{contents}</span>'
        return f'<a class="ai-logo" href="{escape(website, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="{escape(name)} resmÃ® sitesi (yeni sekme)">{contents}</a>'

    first = "".join(card(*platform) for platform in ai_platforms)
    second = "".join(card(*platform, duplicate=True) for platform in ai_platforms)
    return f'''<section class="ai-ecosystem" aria-labelledby="ai-ecosystem-title">
      <div class="wrap ai-ecosystem-heading"><div><p class="eyebrow">Yapay zekÃ¢ ekosistemi</p><h2 id="ai-ecosystem-title">Yapay zekÃ¢ dÃ¼nyasÄ±ndan seÃ§kiler.</h2></div><p>Ã–ne Ã§Ä±kan platformlarÄ± keÅŸfedin.</p></div>
      <div class="ai-marquee" aria-label="Yapay zekÃ¢ platformlarÄ±"><div class="ai-marquee-track"><div class="ai-marquee-group">{first}</div><div class="ai-marquee-group" aria-hidden="true">{second}</div></div></div>
    </section>'''


def main():
    DIST.mkdir(exist_ok=True)
    (DIST / "style.css").write_text((SRC / "style.css").read_text(encoding="utf-8"), encoding="utf-8")
    (DIST / "site.js").write_text((SRC / "site.js").read_text(encoding="utf-8"), encoding="utf-8")
    (DIST / "social-card.png").write_bytes((SRC / "social-card.png").read_bytes())
    home = (SRC / "home.html").read_text(encoding="utf-8").replace("{{AI_SLIDER}}", ai_slider()).replace("{{CONTACT_FORM}}", contact_form()).replace("{{FOOTER}}", footer(show_cta=False))
    (DIST / "index.html").write_text(shell(
        "Raiko | Yapay zekÃ¢ Ã§alÄ±ÅŸanlarÄ± ve otonom satÄ±ÅŸ sistemleri",
        "Raiko; AI Call Agent, AI Chatbot, akÄ±llÄ± CRM, B2B outreach ve yapay zekÃ¢ otomasyonlarÄ±yla mÃ¼ÅŸteri iletiÅŸimini ve satÄ±ÅŸ sÃ¼reÃ§lerini birleÅŸtirir.",
        home,
    ), encoding="utf-8")
    for slug, data in {**pages, **sectors}.items():
        directory = DIST / slug
        directory.mkdir(exist_ok=True)
        title = data["title"] + " | Raiko"
        (directory / "index.html").write_text(shell(title, data["summary"], page_body(data), f"/{slug}/"), encoding="utf-8")
    directory = DIST / "rehberler"
    directory.mkdir(exist_ok=True)
    (directory / "index.html").write_text(shell(
        "Yapay zekÃ¢ ajanlarÄ± ve satÄ±ÅŸ otomasyonu rehberleri | Raiko",
        "AI Call Agent, AI SDR, chatbot ve CRM sÃ¼reÃ§leri hakkÄ±nda anlaÅŸÄ±lÄ±r rehberler ve Ã¶rnek iÅŸ akÄ±ÅŸlarÄ±.",
        resources_body(), "/rehberler/"
    ), encoding="utf-8")
    for slug, guide in GUIDES.items():
        guide_dir = directory / slug
        guide_dir.mkdir(exist_ok=True)
        (guide_dir / "index.html").write_text(shell(
            guide["title"] + " | Raiko", guide["description"], guide_body(guide),
            f"/rehberler/{slug}/"
        ), encoding="utf-8")

    paths = ["/", *(f"/{slug}/" for slug in {**pages, **sectors}), "/rehberler/", *(f"/rehberler/{slug}/" for slug in GUIDES)]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{xml_escape(SITE_URL + path)}</loc></url>\n" for path in paths)
    sitemap += "</urlset>\n"
    (DIST / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    main()


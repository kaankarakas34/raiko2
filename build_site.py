from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"


def item(href, title, description):
    return f'<a class="mega-link" href="{href}"><strong>{title}</strong><span>{description}</span></a>'


menus = {
    "cozumler": {
        "label": "Çözümler",
        "intro": "Konuşan, düşünen ve işi ilerleten sistemler.",
        "columns": [
            ("Müşteri iletişimi", [
                ("/ai-call-agent/", "AI Call Agent", "Yapay zekâ çağrı merkezi"),
                ("/ai-call-agent/#gelen", "Gelen çağrı ajanı", "Aramaları karşılayın ve yönlendirin"),
                ("/ai-call-agent/#giden", "Giden çağrı ajanı", "Tanımlı takip görüşmeleri"),
                ("/ai-chatbot/", "AI Chatbot", "Web ve mesajlaşma sohbetleri"),
                ("/ai-chatbot/#whatsapp", "WhatsApp AI Agent", "Mesajdan iş akışına"),
            ]),
            ("Satış ve büyüme", [
                ("/akilli-crm/", "Akıllı CRM", "Müşteri kaydını tek yerde toplayın"),
                ("/ai-satis-ajani/", "AI Satış Ajanı", "Lead nitelendirme ve takip"),
                ("/b2b-outreach/", "B2B Outreach", "Hedefleme ve satış iletişimi"),
                ("/b2b-outreach/#musteri-bulma", "Lead Generation", "Doğru şirketleri araştırın"),
            ]),
            ("Operasyon", [
                ("/otomasyonlar/", "İş akışı otomasyonları", "Tekrarlanan adımları bağlayın"),
                ("/otomasyonlar/#ozel-ajanlar", "Özel AI agent", "Şirketinize göre kurgulayın"),
            ]),
        ],
    },
    "sektorler": {
        "label": "Sektörler",
        "intro": "Her sektörün konuşması ve iş akışı farklıdır.",
        "columns": [
            ("Öne çıkan kullanım alanları", [
                ("/saglik-turizmi/", "Sağlık turizmi", "Çok dilli ilk temas ve randevu"),
                ("/ihracat-uretim/", "İhracat ve üretim", "Hedef şirket araştırması ve takip"),
                ("/b2b-hizmetler/", "B2B hizmetler", "Talep toplama ve satış süreci"),
            ]),
        ],
    },
    "kaynaklar": {
        "label": "Kaynaklar",
        "intro": "Karar vermeden önce sorulması gerekenler.",
        "columns": [
            ("Rehberler", [
                ("/rehberler/#call-agent", "AI Call Agent nedir?", "Kullanım ve kurulum adımları"),
                ("/rehberler/#ai-sdr", "AI SDR nedir?", "Satış sürecindeki rolü"),
            ]),
            ("Karşılaştırmalar", [
                ("/rehberler/#karsilastirma", "Chatbot, ajan, canlı destek", "Hangi işi kim üstlenmeli?"),
            ]),
            ("Kullanım senaryoları", [
                ("/rehberler/#ornek-akis", "Uçtan uca örnek akış", "Telefon, CRM ve satış takibi"),
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
            f'<button class="nav-trigger" type="button" aria-expanded="false" aria-controls="menu-{key}">{menu["label"]}<span aria-hidden="true">⌄</span></button>'
            f'<div class="mega" id="menu-{key}" hidden><div class="wrap mega-inner">'
            f'<div class="mega-intro"><span class="mega-mark">RAIKO / {menu["label"].upper()}</span><p>{menu["intro"]}</p></div>'
            f'<div class="mega-columns">{groups}</div></div></div></div>'
        )
    return (
        '<header class="header"><div class="wrap nav">'
        '<a class="brand" href="/" aria-label="Raiko ana sayfa"><img src="/raiko-logo.webp" alt="Raiko" width="144" height="48"><small>AI Techs</small></a>'
        '<button class="menu" type="button" aria-expanded="false" aria-controls="nav-links">Menü</button>'
        '<nav class="links" id="nav-links" aria-label="Ana menü">'
        + "".join(triggers)
        + '<a class="nav-simple" href="/#sistemler">Nasıl çalışır?</a>'
        '</nav></div></header>'
    )


def shell(title, description, main, path="/"):
    escaped_title = escape(title)
    escaped_description = escape(description)
    return f'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#11110f">
  <meta name="description" content="{escaped_description}">
  <title>{escaped_title}</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%2311110f'/%3E%3Cpath d='M37 4 10 36h19l-5 24 30-36H35z' fill='%23ffc400'/%3E%3C/svg%3E">
  <link rel="stylesheet" href="/style.css">
  <script src="/site.js" defer></script>
</head>
<body>
  <a class="skip" href="#icerik">İçeriğe geç</a>
  {header()}
  <main id="icerik">{main}</main>
</body>
</html>'''


pages = {
    "ai-call-agent": {
        "category": "Müşteri iletişimi / Sesli ajan",
        "title": "AI Call Agent: yapay zekâ çağrı merkezi",
        "summary": "Gelen aramaları karşılayan, ihtiyacı anlayan ve tanımladığınız sonraki adımı başlatan sesli yapay zekâ ajanları.",
        "lead": "Telefon hâlâ birçok müşteri için ilk temas noktası. Raiko, çağrı akışını şirketinizin bilgisi, yönlendirme kuralları ve CRM süreçleriyle birlikte tasarlar.",
        "steps": [
            ("Arayanı anlar", "Sorunun veya talebin konusunu belirler; gerekli bilgileri konuşma içinde toplar."),
            ("Bilgiye dayanır", "Onaylanmış bilgi kaynaklarından yararlanarak sık sorulara yanıt verir."),
            ("İşi ilerletir", "Randevu, kayıt, geri arama veya ekip yönlendirmesi gibi tanımlı adımı başlatır."),
        ],
        "sections": [
            ("gelen", "Gelen çağrı ajanı", "Aramaları yanıtlayan yapay zekâ telefon asistanı, yoğun anlarda ilk teması karşılar. Sık soruları ele alır, müşterinin amacını belirler ve insan görüşmesi gereken konuyu doğru ekibe taşır."),
            ("giden", "Giden çağrı ajanı", "Geri arama, randevu hatırlatma veya daha önce izin verilmiş takip görüşmeleri için senaryolar kurulabilir. Görüşmenin kapsamı ve insana devredilecek noktalar önceden tanımlanır."),
        ],
        "example": ("Örnek akış", "Bir müşteri randevu için arar. Ajan uygun bilgileri toplar, mevcut takvim veya CRM bağlantısı varsa uygun adımı başlatır. Belirsiz ya da hassas bir konu ortaya çıktığında görüşmeyi ekibe aktarır."),
        "questions": [
            ("Yapay zekâ çağrı merkezi insan temsilcinin yerini tamamen alır mı?", "Süreç tasarımına bağlıdır. Tekrarlanan ve açık kurallı görüşmeler otomatik ilerleyebilir; karmaşık veya hassas konular için insan devri tanımlanmalıdır."),
            ("CRM bağlantısı zorunlu mu?", "Hayır. Temel çağrı karşılama ayrı kurgulanabilir. Ancak kayıt ve takip sürecini birleştirmek için CRM entegrasyonu faydalı olabilir."),
        ],
        "related": [("/ai-chatbot/", "AI Chatbot"), ("/akilli-crm/", "Akıllı CRM")],
    },
    "ai-chatbot": {
        "category": "Müşteri iletişimi / Yazılı ajan",
        "title": "AI Chatbot ve WhatsApp AI Agent",
        "summary": "Web ve mesajlaşma kanallarındaki soruları karşılayan, müşteri adaylarını nitelendiren ve görüşmeyi doğru akışa taşıyan yapay zekâ sohbet ajanları.",
        "lead": "Kurumsal AI chatbot, yalnızca hazır yanıt gösteren bir pencere değildir. Şirketinizin bilgi kaynaklarıyla ve gerektiğinde iş sistemleriyle bağlantılı bir konuşma akışı olarak kurgulanır.",
        "steps": [
            ("Karşılar", "Ziyaretçinin sorusunu ve niyetini doğal dilde anlar."),
            ("Yanıtlar", "Onaylı ürün, hizmet ve süreç bilgisini kullanır; belirsizlikte insan desteğine yönlendirir."),
            ("Aktarır", "Toplanan bağlamı uygun satış veya destek sürecine taşır."),
        ],
        "sections": [
            ("web", "Web sitesi chatbotu", "Ziyaretçiler hizmetler hakkında soru sorarken onları doğru bilgiye ve sonraki adıma yönlendirebilir. Satış ekibine aktarılacak talepte görüşme bağlamı korunur."),
            ("whatsapp", "WhatsApp yapay zekâ asistanı", "WhatsApp üzerinden gelen sorular için bilgi verme, ön değerlendirme ve randevu talebi toplama akışları tasarlanabilir. Kullanılacak kanal ve entegrasyonların kapsamı kurulumda belirlenir."),
        ],
        "example": ("Örnek akış", "Bir ziyaretçi web sitesinde hizmet kapsamını sorar. Ajan ilgili bilgiyi verir, ihtiyacını birkaç soruyla netleştirir ve uygun ekip için bir talep oluşturur."),
        "questions": [
            ("Şirket verileriyle eğitilmiş chatbot yanlış cevap verirse ne olur?", "Yanıtların kullanılacağı kaynaklar, sınırlar ve insan devri önceden tanımlanır. Kritik konular için otomatik yanıt yerine yönlendirme tercih edilir."),
            ("Chatbot ile canlı destek birlikte çalışabilir mi?", "Evet. Tekrarlanan sorular ajan tarafından ele alınırken karmaşık görüşmeler insan ekibe aktarılacak biçimde tasarlanabilir."),
        ],
        "related": [("/ai-call-agent/", "AI Call Agent"), ("/akilli-crm/", "Akıllı CRM")],
    },
    "akilli-crm": {
        "category": "Satış ve büyüme / Müşteri verisi",
        "title": "Akıllı CRM ve otomatik lead yönetimi",
        "summary": "Telefon, sohbet ve satış temaslarından gelen bilgiyi düzenleyen; ekibin sonraki adımı görmesini kolaylaştıran CRM odaklı yapay zekâ akışları.",
        "lead": "Yapay zekâ destekli CRM yaklaşımı, yeni bir ekran eklemekten çok müşteri kaydının doğru anda güncel kalmasını ve satış fırsatının kaybolmamasını hedefler.",
        "steps": [
            ("Teması toplar", "Form, çağrı veya sohbetten gelen bilgileri tanımlı alanlara aktarır."),
            ("Bağlamı düzenler", "Talebin konusu, aşaması ve sonraki aksiyon için anlaşılır bir özet oluşturur."),
            ("Takibi destekler", "Ekip için görev, yönlendirme veya hatırlatma adımlarını iş akışına bağlar."),
        ],
        "sections": [
            ("lead-yonetimi", "Lead yönetimi", "Potansiyel müşterinin kaynağı, ihtiyacı ve görüşme geçmişi aynı kayıtta bir araya geldiğinde satış ekibi önceliklendirmeyi daha sağlıklı yapabilir."),
            ("entegrasyon", "Mevcut CRM ile çalışma", "Kurulum mevcut CRM'inizi temel alabilir. Veri alanları, yetkiler ve hangi adımların otomatik işleyeceği sisteminize göre planlanır."),
        ],
        "example": ("Örnek akış", "Bir müşteri web sohbetinden teklif talep eder. Talep özetlenir, CRM'de ilgili kayda eklenir ve satış ekibinin takip edeceği adım belirlenir."),
        "questions": [
            ("Yeni bir CRM kullanmak zorunda mıyız?", "Hayır. İlk adım mevcut sistemlerin ve veri akışının değerlendirilmesidir."),
            ("AI lead scoring nasıl ele alınır?", "Önceliklendirme için kullanılacak işaretler şirketinizin satış sürecine göre belirlenir; nihai karar ve önemli aksiyonlar için insan onayı korunabilir."),
        ],
        "related": [("/ai-satis-ajani/", "AI Satış Ajanı"), ("/b2b-outreach/", "B2B Outreach")],
    },
    "ai-satis-ajani": {
        "category": "Satış ve büyüme / AI SDR",
        "title": "AI Satış Ajanı ile daha düzenli satış takibi",
        "summary": "Potansiyel müşteri bilgisini araştıran, gelen talepleri nitelendiren ve satış temsilcisinin doğru görüşmeye hazırlanmasına yardımcı olan AI SDR akışları.",
        "lead": "AI sales agent, satış ekibine bağlam hazırlar ve tanımlı takip adımlarını yürütür. İlişki kurma, teklif kararı ve hassas iletişim noktalarında insan kontrolü önemini korur.",
        "steps": [
            ("Araştırır", "Hedef müşteri profiline uygun şirket ve talep bilgisini toplar."),
            ("Nitelendirir", "İhtiyaç, zamanlama ve uygunluk gibi işaretleri düzenler."),
            ("Takibi hazırlar", "CRM kaydını ve satış temsilcisi için bir sonraki adımı netleştirir."),
        ],
        "sections": [
            ("nitelendirme", "Lead nitelendirme", "Her talep aynı aşamada değildir. AI satış ajanı, önceden belirlenmiş ölçütlere göre görüşme bağlamını oluşturabilir."),
            ("insan-onayi", "İnsan onayı nerede gerekir?", "Dışarıya gönderilecek kişiselleştirilmiş mesajlar, teklif ve önemli satış kararları için onay noktaları belirlenir. Otomasyonun sınırları açık olur."),
        ],
        "example": ("Örnek akış", "Bir şirket demo ilgisi gösterir. Ajan talebin konusunu ve şirket bilgisini toplar, CRM kaydını günceller, ekibe kısa bir özet sunar ve uygun takip adımını önerir."),
        "questions": [
            ("AI SDR klasik satış otomasyonundan nasıl ayrılır?", "Klasik otomasyon önceden tanımlı tetikleyicileri işler. AI SDR akışı, gelen bilgiyi yorumlayarak nitelendirme ve özetleme gibi adımlara katkı sağlar."),
            ("Toplantıları otomatik ayarlayabilir mi?", "Takvim ve onay süreçleri uygun biçimde bağlandığında toplantı talebi toplama veya planlama adımları kurgulanabilir."),
        ],
        "related": [("/b2b-outreach/", "B2B Outreach"), ("/akilli-crm/", "Akıllı CRM")],
    },
    "b2b-outreach": {
        "category": "Satış ve büyüme / Outbound",
        "title": "B2B Outreach ve otonom satış sistemleri",
        "summary": "Hedef şirket araştırması, müşteri adayı nitelendirme, kişiselleştirilmiş iletişim ve CRM takibini tek bir satış akışında birleştirin.",
        "lead": "B2B müşteri bulma sistemi, yalnızca toplu mesaj göndermek değildir. Doğru müşteri profilini seçmek, bağlamı araştırmak ve iletişimi kontrollü biçimde yürütmek gerekir.",
        "steps": [
            ("Hedefler", "İdeal müşteri profiline göre uygun şirketleri ve karar verici rollerini araştırır."),
            ("Hazırlar", "Şirkete ve ihtiyaca uygun iletişim taslağı ile takip planını oluşturur."),
            ("İzler", "Yanıtları, fırsatları ve sonraki aksiyonları CRM sürecinde düzenler."),
        ],
        "sections": [
            ("musteri-bulma", "Yapay zekâ ile müşteri bulma", "Hedef şirket listesi, sektör, ölçek, coğrafya ve ihtiyaç işaretlerine göre oluşturulabilir. Araştırmanın kalitesi, kullanılan veri kaynaklarına bağlıdır."),
            ("iletisim", "Çok kanallı satış iletişimi", "E-posta, telefon ve uygun diğer temas noktaları ortak bir plan içinde ele alınabilir. Kanalların kuralları, izinler ve insan onayı iletişim tasarımına dahil edilir."),
        ],
        "example": ("Örnek akış", "İhracat yapan bir üretici hedef pazarını tanımlar. Sistem uygun şirketleri araştırır, satış ekibinin incelemesi için kısa bağlam ve iletişim taslağı hazırlar. Onaylanan temaslar CRM'de takip edilir."),
        "questions": [
            ("Full outreach sistemi tamamen kendi başına çalışır mı?", "Araştırma ve takip adımları otomatikleştirilebilir. Dış iletişim, veri kullanımı ve önemli kararlar için onay ve kontrol noktaları tanımlanmalıdır."),
            ("LinkedIn hesap etkinliklerini otomatikleştiriyor musunuz?", "Hedefleme ve araştırma akışları platform kurallarına uygun biçimde planlanmalıdır. İzinsiz hesap etkinliği otomasyonu vaat edilmez."),
        ],
        "related": [("/ai-satis-ajani/", "AI Satış Ajanı"), ("/ihracat-uretim/", "İhracat ve üretim")],
    },
    "otomasyonlar": {
        "category": "Operasyon / Özel sistemler",
        "title": "Yapay zekâ otomasyonları ve özel AI agent sistemleri",
        "summary": "Uygulamalar arasında kalan tekrarlı işleri, şirketinizin veri kaynakları ve onay süreçleriyle uyumlu otomasyonlara dönüştürün.",
        "lead": "Hazır bir araç her iş akışını çözmez. Raiko, görevin nerede başladığını, hangi veriye ihtiyaç duyduğunu ve ne zaman insana dönmesi gerektiğini birlikte tasarlar.",
        "steps": [
            ("Süreci haritalar", "Tekrarlanan adımları, karar noktalarını ve kullanılan araçları belirler."),
            ("Bağlantıları kurar", "Gerekli veri kaynakları ve uygulamalar arasındaki akışı tanımlar."),
            ("Kontrolü korur", "Hata, belirsizlik ve insan onayı gereken durumlar için açık sınırlar oluşturur."),
        ],
        "sections": [
            ("is-akislari", "İş akışı otomasyonları", "Müşteri kaydı, destek talebi, bildirim, rapor özeti ve benzeri adımlar uygulamalar arasında taşınabilir. Otomasyonun kapsamı mevcut sistemlere göre belirlenir."),
            ("ozel-ajanlar", "Özel AI agent geliştirme", "Şirkete özel ajan, belirli görevi yerine getirmek için kendi bilgi kaynakları, araçları ve yetki sınırlarıyla tasarlanır. Çoklu ajan yaklaşımı ancak işin gerçekten gerektirdiği durumlarda kullanılır."),
        ],
        "example": ("Örnek akış", "Bir destek talebi geldiğinde sistem konuyu sınıflandırır, ilgili kaynağı bulur, taslak yanıt hazırlar ve gerekli ise ekip onayına sunar."),
        "questions": [
            ("Kurulum maliyeti nasıl belirlenir?", "Kapsam, entegrasyon sayısı, veri hazırlığı ve kullanım hacmi maliyeti etkiler. Net teklif için gerçek süreç değerlendirilmelidir."),
            ("Her adımı otonomlaştırmak gerekir mi?", "Hayır. Tekrarlı ve açık kurallı adımlar öncelikli olabilir; riskli veya belirsiz kararlar insanda kalmalıdır."),
        ],
        "related": [("/akilli-crm/", "Akıllı CRM"), ("/ai-chatbot/", "AI Chatbot")],
    },
}


sectors = {
    "saglik-turizmi": {
        "category": "Sektörler / Sağlık turizmi",
        "title": "Sağlık turizmi için çok dilli ilk temas",
        "summary": "Yurt dışından gelen hasta adayının sorusunu karşılayan, talebini düzenleyen ve uygun ekibe taşıyan yapay zekâ iletişim akışları.",
        "lead": "Sağlık turizminde hız kadar doğru yönlendirme de önemlidir. Ajan, onaylı operasyonel bilgiyle ilk teması yönetir; tıbbi değerlendirme ve kararlar yetkili insan ekibinde kalır.",
        "steps": [
            ("Talebi karşılar", "Dil, iletişim kanalı ve talep konusunu belirler."),
            ("Bilgiyi düzenler", "Randevu, ulaşım ve süreç gibi onaylı genel bilgileri paylaşır."),
            ("Ekibe aktarır", "Klinik veya hasta koordinasyon ekibine gerekli bağlamı iletir."),
        ],
        "sections": [("sinirlar", "Klinik sınırları", "Ajan tıbbi teşhis veya tedavi önerisi üretmek için konumlandırılmaz. Hasta verisi ve iletişim izinleri tasarımın başında ele alınır.")],
        "example": ("Örnek akış", "Yurt dışındaki bir kişi WhatsApp'tan süreç ve uygunluk sorar. Ajan genel süreç bilgisini paylaşır, iletişim tercihlerini toplar ve tıbbi değerlendirme gerektiren soruyu koordinasyon ekibine aktarır."),
        "questions": [("Sesli ajan randevu talebi alabilir mi?", "Uygun takvim ve ekip akışı kurulursa randevu talebini toplayıp ilgili birime yönlendirebilir.")],
        "related": [("/ai-call-agent/", "AI Call Agent"), ("/ai-chatbot/#whatsapp", "WhatsApp AI Agent")],
    },
    "ihracat-uretim": {
        "category": "Sektörler / İhracat ve üretim",
        "title": "İhracatçı ve üreticiler için B2B müşteri araştırması",
        "summary": "Hedef pazardaki şirketleri araştıran, satış temasını hazırlayan ve fırsatları CRM sürecine taşıyan kontrollü B2B outreach akışları.",
        "lead": "Farklı ülkelerde doğru şirketi ve doğru ihtiyacı bulmak zaman alır. AI destekli araştırma, ekibin inceleyeceği hedefleri daha düzenli oluşturmasına yardımcı olur.",
        "steps": [
            ("Pazarı tanımlar", "Ürün, ülke ve ideal müşteri profiline göre araştırma sınırlarını belirler."),
            ("Hedefleri inceler", "Potansiyel şirketlere ilişkin açık ve kullanılabilir bağlamı toplar."),
            ("Satışa taşır", "İncelenen hedefler için iletişim taslağı ve CRM takip adımı oluşturur."),
        ],
        "sections": [("insan-onayi", "Kontrollü dış iletişim", "Yurt dışı iletişimde dil, yerel beklentiler, veri kullanımı ve ekip onayı sürecin bir parçasıdır.")],
        "example": ("Örnek akış", "Bir üretici hedef ülke ve alıcı profilini belirler. Sistem uygun şirketleri araştırır, her biri için kısa gerekçe sunar; satış ekibi seçtikleri hedeflerle iletişime geçer."),
        "questions": [("Sistem otomatik e-posta gönderir mi?", "İletişim akışı teknik ve hukuki koşullara göre planlanır. Onay gerektiren adımlar şirket politikasına göre belirlenir.")],
        "related": [("/b2b-outreach/", "B2B Outreach"), ("/ai-satis-ajani/", "AI Satış Ajanı")],
    },
    "b2b-hizmetler": {
        "category": "Sektörler / B2B hizmetler",
        "title": "B2B hizmet şirketleri için satış akışı",
        "summary": "Web, telefon ve satış temaslarından gelen talepleri nitelendiren; görüşme bağlamını satış ekibine taşıyan AI agent sistemleri.",
        "lead": "Uzun karar süreçlerinde ilk görüşmeden sonraki takip kolayca kopabilir. Raiko, müşteri iletişimini ve CRM adımlarını aynı süreçte ele alır.",
        "steps": [
            ("İlk teması alır", "Hizmet, ihtiyaç ve şirket bağlamını toplar."),
            ("Uygunluğu değerlendirir", "Tanımlanmış kriterlere göre talebi düzenler ve eksik bilgiyi belirler."),
            ("Devreder", "Satış ekibine konuşma özeti ve önerilen takip adımını sunar."),
        ],
        "sections": [("uzun-satis", "Uzun satış döngüsü", "Birden fazla görüşme ve karar verici olduğunda müşteri geçmişinin tek kayıtta korunması önem kazanır.")],
        "example": ("Örnek akış", "Bir şirket hizmet kapsamını sorar. Ajan temel bilgiyi paylaşır, ihtiyaç ve zamanlamayı netleştirir; ekip görüşmeye hazırlanırken bu özet CRM kaydında yer alır."),
        "questions": [("Satış temsilcisi hangi noktada devreye girer?", "Görüşme karmaşıklaştığında, özel teklif gerektiğinde veya ilişki yönetimi önem kazandığında insan devri tasarlanır.")],
        "related": [("/akilli-crm/", "Akıllı CRM"), ("/ai-satis-ajani/", "AI Satış Ajanı")],
    },
}


def page_body(data):
    steps = "".join(f'<li><span>0{i}</span><div><h3>{title}</h3><p>{copy}</p></div></li>' for i, (title, copy) in enumerate(data["steps"], 1))
    sections = "".join(f'<section class="detail-section" id="{sid}"><div class="wrap detail-columns"><p class="eyebrow">{data["category"]}</p><div><h2>{heading}</h2><p>{copy}</p></div></div></section>' for sid, heading, copy in data["sections"])
    questions = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in data["questions"])
    related = "".join(f'<a href="{href}">{label}<span aria-hidden="true">↗</span></a>' for href, label in data["related"])
    example_title, example_copy = data["example"]
    return f'''
    <section class="detail-hero"><div class="wrap"><a class="back-link" href="/">← Ana sayfa</a><p class="hero-kicker">{data["category"]}</p><h1>{data["title"]}</h1><p class="detail-summary">{data["summary"]}</p><a class="raiko-button raiko-button--shine" href="#is-akisi" aria-label="İş akışını gör"><span class="raiko-button__surface">İş akışını gör <span aria-hidden="true">↘</span></span></a></div></section>
    <section class="detail-lead"><div class="wrap detail-columns"><p class="eyebrow">Yaklaşım</p><p>{data["lead"]}</p></div></section>
    <section class="detail-process" id="is-akisi"><div class="wrap detail-columns"><div><p class="eyebrow">İş akışı</p><h2>Nasıl çalışır?</h2></div><ol>{steps}</ol></div></section>
    {sections}
    <section class="example-band"><div class="wrap detail-columns"><p class="eyebrow">{example_title}</p><p>{example_copy}</p></div></section>
    <section class="detail-faq"><div class="wrap detail-columns"><div><p class="eyebrow">Sık sorulanlar</p><h2>Açık yanıtlar.</h2></div><div>{questions}</div></div></section>
    <section class="related"><div class="wrap"><p class="eyebrow">İlgili çözümler</p><div>{related}</div></div></section>
    {footer(show_cta=True)}
    '''


def footer(show_cta=False):
    cta_html = ""
    if show_cta:
        cta_html = '''
    <div class="footer-cta-card">
      <div class="footer-cta-content">
        <div class="footer-status-pill">
          <span class="status-dot"></span>
          <span>Tüm AI Sistemleri Aktif • 7/24 Kesintisiz Hizmet</span>
        </div>
        <h3 class="footer-cta-title">Yapay zekâ çalışanlarınızla işinizi bir adım öne taşıyın.</h3>
        <p class="footer-cta-desc">Telefonları yanıtlayan, mesajları karşılayan ve CRM sürecini ilerleten sistemleri bugün hayata geçirin.</p>
      </div>
      <div class="footer-cta-actions">
        <a class="raiko-button raiko-button--shine" href="/#cozumler" aria-label="Çözümleri keşfet">
          <span class="raiko-button__surface">Çözümleri Keşfet <span aria-hidden="true">↗</span></span>
        </a>
        <a class="footer-contact-link" href="mailto:info@raiko.ai">
          <span>info@raiko.ai</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
        </a>
      </div>
    </div>'''

    status_pill_home = ""
    if not show_cta:
        status_pill_home = '''
        <div class="footer-status-pill">
          <span class="status-dot"></span>
          <span>Tüm AI Sistemleri Aktif • 7/24 Otonom Sistem</span>
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
          Telefonları yanıtlayan, mesajları karşılayan, müşteri adaylarını nitelendiren ve CRM sürecini ilerleten yapay zekâ çalışanları kuruyoruz.
        </p>
        {status_pill_home}
        <div class="footer-contact-info">
          <div class="footer-info-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
            <a href="mailto:info@raiko.ai">info@raiko.ai</a>
          </div>
          <div class="footer-info-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
            <span>İstanbul, Türkiye</span>
          </div>
        </div>
        <div class="footer-socials" aria-label="Sosyal Medya">
          <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="LinkedIn (yeni sekme)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 8.76a1.59 1.59 0 1 0 0-3.18 1.59 1.59 0 0 0 0 3.18m1.4 9.74v-8.37H5.06v8.37h2.8z"/></svg>
          </a>
          <a href="https://x.com" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="X / Twitter (yeni sekme)">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
          </a>
          <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="GitHub (yeni sekme)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0 1 12 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0 0 22 12.017C22 6.484 17.522 2 12 2Z"/></svg>
          </a>
        </div>
      </div>

      <div class="footer-col">
        <p class="footer-heading">Çözümler</p>
        <ul class="footer-nav-list">
          <li><a href="/ai-call-agent/">AI Call Agent <span class="footer-sub">Sesli Ajan</span></a></li>
          <li><a href="/ai-chatbot/">AI Chatbot <span class="footer-sub">WhatsApp & Web</span></a></li>
          <li><a href="/akilli-crm/">Akıllı CRM <span class="footer-sub">Satış Takibi</span></a></li>
          <li><a href="/ai-satis-ajani/">AI Satış Ajanı <span class="footer-sub">Lead SDR</span></a></li>
          <li><a href="/b2b-outreach/">B2B Outreach <span class="footer-sub">İletişim Akışı</span></a></li>
          <li><a href="/otomasyonlar/">Özel Otomasyonlar <span class="footer-sub">Entegrasyon</span></a></li>
        </ul>
      </div>

      <div class="footer-col">
        <p class="footer-heading">Sektörler</p>
        <ul class="footer-nav-list">
          <li><a href="/saglik-turizmi/">Sağlık Turizmi</a></li>
          <li><a href="/ihracat-uretim/">İhracat ve Üretim</a></li>
          <li><a href="/b2b-hizmetler/">B2B Hizmetler</a></li>
          <li><a href="/#kullanim">Müşteri Desteği</a></li>
          <li><a href="/#sistemler">Nasıl Çalışır?</a></li>
          <li><a href="/#sorular">Sık Sorulan Sorular</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <p class="footer-heading">Kaynaklar</p>
        <ul class="footer-nav-list">
          <li><a href="/rehberler/">Tüm Rehberler</a></li>
          <li><a href="/rehberler/#call-agent">AI Call Agent Nedir?</a></li>
          <li><a href="/rehberler/#ai-sdr">AI SDR Satış Süreci</a></li>
          <li><a href="/rehberler/#karsilastirma">Chatbot vs AI Agent</a></li>
          <li><a href="/rehberler/#ornek-akis">Örnek Akış Modeli</a></li>
          <li><a href="/#ust">Ekosistem Platformları</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-divider"></div>

    <div class="footer-bottom">
      <div class="footer-copy">
        <span>© <span class="year">2026</span> Raiko AI Technologies Inc. Tüm hakları saklıdır.</span>
      </div>
      <div class="footer-legal">
        <a href="/rehberler/">Gizlilik Politikası</a>
        <span class="sep" aria-hidden="true">•</span>
        <a href="/rehberler/">Kullanım Koşulları</a>
        <span class="sep" aria-hidden="true">•</span>
        <a href="/rehberler/">KVKK</a>
      </div>
      <a class="footer-back-to-top" href="#ust" aria-label="Sayfanın başına dön">
        <span>Başa dön</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m18 15-6-6-6 6"/></svg>
      </a>
    </div>
  </div>
</footer>'''


def resources_body():
    return '''
    <section class="detail-hero resource-hero"><div class="wrap"><a class="back-link" href="/">← Ana sayfa</a><p class="hero-kicker">Kaynaklar / Rehberler</p><h1>Doğru sistemi seçmek için açık rehberler.</h1><p class="detail-summary">Yapay zekâ çalışanları, satış otomasyonu ve müşteri iletişimi hakkında temel karar noktaları.</p></div></section>
    <section class="resource-index"><div class="wrap"><a href="#call-agent">AI Call Agent nedir? ↗</a><a href="#ai-sdr">AI SDR nedir? ↗</a><a href="#karsilastirma">Hangi çözüm ne yapar? ↗</a><a href="#ornek-akis">Örnek akış ↗</a></div></section>
    <article class="resource-article" id="call-agent"><div class="wrap detail-columns"><p class="eyebrow">01 / Sesli ajan</p><div><h2>AI Call Agent nedir?</h2><p>AI Call Agent, telefon görüşmesini doğal dilde yürüten ve belirli iş adımlarına bağlanan sesli yapay zekâ ajanıdır. Gelen çağrıları karşılamak, sık soruları yanıtlamak ve talebi doğru ekibe aktarmak için kullanılabilir.</p><p>Kurulumda üç konu nettir: hangi bilgi kaynakları kullanılacak, ajan hangi işlemleri yapabilecek ve ne zaman insana devredecek? Görüşme kalitesi yalnızca ses teknolojisine değil, bu sınırların doğru tasarlanmasına da bağlıdır.</p><a class="text-link" href="/ai-call-agent/">AI Call Agent çözümünü incele <span aria-hidden="true">↗</span></a></div></div></article>
    <article class="resource-article" id="ai-sdr"><div class="wrap detail-columns"><p class="eyebrow">02 / Satış</p><div><h2>AI SDR nedir?</h2><p>AI SDR, satış geliştirme ekibinin araştırma, lead nitelendirme ve takip hazırlığı gibi adımlarında kullanılan yapay zekâ akışıdır. Hedef müşteriye ilişkin bağlamı toplar ve satış temsilcisine daha düzenli bir başlangıç sağlar.</p><p>İnsan onayı, özellikle dış iletişim ve teklif gibi önemli noktalarda korunmalıdır. Satış performansını değerlendirirken yalnızca gönderilen mesaj sayısına değil, nitelikli görüşme ve fırsat kalitesine bakmak gerekir.</p><a class="text-link" href="/ai-satis-ajani/">AI Satış Ajanını incele <span aria-hidden="true">↗</span></a></div></div></article>
    <article class="resource-article" id="karsilastirma"><div class="wrap detail-columns"><p class="eyebrow">03 / Karşılaştırma</p><div><h2>Chatbot, AI agent ve canlı destek arasındaki fark</h2><p>Chatbot konuşma kanalında soruları yanıtlar. AI agent, izin verilen araçları kullanarak bir iş adımını da başlatabilir. Canlı destek ise belirsiz, hassas veya ilişki yönetimi gerektiren görüşmelerde insan kararını sağlar.</p><p>En iyi kurgu çoğu zaman bu üç rolü netleştirir: otomasyon tekrar eden işi alır, insan ekip gerekli bağlamla devreye girer.</p><a class="text-link" href="/ai-chatbot/">AI Chatbot çözümünü incele <span aria-hidden="true">↗</span></a></div></div></article>
    <article class="resource-article" id="ornek-akis"><div class="wrap detail-columns"><p class="eyebrow">04 / Kullanım senaryosu</p><div><h2>Telefon, CRM ve satış takibi nasıl birleşir?</h2><p>Bir müşteri arar ve hizmet hakkında bilgi ister. Sesli ajan soruyu karşılar, ihtiyacı netleştirir ve görüşme özetini uygun CRM kaydına taşır. Satış ekibi talebi inceleyip bir sonraki görüşmeyi planlar.</p><p>Bu örnek, tüm adımların otomatik olması gerektiği anlamına gelmez. Kayıt izinleri, entegrasyonlar ve insan devri gerçek iş sürecine göre belirlenir.</p><a class="text-link" href="/akilli-crm/">Akıllı CRM çözümünü incele <span aria-hidden="true">↗</span></a></div></div></article>
    ''' + footer(show_cta=True)


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
        icon = f'<span class="ai-logo-mark"><span aria-hidden="true">{escape(name[0])}</span><img src="{escape(logo, quote=True)}" alt="" width="36" height="36" decoding="async"></span>'
        contents = f'{icon}<span class="ai-logo-name">{escape(name)}</span>'
        if duplicate:
            return f'<span class="ai-logo">{contents}</span>'
        return f'<a class="ai-logo" href="{escape(website, quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="{escape(name)} resmî sitesi (yeni sekme)">{contents}</a>'

    first = "".join(card(*platform) for platform in ai_platforms)
    second = "".join(card(*platform, duplicate=True) for platform in ai_platforms)
    return f'''<section class="ai-ecosystem" aria-labelledby="ai-ecosystem-title">
      <div class="wrap ai-ecosystem-heading"><div><p class="eyebrow">Yapay zekâ ekosistemi</p><h2 id="ai-ecosystem-title">Yapay zekâ dünyasından seçkiler.</h2></div><p>Öne çıkan platformları keşfedin.</p></div>
      <div class="ai-marquee" aria-label="Yapay zekâ platformları"><div class="ai-marquee-track"><div class="ai-marquee-group">{first}</div><div class="ai-marquee-group" aria-hidden="true">{second}</div></div></div>
    </section>'''


def main():
    DIST.mkdir(exist_ok=True)
    (DIST / "style.css").write_text((SRC / "style.css").read_text(encoding="utf-8"), encoding="utf-8")
    (DIST / "site.js").write_text((SRC / "site.js").read_text(encoding="utf-8"), encoding="utf-8")
    home = (SRC / "home.html").read_text(encoding="utf-8").replace("{{AI_SLIDER}}", ai_slider()).replace("{{FOOTER}}", footer(show_cta=False))
    (DIST / "index.html").write_text(shell(
        "Raiko | Yapay zekâ çalışanları ve otonom satış sistemleri",
        "Raiko; AI Call Agent, AI Chatbot, akıllı CRM, B2B outreach ve yapay zekâ otomasyonlarıyla müşteri iletişimini ve satış süreçlerini birleştirir.",
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
        "Yapay zekâ ajanları ve satış otomasyonu rehberleri | Raiko",
        "AI Call Agent, AI SDR, chatbot ve CRM süreçleri hakkında anlaşılır rehberler ve örnek iş akışları.",
        resources_body(), "/rehberler/"
    ), encoding="utf-8")


if __name__ == "__main__":
    main()

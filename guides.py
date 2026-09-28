"""Editorial guides for distinct research intents. Keep claims conditional on implementation."""

GUIDES = {
    "ai-call-agent-nedir": {
        "title": "AI Call Agent nedir? Çağrı akışı ve kurulum rehberi",
        "description": "AI Call Agent'ın gelen çağrıyı nasıl karşıladığını, ne zaman insana devrettiğini ve kurulumda hangi bilgilerin gerektiğini öğrenin.",
        "intro": "AI Call Agent, telefon görüşmesini doğal dilde yürüten ve izin verilen iş adımlarına bağlayan sesli yapay zekâ ajanıdır. Gelen çağrıda sorunun konusunu anlayabilir, onaylı bilgiyi paylaşabilir ve talebi doğru kişiye aktarabilir. Yapabilecekleri kullanılan telefon altyapısı, veri kaynakları ve kurumun belirlediği yetkilere bağlıdır.",
        "sections": [
            ("Çağrıdan sonra ne olur?", "Bir arayan randevu isterse ajan tarih tercihini ve iletişim bilgisini toplar. Takvim bağlantısı kurulmuşsa uygunluğu kontrol etmek için tanımlı akışı başlatabilir; bağlantı yoksa talebi ekibe görev olarak iletir. Görüşme özeti, arama nedeni ve açık sonraki adım CRM'e yazılabilir. Bu kayıtlar için saklama ve erişim kuralları önceden belirlenmelidir."),
            ("Kurulumda hangi kararlar verilir?", "İlk aşamada çağrı türlerini, sık sorulan soruları, mesai dışı davranışı ve kullanılacak bilgi kaynaklarını çıkarın. Ardından ajan hangi soruları yanıtlayacak, hangi durumda geri arama isteyecek ve hangi durumda temsilciye bağlayacak sorularını netleştirin. Gerçek çağrı örnekleriyle farklı aksan, eksik bilgi ve beklenmeyen soru senaryolarını test edin."),
            ("Sesli ajan, IVR ve insan temsilci", "Tuşlamalı IVR sabit seçeneklerde yönlendirir. Sesli ajan, doğal dilde soruyu anlayıp kurallı bir sonraki adımı başlatabilir. İnsan temsilci ise belirsiz, duygusal veya bağlayıcı karar gerektiren görüşmelerde ilişkiyi yönetir. Üçü birlikte çalışabilir; çağrının her aşamasında otomasyon şart değildir."),
            ("Başarı nasıl değerlendirilir?", "Yalnızca karşılanan çağrı sayısını ölçmeyin. Doğru yönlendirme, çözülemeyip insana aktarılan konu, kayıtların doğruluğu ve arayanın yeniden arama ihtiyacı birlikte incelenmelidir. Başlangıç koşullarını ölçmeden tasarruf veya satış artışı vaadi verilmemelidir."),
        ],
        "related": [("/ai-call-agent/", "AI Call Agent çözümü"), ("/akilli-crm/", "Çağrıyı CRM'e bağlama")],
    },
    "ai-sdr-nedir": {
        "title": "AI SDR nedir? Satış ekibindeki rolü ve sınırları",
        "description": "AI SDR'nin araştırma, lead nitelendirme ve takip hazırlığında nasıl kullanılabileceğini; insan onayı ve ölçüm noktalarını inceleyin.",
        "intro": "AI SDR, satış geliştirme işlerini destekleyen yapay zekâ akışıdır. Hedef şirket araştırması, talep özeti, uygunluk değerlendirmesi ve takip taslağı hazırlayabilir. Sözleşme, fiyat, dış iletişim ve müşteri ilişkisi üzerindeki yetkisi şirketin belirlediği sınırlarla tanımlanır.",
        "sections": [
            ("İlk adım: uygun müşteri tanımı", "İdeal müşteri profilinde sektör, şirket ölçeği, ihtiyaç ve dışlama ölçütleri yazılı olmalıdır. Ajanın araştırdığı şirketin neden uygun göründüğü kaynaklarıyla birlikte incelenir. Belirsiz veri, kesin iddia veya sahte kişiselleştirme içeren mesajlara dönüşmemelidir."),
            ("Gelen talebi nasıl nitelendirir?", "Bir demo talebinde şirket, sorun, zamanlama ve gerekli karar verici bilgisi ayrı alanlara alınabilir. Eksik bilgi varsa soru önerilir; uygun olmayan talep de kaybolmadan doğru duruma işlenir. Öncelik sırası, satış ekibinin gerçek kriterlerine göre belirlenir."),
            ("İnsan hangi noktada devreye girer?", "Dışarı giden mesajın onayı, özel teklif ve müşteriyle ilişki gerektiren görüşme insanda kalmalıdır. Otomatik taslaklar, araştırma kaynağı ve önceki temaslarla birlikte temsilciye sunulursa denetlemek kolaylaşır. Yanıt geldiğinde birden fazla kanaldaki tekrarlar durdurulmalıdır."),
            ("Pilotun sonucunu neyle ölçersiniz?", "Üretilen lead veya mesaj sayısından çok nitelikli görüşme, gerçekleşen toplantı ve fırsata dönüşüm izlenir. Ekibin düzeltme yükü ve yanlış eşleşmeler de ölçülmelidir. CRM'de aşamalar net değilse otomasyonun katkısını ayırmak güçleşir."),
        ],
        "related": [("/ai-satis-ajani/", "AI Satış Ajanı çözümü"), ("/b2b-outreach/", "B2B Outreach")],
    },
    "chatbot-ai-agent-canli-destek": {
        "title": "Chatbot, AI agent ve canlı destek: hangisi hangi işi yapar?",
        "description": "Chatbot, iş adımı başlatan AI agent ve insan temsilci arasındaki farkı örnek müşteri akışlarıyla karşılaştırın.",
        "intro": "Bir web sohbet penceresi, bir iş akışı ajanı ve insan temsilci farklı sorumluluklar üstlenir. Doğru seçim; sorunun tekrarlanma sıklığına, bilginin doğrulanabilirliğine ve işlemin riskine bağlıdır. Ziyaretçi için tek bir konuşma gibi görünen süreç arka planda bu roller arasında geçebilir.",
        "sections": [
            ("Chatbot ne zaman yeterlidir?", "Çalışma saatleri, hizmet kapsamı ve başvuru adımları gibi onaylı bilgiye dayalı sorularda chatbot ilk yanıtı verebilir. Yanıtın kaynağı güncel tutulmalı ve belirsizlikte temsilciye geçiş görünür olmalıdır. Sırf daha doğal konuşuyor diye bir botun sistemlerde işlem yapabildiği varsayılmamalıdır."),
            ("AI agent ne ekler?", "Yetki verilmiş bir agent, yalnızca yanıt yazmakla kalmayıp CRM'de talep açma veya takvimde uygunluk kontrolü gibi bir adımı başlatabilir. Bu iş için uygulama erişimi, alan eşleştirmesi ve hata durumunda geri dönüş gerekir. Bağlayıcı veya geri alınması zor işlemlerde onay noktası tasarlanmalıdır."),
            ("Canlı destek ne zaman devralır?", "Şikâyet, fiyat istisnası, hassas veri veya konuşmada belirsizlik insan kararını gerektirebilir. Temsilciye yalnızca sohbet geçmişi değil, müşterinin amacı, verilen yanıtlar ve bekleyen adım da aktarılmalıdır. Böylece müşteri aynı bilgiyi tekrar anlatmak zorunda kalmaz."),
            ("Örnek seçim akışı", "Ziyaretçi hizmetin çalışma saatini sorar: chatbot yanıtlar. Randevu ister: takvim erişimi varsa agent uygunluk arar. Özel fiyat ister: temsilciye aktarılır. Her geçişin sonucu aynı müşteri kaydında izlenirse ekip süreçte nerede kalındığını görür."),
        ],
        "related": [("/ai-chatbot/", "AI Chatbot çözümü"), ("/otomasyonlar/", "İş akışı otomasyonları")],
    },
    "telefon-crm-satis-takibi": {
        "title": "Telefon, CRM ve satış takibi tek akışta nasıl birleşir?",
        "description": "Çağrıdan CRM kaydına, ekip atamasından satış takibine örnek bir iş akışı ve kurulum kontrol noktaları.",
        "intro": "Müşteri görüşmesi tek başına bir satış fırsatı oluşturmaz. Talebin kime ait olduğu, ne istendiği ve sıradaki adım belirlenirse ekip görüşmeyi sürdürebilir. Telefon, sohbet, form ve e-posta kanallarını aynı kayıt düzenine bağlamak bunun temelidir.",
        "sections": [
            ("Talep → sınıflandırma → kayıt", "Bir müşteri telefonla fiyat bilgisi ister. Ajan veya temsilci ürün ilgisini, iletişim tercihini ve zamanlamayı kaydeder. CRM'de önce mevcut kişi aranır; yoksa yeni kayıt açılır. Talebin kaynağı ve verilen izinler korunur. Eksik bilgi sessizce uydurulmaz."),
            ("Kayıt → ekip ataması → insan devri", "Talep ürün, bölge veya müşteri tipine göre ilgili kişiye atanabilir. Atama kuralında izin ve mesai durumu da düşünülmelidir. Ekip, görüşme özetiyle birlikte açık soruları görür. Belirlenen sürede yanıt verilmezse yeniden atama veya hatırlatma kuralı çalışabilir."),
            ("Takip → sonuç", "Temsilci görüşür, teklif gerekiyorsa koşulları doğrular ve sonucu CRM'e işler. Takip tarihi belirsiz bırakılmaz. Müşteri kazanılmış, kaybedilmiş veya ertelenmiş olabilir; her durum sonraki öğrenme için ayrı tutulmalıdır."),
            ("Neyi ölçmek gerekir?", "İlk yanıt süresi, yanlış atama, mükerrer kayıt, takip süresi ve nitelikli fırsata dönüşüm ölçülebilir. Bu metriklerin anlamlı olması için çağrı ve CRM kayıtlarının doğru eşleşmesi gerekir. Otomasyonun hızı tek başına müşteri deneyimini kanıtlamaz."),
        ],
        "related": [("/ai-call-agent/", "AI Call Agent"), ("/akilli-crm/", "Akıllı CRM")],
    },
    "emlak-yapay-zeka-asistani": {
        "title": "Emlakta AI asistan: İlan talebinden gösterime iş akışı",
        "description": "Emlak danışmanları için portal, WhatsApp ve telefon taleplerini tek kayıtta izleyen örnek AI asistan akışı.",
        "intro": "Bir ilan talebi portaldan gelir, müşteri sonra WhatsApp'tan yazar ve telefonla gösterim ister. Kanallar ayrı tutulursa danışman hangi mülkün konuşulduğunu kaybedebilir. Emlak AI asistanı ilk bilgiyi toplayıp aynı müşteri ve ilan bağlamını ekibe taşıyacak şekilde kurgulanabilir.",
        "sections": [
            ("Hangi bilgi toplanır?", "İlan bağlantısı veya kodu, alım ya da kiralama amacı, bütçe aralığı, konum ve iletişim tercihi kaydedilir. İstenmeyen kişisel bilgiler toplanmamalı; müşteriyle temas için gereken izinler korunmalıdır. Aynı kişinin farklı kanallardan yazdığı anlaşılırsa mükerrer kayıt birleştirilir."),
            ("Gösterim nasıl planlanır?", "Asistan uygun zaman tercihlerini alabilir, fakat ilan müsaitliği ve danışman takvimi güncel kaynaktan doğrulanmalıdır. Danışman onayı olmadan randevu kesinleşmiş gibi sunulmaz. Gösterim sonrası geri bildirim ve bir sonraki temas CRM'e işlenir."),
            ("Fiyat ve portföy sınırı", "Fiyat, aidat ve satılık durumu değişebilir. Onaylı portföy kaynağında güncel olmayan bilgi varsa ajan kesin yanıt vermek yerine danışmana yönlendirir. Pazarlık veya bağlayıcı teklif kararı insan ekipte kalır."),
        ],
        "related": [("/emlak/", "Emlak sektörü çözümü"), ("/akilli-crm/", "Akıllı CRM")],
    },
    "otomotiv-test-surusu-takibi": {
        "title": "Otomotivde AI asistan: Araç talebinden test sürüşüne",
        "description": "Otomotiv satışında araç ilgisi, stok doğrulama, test sürüşü ve CRM takibini bağlayan örnek akış.",
        "intro": "Araç arayan kişi önce model ve donanımı sorabilir, ardından stok, takas ve test sürüşü hakkında bilgi isteyebilir. Bu soruların farklı ekiplere dağıldığı yerde görüşmenin bağlamı kaybolmamalıdır. AI asistan, ilk talebi düzenleyip doğru uzmana taşımak için kullanılabilir.",
        "sections": [
            ("Talep nasıl nitelendirilir?", "Model veya ilan kodu, yeni ya da ikinci el tercihi, lokasyon, satın alma zamanlaması ve iletişim kanalı kaydedilir. Çok fazla soru sorarak görüşmeyi uzatmak yerine satış ekibinin gerçekten kullanacağı bilgiler seçilmelidir."),
            ("Stok ve test sürüşü", "Canlı stok bağlantısı varsa müsaitlik kontrol edilebilir; yoksa temsilci teyidi gerekir. Asistan test sürüşü için zaman tercihini alır. Bayi takvimi ve araç uygunluğu doğrulandıktan sonra randevu kesinleşir; değişiklik müşteriye açıkça bildirilir."),
            ("Takas, finansman ve teklif", "Takas değeri, kredi koşulu veya kampanya kişiye ve zamana göre değişebilir. Ajan bu alanlarda bağlayıcı rakam vermeden talebin bağlamını toplar ve yetkili ekibe iletir. Görüşme sonucu ile sonraki takip tarihi CRM'de görünür olmalıdır."),
        ],
        "related": [("/otomotiv/", "Otomotiv sektörü çözümü"), ("/ai-call-agent/", "AI Call Agent")],
    },
}

# Üç uzman araştırması — tam arşiv (2026-10-14)

Pedagoji (dil öğretimi/SLA) · Ürün (öğrenme deneyimi/oyunlaştırma) · Görsel (görsel tasarım + ön yüz).
İki tur: bağımsız analiz (uygulamayı headless Chrome'da gerçekten kullanarak, ses kapalı) → çapraz eleştiri ve uzlaşma.
Koordinatör doğrulaması: Pedagojinin motor iddiası gerçek — `python3 araclar/motor_test.py araclar/ajan-2026-10-14/fp.js`
→ **18/40** (40 doğru öğrenci cümlesinin 22'sini motor bozuyor). `tp.js` (yaygın Türk hataları) 12/42 yakalanıyor.
`icerik.js` (uygulamanın kendi 391 cümlesi) 387/391 — kalan 4 dilbilgisi değil, parça başında büyük harf / "Best regards," sonuna nokta.
Ajan betikleri ve vaka dosyaları: `araclar/ajan-2026-10-14/`.

Uzlaşma özeti ve kullanıcı kararları: aşağıda "Uzlaşma" bölümü (kullanıcı onayından sonra karar satırı eklenecek).

## Kullanıcı kararı ve uygulama (2026-10-14)

Kullanıcı: "sıradan yapalım". Dalga 1 ve Dalga 2 uygulandı:
- `c0e2ca0` Dalga 1 — motor yaması (fp.js 40/40; regresyon 72→123), düzeltme kartı (diffWords, ✅/Dinle kuralı),
  9 içerik hatası, Cümle Diz zarf sırası, görsel/erişilebilirlik paketi.
- `722b14a` Dalga 2a — Benim cevaplarım (KITS, 217 birleşim self-test'te), Hızlı/Tam prova + rapor kartı,
  etkinlik günlüğü + üretimle seri, Bugün · 3 adım, dürüst hazırlık, öğrenme adımında TR→EN.
- `eac7c67` Dalga 2b — okumada cümle vurgusu, kalıp dilimleri, dönüş karşılaması, .ics, kulak paraphrase + ses çiftleri.

Bekleyen: **Dalga 3** (motor kesinlik katmanı + 500 vakalık korpus; içerik doğrulama protokolü → +250 kelime →
ünite; 2 dk seviye yoklaması; SVG ikon seti, self-host font, maskable simge, aydınlık tema). İçerik protokolü
kullanıcının Türkçe kontrolünü ister — ayrı oturum.
Açık sorular: ilk örnek cevaptaki "worked as a supervisor" gerçek mi; havuzda kaç kelime görüldü (+250 önceliği).

---

## Brief
# İngilizce Koçu — 3 uzman araştırması (2026-10-14): "daha güçlü modelle ne yapabiliriz?"

## Uygulama
Kişisel İngilizce öğrenme PWA'sı. Kullanıcı: İTÜ işletme mühendisliği öğrencisi, İngilizcesi çok düşük (A1-A2),
birincil hedef **staj/iş mülakatı İngilizcesi**, ikincil günlük konuşma; zayıf yanı cümle kurma + kelime.
Kullanıcı uygulamayı hem kendisi kullanıyor hem ileride pazarlayabilir.
- Kaynak (SADECE OKU): `/Users/zahit/Downloads/ingilizce-app/index.html` (~2300 satır, tek dosya, vanilla JS/CSS), `sw.js`, `manifest.json`.
- Canlı: https://zahitdoganayitu.github.io/ingilizce-koc/ (GitHub Pages). **Canlıya gitme, yerel önizlemeyi kullan.**
- 5 sekme: Öğren (SRS kart merdiveni: klasik → dinle-seç → TR'den hatırla → dikte → yazarak üret), Cümle (Diz / Çevir),
  Mülakat (Hazırlık 15 soru / Kulak / Akıcılık 4-3-2 / Sahte mülakat), Pratik (Oku 16 metin / Yaz: kural motoru 26 tuzak,
  paragraf denetimi / Kalıplar 11 kategori), İlerleme. 258 kelime (5 seviye), tamamen çevrimdışı kural tabanlı (API yok).
- **Geçmiş — MUTLAKA OKU, TEKRAR ETME:**
  - `git -C /Users/zahit/Downloads/ingilizce-app log --format='%h %s%n%b' -8` — her commit mesajı ne yapıldığını ve neden yapıldığını anlatıyor.
    En son `a4fbaaf`: önceki 3 uzman (pedagoji / ön yüz / ürün) turunun uzlaştığı 35 madde.
  - `/Users/zahit/.claude/projects/-Users-zahit/memory/ingilizce-uygulamasi.md` — mimari, kararlar, **reddedilen/ertelenen** fikirler
    (WebLLM elendi: küçük modeller Türkçe dilbilgisinde uydurma kural üretiyor; Cloudflare Workers AI ücretsiz seçenek olarak not edilmiş ama kurulmadı;
    mikrofonla sözlü üretim ertelendi; there is/are dönüşümü motor sınırı vb.).
  - Reddedileni yeniden açacaksan YENİ gerekçe yaz ve işaretle.

## Kullanıcının isteği
"Opus 5.5'in gücü ve yetenekleriyle uygulamamıza geliştirmeler ekleyebilir miyiz? Kalitesini, arayüzünü, oynanışını
(öğrenme deneyimi / oyunlaştırma), görsellerini nasıl geliştirebiliriz, neler yapabiliriz — kapsamlı araştırma."
Yorum: önceki tur hata düzeltme ve küçük-orta iyileştirmelere odaklandı. Bu tur **iddia merdiveni** istiyor:
hızlı kazançlar (S), orta işler (M) ve önceki turun dokunmadığı **büyük bahisler (L/XL)** — güçlü bir modelin
artık güvenle yapabileceği iddialı işler: ör. büyük ve yüksek kaliteli içerik üretimi (kelime/örnek/diyalog/okuma —
doğrulama yöntemiyle), müfredat/ünite yapısı, kural motorunun ciddi genişlemesi, sesli/telaffuz özellikleri,
görsel kimlik ve illüstrasyon (satır içi SVG), oyunlaştırma, isteğe bağlı bulut AI (Workers AI) vb.
Her büyük bahis için: neden şimdi mümkün, nasıl doğrulanır, riski ne, geri alma yolu ne, kullanıcıya maliyeti (para/hesap) var mı.

## Kısıtlar (değişmez)
- Tek dosya `index.html` tercih (gerekirse ek statik dosya — gerekçele), vanilla JS/CSS, build yok, framework yok.
  Bu makinede **node/npm YOK** (python3 + JavaScriptCore + Chrome var).
- Mobil 375×812 birincil, tamamen çevrimdışı çalışma çekirdek özellik; kayıt localStorage (`ing:` öneki) — kullanıcının mevcut ilerlemesi bozulmamalı.
- **Ücretli API önerme** (Anthropic API anahtarı abonelik dışı ekstra ücret). Ücretsiz bulut seçeneği önerebilirsin ama çevrimdışı çekirdek bozulmamalı.
- Dil öğrenene **yanlış İngilizce öğretmek** en ağır hata — her içerik/kural önerisinde doğrulama yöntemi yaz.
- Pazarlama: sıfır kullanıcı tabanında paylaşım/viral mekaniği önce kurulmaz.

## Kurallar (çok önemli)
1. **Depoyu DEĞİŞTİRME.** Dosya yazma/commit/push yok. Not/betik sadece kendi klasörüne:
   `/private/tmp/claude-501/-Users-zahit/a23d21e5-1651-4009-9279-5f00ef8fb1f6/scratchpad/ing-ajan/<senin-klasörün>/`
2. **Uygulamayı gerçekten kullan/ölç.** Önizleme: `http://localhost:8777/index.html?v=<rastgele>` (sessiz kopya — TTS çalmaz).
   Headless Chrome numaran N sana verildi (port 935N). Kullanım `/Users/zahit/Downloads/ingilizce-app/araclar/README.md`:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --mute-audio --remote-debugging-port=935N --user-data-dir=/tmp/ing-chrome-N --no-first-run about:blank &`
   sonra her komutta `CDP_PORT=935N python3 /Users/zahit/Downloads/ingilizce-app/araclar/cdp.py ...` (open / emu 375 812 1 / nav / js / shot).
   Ekran görüntüsüne Read ile bakabilirsin. Bitince `pkill -f remote-debugging-port=935N`. **`--mute-audio` ŞART.**
   **Uygulamadaki Browser panelini (mcp__Claude_Browser__*) KULLANMA** — tek panel var, ajanlar çakışır.
   Kural motorunu test etmek için: `python3 /Users/zahit/Downloads/ingilizce-app/araclar/motor_test.py <kendi-vakaların.js>`
   (biçim `araclar/cumleler.js` gibi `const C=[[girdi,beklenen],...]`).
3. Doğrulama disiplini: bir sorunu "kritik" yazmadan önce ölç/ekran görüntüsü al. a11y aracı "isimsiz" derse probe ile doğrula;
   opacity ≠ tıklanmaz; `elementFromPoint` pointer-events:none öğeyi atlar. Doğrulamadığını **"şüphe"** diye işaretle. Satır numarası ver.
4. Web araştırması serbest (araştırma kanıtı, benzer uygulamalar — Duolingo, Anki, Speak, Elsa, Busuu vb., teknikler) — kaynağı belirt.

## Rapor biçimi (Markdown, Türkçe, en fazla ~1600 kelime, övgü yok)
1. **Ölçtüklerin / kullandıkların** (kısa; ne gördün, sayılar).
2. **Önceki turdan farkın** — dokunmadığın maddeler ve neden; yeniden açtığın varsa gerekçe.
3. **Öneriler — iddia merdiveni**: her madde
   `[S|M|L|XL] başlık — ne / nerede (satır, fonksiyon) / beklenen etki (öğrenmeye etkisi) / nasıl doğrulanır / risk + geri alma`.
   En az 3 tane L/XL "büyük bahis"; her biri için neden ŞİMDİ mümkün.
4. **Diğer iki uzmana sorular / bağımlılıklar**.
5. **Yapmayın** — cazip ama zararlı fikirler, gerekçeyle.
6. **İlk 5** — alanındaki en yüksek getirili 5 iş, sıralı.

---

## Tur 1 — pedagoji

# Pedagoji — Tur 1 raporu (2026-10-14)

## 1. Ölçtüklerim / kullandıklarım
- **Öğren:** 14 kart oynadım (2'si "again"). 1. gün = 6 kelime × 2 klasik EN→TR tanıma; üretim sıfır, her kelime tek örnek cümle.
  **70 günlük simülasyon** (%15 hata, `grade`/`buildSession` sahte saatle; dosya: `pedagoji/sim.js`): **ilk "yazarak üret" kartı 41. günde**. 0-40. günler arası kartların %50-60'ı klasik tanıma. 70. günde 143/258 kelime pekişmiş.
- **Kural motoru**, iki vaka dosyası (`pedagoji/fp.js`, `tp.js`):
  - Doğru öğrenci cümlesi: **40'ın 22'sinde motor doğru cümleyi bozdu.**
  - Yaygın Türk hatası: 42 vakanın **12'si** yakalandı.
  - Uygulamanın kendi 391 cümlesi: 0 yanlış alarm (`icerik.js`). Regresyon seti, motorun kendi içeriğine göre ayarlanmış; gerçek öğrenci dilini temsil etmiyor.
- **Yaz:** 18 gerçekçi cümle/paragraf. **Çevir:** 10 hatalı çeviri. **Cümle Diz:** geçerli alternatif sıra denedim. **Mülakat:** 4 bölüm, sahte mülakatta 6 cevap (hatalı, kısa, kurtarma cümlesi, STAR dahil).
- **İçerik taraması:** WORDS 258 (lvl1 = sadece 12), INTERVIEW_QA 15, CHUNKS 11 kategori / 57 cümle, READINGS 16 × ~50 kelime, MNEM 45.

### Ölçülen kritik bulgular
1. **Motor doğru soruları bozuyor** (`missing_be_ing`, 1026-1031; guard yok):
   - "Are you coming to the meeting?" → *Are you are coming*
   - "How is it going?" → *How is it is going*
   - "What are you studying?" → *What are you are studying*

   Sahte mülakatta "Do you have any questions?" sorusuna gerçekçi cevap ("Are you working with international customers?") da bozuldu.
2. **`tobe_bare`** (964-970): "My favorite course is design." → *My favorite course design.* Üstüne "Şu an oluyorsa: *is designing*" önerisi geliyor, yani iki yanlış birden. Aynı hata:
   - "What I need is help" → *What I need help*
   - "Is work important for you?" → *Work important for you?*
   - "Our main problem was change management" → *…changed management*
3. **`past_marker`** (974-981) ana fiile yapışıyor:
   - "I think I made a mistake yesterday" → *I thought…*
   - "Do you remember what you did yesterday?" → ***Do you remembered***. Motor burada yeni bir hata üretiyor.
4. **`pres_perf`** (1003-1009):
   - "I want to work abroad for two years" → *I have wanted to work…*
   - "I am in Istanbul for two weeks" → *I have been…*
5. Diğer yanlış düzeltmeler:
   - `have_years` (1087): "I have two years left at university" → *I am two years old left*
   - `interested_with` (1068): "interested to hear" → *interested in hear*
   - `want_to` (989): "I need study materials" → *I need to study materials*
   - `no_be` (1055): "We students need…" → *We are students need*
   - `prep_table` (1074): "arrived to Istanbul" → *arrived **at** Istanbul* (doğrusu *in*)
   - "I have finished the report yesterday" → *I **had** finished* (yanlış ders veriyor)
6. **iOS akıllı noktalama** (şüphe: kullanıcının cihazında doğrulanmadı): "He don**’**t like coffee" ve "I**’**m agree" yakalanmıyor. `third_neg` (1021) sadece düz `'` tanıyor. Girdi normalize edilmiyor (`checkWriting` 1646).
7. **Kaçan sık Türk hataları:**
   - "didn't went" / "Did you went"
   - "can speaks", "Does he works"
   - "interesting in", "boring"
   - "go to home", "look forward to hear", "If I will get"
   - "According to me", "since 3 years"
   - "an university", "a idea"
   - "I'm student", "I'm study"
   - "he **always** finish" (özne ile fiil arasına zarf girince)
   - "**third grade**" (ABD'de ilkokul 3 demek; "üçüncü sınıf öğrencisiyim" çevirisi)
8. **Çevir / Yaz kartı** (`buildCheckCard` 1655-1668): "I need you help." için yeşil **✅ Bilinen tuzaklara takılmadın** çıkıyor. Hatalı cümle büyük puntoyla basılıyor, **🔊 Dinle düğmesi yanlış cümleyi anadili sesiyle okuyor**. Örnek çeviri ekranın altında kalıyor (ekran görüntüsü `s4.png`).
9. **Cümle Diz** (1735): "Today I have a meeting" yanlış sayıldı, çünkü tek doğru sıra kabul ediliyor. Havuzda en az 27 cümle sonda zaman zarfıyla bitiyor. Türkçe sezgiyle zarfı başa koyan öğrenci, doğru cümle kurduğu hâlde cezalandırılıyor.
10. **Sahte mülakat:**
    - STAR cevabı "Last year our order was late. I call the supplier and we finish in two days." için "takılmadın" dendi. Zarfsız geçmiş bağlam, en önemli bağlam olan davranışsal sorularda kaçıyor.
    - `MOCK_KEYS` alt dize eşliyor (2082): "I don't **know** about this" zayıf yön sorusunda "now" kalıbını kazanıyor. "but" de "about" içinde eşleşir.
    - Anahtar "middle way" (1880) doğal değil.
11. **İçerik hataları:**
    - #64 "When do you come?" (443) → *When are you coming?*
    - #143 "I am tired but I finish the work." (522) → *…but I will finish it*
    - #135 "The internship is three months." (514) → *…three months long*
    - Okuma (885): vocab "speak about", metinde "talk about"
    - Diyalog (871): anahtar bulmak için "Call your phone." mantıksız
    - Q15 (1860) "The teacher liked…" ve okuma (895) "teacher": üniversitede *professor/instructor* olmalı ("hoca" aktarması)
    - Q3 (1812) "focus too much on details" mülakatçıların tanıdığı klişe kaçamak
    - Q12 (1848) "willing to do the boring parts" kendini küçültüyor
    - Q1 (1804) uydurma "supervisor" geçmişi duruyor
12. **Hafıza ipuçları /w/ sesini /v/ diye öğretiyor:** "water"=VATER (822), "weakness"=VİKS (797), "wake up"=VEY KAP (813). Bu tam olarak Türk öğrencinin tipik telaffuz hatası.
13. **Temel kelime boşluğu:** be, study, say, idea, manager, family, next/last/first, other, different, really, often, ago, than, then, career, role, office, product, price, email yok. Motor "am/is/are eksik" diye öğretiyor ama **"be" kartı yok**.

## 2. Önceki turdan farkım
- 35 madde (fix dilimi, öğrenme adımı, mock döngüsü vb.) tekrar edilmedi.
- Önceki tur yanlış pozitifleri uygulamanın kendi cümleleriyle ölçtü. Ben öğrenci cümleleriyle ölçtüm ve yeni bir hata sınıfı buldum: **soru yapısı ve isim-fiil belirsizliği**.
- **Yeniden açtıklarım:**
  - **Zarfsız geçmiş bağlam.** Önceki tur bunu "açık sınır" diye bırakmıştı. Yeni gerekçe: mock zaten sorunun türünü biliyor. "Tell me about a time…" sorularında bağlam bayrağıyla çözülebilir; genel Yaz sekmesine dokunmak gerekmez.
  - **Sesli tekrarda mikrofon** ("Android ağ ister" diye ertelenmişti). Yeni gerekçe: Akıcılık ve Mock zaten aynı `makeRecognizer`'ı kullanıyor, yani ağ bağımlılığı başka yerde kabul edilmiş. Çevrimdışıyken öz-değerlendirmeye düşer.
- Dokunmadıklarım: there is/are dönüşümü, "married with" (motor sınırı kararı duruyor). WebLLM'yi yeniden açmıyorum.

## 3. Öneriler — iddia merdiveni

**[S] Motor için acil "zarar verme" yaması.** Ne / nerede:
- `missing_be_ing`'e guard ekle: önceki kelime am/is/are/was/were ise dokunma.
- `tobe_bare`: V_BASE'ten isim olarak da kullanılan kelimeleri (design, test, change, help, work, plan, answer, study, run) çıkar ya da bunlar için alt-only yap.
- `past_marker`: öncesinde do/does/did varsa dokunma; aynı cümlede zaten geçmiş fiil varsa (made/did/-ed) ana fiile dokunma.
- `pres_perf`: want/like/love'ı listeden çıkar; `am/is/are + in/at` (ziyaret anlamı) hariç tut.
- `have_years` için `left` guard'ı; `interested to` dalını sil.
- `arrive to` → *arrive in/at*: elle düzeltme yerine sadece açıklama.
- Girdiyi normalize et: `’` → `'`.

Etki: yanlış öğretme kesilir. Doğrulama: `fp.js` 40/40 + mevcut 72 + `icerik.js` 391. Risk düşük, tek tek kural geri alınabilir.

**[S] Çevir/Yaz kartı.** Temiz sonuçta ✅ başlığı "Tuzak bulunamadı — örnekle karşılaştır" olsun. Örnek çeviri üste çıksın, öğrencinin cümlesi küçük ve nötr basılsın. **Hiçbir düzeltme yoksa Dinle düğmesi öğrencinin cümlesini değil örneği okusun.** Çevir'de öğrenci cevabı ile örnek arasında kelime düzeyinde fark göster (LCS, ~20 satır).

**[S] İçerik düzeltmeleri:** 11. maddedeki 9 hata. MNEM'de /w/ ipuçlarına "w = dudak yuvarla, v değil" notu ekle. Q1 "supervisor" cümlesini "part-time job / club" ile değiştir (kullanıcıya sor).

**[S] Cümle Diz:** kabul anahtarı listesi yap: `[tokens, zarf başa alınmış hâli]`. Zarf kalıpları sabit bir regex.

**[M] STAR bağlam bayrağı:** `checkEnglish(text,{past:true})`, yalnız "Tell me about a time / challenge / mistake / project" sorularında çalışır. Geniş zamanlı I/we + V_BASE için otomatik düzeltme yapmaz, "Geçmişi mi anlatıyorsun? *call → called*" ipucu verir. Doğrulama: 30 STAR cevabı, yarısı zaten geçmiş zamanlı.

**[M] Kelime kartında 3 örnek cümle döngüsü:** format değiştikçe cümle değişsin. Kodlama çeşitliliği kelimenin yeni bağlama aktarımını artırır. Ayrıca **merdiveni öne çek**: öğrenme adımındaki 2. görüş TR→EN olsun (`renderStudy` 1331). Hedef: ilk üretim kartı 41. gün yerine 1. günde. Doğrulama: `sim.js` ile format dağılımı.

**[M] Sorular için kulak çeşitlemesi:** her soruya 3-5 doğal paraphrase ("Walk me through your CV", "What would you say your strengths are?"). Şu an kulak eğitimi ilk kelimeden tanınıyor.

**[M] Minimal çift algı eğitimi:**
- Çiftler: work/walk, west/vest, think/sink, live/leave, full/fool, ship/sheep.
- Kelime vurgusu: deVElop, COMpany.
- Teknik: TTS, cihazdaki birden çok sesle (HVPT'ye yaklaşım; Thomson 2018: algı eğitimi üretime taşınıyor). Çevrimdışı çalışır.

**[M] Seviye tespiti (10 dk):** frekans bantlarından örnek kelime (Nation'ın VST yöntemi), bilinenler box 3'ten başlar. Neden: A2 kullanıcı lvl1 "hello/good" ile vakit kaybediyor. Doğrulama: aynı testi 2 hafta sonra tekrar, tutarlılık.

**[L] Motor yenilemesi: kesinlik katmanları + 500 cümlelik korpus.**
- Her kurala `conf: high|low`. Low ise metni yeniden yazmaz, "kontrol et" ipucu verir.
- Küçük kapalı sözlükle (isim/fiil etiketi, ~600 kelime) belirsizlik çözülür.
- Korpus: 250 gerçek Türk öğrenci hatası (TICLE/CLC literatüründeki hata tipleri) + 250 doğru cümle (Tatoeba + mülakat cevapları). **Kabul eşiği: doğru sette %100 dokunmama, hata setinde ≥%50 yakalama.**
- Neden şimdi: güçlü model 500 vakayı tutarlı üretip sınıflayabilir; `motor_test.py` hazır.
- Risk: kural sayısı büyür. Geri alma: `conf` alanı yoksa eski davranış.

**[L] Kişisel mülakat cevabı oluşturucu (STAR sihirbazı).**
- Türkçe yönlendirmeli 4 adım (Ne oldu? / Görevin? / Ne yaptın? / Sonuç?).
- Her adımda **önceden doğrulanmış İngilizce çerçeveler** var ("In my ___ project, ___ was late."). Öğrenci boşluğa kendi ismini/fiilini yazar (serbest çeviri yok).
- Motor + geçmiş bayrağıyla denetlenir. Çıktı "Benim cevaplarım" olur ve Akıcılık / Sahte mülakat / SRS cümle kartlarına beslenir.
- Neden şimdi: 3-5 hikâyeyi önceden hazırlamak mülakatta en yüksek getirili iş. Uygulama bunu öneriyor (Q4 notu) ama araç vermiyor.
- Risk: öğrencinin yazdığı boşluk hatalı olabilir. Etiket "senin metnin" olur, örnek çerçeve ayrı tutulur. Maliyet sıfır, çevrimdışı.

**[XL] Mülakat odaklı ünite müfredatı.**
- 10 ünite: kendini tanıt, eğitim/bölüm, deneyim-STAR, güçlü-zayıf, motivasyon/şirket, takım-çatışma, hata, lojistik, soru sor, telefon/online mülakat.
- Her ünite: 30-40 kelime + 8 kalıp + diyalog + 2 okuma (anlama sorulu + "kendi cümlenle anlat") + hedef soru + kişisel cevap.
- `buildSession` yeni kelimeyi aktif üniteden çeker. Ünite alanı yoksa lvl sırasına düşer, mevcut id'ler ve localStorage korunur.
- Neden şimdi: bir modelin tek oturumda kelime ↔ kalıp ↔ okuma ↔ soru hizasını tutarlı üretmesi artık mümkün.
- Risk: büyük iş, içerik hatası. Doğrulama protokolü aşağıda.

**[XL] 1000-1200 kelimeye doğrulanmış genişleme.**
- Seçim nesnel olsun: NGSL ilk 1000 ∩ Business Service List (CC BY-SA 4.0) + mülakat listesi. "Model ne seçerse" değil.
- Örnek cümleler önce **insan yazımı Tatoeba EN-TR çiftlerinden** (CC BY 2.0 FR, atıf şart) seviye filtresiyle alınır. Üretim yalnız boşlukta yapılır.
- Otomatik lint (python3):
  - hedef kelime cümlede geçer (dikte yapılabilir)
  - diğer kelimeler bilinen + NGSL-1000 içinde (i+1)
  - 4-10 kelime, tekrar yok
  - motor 0 isabet
- Sonra **kör ikinci model incelemesi** ("Bir anadili konuşanı bunu söyler mi? evet/hayır + düzeltme"). Uyuşmazlık olan cümle atılır. Kullanıcı 50 rastgele cümleyi okuyup denetler.
- Geri alma: içerik ayrı `const` bloğunda, eski id'ler sabit. Maliyet sıfır.

**[L] Gölgeleme ölçümü:** mevcut `makeRecognizer` ile kalıp/okuma cümlesini sesli tekrar. Transkript hedef cümleyle kelime kelime hizalanır, eksik/yanlış kelimeler renklenir. Akıcılık turlarında kelime/dakika gösterilir, tur 1 ile tur 3 karşılaştırılır. Bu, 4/3/2'nin ölçülebilir çıktısı. Ağ yoksa öz-değerlendirme. Risk: tanıma, aksanı "yanlış" sayabilir. Bunu "telaffuz notu" değil "anlaşılırlık" diye çerçevele.

## 4. Diğer uzmanlara
- **Ön yüz:**
  - Çevir kartının yeni hiyerarşisi (örnek üstte, fark vurgusu) mobilde nasıl görünmeli?
  - Motorda kesinliği düşük ipucu için "şüphe" rozeti tasarımı.
- **Ürün:**
  - Ünite yapısı mevcut 5 sekmeyle mi çalışır, yoksa "Bugün" akışı mı gerekir?
  - Seviye testi onboarding'e mi konmalı?
  - Tatoeba ve BSL atıf/lisans koşulları pazarlamayla uyumlu mu? Bana göre CC BY-SA, içerik dosyasına da SA yükümlülüğü getirir. Hukuki kontrol gerekir.
- **Bağımlılık:** STAR sihirbazı Mock ve Akıcılık'a veri besler, ortak bir "Benim cevaplarım" deposu gerekir (`ing:` öneki).

## 5. Yapmayın
- **Motora yeni otomatik düzeltme kuralı eklemeden önce yanlış pozitif korpusunu büyütün.** Ölçüm: doğru cümlelerin %55'i bozuldu. Kural eklemek yanlış öğretmeyi artırır.
- **Örnek cümle / okuma metnini tek modelle üretip doğrudan koymayın.** Kör ikinci inceleme ve lint şart.
- **Telaffuza puan (0-100) vermeyin.** Web Speech tanıma telaffuz değerlendirmesi değildir; yanlış güven ve yanlış ceza verir.
- **Mock'ta anahtar kelime sayısını puana çevirmeyin.** Alt dize eşleşmesi papağanlığı ödüllendirir. Yapı (STAR) ve geçmiş zaman daha anlamlı.
- **Serbest Türkçe → İngilizce "AI çeviri" özelliği eklemeyin** (Workers AI dahil). Öğrenci üretmek yerine kopyalar; küçük modeller yanlış İngilizce üretebilir.

## 6. İlk 5
1. **[S] Motor zarar verme yaması** + `’` normalizasyonu + `fp.js`'i regresyona ekle.
2. **[S] Çevir/Yaz kartı:** yanlış cümleye ✅ ve Dinle yok, örnek üstte, fark vurgusu.
3. **[M] Üretimi öne çek:** öğrenme adımında TR→EN + kelime başına 3 örnek cümle.
4. **[L] STAR sihirbazı + geçmiş bağlam bayrağı:** kişisel 3-5 hikâye, mock/akıcılıkla bağlı.
5. **[XL] Doğrulanmış ünite müfredatı + 1000 kelime:** NGSL/BSL + Tatoeba + lint + kör inceleme.

Kaynaklar: [Business Service List (CC BY-SA 4.0)](https://www.newgeneralservicelist.com/business-service-list), [NGSL 1.2](https://www.newgeneralservicelist.com/new-general-service-list), [Tatoeba indirmeler (CC BY 2.0 FR)](https://tatoeba.org/eng/downloads), [Tatoeba — Wikipedia](https://en.wikipedia.org/wiki/Tatoeba). Thomson (2018) HVPT ve Nation (2006) kelime eşikleri bellekten aktarıldı, bu turda web'de doğrulanmadı (şüphe).

Dosyalar: `scratchpad/ing-ajan/pedagoji/{fp.js,tp.js,icerik.js,sim.js,yaz.js,mock.js,s1-s5.png}`

---

## Tur 1 — urun

# Ürün (oynanış / öğrenme deneyimi) — Tur 1

## 1. Ölçtüklerim / kullandıklarım
Headless Chrome 9352, 375×812 dokunmatik + 1280×800. Ekran görüntüleri ve betikler: `scratchpad/ing-ajan/urun/` (`step.js` seans botu, `seed7.js` 7 günlük kayıt, `sim.py` hazırlık simülasyonu). Depoya dokunulmadı.

- **İlk açılış:** onboarding yok; doğrudan "job" kartı (`init` 2246).
- **İlk seans:** 6 yeni kelime × öğrenme adımı = 12 kart, **24 dokunuş**, tahminen 2-3 dk. Hepsi klasik kart. Tamam ekranı sonrası tek yönlendirme Kulak / Sahte mülakat; Cümle sekmesine hiç çağrı yok.
- **İlerleme çubuğu ilk yarıda donuk (doğrulandı):** 5 kart sonra `#sessProg` = %0, `done=0`, `relearn=5`. Sebep: `answerCard` (1510) öğrenme adımında `done++` yapmıyor, `planned=6` ama gerçek gösterim 12. Yeni kullanıcı ilk seansın yarısında sıfır geri bildirim alıyor.
- **7 günlük dönüş (seed: 42 kelime, %80 kolay):** karşılama/özet yok, doğrudan kart. Plan 20 + 6 tekrar = 26 kart, **52 dokunuş** (~6-8 dk tahmin). Isınma kuralı (`warm`, box≥4, satır 1283) 8. günde hiç devreye girmiyor (box≥4 kart yok). 7. gün serisi yalnız toast.
- **Tamam ekranı:** sayfa yeniden açılınca "0 BU SEANS" (`session.done` sıfırlanıyor, 1310). Bugün öğrenilen kelimeler listelenmiyor.
- **Hazırlık yüzdesi (2150) yalnız kelimeye bağlı.** Simülasyon (günde 6, hepsi kolay = en iyi durum): 1. gün %15, 7. gün %18, 30. gün %27, %50 ancak ~60. gün. "Pekişmiş" sayacı **~45-50 gün 0** kalıyor. "%25 Kendini 2-3 cümleyle tanıtabilirsin" ~25. günde tek bir tanıtma alıştırması yapılmadan "açılıyor" (`MILES` 2151) — yanlış vaat.
- **Kalıcı olmayan etkinlik:** Diz/Çevir skoru (`sent` 1676), Kulak (`earScore` 1900), Akıcılık, Sahte mülakat, Okuma, Yaz — hiçbiri kaydedilmiyor. Seri yalnız `grade()` içinden artıyor (`bumpStreak` 1258); bir gün sadece sahte mülakat yapan kullanıcı seriyi kaybeder. Hedef mülakat, ama uygulama yalnız kelime kartını "çalışma" sayıyor.
- **Bilgi mimarisi:** 5 sekme + 9 alt sekme. Mülakat altında "Mülakat" alt sekmesi var (isim tekrarı, 333). Kalıplar listesi **9683 px** (56 madde, ~14 ekran kaydırma). Oku sekmesi boş durumda düğmeye basmadan içerik yok.
- **Sahte mülakat:** 15 soru sırayla, seçim yok, kısa mod yok; sonunda yalnız "That's all my questions" balonu (2053). Rapor yok, geçmiş yok.
- **Hedefler/erişilebilirlik:** nav 73×47, kart dinle 44×44, puanlama 92×58 iyi. 44 px altı: mülakat alt sekmeleri 79×41, "🔊 Dinle" 45×39, "Tekrar dene/Sonraki soru" 38 yükseklik, okuma konu çipleri 34, tamam ekranı çipleri 39. Segment düğmelerinde `aria-pressed`/`role=tab` yok (seçili durum sadece `.on` sınıfı). `--muted2` / `--bg2` kontrastı 4.36:1 (11.5 px metinde <4.5).
- **Hatırlatma:** cue seçiliyor (tamam ekranı), ama hiçbir hatırlatma mekanizmasına bağlı değil.

## 2. Önceki turdan farkım
`a4fbaaf` motor, öğrenme adımı, mock döngüsü ve tamam ekranı düzeltmelerini yaptı. Bunları tekrar açmıyorum. Reddedilen "Kalıplar sekmesini taşıma"yı taşıma olarak değil, **içerik dilimleme** (kategori başına bir ekran) olarak öneriyorum. Bu tur farkı: tek tek ekranlar yerine **günlük döngü + kalıcı etkinlik verisi + mülakat hedefine bağlı ilerleme**. Önceki tur bunlara dokunmadı. Mikrofon ertelemesine dokunmuyorum (sesli mock metin yedekli kalır).

## 3. Öneriler — iddia merdiveni

**[S] İlerleme çubuğu öğrenme adımını saysın** — `buildSession` 1296 `planned = queue.length + yeni kart sayısı`; `answerCard` 1512 her geçişte ilerleme. Etki: ilk seansın ilk dokunuşundan geri bildirim. Doğrulama: boş kayıt + `step.js` ile 1. puanlamadan sonra genişlik >0, son kartta %100. Risk yok, tek satır geri alınır.

**[S] Tamam ekranı: günlük sayaç + "bugün öğrendiklerin"** — `stats.doneToday` (gün devrinde sıfır) ve bugünün 6 yeni kelimesi dinle düğmeli liste (1303-1326). Etki: seans sonu kısa geri getirme + doğru sayı (yeniden açınca "0" yok). Doğrulama: seans bitir, yeniden yükle, sayı aynı.

**[S] Takvim hatırlatması (.ics)** — cue seçilince "Takvime ekle": `RRULE:FREQ=DAILY` içeren bir .ics Blob üretilir. Çevrimdışı ve ücretsiz, iOS/Android takvim bildirimi verir. Web Push iOS'ta yalnız ana ekran PWA'sında çalışır ve gönderen bir sunucu ister ([OneSignal](https://documentation.onesignal.com/docs/web-push-for-ios), [Progressier](https://progressier.com/pwa-capabilities/declarative-web-push)). Doğrulama: gerçek iPhone ana ekran modunda Blob indirme — **şüphe**, standalone modda indirme takılabilir; yedek `navigator.share({files})`. Risk düşük.

**[S] Küçük IA/a11y paketi** — alt sekme "Mülakat" → "Prova"; segmentlere `aria-pressed`; `.progressbar`'a `role=progressbar` + `aria-valuenow`; 38-41 px hedefleri 44'e çıkar; masaüstünde Space = göster, 1/2/3 = puanla. Doğrulama: aynı ölçüm betiği (44 altı liste boş).

**[M] Etkinlik günlüğü** — `ing:log` = `{tarih:{kart, cümle, kulak, tur432, mock}}`, 90 gün sınırı. Her alt sekme yazar. İlerleme'ye 8 haftalık ısı haritası. Seri kuralı: "bugün kelime tekrarı **veya** bir mülakat alıştırması" (pedagojiye soru). Doğrulama: her etkinlikten sonra `localStorage['ing:log']`; eski kayıtla açılış bozulmamalı (anahtar yoksa `{}`). Geri alma: anahtar okunmaz.

**[M] Dürüst hazırlık yüzdesi** — `renderProgress` 2150'yi 4 bileşene böl: kelime (lvl5 pekişme), soru hazırlığı (kendi cevabı olan + 4/3/2 yapılmış soru / 15), prova (son mock), kulak doğruluğu. Kilometre taşları eyleme bağlansın ("%25 = 1. soruya kendi cevabın + 3 tur"). 45 gün "0 pekişmiş" yerine her gün oynayan dürüst metrik: "Bu hafta hatırlama oranın %88" (Anki tarzı). Etki: vaat ile beceri eşleşir, ilerleme hissi erkenden gelir. Doğrulama: `sim.py` + seed ile yüzde eğrisi; tek bileşenle %50'yi geçmemeli.

**[M] Dönüş karşılaması** — ≥2 gün ara veya due>25 ise kartın üstünde: "Hoş geldin — 34 tekrar bekliyor (~8 dk). [Kısa seans: 15] [Hepsi]". Dondurma bilgisi de burada. Doğrulama: seed ile 5 gün boşluk.

**[M] Kalıplar dilimleme** — 9683 px liste yerine kategori çipi + tek kategori. Tamam ekranında "günün kalıbı". Doğrulama: sekme yüksekliği < 2 ekran.

**[M] Bugün — tek ekran günlük plan** (Öğren sekmesinin başı) — 3 adım, işaretlenir: ① Kelime (N kart, ~dk) ② Cümle: bugünün kelimeleriyle 3 Diz/Çevir ③ Mülakat: 1 soru (sırayla) 4/3/2 veya tek-soru prova. Hepsi bitince tamam ekranı. Etki: 5 sekmeyi tek döngüye bağlar; şu an günlük akış kelimede bitiyor, cümle kurma (kullanıcının en zayıf yanı) hiç önerilmiyor. Doğrulama: seed'li 3 gün akışı, adım sayısı ≤ 3 + kartlar. Risk: özerklik kaybı → adımlar atlanabilir, sekmeler serbest kalır.

**[L] Benim cevaplarım — kişisel mülakat cevap bankası** — 15 soru için yuva tabanlı kurucu: `tmpl` (zaten var) yuvalarına **önceden doğrulanmış seçenek listeleri** (bölüm, sınıf, proje türü, güçlü yön…) + isteğe bağlı serbest metin. Kayıt `ing:answers`. Kullanıldığı yerler: 4/3/2'de örnek yerine kendi cevabı, provada kendi cevabının anahtar ifadelerine göre kapsama, SRS'te kendi cümlelerinden cloze kartı. Neden şimdi: güçlü model 15 soru × 4-6 yuva × seçenek kombinasyonlarını tutarlı yazabilir. Her birleşim betikle üretilip `motor_test.py`'den yanlış-pozitif taramasıyla + pedagoji ajanının okumasıyla doğrulanır (kombinasyonlar sonlu, hepsi listelenebilir). Etki: öz-ilgi etkisi + hazır hikâye (mülakat hazırlığının çekirdeği). Risk: serbest metin yanlış İngilizce saklar → "kontrol edilmedi" rozeti, örnek cevap yanında durur. Geri alma: ayrı anahtar, özellik kapanınca eski akış.

**[L] Sahte mülakat → tam prova + rapor kartı** — İki mod: **Hızlı** (3 soru, Bugün planına girer) ve **Tam** (8 soru, düşünme 10 sn + cevap sayacı 60 sn, sesli ya da yazılı). Her soruya 1-2 takip sorusu ("Why?", "What did you learn?"). Sonunda rapor kartı: soru başına bulunan tuzaklar, kapsanan/eksik kalıplar, kelime sayısı, kurtarma cümlesi kullanımı, **önceki denemeyle karşılaştırma** (`ing:mocks`). Sayısal not yok, betimsel. Neden şimdi: deterministik puanlama mevcut motorla mümkün. Model, takip sorularını ve `MOCK_KEYS` eş anlamlılarını toplu yazabilir; doğrulama: her takip sorusu + örnek cevap `motor_test` + pedagoji incelemesi, eş anlamlılar için yanlış-eşleşme vaka listesi. Risk: anahtar kelime doldurma → rapor "kapsama"yı gösterir, ödül vermez. Android'de konuşma tanıma ağ ister → metin yedek. Geri alma: eski sohbet modu "serbest" olarak kalır.

**[L] Kişisel hata profili + hedefli alıştırma** — `checkEnglish` her çağrıda (Yaz, Çevir, Mock) bulunan tuzak id'lerini `ing:traps` sayacına yazar. İlerleme'de "En sık 3 tuzağın" + son 10 üretimde azalma. Cümle sekmesi, Diz/Çevir havuzunu o tuzağı içeren cümlelerden seçer. Ustalık rozeti buradan çıkar ("Geçmiş zaman: son 10 cümlede temiz"). Neden şimdi: 26 kurallı motor artık yeterince güvenilir. Model tuzak başına 15-20 hedef cümle (TR→EN) yazar; doğrulama: her EN cevap motordan temiz geçmeli + pedagoji onayı. Risk: motor kapalı liste, "temiz" ≠ doğru → rozet metni "bilinen tuzak görülmedi" der. Geri alma: sayaç okunmaz.

**[XL] Mülakat hazırlık yolculuğu (ünite haritası)** — 258 kelime, 15 soru, 56 kalıp, okumalar ~10 üniteye etiketlenir. Her ünite bir mülakat sorusuna demirli (Ünite 1 "Kendini tanıt": ~20 kelime, 4 kalıp, 1 okuma, 6 cümle, kendi cevabın, 3 tur 4/3/2, mini prova). Ünite bitişi = "kendi cevabını 45 sn'de söyle". Satır içi SVG yol haritası. Yeni kelimeler aktif üniteden gelir; SRS tekrarları global ve serpiştirilmiş kalır. Neden şimdi: etiketleme + ünite başına yeni diyalog/cümle yazımı büyük ölçekli içerik işi. Doğrulama: python ile sözcük kapsama betiği (metinlerin ≥%95'i bilinen/önceki ünite kelimesi), motor taraması, pedagoji okuması. Risk: Duolingo'nun doğrusal yol eleştirisi (özerklik kaybı) → kilit yok, üniteler önerilir, sekmeler serbest. `buildSession` değişir; `unit` alanı yoksa seviye sırasına düşer (geri alma).

## 4. Diğer uzmanlara sorular / bağımlılıklar
- **Pedagoji:** Seri bir mülakat alıştırmasıyla da sayılsın mı, yoksa SRS tekrarı şart mı? Ünite yapısı serpiştirmeyle çatışır mı (yeni kelime ünite içi, tekrar global önerim)? Yuva seçenek listelerini ve takip sorularını kim/nasıl onaylar? Hatırlama oranı metriği A1 için moral bozar mı?
- **Ön yüz / görsel:** harita SVG ve rapor kartı görsel dili; 38-41 px hedefler, `--muted2`/`--bg2` 4.36:1; Akıcılık'taki beyaz `<select>` (1940 civarı) karanlık temayı bozuyor; .ics Blob indirmesi iOS standalone'da çalışır mı (cihazda test)?
- **İkisine:** Workers AI'ı yalnız provadaki takip sorusu için isteğe bağlı kullanmak — bu, yanlış İngilizce riskine değer mi?

## 5. Yapmayın
- **XP, lig, sıralama tablosu:** tek kullanıcı, sıfır taban. Hacmi ödüllendirir ("Kolay"a basıp geç), öğrenmeyi değil.
- **Kalp / can sistemi:** hatayı cezalandırır. Bu seviyede hata, öğrenmenin kendisi.
- **Kayıp korkusunu büyütmek:** "serin yanıyor!" bildirimi, dondurma satın alma, mülakat tarihine geri sayım. Stres terk ettirir (kullanıcının YKS uygulamasında da geri sayım bilinçli olarak yok). Duolingo dondurmayı tam da bu caydırıcı etkiyi yumuşatmak için koymuş ([Lenny's](https://lennysnewsletter.com/p/behind-the-product-duolingo-streaks)).
- **Hacim rozetleri** ("100 kart"), her kartta konfeti.
- **Provaya yüzdelik not:** kapalı liste motor sahte kesinlik verir.
- **Push sunucusu kurmak (şimdi):** iOS'ta sunucu + ana ekran şartı var, tek kullanıcı için .ics yeterli.
- **Günlük kelime tavanını / 40 tekrar kesmesini kaldırmak:** "daha çok" moduna geçmek tekrar yığını yaratır.
- **Sekme sayısını azaltmak için özellik silmek:** sorun sekme sayısı değil, günlük akışın olmaması; çözüm Bugün planı.

## 6. İlk 5
1. **[M] Bugün planı** — 5 sekmeyi tek günlük döngüye bağlar, cümle kurma ve mülakatı her güne sokar.
2. **[M] Etkinlik günlüğü + dürüst hazırlık yüzdesi** — her şeyin veri temeli. Yanlış kilometre taşı vaadini kapatır.
3. **[L] Benim cevaplarım** — birincil hedefe (staj mülakatı) en doğrudan katkı.
4. **[L] Hızlı/tam prova + rapor kartı** — öğrenmeyi görünür kılan geri bildirim anı.
5. **[S] paketi** — ilerleme çubuğu, tamam ekranı sayacı + bugünün kelimeleri, .ics hatırlatma, 44 px / aria-pressed.

---

## Tur 1 — gorsel

# Görsel — Tur 1: görsel kimlik ve teknik kalite

## 1. Ölçtüklerim / kullandıklarım
Headless Chrome 9353, 375×812@2x ve 1280×800. Ekran görüntüsü aldığım durumlar: 5 sekme, 9 alt sekme, kart kutu 0/2/3/4/5, cevap + hafıza ipucu, bitiş ekranı, Yaz sonucu, sahte mülakat geri bildirimi. Görüntüler `gorsel/m-*.png`, `d-*.png`. cdp.py'yi klasörüme kopyaladım, depoya durum dosyası yazmadım.

- **Doğrulanmış hata, sınıf adı çakışması:** `.stat .v.acc` (satır 158, 2159) vurgu rengi için yazılmış, ama `.acc` akordeon sınıfı (satır 178) da aynı öğeye uygulanıyor. Ölçülen hesaplanmış stil: `border:1px rgba(255,255,255,.08)`, `radius:16px`, `bg #1E2140`. Sonuç: İlerleme sekmesinde seri sayısı "0 🧊2", amaçsız bir hap kutusunun içinde çıkıyor (m-ilerleme.png).
- **Doğrulanmış hata, diyalog seslendirmesi:** `buildReadCard` (satır 1622) `.replace(/^A:|B:/g,'')` kullanıyor. Bu regex yalnız baştaki "A:"yı siliyor. 7 diyalogun ilkinde 2 tane "A:" kalıyor ve TTS bunları sesli okuyor.
- **Kontrast (WCAG oranları, hesapladım):**
  - "Kolay" düğmesi, beyaz yazı nane zeminde: **1.91–2.62**
  - "Tekrar" düğmesi, beyaz yazı mercan zeminde: 2.55–3.31
  - `.ai-btn`, beyaz yazı mor zeminde: 2.77–4.26
  - Seviye etiketi `.tag` (`#E09A2D`, 10.5px): **2.12**
  - Dikte boşluğu ve `.tip b`: 2.28
  - Oturum ilerleme çubuğunun yolu, zemine karşı: 1.27 (boş hâli görünmüyor)
  - `.say.sm` (`--ink`), `--bg2` üstünde: 1.05. Kalıplar sekmesinde hoparlör düğmesinin sınırı yok olmuş.
- **Emoji:** 155 kullanım, 47 farklı. SVG yalnız 11 tane. Riskler:
  - 🇹🇷 Windows'ta "TR" harfleri olarak çıkar.
  - 🫥 Unicode 14; eski Android'de kutu (tofu) olur.
  - ⏱ VS16 olmadan metin glifi olarak çiziliyor. Ekranda "⏱Akıcılık" kayık ve küçük duruyor.
  - 🎙 lacivert düğme üstünde gri ve neredeyse görünmüyor (m-mul-mock.png).
  - Hoparlör için iki ayrı sistem var: SVG (4 yer) ve 🔊 emoji (6 yer).
  - 🎯 üç farklı anlamda kullanılıyor: hedef, hazırlık, örnek çeviri.
- **CSS ve kod:**
  - Satır içi `style=` 67 tane, bunların 60'ı JS şablonlarında. `.ai-btn`'i satır içi stille ikincil düğmeye çeviren 8 yer var.
  - 27 farklı font-size, 13 farklı radius.
  - Token dışı renkler: `#fff` ×21, `#EDEEF7` ×15, `rgba` ×32.
  - `cursor:pointer` taşıyan 20 düğme varyantı var. Aynı "Kontrol et" eylemi üç renkte: Diz'de sarı, Çevir'de mor, dikte'de mürekkep.
  - `.qa` (216–221) ile `.acc` (178–192) neredeyse aynı akordeonun iki kopyası.
  - Segment bağlama kodu 3 kez kopyalanmış (`switchTab` 2195+).
  - `SPK` sabiti var (1341), yine de hoparlör SVG'si 3 yerde elle tekrar yazılmış (1485, 1523, 1996).
  - 🐢 tek başına düğme ve `aria-label` yok (1617, 1909).
- **Font:** Fraunces yalnız 600 ağırlığında kullanılıyor, ama değişken opsz+wght dosyası iniyor: latin 67KB + latin-ext 60KB. Jakarta 49KB. **Toplam 176KB**, HTML gzip'li 61KB.
  - `Fraunces:wght@600&text=<ASCII+Türkçe>` tek dosya ve **14.4KB** (ölçtüm).
  - googleapis CSS'i render'ı bloklayan üçüncü taraf kaynak (`renderBlockingStatus: blocking`).
  - SW fontu ilk ziyarette önbelleğe almıyor, çünkü sayfa o sırada henüz SW kontrolünde değil. Kurulumdan hemen sonra çevrimdışı açılırsa sistem fontuna düşer. Bu çıkarım; çevrimdışı açılışı test etmedim.
- **Yükleme:** 3G benzetimi: FCP 360ms, DCL 2041ms. Sorun değil.
- **Biçim:** `color-scheme` yok. Akıcılık'taki `<select>` koyu temada bembeyaz açılır kutu olarak çıkıyor.
- **Defter metaforu:** Çizgiler 30px aralıklı, metin satır yükseklikleri 24/26/42px. Yazı çizgilerin arasından geçiyor, çizgilerin üstüne oturmuyor. Defter değil, rastgele şerit gibi okunuyor.
- **Masaüstü:** 460px sütun, klavye kısayolu yok.
- **PWA:**
  - Simgede düz blok bir "E" var ve markanın Fraunces fontu kullanılmamış.
  - 3 PNG de köşeleri şeffaf, önceden yuvarlatılmış (köşe pikseli alpha=0).
  - `maskable` yok, yani Android uyarlanabilir simgede beyaz daire içinde küçülmüş görünür. Bu çıkarım, cihazda görmedim.
  - `apple-touch-icon` şeffaf; iOS şeffaf alanı siyahla doldurur.
  - Manifest'te `id`, `screenshots`, `shortcuts` yok.
- **Geri bildirim görseli:**
  - Yaz ve Mülakat düzeltmeleri değişen kelimeyi işaretlemiyor. "I am **a** student" düz metin olarak geliyor.
  - Mülakat düzeltme balonu tamamen nane renkli, oysa nane = başarı anlamı taşıyor.
  - Bitiş ekranı sıfır kartta da 🎉 gösteriyor. Kartlar arasında geçiş hareketi yok.

## 2. Önceki turdan farkım
- Dokunmadım: 44px hedefler, `--muted2` kontrastı, odak yönetimi, `aria-current`, toast `aria-live`, `user-scalable`. Bunlar önceki ön yüz turunda yapıldı.
- Yeni olanlar: rate/tag kontrastı (önceki tur yalnız muted2'ye baktı), token/tema mimarisi, ikonografi, font yükü, PWA simgesi, hareket, TTS cümle bölme.
- Yeniden açtığım bir şey yok. Mikrofonla sözlü üretim ertelenmişti. Ben yalnız *mevcut* mikrofon çıktısının görselleştirilmesini öneriyorum ("Mikrofon sonucunu görselleştir" maddesi). Yeni mikrofon özelliği önermiyorum.

## 3. Öneriler: iddia merdiveni

**[S] Sınıf çakışmasını düzelt.** `.v.acc` yerine `.v.hl` kullan (158, 2159). Etki: İlerleme ekranındaki bozuk kutu gider. Doğrulama: hesaplanmış stilde `border` 0px olmalı. Geri alma: tek satır.

**[S] Diyalog TTS regex'i.** `/^[AB]:\s*/gm` satır kırılmasından *önce* uygulanmalı (1622). Doğrulama: `flat.match(/[AB]:/)` null olmalı.

**[S] `color-scheme: dark`** `:root`'a eklenmeli. Böylece select ve kaydırma çubukları koyu olur.

**[S] Rate ve tag kontrastı.**
- Kolay/Tekrar/`.ai-btn` yazısı koyu mürekkep olsun (`#3d2b06` modeli, Zor zaten 7.56) ya da zeminler koyulaşsın.
- `.tag` rengi `#9A6410` civarı olsun (≥4.5).
- Doğrulama: kontrast betiğim (`gorsel/kontrast.py`) her çift için ≥4.5 vermeli.

**[S] 🐢 düğmelerine `aria-label`; 🇹🇷 kaldırılsın.**

**[S] Masaüstü klavye.** Space ile göster, 1/2/3 ile puanla. `keydown`, yalnız `.card` görünürken çalışsın.

**[M] Okuma TTS'ini cümlelere böl, okunan cümleyi vurgula.**
- `buildReadCard` `splitSentences()` ile bölsün (zaten var, 2534d2a). Cümleler `onend` zinciriyle okunsun ve okunan `<span>` vurgulansın.
- Neden: Chrome masaüstünde "Google US English" sesi uzun konuşmayı ~15 sn'de kesiyor. Bu bilinen Chromium hatası; şüphe olarak işaretliyorum, cihazda duymadım. Ortalama metin 47 kelime, 0.85 hızda ~20 sn sürüyor.
- Öğrenme etkisi: yazı ile ses eşleşmesi (okurken dinleme).
- Risk düşük. Kelime düzeyi `onboundary` ağ seslerinde gelmiyor, o yüzden cümle düzeyi güvenli taban.

**[M] Düzeltme farkı görselleştirmesi (ins/del).**
- `buildCheckCard` (1655) ve mülakat geri bildirimine, girdi ile `res.fixed` arasında kelime düzeyi LCS farkı eklenmeli. Silinen `<del>` mercan, eklenen `<ins>` amber olsun.
- Düzeltme balonunun rengi naneden amber'e geçsin.
- Etki: öğrenci ne değiştiğini *fark eder*; dikkat ve fark etme etkisi var (pedagojiye soru).
- Doğrulama: `araclar/` biçiminde 10 vakalık fark testi.
- Risk: noktalama ve büyük harf gürültüsü. `normAns` tarzı normalize ederek karşılaştır.

**[M] Fontları kendin barındır ve alt kümele.**
- Fraunces 600 + `text=` alt kümesi 14KB. Jakarta latin ve latin-ext olarak `@font-face` ile alınır. İki woff2 dosyası depoya girer (tek dosya kuralının gerekçeli istisnası). `sw.js` FILES listesine eklenir.
- Etki: 176KB yerine ~63KB. Üçüncü taraf render engeli kalkar. İlk kurulumdan itibaren çevrimdışı yazı tipi garanti olur.
- Doğrulama: önce/sonra ekran görüntüsü. opsz ekseni kaybı 40px başlıkta göze batıyor mu, kullanıcı baksın. Ardından `Network.emulateNetworkConditions offline` ile soğuk açılış testi.
- Geri alma: `<link>` geri konur.

**[M] Simge ve manifest kalitesi.**
- Fraunces "İ" veya kart/defter motifi taşıyan SVG simge. Headless Chrome'da `omitBackground` ile 512/192/180 PNG üretilir (node gerekmez, cdp.py yeter).
- `maskable` (güvenli bölge %80), `monochrome`, opak apple-touch-icon.
- Manifest'e `id` ve 2 `shortcut` ("Bugünkü kartlar", "Sahte mülakat"). Bunun için `#study`/`#mock` hash yönlendirmesi gerekir.
- Doğrulama: maskable.app benzeri daire ve kare maske önizlemesi; ekran görüntüleri kullanıcı onayına.

**[M] Defter çizgisi ritmi.**
- Kart içi metin 30px ızgaraya oturtulmalı (line-height 30px katları) ya da çizgiler yalnız örnek cümle bölgesine indirilmeli.
- Estetik bir karar; iki varyantın ekran görüntüsü kullanıcıya gösterilsin.

**[L] Büyük bahis 1: Tasarım token sistemi + CSS temizliği + aydınlık "kâğıt" tema.**
- **Ne:**
  - 27 font-size 8 adımlı ölçeğe, 13 radius 4'e insin.
  - `#fff`/`#EDEEF7`/rgba token'a dönsün.
  - 60 JS satır içi stil sınıfa taşınsın.
  - 20 düğme varyantı ~6'ya insin: primary, secondary, ghost, chip, icon, rate.
  - `.qa` ile `.acc` birleşsin; segment bağlama tek fonksiyona insin.
  - Sonra `[data-theme=light]` + `prefers-color-scheme` ile aydınlık tema yalnız token yeniden tanımı olur. İlerleme sekmesine tema seçici gelir.
- **Neden şimdi:** 2300 satırlık tek dosyada tutarlı, tüm dosyayı tarayan bir refaktörü tek geçişte yapıp her durumu ekran görüntüsüyle doğrulamak artık güvenilir. Altyapı hazır: cdp.py + 14 durumlu çekim listem.
- **Doğrulama:**
  - Koyu temada önce/sonra 14+ durumun piksel karşılaştırması. PNG'yi zlib ile açmak bu turda simge pikselleri için çalıştı, PIL gerekmiyor. Değişiklik ≈0 olmalı.
  - Aydınlık temada kontrast betiği tüm çiftlerde ≥4.5 vermeli.
- **Risk:** nadir durumlar (mikrofon canlı, hata kutusu, bitiş ekranı) kayabilir.
- **Geri alma:** tek commit revert. Kayıt (localStorage) etkilenmez. Maliyet 0.

**[L] Büyük bahis 2: Tutarlı satır içi SVG ikon seti.**
- **Ne:**
  - `<body>` başına ~24 sembollük `<svg><symbol>` sprite eklenir. Çizgi kalınlığı nav ikonlarıyla aynı 1.9, renk `currentColor`.
  - Arayüzdeki 155 emojinin işlevsel olanları (mikrofon, hoparlör, yavaş, şablon, tekrar, sonraki, ipucu, uyarı, kontrol) ikona geçer.
  - Veri içindeki emojiler (`INTERVIEW_QA.tmpl` 🧭 ×10, `GUIDE.ico`) anahtara çevrilir.
  - Duygusal emojiler kalabilir: 🔥 seri, 🧊 dondurma.
  - Nav'daki belirsiz "Pratik" ikonu yenilenir.
- **Neden şimdi:** tutarlı bir el yazımı SVG seti tek oturumda üretilebilir. Ek boyut ~5KB.
- **Doğrulama:** emoji regex sayımı 155'ten ≤20'ye inmeli. Her görünümün ekran görüntüsü alınmalı. Dekoratif ikonlara `aria-hidden`, tek başına ikon düğmelerine `aria-label`.
- **Risk:** sıcaklık kaybı; 🔥/🧊/🎉 bu yüzden kalır.
- **Geri alma:** sprite ve çağrılar tek commit.

**[L] Büyük bahis 3: Mülakat "sahnesi".**
- **Ne:**
  - Sahte mülakat ve Kulak üstüne SVG görüşmeci figürü (2–3 poz: dinliyor, konuşuyor, başını sallıyor) ve sade ofis arka planı.
  - Konuşma animasyonu TTS `onstart`/`onend` ile senkronize olur.
  - Soru balonunda cümle vurgusu (yukarıdaki TTS bölme altyapısı kullanılır).
  - İsteğe bağlı: diyaloglarda A/B için iki ses, iki renk balon.
- **Neden şimdi:** tutarlı karakter SVG'si artık el yazımıyla yapılabilir; dış görsel ve ücret yok.
- **Etki:** prova hissi; kanıtı zayıf, motivasyon tarafı (ürüne soru).
- **Doğrulama:** kullanıcı onayı şart, çünkü öznel kalite. `prefers-reduced-motion`'da statik poz. 60fps için yalnız transform/opacity, performans izi alınmalı.
- **Risk:** kitsch ya da "tekinsiz vadi" etkisi.
- **Geri alma:** `#intMock`'tan önce bağımsız bir blok; bayrakla kapatılır.

**[L] Büyük bahis 4: Anlamlı hareket sistemi.**
- **Ne:**
  - Hareket token'ları: `--dur-1 120ms`, `--dur-2 240ms`, `--ease-out`.
  - Kart çıkış ve giriş kayması (puanlamadan sonra yön: Tekrar sola, Kolay sağa).
  - Doğru cevapta çizilen onay işareti (stroke-dashoffset).
  - İlerleme çubuğu dolunca nabız efekti.
  - Bitiş ekranında yalnız gerçek iş yapıldıysa kutlama; 0 kartta 🎉 yerine nötr görsel.
  - Android'de `navigator.vibrate(10)` (iOS'ta yok, sessizce düşer).
- **Doğrulama:** `performance` izinde layout yok. Azaltılmış hareket global kuralı zaten var (297).
- **Risk:** hız kaybı. Animasyon ≤240ms olmalı ve tıklamayı bloklamamalı.

**[M] Mikrofon sonucunu görselleştir.** Yeni özellik değil: mevcut transkript hedef kalıpla kelime kelime eşleşir (eşleşen nane, eksik kesik çizgi). Akustik puan yok.

## 4. Diğer uzmanlara sorular / bağımlılıklar
- **Pedagoji:**
  - ins/del farkı A1-A2 düzeyde fark etmeye yardım eder mi, yoksa bilişsel yük mü olur? Yalnız ilk 3 düzeltme mi gösterilsin?
  - Okuma sırasında cümle vurgusu mu, yalnız ses mi?
  - "went to interview"daki eksik artikel ve "in ITU" (doğrusu at ITU) motorda yakalanmıyor. Bunlar sizin alanınız.
- **Ürün:**
  - Aydınlık tema ve mülakat sahnesi pazarlama ekran görüntüsü için öncelikli mi?
  - Mağaza ekran görüntüleri ancak simge ve tema bittikten sonra anlamlı.
  - Shortcut'lar için hash yönlendirme sizin akışınızla çakışıyor mu?
- **İkisine:** yeni içerik üretilirse (diyalog, mülakat sahnesi), A/B konuşmacı etiketi biçimi veride sabitlensin. Regex'e güvenilmesin.

## 5. Yapmayın
- **258 kelimenin her birine illüstrasyon:** çoğu soyut kelime (responsibility, experience). Kötü metafor yanlış çağrışım öğretir. Ayrıca boyut ve kitsch riski var.
- **Dalga formu veya "telaffuz puanı":** akustik model olmadan uydurma puan olur. iOS'ta `getUserMedia` ile `SpeechRecognition` aynı anda mikrofonu ister ve çakışır (şüphe).
- **CSS framework / ikon CDN'i:** çevrimdışı çekirdek bozulur.
- **Varsayılan aydınlık tema:** mevcut kullanıcının alışkanlığını bozar. Sistem tercihi + manuel seçim olsun.
- **Tüm emojiyi silmek:** sıcaklık kaybı. İşlevsel olanları ikona geçir, duygusal olanlar kalsın.

## 6. İlk 5
1. S paketi: `.acc` çakışması + diyalog regex + `color-scheme` + rate/tag kontrastı + 🐢 etiketi (1 saat, risk ~0).
2. M: düzeltme farkı görselleştirmesi (ins/del + amber).
3. M: TTS cümle bölme + okunan cümle vurgusu.
4. L: token sistemi + CSS temizliği; aydınlık tema bunun üstüne gelir.
5. L: SVG ikon seti, ardından simge/manifest ve self-host font.

---

## Tur 2 — pedagoji

# Pedagoji — Tur 2: eleştiri ve uzlaşma

## 1. Diğer raporlara cevap

**Birleştirilenler**
- **Ürün "Benim cevaplarım" = Pedagoji "STAR sihirbazı"** → tek özellik: *Benim cevaplarım*. **DEĞİŞTİR:**
  - Yuvalar önceden doğrulanmış çerçeve ve seçenek listesinden gelir; bu kısım sonlu olduğu için betikle listelenip denetlenebilir.
  - Serbest metin sonlu değil; onu motor ve geçmiş zaman bayrağı denetler, yanında "kendi metnin" rozeti durur.
  - STAR soruları (Q4, Q9, Q10, Q14, Q15) Durum/Görev/Eylem/Sonuç adımlarıyla, diğer sorular mevcut `tmpl` yuvalarıyla kurulur.
- **Görsel ins/del = Pedagoji Çevir farkı** → tek bileşen. **DEĞİŞTİR:**
  - A1-A2 öğrenci için en fazla 3 değişiklik gösterilir, kalanı "+2 düzeltme daha" diye özetlenir. Fark etme etkisi var, ama bilişsel yük sınırı da var.
  - Çevir'de örnek çeviriyle fark yalnız yakın cevapta (≤3 kelime fark) otomatik gösterilir. Uzak cevapta ancak "Farkı göster" ile açılır, çünkü geçerli başka bir çeviri kırmızıyla boyanmamalı.
  - Görsel'in amber düzeltme balonu ile benim "yanlışa ✅ yok" maddem aynı düzeltmenin parçası.
- **Görsel "mikrofon sonucunu görselleştir" = Pedagoji "gölgeleme ölçümü"** → KABUL, tek madde. Akustik puan yok.
- **İki XL ünite önerisi aynı** → birleşti. **DEĞİŞTİR:** iki aşamaya ayrılsın (bkz. §3).

**Ürün**
- Bugün planı: **KABUL.** 2. adım (cümle) şart; kullanıcının en zayıf yanı bugün hiç önerilmiyor.
- Seri sorusu: seri herhangi bir üretim alıştırmasıyla (3 Diz/Çevir, 1 prova sorusu, 1 tur 4/3/2) sayılsın. SRS tekrar borcu ayrıca görünür kalır.
- Etkinlik günlüğü, dönüş karşılaması, ilerleme çubuğu, tamam ekranı listesi: **KABUL.**
- Dürüst hazırlık yüzdesi: **KABUL.** "Hatırlama oranı" A1 öğrencinin moralini bozmaz: hedef %85-90 aralığı olduğu için oran genelde yüksek çıkar.
- Prova + rapor kartı: **DEĞİŞTİR.** Kapsama anahtar kelimeyle değil, yapıyla ölçülsün: zaman bağlamı var mı, geçmiş fiiller doğru mu, sonuç cümlesi var mı. `MOCK_KEYS` alt dize eşlemesi kelime sınırına çekilsin (`\b`). Takip soruları önceden yazılı ve doğrulanmış olsun.
- Kişisel hata profili: **DEĞİŞTİR + ERTELE.** "Motor artık yeterince güvenilir" öncülü ölçümle çürüdü: doğru öğrenci cümlelerinin 22/40'ı bozuluyor. Kesinlik katmanından sonra gelsin ve yalnız `conf:high` kuralları saysın; aksi hâlde profil sahte hatayı "zayıf yönün" diye öğretir.
- Kalıplar dilimleme: **KABUL**, gölgeleme düğmesi korunarak.
- Workers AI ile takip sorusu: **REDDET** (§6).

**Görsel**
- Okuma TTS cümle bölme + vurgu: **KABUL.** Soruya cevap: evet, cümle vurgusu olsun; okurken dinleme akıcılığa yardım eder.
- S paketi (sınıf çakışması, regex, kontrast, `color-scheme`): itiraz yok.
- Token sistemi, aydınlık tema, SVG ikon seti, self-host font, simge: pedagojik itiraz yok. Mülakat hedefine katkıları dolaylı, sırada geride kalsınlar.
- Hareket sistemi: **KABUL**, ≤240 ms ve tıklamayı bloklamadan.
- Mülakat sahnesi: **ERTELE.** Öğrenme kanıtı zayıf. Aynı emekle soru paraphrase bankası, gerçek mülakatta kulağın karşılaşacağı zorluğu doğrudan çalıştırır.
- Görsel'in sorusu ("in ITU", eksik artikel):
  - "in ITU/university" → *at* için düşük kesinlikli ipucu verilebilir.
  - Genel artikel eksikliği regex'le güvenilir yakalanamaz; otomatik düzeltme yok.

## 2. Kendi tur 1'imden geri çektiklerim / değiştirdiklerim
- **Çevir'de "Dinle örneği okusun"** → genişletiyorum: Yaz'da temiz sonuçta referans cümle yok, bu yüzden Dinle düğmesi hiç gösterilmesin. Anadili sesi, doğrulanmamış cümleyi seslendirmemeli.
- **Seviye tespiti (M)** → ayrı özellik değil, ünite yerleştirmesine katıldı ("hangi üniteden başlayayım").
- **Kelime başına 3 örnek cümle** → içerik protokolüne bağlandı. Önce yalnız 88 adet lvl5 kelimeye 2. cümle eklensin.
- **Kör ikinci model incelemesi** → zayıflattım: aynı model ailesi aynı kör noktaları paylaşır (bkz. §4).
- **"TICLE/CLC'den 250 hata"** → ham korpus erişimi şüpheli. Hata tipleri literatürden alınsın, cümleleri ben yazayım; doğru set ise gerçek öğrenci cümlesi biçiminde olsun (`fp.js` gibi).

## 3. Sıralama
Birincil hedef mülakat, seviye A1-A2. Hedefe en çok hizmet eden büyük bahis **Benim cevaplarım + prova**: öğrenci 3-5 kendi hikâyesini İngilizce kurar, 4/3/2 ile otomatikleştirir, provada dener. Mülakat hazırlığının çekirdeği budur.

Bağımlılık zinciri:
1. **Motor zarar verme yaması (S)** her şeyin önkoşulu. Prova raporu, Benim cevaplarım ve hata profili `checkEnglish` kullanıyor; motor bozuk kaldıkça her yeni özellik yanlış öğretmeyi çoğaltır.
2. **İçerik doğrulama protokolü** (betik + inceleme akışı) yeni içerikten önce kurulur.
3. **Ünite A (M):** mevcut 258 kelime, 15 soru ve 57 kalıp 10 üniteye etiketlenir. Yeni içerik yok, risk düşük, Bugün planına hemen bağlanır.
4. **Ünite B (XL):** 1000 kelimeye genişleme ve ünite başı diyalog/okuma. Protokol işledikten sonra yapılır.
5. **Motor kesinlik katmanı (L)**, hata profilinden önce gelir.

## 4. İçerik doğrulama protokolü ve lisans

**Protokol (değiştirilmiş hâli)**
- **Seçim:**
  - Liste yalnız geliştirme sırasında ölçüt olarak kullanılır; listenin kendisi depoya girmez.
  - Kelime ve anlam kararı bizim.
- **Örnek cümle önceliği:** önce kendi yazımımız. Tatoeba yalnız karşılaştırma ve ilham kaynağı.
- **Lint (python3):**
  - hedef kelime cümlede geçer
  - diğer kelimeler bilinen kelime + 1000 bandı içinde
  - 4-10 kelime, tekrar yok
  - `motor_test` 0 isabet
- **İnceleme:** ikinci geçiş "kör onay" değil, Türk öğrenci hata listesini taşıyan bir **hata avcısı** rolü. Her cümle için doğallık, anlam, Türkçe-İngilizce eşleşmesi ve kayıt (resmi/gündelik) sorulur.
- **Yeni katman, kullanıcı:** Türkçe tarafını kullanıcı doğrular; bu konuda en güvenilir kaynak anadilli olan o. İngilizce tarafını model inceler, emin olunmayan cümle atılır.
- **Örneklem:** her 100 cümleden 20'si raporla kullanıcıya gösterilir. Bir anlam hatası çıkarsa o parti yeniden incelenir.

**Lisans** (hukuki görüş değil):
- Tatoeba: CC BY, share-alike yok. Atıfla pazarlamaya uygun, ama kalite değişken. Bu yüzden içerik kaynağı değil, ilham olsun.
- NGSL/BSL: CC BY-SA. Listeyi gömmek SA yükümlülüğü getirebilir. Listeyi dağıtmadan yalnız seçim ölçütü olarak kullanmak düşük riskli yol (şüphe: avukat onayı yok).
- Oxford 3000 vb. tescilli listeleri kopyalamayın.

## 5. Son liste (öncelik sırasıyla)
1. **[S] Motor zarar verme yaması.**
   - `missing_be_ing`, `tobe_bare`, `past_marker`, `pres_perf`, `have_years`, `interested_with`, `want_to`, `no_be`, `speak_than` guard'ları; `’` → `'` dönüşümü.
   - Yer: index.html 958-1113, `checkWriting` 1646.
   - Kabul ölçütü: `fp.js` 40/40 + 72 + 391. **Kabul.**
2. **[M] Düzeltme kartı + ins/del** (en fazla 3 fark). `buildCheckCard` 1655, mock fb 2087. **Değiştirildi (birleşik).** Yeni metin:
   - Temiz Yaz: "Bilinen tuzak yok. Tam denetim değil — kelime seçimine sen de bak."
   - Temiz Çevir: "Bilinen tuzak yok — örnekle karşılaştır 👇"
3. **[S] İçerik düzeltmeleri.**
   - #64, #143, #135 kelime örnekleri; okuma 871 ve 885; Q15 ile 895'teki "teacher" → "professor"; Q3, Q12, `MOCK_KEYS` "middle way" → "middle ground".
   - MNEM w-notu: "Dikkat: w dudak yuvarlanarak söylenir — v değil."
   - Q1 "supervisor" için kullanıcıya sorulacak.
   - **Kabul.**
4. **[S] Cümle Diz alternatif sıra.** Yer: 1735. Yeni metin: "Doğru! 🎯 Bu sıra da olur: *I have a meeting today.*" **Kabul.**
5. **[M] Bugün planı**, cümle adımı zorunlu (Ürün). **Kabul.**
6. **[L] Benim cevaplarım** (birleşik) + geçmiş zaman bayrağı. Yeni metinler:
   - STAR geçmiş ipucu: "Geçmişi anlatıyorsun — fiiller de geçmişte mi? (call → called)"
   - Serbest metin rozeti: "Kendi metnin — bilinen tuzak yok, ama tam denetim değil."
   - **Değiştirildi.**
7. **[L] Prova + rapor kartı**, kapsama yapı ölçüsüyle. `sendMock` 2063. **Değiştirildi.**
8. **[M] Üretimi öne çek:** öğrenme adımındaki 2. görüş TR→EN. `grade` 1247, `renderStudy` 1331. **Kabul.**
9. **[M] Ünite A:** mevcut içerik etiketlenir, `buildSession` aktif üniteden çeker. **Yeni.**
10. **[L] Motor kesinlik katmanı + 500 vakalık korpus.** Yeni metin (düşük kesinlik rozeti): "Emin değilim — şuna bir bak:" **Kabul.**
11. **[M] Kulak:** soru başına 3-5 paraphrase + minimal çift algı eğitimi. **Kabul.**
12. **[XL] Ünite B / 1000 kelime**, §4 protokolüyle. **Değiştirildi.**

## 6. Reddedilenler
- **Workers AI takip sorusu:** önceden yazılmış ve doğrulanmış 2-3 takip sorusu aynı işi görür; serbest üretim yanlış İngilizce riskini geri getirir.
- **Hata profilinin şimdi yapılması:** yanlış pozitif oranı düşmeden profil sahte hatayı kişisel zayıflık diye öğretir.
- **Mülakat sahnesi (şimdilik):** öğrenme kanıtı zayıf, emek paraphrase bankasına gitsin.
- **Provada anahtar kelime kapsamasını rapora koymak:** alt dize eşleşmesi papağanlığı ödüllendirir ("know" kelimesi "now" kalıbını karşılıyor).
- **Tatoeba/NGSL içeriğini doğrudan gömmek:** kalite değişken, SA lisans riski var.

---

## Tur 2 — urun

# Ürün — Tur 2: çapraz eleştiri ve uzlaşma

## 1. Diğer raporlara cevap

**Pedagoji**
- **Motor zarar verme yaması [S]: KABUL, 1 numara.**
- **Kesinlik katmanı + 500 vakalık korpus [L]: KABUL.** Ürün tarafında gereken tek şey: `conf:low` sonuçları düzeltme olarak değil, "Kontrol et" ipucu olarak göstermek.
- **Çevir/Yaz kartı [S] + Görsel'in ins/del farkı [M]: aynı iş, BİRLEŞTİR.** Tek LCS fark bileşeni iki yerde kullanılır:
  - Yaz ve Mock'ta karşılaştırma girdi ↔ `fixed`: mercan del, amber ins.
  - Çevir'de karşılaştırma girdi ↔ örnek. Buradaki fark hata değil, çünkü başka doğru çeviriler de olabilir. Bu yüzden **nötr renk** ve "örnekten farklı" etiketi.
  - Ortak kural: düzeltme yoksa ✅ yok ve Dinle düğmesi örneği okur.
- **STAR sihirbazı [L] = benim "Benim cevaplarım" [L]: BİRLEŞTİR.** Tek depo `ing:answers`, iki kurucu:
  - STAR adımları 5 davranışsal soru için (Q4, 9, 10, 14, 15).
  - Yuva çerçevesi kalan 10 soru için.
  - Uzlaşma: önce doğrulanmış seçenek listesi gelir, serbest boşluk ikincil. Serbest boşluk motor + geçmiş bayrağıyla denetlenir ve "Senin metnin" etiketi taşır.
- **STAR geçmiş bayrağı [M]: KABUL.** Prova rapor kartının ön şartı.
- **Üretimi öne çek [M]: KABUL.**
- **3 örnek cümle döngüsü: KABUL, ama doğrulama protokolünden sonra.**
- **Kulak paraphrase, minimal çift [M]: KABUL.** Kulak alt sekmesinde kalır.
- **Cümle Diz alternatif sıra [S], içerik düzeltmeleri [S], /w/ ipucu: KABUL.**
- **Seviye tespiti (10 dk): DEĞİŞTİR.** Onboarding'de 10 dakika, ilk değerin gelmesini çok geciktirir. Benim önerim:
  - İlk seanstan *sonra* sunulan 2 dakikalık öz-değerlendirme: 20 kelime, "biliyorum / bilmiyorum".
  - Her 5 "biliyorum"dan biri 3 şıkla yoklanır.
  - Bilinen kelime box 3'ten başlar.
- **Ünite müfredatı [XL]: KABUL, ortak öneri, ama SON sırada.**
- **1000-1200 kelime [XL]: DEĞİŞTİR, kademeli yap.** 258 kelime günde 6 hızla ~44 günde bitiyor. Kullanıcı Ağustos'tan beri kullanıyorsa havuz büyük ihtimalle bitmiştir (**şüphe**, gerçek kaydı görmedim), yani genişleme gerçek bir ihtiyaç.
  - Önce +250 kelime: Pedagoji'nin listelediği temel boşluklar (be, study, say…) + mülakat kelimeleri.
  - 1000'e ancak protokol bir kez işledikten sonra çıkılır.
- **Gölgeleme ölçümü [L] + Görsel'in "mikrofon sonucunu görselleştir" [M]: aynı iş, BİRLEŞTİR → [M].** "Anlaşılırlık" diye çerçevelenir, puan verilmez.
- **Workers AI çeviri reddi: KABUL.**

**Görsel**
- **S paketi** (`.acc` çakışması, diyalog regex'i, `color-scheme`, rate/tag kontrastı, 🐢 etiketi): **KABUL.** Masaüstü klavye maddesi bende de vardı, birleşti.
- **Token sistemi + CSS temizliği [L]: DEĞİŞTİR → [M].** Yeni bileşenlerden (Bugün, rapor kartı, fark) *önce* ya da onlarla birlikte yapılır, çünkü yeni ekranlar satır içi stille çoğalmasın.
- **Aydınlık tema: ERTELE.** Öğrenmeye etkisi yok. Pazarlama ekran görüntüsü aşamasında yeniden açılır.
- **SVG ikon seti [L]: DEĞİŞTİR → [M].** Yalnız işlevsel ikonlar, token işiyle birlikte. 🔥🧊 kalır.
- **Mülakat sahnesi [L]: ŞİMDİLİK REDDET.** Değer rapor kartında ve kişisel cevapta. Figürün öğrenme kanıtı zayıf, kitsch riski yüksek.
- **Hareket sistemi [L]: DEĞİŞTİR → [S].** Yalnız üç şey:
  - 0 kartta 🎉 gösterme (benim tamam ekranı maddemle birleşti),
  - onay işareti çizimi,
  - ≤200 ms kart geçişi.
- **Self-host font [M], simge/manifest [M], TTS cümle bölme [M]: KABUL.** Manifest kısayolları (`#bugun`, `#prova`) Bugün planıyla uyumlu.

## 2. Kendi tur 1 maddelerimden geri çektiklerim / değiştirdiklerim
- **Kişisel hata profili [L]: GERİ ÇEKTİM.** Motor doğru cümlelerin %55'ini bozarken sayaç sahte tuzak kaydeder, "en sık 3 tuzağın" yanlış teşhis olur. Kesinlik katmanından sonra, yalnız `conf:high` kurallarla yeniden açılabilir.
- **Prova rapor kartı: DEĞİŞTİ.** `MOCK_KEYS` alt dize eşliyor (2082, "know" içinde "now" bulunuyor). "Kapsanan kalıplar" bölümü çıkıyor. Yerine:
  - STAR yapısı var mı,
  - geçmiş zaman,
  - yalnız `conf:high` tuzaklar,
  - kişisel cevaba yakınlık.
- **Dürüst hazırlık yüzdesi: DEĞİŞTİ.** Prova bileşeni anahtar kelime kapsamasına değil, tamamlanma + kişisel cevabın varlığına bakar.

## 3. Sıralama ve bağımlılıklar
Kullanıcının hedefi mülakat, seviyesi A1-A2. Bu hedefe en çok hizmet eden büyük bahis **Benim cevaplarım**: 3-5 hazır hikâye mülakatta en yüksek getirili iş. Bağımlılık zinciri:

1. Motor yaması → cevap denetimi, prova ve hata profili mümkün olur.
2. Etkinlik günlüğü → Bugün planı ve hazırlık yüzdesi.
3. Benim cevaplarım → 4/3/2'de kendi cevabın, prova karşılaştırması, ünitenin "hedef soru"su.
4. Doğrulama protokolü → 3 örnek cümle, +250 kelime, ünite müfredatı.
5. Token işi → yeni ekranlar (bloklamaz, ama önce gelirse stil borcu birikmez).

## 4. İçerik doğrulama protokolü
**Lint + kör ikinci inceleme: KABUL.** Notlar:
- **"İkinci model"** = abonelik içinde ayrı bir Claude ajan oturumu. Ücretli API değil.
- **Kullanıcı örneklemi İngilizce doğruluğunu ölçemez,** çünkü kullanıcı A1. Kullanıcı yalnız Türkçenin doğallığını ve konunun kendine uygunluğunu denetler. İngilizce doğruluğu iki modelin uyuşmasına + motorun 0 isabet vermesine dayanır.
- **NGSL/BSL:** listeyi yalnız seçim filtresi olarak kullan. Sıra ve frekans dosyası uygulamaya girmesin, tek tek kelimeler telif konusu değil. Bu hukuki görüş değil (**şüphe**); pazarlamadan önce kontrol edilmeli.
- **Tatoeba (CC BY 2.0 FR):** atıf şartı yönetilebilir (Hakkında sayfası + her cümlede `src` alanı). Ama mülakat alanında cümle az ve kalite değişken. Öneri: yalnız temel kelimelerde ve atıflı kullanılsın; mülakat içeriği üretilip doğrulansın.
- **İçerik dosyası düzeni:** her öğeye `src` (`tatoeba:id` / `gen:v1`) ve `rev` alanı.

## 5. Son liste (öncelik sırası)
1. **[S] Motor zarar yaması + `’` normalizasyonu** — 964-1087 — kabul (Pedagoji).
2. **[S] Ortak fark bileşeni; Çevir/Yaz kartı** — `buildCheckCard` 1655 — birleşik. Temiz sonuç metni: **"Bilinen bir tuzak görmedim — örnekle karşılaştır."** Çevir'deki fark etiketi: **"Örnekten farklı"**.
3. **[S] Ürün + Görsel S paketi** — ilerleme çubuğu (1296, 1512), tamam ekranında günlük sayaç ve bugünün kelimeleri, alt sekme **"Prova"** (333), `aria-pressed`, klavye, kontrast — birleşik. Kart kalmadığında: **"Bugünlük kart kalmadı — yarın görüşürüz 👋"** (🎉 yok).
4. **[M] Etkinlik günlüğü `ing:log`** — kabul (benim).
5. **[L] Benim cevaplarım (STAR + çerçeve)** — Mülakat › Hazırlık — birleşik. Etiket: **"Senin metnin · bilinen tuzak yok"**. Boş durum: **"Henüz cevabın yok — ilk soruyla başlayalım, 3 dakika sürer."**
6. **[M] Bugün planı** — Öğren sekmesinin başı — kabul. Başlık: **"Bugün · 3 adım"**. Adımlar: **"Kelimeler — 18 kart, ~5 dk"**, **"Cümle kur — 3 cümle"**, **"Mülakat — 1 soru, sesli"**. Bitişte "Bugünlük tamam!"
7. **[M] Üretimi öne çek** — `renderStudy` 1331 — kabul. 2. görüş ipucu: **"Az önce gördün — şimdi İngilizcesini sen hatırla."**
8. **[L] Prova: Hızlı (3) / Tam (8) + rapor kartı** — `sendMock` 2063 — değiştirildi (kalıp kapsaması yok). Rapor başlığı: **"Provan bitti — işte notların"**.
9. **[M] Dürüst hazırlık yüzdesi** — 2150 — değiştirildi. Kilometre taşları: **"İlk cevabın hazır"**, **"3 soruya cevabın hazır"**, **"Kısa provayı bitirdin"**, **"Tam provayı bitirdin"**.
10. **[M] Dönüş karşılaması + .ics hatırlatma** — yeni. Metin: **"Tekrar hoş geldin! 34 kart seni bekliyor (~8 dk)."** Düğmeler: **"15 kartla başla"** / **"Hepsini yap"**. Hatırlatma düğmesi: **"Takvimime ekle"**.
11. **[M] 2 dakikalık seviye yoklaması** (ilk seanstan sonra) — değiştirildi (Pedagoji). Metin: **"Bildiğin kelimeleri atlayalım mı? 2 dakika."**
12. **[XL] Ünite müfredatı + kademeli kelime genişlemesi (önce +250)** — protokolden sonra — ortak, değiştirildi.

## 6. Reddedilenler
- **Mülakat sahnesi:** öğrenme kanıtı zayıf, kitsch riski var, değer rapor kartında.
- **Aydınlık tema (şimdi):** öğrenmeye etkisi yok, pazarlama aşamasına ertelendi.
- **Tek seferde 1000 kelime:** doğrulanmamış protokolün hatasını katlar.
- **Onboarding'de 10 dk seviye testi:** ilk değerin gelmesini geciktirir.
- **Kişisel hata profili (şimdi):** bozuk motorla yanlış teşhis koyar.
- **Provada kalıp kapsaması puanı:** alt dize eşleşmesi papağanlığı ödüllendirir.
- **Takip sorusu için Workers AI:** yanlış İngilizce riski, deterministik takip yeterli.

---

## Tur 2 — gorsel

# Görsel — Tur 2: çapraz eleştiri ve uzlaşma

## 1. Diğer raporlara cevaplar

**Pedagoji**
- **Motor zarar verme yaması + `’` normalizasyonu: KABUL, 1 numara.** 22/40 bozulma ölçülmüş. Bu hata gizlenecek bir şey değil, motorun yanlış öğrettiği bir şey. Hiçbir görsel iş bundan önce gelmez.
- **Kesinlik katmanı (high/low): KABUL.** Görsel karşılığını ben öneriyorum. **high** kuralda ins/del ile metin yeniden yazılır. **low** kuralda metin değişmez; kelimenin altında kesik amber çizgi ve bir çip çıkar. Çip metni: **"Emin değilim — buna bir bak"**. low ipucu asla yeşil ✅ göstermez.
- **Çevir/Yaz kartı ile benim ins/del önerim: aynı iş, BİRLEŞTİR.**
  - Tek bir `diffWords(a,b)` fonksiyonu üç yerde kullanılır: Çevir'de öğrenci–örnek, Yaz'da girdi–`fixed` (yalnız high kurallar), Mock'ta girdi–`fixed`.
  - Hiyerarşi şöyle: örnek ya da düzeltilmiş hâl üstte ve büyük; öğrencinin cümlesi altta, küçük ve nötr.
  - Düzeltme rengi amber olur. Nane yalnız gerçek başarıda kullanılır.
  - Dinle düğmesi düzeltilmemiş cümleyi hiç okumaz.
  - Başlık: **"Tuzak bulunamadı — örnekle karşılaştır"** (Pedagoji metni, aynen).
- **STAR sihirbazı ile Ürün'ün "Benim cevaplarım": aynı şey, BİRLEŞTİR.**
  - Pedagojinin 4 adımı (Ne oldu / Görevin / Ne yaptın / Sonuç) ve Ürün'ün kapalı seçenek listeleri tek kurucuda birleşir. Depo: `ing:answers`.
  - Görsel taraf: üstte 4 noktalı adım göstergesi. Cümle çerçevesi sabit metin; doldurulan yuvalar çip olarak görünür. Serbest metin girilen yuvada **"senin metnin — kontrol edilmedi"** rozeti çıkar.
- **Gölgeleme ölçümü ile benim "mikrofon sonucunu görselleştir" önerim: aynı, BİRLEŞTİR.** Çerçeve Pedagojinin: "anlaşılırlık", puan yok.
- **Minimal çiftler + HVPT: DEĞİŞTİR.** iOS'ta varsayılan kurulu en-US ses sayısı az. Şüphe: cihazda `getVoices()` sayılmadı. Ses ≥3 değilse "çok konuşmacı" iddiası düşer, tek sesle algı alıştırması olarak kalır. Önce cihazda ses sayısı ölçülmeli.
- **Ünite müfredatı (XL), 1000 kelime (XL): DEĞİŞTİR (sıra).** İkisi de önce motor yamasına ve içerik protokolüne bağlı.
  - Boyut ölçtüm: WORDS kelime başına 152 bayt. 1000 kelime × 3 örnek ≈ 330KB ham, ~100KB gzip. Tek dosyada kalabilir, performans engeli yok.
- **3 örnek cümle, merdiveni öne çekme, seviye tespiti: KABUL.** Bunlar benim alanım dışında. Görsel itirazım yok.

**Ürün**
- **İlerleme çubuğu donuyor: KABUL.** Benim ölçümüm de bunu tamamlıyor: çubuğun yolu zemine karşı 1.27, yani çubuk boşken görünmüyor. Düzeltme şu iki şey birlikte: ilerleme sayımı (Ürün) + yolun rengi `--bg4`'e alınır.
- **Bugün planı: DEĞİŞTİR.** Yeni sekme değil, Öğren'in başında 3 satırlık bir kontrol listesi kartı. Kart tamamlanınca daralır. Simge seti hazır değilse ilk sürüm metinle çıkar, seti beklemez.
- **Dürüst hazırlık yüzdesi: KABUL.** Tek çubuk yerine 4 ince bileşen çubuğu (kelime / soru / prova / kulak). Kilometre taşları eyleme bağlanır.
- **Prova + rapor kartı: KABUL.** Sayısal not yok. Soru başına bir satır: tuzaklar, eksik kalıp, önceki denemeye göre ↑/↓.
- **Etkinlik günlüğü + ısı haritası: KABUL.** 8×7 ızgara, tek renk tonu (amber yoğunluğu). Kırmızı ve "boş gün" cezası yok.
- **Kalıplar dilimleme: KABUL.** Kendi ölçümüm de bunu destekliyor: 56 kez tekrarlanan "Gölge tekniği" düğmesi görsel gürültü yapıyor.
- **Dönüş karşılaması, hata profili: KABUL.** Hata profili ancak motor yamasından sonra gelmeli. Rozet metni Ürün'ünki: "bilinen tuzak görülmedi".
- **Ünite haritası SVG: DEĞİŞTİR.** İlk sürümde liste olsun. Yol çizimi doğrusal ilerleme algısı yaratır, Ürün de bu riski kendisi yazmış. Harita en sona kalır.
- **a11y paketi: BİRLEŞTİR.** Ürün'ün 38–41 px ölçümü benim "44 px önceki turda yapıldı" sözümü düzeltiyor. Benim S paketimle tek iş olur: `aria-pressed`, `role=progressbar`, Space ve 1/2/3 kısayolları, 44 px, "Mülakat" alt sekmesinin adı "Prova".

## 2. Geri çektiklerim / değiştirdiklerim
- **Mülakat sahnesi (L): ERTELE.** Öğrenmeye etkisinin kanıtı zayıf. Diğer iki uzman bunu hedefe hizmet eden iş olarak görmüyor. Önce prova ve rapor kartı gelir; sahne en fazla onun görsel çerçevesi olur.
- **Hareket sistemi: L'den M'ye.** Yalnız kart geçişi, onay işareti çizimi ve sıfır kartta kutlama olmaması kalıyor.
- **Token sistemi + aydınlık tema: BÖL.**
  - **Token + bileşen sınıfları önce (M):** düğme varyantları, aralık ve yazı ölçeği. Gerekçe: Bugün, Cevaplarım ve rapor kartı yeni ekran getirecek. Bunlar bugünkü 60 satır içi stil düzeninde yazılırsa borç katlanır.
  - **Aydınlık tema sonra (M).** Önceliği düşük.
- **ins/del ayrı bir madde olmaktan çıktı,** Pedagojinin Çevir/Yaz kartına birleşti.
- **Self-host font:** M olarak kalıyor, sırası geriye kaydı.

## 3. Sıralama
Hedef mülakat İngilizcesi, seviye A1-A2. Bu hedefe en çok hizmet eden büyük bahis **Benim cevaplarım**. Bağımlılık zinciri:

1. Motor yaması + `fp.js` regresyonu.
2. Fark kartı (kesinlik katmanının görseli).
3. Mini token/bileşen geçişi.
4. Benim cevaplarım. Çerçeveleri doğrulanmış motor ve protokolle sınanır.
5. Prova + rapor kartı. Cevapları besin olarak kullanır.
6. Bugün planı + günlük. Bunlar 4 ve 5'i günlük döngüye sokar.
7. Ünite ve 1000 kelime. Bunlar protokol ister.

Görsel büyük bahisler (ikon seti, tema, sahne) hedefe dolaylı hizmet ediyor. Bu yüzden 3. adım dışında hepsi en sona kalıyor.

## 4. İçerik doğrulama protokolü
- **Lint + kör ikinci model + kullanıcı örneklemi: KABUL.** Lint'e iki görsel kontrol eklensin:
  - Örnek cümle ≤10 kelime olsun ki kartta tek satır kalsın.
  - Emoji ya da biçim karakteri veriye girmesin (bugün 🧭 ×10 veride duruyor).
- **Lisans (şüphe; hukukçu değilim):**
  - **NGSL/BSL CC BY-SA:** listeyi yalnız seçim ve lint süzgeci olarak kullanın, dosyaya kopyalamayın. Uygulamaya giden kelime girdileri (çeviri, örnek, tür) bizim yazımımız olur. Böylece SA yükümlülüğünün içeriğe bulaşma riski azalır.
  - **Tatoeba CC BY 2.0 FR:** SA değil, ticari kullanım serbest, cümle başına atıf şart. Gerekenler: girdilerde `src:'tatoeba#id'` alanı ve İlerleme altında bir "Kaynaklar" ekranı.
  - **Daha temiz alternatif:** tüm örnekleri kendimiz üretip lint + kör inceleme + kullanıcı örneklemi uygulamak. Lisans yükü sıfır olur, kalite bekçisi yine protokolün kendisi kalır.

## 5. Son liste (öncelik sırasıyla, en fazla 12)
1. **[S] Motor yaması + `’` normalizasyonu** — Pedagoji 964-1087, `checkWriting` 1646. Durum: kabul.
2. **[M] Fark kartı** — `buildCheckCard` 1655, Çevir, Mock. Ortak `diffWords`, amber düzeltme, low için çip. Durum: birleştirildi. Metinler: "Tuzak bulunamadı — örnekle karşılaştır" / "Emin değilim — buna bir bak".
3. **[S] Görsel hata paketi.** Durum: kabul (kendi turum).
   - `.v.acc` sınıf çakışması (158, 2159).
   - Diyalog regex'i (1622).
   - `color-scheme: dark`.
   - Rate ve `.tag` kontrastı.
   - İlerleme çubuğunun yolu (`--bg4`).
   - 🐢 düğmelerine `aria-label`; 🇹🇷 kaldırılır.
4. **[S] a11y + IA paketi** — 44 px, `aria-pressed`, `role=progressbar`, klavye kısayolları, "Prova" adı. Durum: birleştirildi.
5. **[M] Mini token + bileşen sınıfları** — `:root`, `.ai-btn` satır içi 8 varyant, `.qa`/`.acc` birleşmesi. Durum: değiştirildi.
6. **[L] Benim cevaplarım (STAR)** — Mülakat sekmesi, `ing:answers`. Görseli 4 adım + çip yuvalar. Durum: birleştirildi.
7. **[M] Prova rapor kartı** — `advanceMock` 2053. Durum: kabul.
8. **[M] Bugün kartı + dürüst 4 bileşenli hazırlık** — `renderStudy` başı, `renderProgress` 2150. Durum: değiştirildi.
9. **[M] TTS cümle bölme + okunan cümleyi vurgulama** — `buildReadCard` 1612. Durum: kabul (kendi turum).
10. **[M] Bitiş ekranı.** 0 kartta 🎉 yok. Durum: yeni. Metin: "Başlamaya hazırsın — ilk 6 kelime seni bekliyor". Gerçek iş yapıldıysa "Bugünlük tamam!" ve onay işareti çizilir.
11. **[L] SVG ikon seti** — 155 emojiden işlevsel olanlar ikona geçer; 🔥/🧊 kalır. Durum: kabul (sırası geriye kaydı).
12. **[M] Self-host + alt küme font (176KB'den ~63KB'ye), PWA simgesi (maskable)** — `sw.js`, manifest. Durum: kabul.

## 6. Reddedilenler
- **Mülakat sahnesi (şimdilik):** öğrenmeye etkisi kanıtlanmadı; prova ve cevap bankası daha doğrudan.
- **Ünite yol haritası SVG'si (ilk sürümde):** doğrusal yol algısı yaratır; liste yeterli.
- **Takip sorusu için Workers AI:** küçük model yanlış İngilizce riski taşıyor, çevrimdışı çekirdek de bölünür.
- **Telaffuz puanı veya dalga formu:** üç uzman aynı yerde. Tanıma sonucu telaffuz ölçümü değildir.
- **NGSL/BSL listesini uygulamaya kopyalamak:** SA yükümlülüğü riski taşır. Liste yalnız süzgeç olsun.

# İngilizce Koçu

Kanıta dayalı, tek sayfalık İngilizce öğrenme aracı. Türkçe konuşanlar için, iş görüşmesi odaklı.

## Ne yapar

- **Öğren** — aralıklı tekrar motoru. Kelime pekiştikçe alıştırma zorlaşır: klasik kart, dinle-anlamını-seç, Türkçeden hatırla, dikte, yazarak üret.
- **Cümle** — kelimeleri sıraya dizerek ve serbest çeviriyle cümle kurma.
- **Mülakat** — 10 soru + şablon ve örnek cevaplar, kulak eğitimi (soruyu sesten tanı), 4/3/2 akıcılık antrenmanı, AI sahte mülakat.
- **AI Koç** — seviyeye uygun metin üretimi, yazma düzeltmesi, hazır kalıplar ve gölge tekniği.
- **İlerleme** — mülakata hazırlık çubuğu, pekişmiş kelime sayısı, Türkçe konuşana özel hata rehberi.

## Kullanım

Telefonda tarayıcıda aç, **Ana Ekrana Ekle** de. Tam ekran çalışır, çevrimdışı da açılır, ilerleme cihazda saklanır.

## Notlar

- **Mikrofon** (4/3/2 yazıya dökme, sesli mülakat cevabı) `https` gerektirir ve Chrome/Edge'de güvenilir çalışır. iOS Safari'de konuşma tanıma kararsızdır — düğme görünmezse teknik mikrofonsuz da uygulanır.
- **AI özellikleri** Anthropic API anahtarı olmadan çalışmaz; anahtarsız kullanımda ilgili bölümler hata mesajı gösterir. Kelime motoru, kulak eğitimi, 4/3/2, kalıplar ve rehber tamamen çevrimdışı çalışır.
- İlerleme `localStorage`'da tutulur; tarayıcı verisini silmek ilerlemeyi de siler.
- Kendi kendini sınayan kontroller için adresin sonuna `#test` ekleyip konsola bak.

## Dosyalar

| Dosya | İş |
|---|---|
| `index.html` | Uygulamanın tamamı — tek dosya, bağımlılık yok |
| `manifest.json` | Ana ekrana ekleme ayarları |
| `sw.js` | Çevrimdışı önbellek (ağ önce, ağ yoksa önbellek) |
| `icon-*.png` | Uygulama ikonları |

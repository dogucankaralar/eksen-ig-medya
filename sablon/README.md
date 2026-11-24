# Koyu soru şablonu (reel)

Dosya: `soru-koyu-ornek.pdf` (sürüm 8, 24 Kasım 2026). Üretici betik: `uret.py`. 2 sayfa: orta soru kartı ve büyük soru kartı.
Bu ölçüler ve renkler sabittir. Yeni soru PDF'i hazırlarken bunları değiştirme.

## Ölçüler (pt, A4 595,28 × 841,89)
- Koyu sütun: x 181,49–413,78. Kenarlarda 1,4 pt turuncu çizgi.
- İç alan (soru kartı, ÇÖZÜM kutusu, başlık): x 207,63–387,63, genişlik 180. Sütunun tam ortasında.
- Üst satır: solda turuncu "EKSEN MATEMATİK" rozeti (78 pt). ZORLUK ve 5 daire, rozet ile sağ kenar arasındaki boşluğun ortasında. Ayrı küçük başlık yok.
- Çıkmış soruda kartın sağ alt köşesinde gri küçük etiket: "ÖSYM · 2019/TYT". Yıl kaynakta yazmıyorsa etiket konmaz.
- Şıklar tek satıra sığarsa tek satırda durur. Sığmazsa 2 veya 3 sütun olur; alt satırda kalan şıklar ortalanır. Şıklar asla sola yaslı yarım satır kalmaz.
- Soru metni Inter 6,3 pt, kök cümlesi kalın, şık harfleri turuncu. Şekil kaynaktaki ipucu boyamaları olmadan yeniden çizilir.
- Soru kartı üstü: y 68. Kartın yüksekliği soru metnine göre değişir. Turuncu gölge 2 pt sağ-alt.
- Altyazı alanı: soru kartı ile ÇÖZÜM kutusu arasında 18 pt boş şerit (gölge dahil 16 pt temiz alan, 1080 px videoda yaklaşık 75 px). Bu şeride hiçbir şey konmaz.
- ÇÖZÜM etiketi kutunun içinde sol üst köşede. Kutu y 317,4'te biter; en az 140 pt yükseklikte kalır.
- Çözüm metni sütunun solundaki beyaz alanda, cevap sağdaki beyaz alanda (kırpma alanının dışında).

## Renkler (Eksen lacivert ailesi)
| Ad | Renk | Kullanım |
|---|---|---|
| Zemin | #0B1B32 | Koyu sütun |
| Izgara | #132846 | Sütun ızgara çizgisi (0,35 pt, 6,98 pt aralık) |
| Kutu | #112440 | ÇÖZÜM kutusu zemini |
| Çizgi | #203E68 | ÇÖZÜM kutusu kenarı |
| Yumuşak metin | #A6B8D2 | ZORLUK, ÇÖZÜM etiketleri, zorluk daireleri |
| Turuncu | #F28C28 | Kenar çizgisi, gölge, EKSEN MATEMATİK, SORU rozeti, şık harfleri |
| Lacivert metin | #0E2442 | Soru kartındaki metin, SORU rozetindeki yazı (#0B1B32) |
| Beyaz | #FFFFFF | Soru kartı |

Yazı tipleri: başlık ve etiketler JetBrains Mono Bold, SORU rozeti Archivo Black, soru metni Inter.
Eski sürümlerdeki #1E2430 (gri-mavi) ve #34353E (gri) artık kullanılmaz.

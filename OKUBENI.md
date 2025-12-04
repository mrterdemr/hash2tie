# Hash2TIE

## Açıklama
**Hash2TIE**, `.txt` dosyasındaki MD5/SHA-1/SHA-256 hash’lerini **Trellix TIE** uyumlu **FileReputation** XML bloklarına dönüştürür.  
Doğru etiketi sizin için seçer ve `ReputationLevel=1` ekler böylece yüzlerce hash değerini tek seferde TIE'a girebilirsiniz.

- Çıktı dosyasının başına `<TIEReputations>` ve sonuna `</TIEReputations>` ekleyip xml olarak kaydedin.
- XML dosyasını Trellix ePO → TIE Reputations → File Overrides kısmına import edin.
- Import edilen hashler File Overrides sayfasında "File Name" içermediğinden listelenmeyebilir.
- Girdilerinizi görüntüleyebilmek için filtre ayarı yaparak "File Name" değerini "Value is blank" olarak belirleyin.

## Gereksinimler
- Python 3.8+
- Her satırda tek bir hash (yalnızca hexadecimal: `0-9a-fA-F`), uzunluk:
  - MD5 → 32 karakter
  - SHA-1 → 40 karakter
  - SHA-256 → 64 karakter

## Kurulum
Dosyaları aynı klasöre koyun:
```
hash2tie.py
hashes.txt
```

## Kullanım
Varsayılan çıktı:
```bash
python hash2tie.py hashes.txt
```
XML çıktı:
```bash
python hash2tie.py hashes.txt -o reputations.xml
```

## Örnek
**Girdi (`hashes.txt`):**
```
d41d8cd98f00b204e9800998ecf8427e
da39a3ee5e6b4b0d3255bfef95601890afd80709
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

**Çıktı (`file_reputations.txt`):**
```xml
<FileReputation>
  <MD5Hash>d41d8cd98f00b204e9800998ecf8427e</MD5Hash>
  <ReputationLevel>1</ReputationLevel>
</FileReputation>
<FileReputation>
  <SHA1Hash>da39a3ee5e6b4b0d3255bfef95601890afd80709</SHA1Hash>
  <ReputationLevel>1</ReputationLevel>
</FileReputation>
<FileReputation>
  <SHA256Hash>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</SHA256Hash>
  <ReputationLevel>1</ReputationLevel>
</FileReputation>
```

## Sorun Giderme
- Dosya bulunamadı → Yol ve ismi kontrol edin.  
- Çıktı yok → Tüm satırlar geçersiz; hash formatını kontrol edin.
- XML formatı hatalı → Çıktı dosyasının başına `<TIEReputations>` ve sonuna `</TIEReputations>` ekleyip xml kaydedin.

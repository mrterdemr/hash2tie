# Hash2TIE

## 📌 Description (EN)
**Hash2TIE** converts a list of MD5/SHA-1/SHA-256 hashes from a `.txt` file into **Trellix TIE** compatible **FileReputation** XML blocks.  
Automatically detects the correct tag and sets `ReputationLevel=1`. Invalid lines are skipped and reported.

## 📌 Açıklama (TR)
**Hash2TIE**, `.txt` dosyasındaki MD5/SHA-1/SHA-256 hash’lerini **Trellix TIE** uyumlu **FileReputation** XML bloklarına dönüştürür.  
Doğru etiketi otomatik seçer ve `ReputationLevel=1` ekler. Geçersiz satırlar atlanır ve bildirilir.

---

## 🔹 1) Prerequisites (EN)
- Python 3.8+
- One hash per line (hexadecimal only: `0-9a-fA-F`), lengths:
  - MD5 → 32 chars
  - SHA-1 → 40 chars
  - SHA-256 → 64 chars

## 🔹 1) Önkoşullar (TR)
- Python 3.8+
- Her satırda tek bir hash (yalnızca hexadecimal: `0-9a-fA-F`), uzunluk:
  - MD5 → 32 karakter
  - SHA-1 → 40 karakter
  - SHA-256 → 64 karakter

---

## 🔹 2) Setup (EN)
Place files in the same folder:
```
hash2tie.py
hashes.txt
```

## 🔹 2) Kurulum (TR)
Dosyaları aynı klasöre koyun:
```
hash2tie.py
hashes.txt
```

---

## 🔹 3) Usage (EN)
Default output:
```bash
python3 hash2tie.py hashes.txt
```
Custom output:
```bash
python3 hash2tie.py hashes.txt -o my_reputations.xml
```

## 🔹 3) Kullanım (TR)
Varsayılan çıktı:
```bash
python3 hash2tie.py hashes.txt
```
Özel çıktı:
```bash
python3 hash2tie.py hashes.txt -o benim_ciktim.xml
```

---

## 🔹 4) Example (EN)
**Input (`hashes.txt`):**
```
d41d8cd98f00b204e9800998ecf8427e
da39a3ee5e6b4b0d3255bfef95601890afd80709
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

**Output (`file_reputations.txt`):**
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

## 🔹 4) Örnek (TR)
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

---

## 🔹 5) Troubleshooting (EN)
- File not found → Check path and name.  
- No output → All lines invalid; check hash format.  

## 🔹 5) Sorun Giderme (TR)
- Dosya bulunamadı → Yol ve ismi kontrol edin.  
- Çıktı yok → Tüm satırlar geçersiz; hash formatını kontrol edin.  

# Hash2TIE

## Description
**Hash2TIE** converts MD5/SHA-1/SHA-256 hashes in a `.txt` file into **FileReputation** XML blocks compatible with **Trellix TIE**.  
It selects the correct tag for you and adds `ReputationLevel=1`, so you can enter hundreds of hash values into TIE in one go.

- Add `<TIEReputations>` to the beginning of the output file and `</TIEReputations>` to the end, then save it as XML.
- Import the XML file into Trellix ePO → TIE Reputations → File Overrides.
- The imported hashes may not be listed on the File Overrides page because they don’t include a "File Name".
- To view your entries, adjust the filter and set the "File Name" value to "Value is blank".

## Requirements
- Python 3.8+
- A single hash per line (hexadecimal only: `0-9a-fA-F`), lengths:
  - MD5 → 32 characters
  - SHA-1 → 40 characters
  - SHA-256 → 64 characters

## Setup
Put the files in the same folder:
```
hash2tie.py
hashes.txt
```

## Usage
Default output:
```bash
python hash2tie.py hashes.txt
```
XML output:
```bash
python hash2tie.py hashes.txt -o reputations.xml
```

## Example
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

## Troubleshooting
- File not found → Check the path and file name.  
- No output → All lines are invalid; check the hash format.
- Invalid XML format → Add `<TIEReputations>` at the beginning and `</TIEReputations>` at the end of the output file and save it as XML.

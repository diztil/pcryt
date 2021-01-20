# Pcryt
Pcryt is a Python-based encryption program.

### About Pcryt
At the moment, Pcryt is highly simplified and minimalistic.

### Running Pcryt
Use the following command in the command line interface. Replace the "MESSAGE" with the text you want to encrypt, and the TAPPOSITION can be a number between 0-5
```python
python lfsr.py MESSAGE TAPPOSITION
```
Use the following command to initiate "mass decrypting" mode.
```python
python lfsr.py attemptall 5
```

### Copyright Notice
Pcryt is open source. That means anyone is free to download, modify, sell, use, etc. any part of this program. It is a kind note to please credit the author(s) of the modules if you can.

### Version Updates
* __v0.1.0 'Cronos'__ (obsolete)
  * [x] encryption with LFSR
  * [x] decryption with LFSR
  * [ ] mass decryption
  * [ ] CUI
* __v0.1.1 'Cronos II'__ (current)
  * [x] encryption with LFSR
  * [x] decryption with LFSR
  * [x] mass decryption
  * [x] CUI
  * [x] Base64 encoding
  * [ ] ASCII encoding
  * [ ] unlimited 'tap position' range

> The features without the tick marks will be added soon, in the next version.

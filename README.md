# Pcryt
Pcryt is a Python-based encryption program.

![Pcryt logo](https://github.com/dmimukto/pcryt/blob/main/pcrytlogo.png)

### About Pcryt
At the moment, Pcryt is highly simplified and minimalistic.

### Running Pcryt
###### For v0.1.2
1. Command Line Method
* Single Message Encryption/Decryption *
Use the following command in the command line interface. Replace the "MESSAGE" with the text you want to encrypt, replace "SEED" with a binary value, e.g. 110010, and the "TAPPOSITION" can be a number less than the maximum number of digits in the SEED you enter.
```python
python lfsr.py MESSAGE SEED TAPPOSITION
```
Use the following command to initiate "mass decrypting" mode.
```python
python lfsr.py _attemptall_ SEED
```
* Text File Encryption/Decryption *
Use the following command in the command line interface.
 ```python
 python lfsr_auto.py SEED TAPPOSITION
 ```
 2. Instruction Prompt (Batch File) Method
 * Single Message Encryption/Decryption *
 Launch the "pcryt_launcher.bat" file. Instructions are presented step-by-step.
 * Text File Encryption *
 Launch the "pcryt_encrypt.bat" file. Nothing else to do. It uses a default seed and tapposition automatically.

###### For earlier versions
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
* __v0.1.1 'Cronos II'__ (previous)
  * [x] encryption with LFSR
  * [x] decryption with LFSR
  * [x] mass decryption
  * [x] CUI
  * [x] Base64 encoding
  * [ ] ASCII encoding
  * [ ] unlimited 'tap position' range (limited to 5 for this version)
  * [ ] text file encryption
* __v0.1.2 'Caesar'__ (current)
  * [x] encryption with LFSR
  * [x] decryption with LFSR
  * [x] mass decryption
  * [x] CUI
  * [x] Base64 encoding
  * [ ] ASCII encoding (still needs adjustments)
  * [x] unlimited 'tap position' range
  * [x] text file encryption
  * [x] automated batch files
  * [ ] non-developer-friendly GUI

> The features without the tick marks will be added soon, in the next version.

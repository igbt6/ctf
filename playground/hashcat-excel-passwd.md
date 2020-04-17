## Crack excell sheet password with help of HASHCAT

### Hashcat usage
```sh
$ ./hashcat64.exe -a 3 -w 3 -m 9500 hashExcel.lst -i --increment-min=4 --increment-max=8 -1 ?l ?1?1?1?1?1?1?1?1
cudaHashcat64.exe -a 0 -m 9400 --username -o found.txt hash.txt pass.txt
$ ./hashcat64.exe -a 0 -m 9500 --username -o cracked.txt hashExcel.lst rockyou.txt
$ ./hashcat64.exe -a 3 -w 3 -m 9500 hashExcel.lst -o cracked.txt rockyou.txt 

$ ./hashcat64.exe -a 0 -m 9500 -o cracked.txt --username hashExcel.lst rockyou.txt 
```


### Resources
https://www.blackhillsinfosec.com/crack-passwords-password-protected-ms-office-documents
http://pentestcorner.com/cracking-microsoft-office-97-03-2007-2010-2013-password-hashes-with-hashcat/
http://stuffjasondoes.com/2018/07/18/cracking-microsoft-office-document-passwords-for-free-using-hashcat/
https://hashcat.net/wiki/doku.php?id=example_hashes
https://hashcat.net/forum/thread-6678.html

### office2john.py example
```py
python office2john.py YOUR_EXCELL_SHEET.xlsx >  hash.txt
./hashcat64.exe -a 0 -m 9500 -o cracked.txt --username hash.txt rockyou.txt 
```

# hertz 2

__PROBLEM__

 This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with `nc 2018shell.picoctf.com 23479`.

__HINT__

These kinds of problems are solved with a frequency that merits some analysis.

__SOLUTION__

Connecting to service we get:
```
Bpr mcusw xadvf tde lcjoq dnra bpr ghzy kdi. U shf'b xrgurnr bpuq uq qcsp hf rhqy oadxgrj uf Ousd. Ub'q hgjdqb hq ut U qdgnrk h oadxgrj hgarhky! Dwhy, tufr. Prar'q bpr tghi: ousdSBT{qcxqbubcbudf_suopraq_har_bdd_rhqy_ijfuxuabfn}
```

Our first step is to be identify what kind of cipher the message has been encoded.
To identify an unknown cipher there is this method called finding Index of coincidence(I.C). Read about I.C [here](http://practicalcryptography.com/cryptanalysis/text-characterisation/identifying-unknown-ciphers/).

Then I used online [I.C calculator](http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/).

We get I.C = `0.054185927067283` which tells us that it is a subsitution cipher.

Again I used that great [decoder](https://www.guballa.de/substitution-solver) and we get the flag.

FLAG - `picoCTF{substitution_ciphers_are_too_easy_gmnibirtnv}`

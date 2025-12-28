# Polyglot
Rewrite quotes in "alien" dialects

This project is spun off of an earlier one, "Babel" that generates alien language words based on a rule set. The words *resemble* Wookie, Klingon, Vulcan, Romulan and Mando'a language vocabulary from Star Wars and Star Trek. The words created might actually be words in those languages - but for this program they are created randomly.

A Carl Sagan quote (from the "sagan" file) is selected and printed, and each unique word is assigned one of the generated words, then the quote is displayed "translated" into the alien dialect. NOTE: this *absolutely* not a real translation, just a fun exercise in generating alien text.

FILES:

* polyglot.py - rename to code.py on the NeoTrinkey Set REPL=True for the output to go to the repl in Mu or Thonny. set to False and the output will be printed as if keyed in on the device the Neotrinkey is plugged into.
* prt.py - helper file to define prt(). 
* sagan - set of Carl Sagan quotes. Feel free to replace quotes with any words of wisdom you choose.

Touch pad #1 to select and translate the quote

Touch pad #2 to click through the language choices

OUTPUT:

```
Wookie
Klingon
Vulcan
We are the representatives of the cosmos; we are an example of what hydrogen atoms can do, given 15 billion years of cosmic evolution. Carl Sagan 

 h hi k t'ity kl k rak h hi nii taai kl lta ht kt te niuhl' naito r'k toat kl taahi w'itka niu kot
Mando'a
If you wish to make an apple pie from scratch, you must first invent the universe. Carl Sagan 

 te 'aa s olj 'eusa eela res oone crl 'e 'aa 'a' yirtt e'' stna elrh arss nthe
Romulan
Imagination will often carry us to worlds that never were. But without it we go nowherw. Carl Sagan

 ihmu eif vuu'i efn leelu ei'h na'dh 'isn uhn uuld ane hemf' enk' feiaf levk' hd viefe muehn

```


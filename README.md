# uru_dict  
ʊ ɹմɯ ɯ սմն dict  
dict of uru ejo  

---
## commands  
### sort  
`sort ([option]) : sort according to [option].`  
`[option] = [null] / mid / traditional : according to dictionary order of traditional uru ejo.`  
`[option] = modern / mod / pronunciation / pr : according to dictionary order of pronunciation.`  
`[option] = explanation / exp / expl : according to dictionary order of explanation.`  
### list / display / show  
`list ([category]) : list words out according to [category].`  
`[category] = [null] / all : all words in dictionary.`  
### find / query  
`find [word] ([option]) : look words up in dictionary according to [option].`  
`[option] = [null] : words exactly the same as [word].`  
`[option] = include / included / inclusive / in : words having [word] as substrings.`  
### findpr / findpronunciation / querypr / querypronunciation  
`find [pronunciation] ([option]) : look up words pronounced as [pronunciation] in dictionary according to [option].`  
`[option] = [null] : words exactly pronounced as [pronunciation].`  
`[option] = include / included / inclusive / in : words having [pronunciation] as substrings of its pronunciation.`  
### findexp / findexpl / findexplanation / queryexp / queryexpl / queryexplanation  
`find [explanation] ([option]) : look up words meaning [explanation] in dictionary according to [option].`  
`[option] = [null] : words exactly meaning [explanation].`  
`[option] = include / included / inclusive / in : words having [explanation] as substrings of its explanation.`  
### insert / add  
`insert [word] [part_of_speech] [explanation] : insert [word] into dictionary with part of speech as [part_of_speech], explanation as [explanation], and auto-generated pronunciation.`  
`insert [word] [part_of_speech] [explanation] {readas / as} [pronunciation]: insert [word] into dictionary with part of speech as [part_of_speech], explanation as [explanation], and [pronunciation] as pronunciation.`  
`insert [pronunciation] [part_of_speech] [explanation] {from ({pr / pronunciation}) / frompr} : insert auto-generated word into dictionary with part of speech as [part_of_speech], explanation as [explanation], and [pronunciation] as pronunciation.`  
`check required.`
### del / delete / remove  
`del [word] : delete words the same as [word] from dictionary.`  
`del [pronunciation] {from (pr / pronunciation) / frompr}: delete words pronounced as [pronunciation] from dictionary.`  
### clear / delall / deleteall / removeall  
`clear : remove all the words from dictionary.`  
### load / reload  
`load : reload dictionary from "dict.txt".`
### save  
`save : save current dictionary into "dict.txt".`  
### back / backup / bkup  
`back : copy "dict.txt" into "dict_backup.txt".`  
### re / recover / recvr / rcvr / recov  
`re : copy "dict_backup.txt" into "dict.txt" and reload dictionary.`  
### fuck / fuckyou  
`fuck ([words_after_fuck]) : print "ah, fuck you man.".`  

---
## 楽しく使いましょうね～  

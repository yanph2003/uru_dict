# -*- coding: UTF-8 -*-
import functools
import os

dict_file = open(file="dict.txt",mode="r",encoding="utf-8")
dict = dict_file.read()
if len(dict) and dict[-1] == "\n" : dict = dict[:-1]
dict = dict.split("\n")
dict_file.close()
dict = [word.split(" ") for word in dict]
dict = [word[:-1] if word[-1] == "" else word for word in dict]
if dict == [[]] : dict = []

def uru_to_num(x) :
	if x == "'" : return 0
	elif x == "ʊ" : return 1
	elif x == "ս" : return 2
	elif x == "ɥ" : return 3
	elif x == "մ" : return 4
	elif x == "տ" : return 5
	elif x == "փ" : return 6
	elif x == "ɹ" : return 7
	elif x == "ɺ" : return 8
	elif x == "ṙ" : return 9
	elif x == "ɼ" : return 10
	elif x == "ɯ" : return 11
	elif x == "ɰ" : return 12
	elif x == "ն" : return 13
	elif x == "ɑ" : return 14
	elif x == "ռ" : return 15
	elif x == "ϵ" : return 16
	elif x == "ı" : return 17
	elif ord("a") <= ord(x) and ord(x) <= ord("z") : return 18+ord(x)-ord("a")
	elif ord("0") <= ord(x) and ord(x) <= ord("9") : return 44+ord(x)-ord("0")
	else : return -1

def str_cmp(x,y):
	lx,ly = len(x),len(y)
	leng = min(lx,ly)
	for i in range(leng):
		if(uru_to_num(x[i]) > uru_to_num(y[i])) : return 1
		elif(uru_to_num(x[i]) < uru_to_num(y[i])) : return -1
		else : continue
	if lx > ly : return 1
	elif ly > lx : return -1
	else : return 0

def dict_cmp_mid(x,y):
	return str_cmp(x[0],y[0])

def dict_cmp_modern(x,y):
	if x[1] < y[1] : return -1
	elif x[1] > y[1] : return 1
	else : return 0

def dict_cmp_explanation(x,y):
	if x[3] < y[3] : return -1
	elif x[3] > y[3] : return 1
	else : return 0

def generate_pronunciation(x):
	ret = ""
	for i in range(len(x))[::-1]:
		if x[i] == "'" :
			ret += "'"
		elif x[i] == "ʊ" :
			if len(ret) and ret[-1] == "'": 
				ret += "u"
			else:
				ret += "uru"
		elif x[i] == "ս" :
			ret += "ur"
		elif x[i] == "ɥ" :
			ret += "s"
		elif x[i] == "մ" :
			if len(ret) == 0 or ret[-1] == "'":
				if i == 0 or x[i-1] == "'":
					ret += "ud"
				else:
					ret += "j"
			elif len(ret) and (ord("A") <= ord(ret[-1]) and ord(ret[-1]) <= ord("Z")) or (ord("0") <= ord(ret[-1]) and ord(ret[-1]) <= ord("9")):
				if i == 0 or x[i-1] == "'" or (ord("a") <= ord(x[i-1]) and ord(x[i-1]) <= ord("z")) or (ord("0") <= ord(x[i-1]) and ord(x[i-1]) <= ord("9")):
					ret += "ud"
				else:
					ret += "j"
			elif len(ret) and ret[-1] in "aeiou":
				ret += "j"
			else:
				ret += "ud"
		elif x[i] == "տ" :
			ret += "an"
		elif x[i] == "փ" :
			ret += "n"
		elif x[i] == "ɹ" :
			ret += "e"
		elif x[i] == "ɺ" :
			ret += "v"
		elif x[i] == "ṙ" :
			ret += "er"
		elif x[i] == "ɼ" :
			ret += "k"
		elif x[i] == "ɯ" :
			ret += "o"
		elif x[i] == "ɰ" :
			ret += "y"
		elif x[i] == "ն" :
			if len(ret) == 0 or ret[-1] == "'":
				if i == 0 or x[i-1] == "'":
					ret += "edu"
				else:
					ret += "t"
			elif len(ret) and (ord("A") <= ord(ret[-1]) and ord(ret[-1]) <= ord("Z")) or (ord("0") <= ord(ret[-1]) and ord(ret[-1]) <= ord("9")):
				if i == 0 or x[i-1] == "'" or (ord("a") <= ord(x[i-1]) and ord(x[i-1]) <= ord("z")) or (ord("0") <= ord(x[i-1]) and ord(x[i-1]) <= ord("9")):
					ret += "edu"
				else:
					ret += "t"
			elif len(ret) and ret[-1] in "aeiou":
				ret += "t"
			else:
				ret += "ed"
		elif x[i] == "ɑ" :
			ret += "a"
		elif x[i] == "ռ" :
			ret += "en"
		elif x[i] == "ϵ" :
			ret += "E"
		elif x[i] == "ı" :
			ret += "!"
		elif ord("a") <= ord(x[i]) and ord(x[i]) <= ord("z") :
			ret += x[i].upper()
		elif ord("0") <= ord(x[i]) and ord(x[i]) <= ord("9") :
			ret += x[i]
		else :
			ret += "?"
	return ret[::-1]

def generate_word(x):
	ret = ""
	flag = ""
	for i in range(len(x)):
		if (ord("0") <= ord(x[i]) and ord(x[i]) <= ord("9")) or (ord("A") <= ord(x[i]) and ord(x[i]) <= ord("Z")) or x[i] == "'":
			if flag == "" or flag == "n":
				ret += x[i].lower()
			elif flag == "u" and x[i] == "'":
				ret += "ʊ'"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "!":
			if flag == "" or flag == "n":
				ret += "ı"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "^":
			if flag == "" or flag == "n":
				ret += "ϵ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "a":
			if "n" == flag:
				ret = ret[:-1] + "տ"
			elif "" == flag:
				ret += "ɑ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "d":
			if flag == "" or flag == "u":
				flag += "d"
			else:
				ret += "?"
		elif x[i] == "e":
			if "r" == flag:
				ret += "ṙ"
			elif "d" == flag or "ud" == flag:
				ret += "ն"
			elif "n" == flag:
				ret = ret[:-1] + "ռ"
			elif "" == flag:
				ret += "ɹ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "j":
			if flag == "":
				ret += "մ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "k":
			if flag == "":
				ret += "ɼ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "n":
			if flag == "":
				flag += "n"
				ret += "փ"
			else:
				ret += "?"
		elif x[i] == "o":
			if flag == "":
				ret += "ɯ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "r":
			if flag == "u" or flag == "":
				flag += "r"
			else:
				ret += "?"
		elif x[i] == "s":
			if flag == "":
				ret += "ɥ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "t":
			if flag == "":
				ret += "ն"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "u":
			if flag == "":
				flag += "u"
			elif flag == "ur":
				ret += "ʊ"
				flag = ""
			elif flag == "r":
				ret += "ս"
				flag = ""
			elif flag == "d":
				ret += "մ"
				flag = ""
		elif x[i] == "v":
			if flag == "":
				ret += "ɺ"
			else:
				ret += "?"
			flag = ""
		elif x[i] == "y":
			if flag == "":
				ret += "ɰ"
			else:
				ret += "?"
			flag = ""
		else:
			ret += "?"
	return ret

while 1:
	try :
		op = input().split()
		if len(op) == 0 : continue
		op[0] = op[0].lower()
		if op[0] == "exit" or op[0] == "end":
			break
		elif op[0] == "sort":
			if len(op) > 1:
				op[1] = op[1].lower()
			if len(op) == 1 or op[1] == "mid" or op[1] == "traditional":
				dict.sort(key=functools.cmp_to_key(dict_cmp_mid))
				print("dictionary sorted.")
			elif op[1] == "modern" or op[1] == "mod" or op[1] == "pronunciation" or op[1] == "pr":
				dict.sort(key=functools.cmp_to_key(dict_cmp_modern))
				print("dictionary sorted.")
			elif op[1] == "explanation" or op[1] == "exp" or op[1] == "expl":
				dict.sort(key=functools.cmp_to_key(dict_cmp_explanation))
				print("dictionary sorted.")
			else:
				dict.sort(key=functools.cmp_to_key(dict_cmp_mid))
				print("dictionary sorted(traditional).")
		elif op[0] == "save":
			dict_file = open(file="dict.txt",mode="w",encoding="utf-8")
			for i in range(len(dict)):
				for j in range(len(dict[0])):
					dict_file.write(dict[i][j])
					dict_file.write(" ")
				dict_file.write("\n")
			dict_file.close()
			print("dictionary saved.")
		elif op[0] == "display" or op[0] == "show" or op[0] == "list":
			if len(op) == 1 or op[1] == "all":
				if len(dict) == 0:
					print("no words listed.")
				else:
					for i in range(len(dict)):
						print(f"[{i+1}] : {dict[i][0]}({dict[i][1]}) - [{dict[i][2]}] {dict[i][3]}")
					print(f"{len(dict)} "+ ("word" if len(dict) == 1 else "words") + " listed.")
			else:
				print("unknown category.")
		elif op[0] == "find" or op[0] == "query":
			flag = False
			for i in range(len(dict)):
				if (op[1] in dict[i][0]) if (len(op) >= 3 and (op[2] == "inclusive" or op[2] == "included" or op[2] == "include" or op[2] == "in")) else (dict[i][0] == op[1]):
					flag = True
					print(f"{dict[i][0]}({dict[i][1]}) : [{dict[i][2]}] {dict[i][3]}")
			if not flag:
				print("no explanations found.")
		elif op[0] == "findpronunciation" or op[0] == "querypronunciation" or op[0] == "findpr" or op[0] == "querypr":
			flag = False
			for i in range(len(dict)):
				if (op[1] in dict[i][1]) if (len(op) >= 3 and (op[2] == "inclusive" or op[2] == "included" or op[2] == "include" or op[2] == "in")) else (dict[i][1] == op[1]):
					flag = True
					print(f"{dict[i][1]}({dict[i][0]}) : [{dict[i][2]}] {dict[i][3]}")
			if not flag:
				print("no explanations found.")
		elif op[0] == "findexp" or op[0] == "queryexp" or op[0] == "findexplanation" or op[0] == "queryexplanation" or op[0] == "findexpl" or op[0] == "queryexpl":
			flag = False
			for i in range(len(dict)):
				if (op[1] in dict[i][3]) if (len(op) >= 3 and (op[2] == "inclusive" or op[2] == "included" or op[2] == "include" or op[2] == "in")) else (dict[i][3] == op[1]):
					flag = True
					print(f"{dict[i][3]} [{dict[i][2]}]: {dict[i][0]}({dict[i][1]})")
			if not flag:
				print("no words found.")
		elif op[0] == "insert" or op[0] == "add":
			word = op[1]
			if len(op) >= 5:
				if op[4].lower() == "readas" or op[4].lower() == "as":
					pronunciation = op[5]
				elif op[4].lower() == "from" or op[4].lower() == "frompr" or op[4].lower() == "using" or op[4].lower() == "usingpr":
					pronunciation = op[1]
					word = generate_word(pronunciation)
					if "?" in word:
						print("invalid word.")
						continue
					for i in range(len(pronunciation)) : 
						if pronunciation[i] == "^" : 
							pronunciation[i] == "E"
				else:
					print("invalid command.")
					continue
			else:
				pronunciation = generate_pronunciation(op[1])
				if "?" in pronunciation:
					print("invalid word.")
					continue
			new_word = [word,pronunciation,op[2],op[3]]
			print("add:")
			print(f"word - {word}")
			print(f"pronunciation - {pronunciation}")
			print(f"explanation - [{op[2]}] {op[3]}")
			print("into dictionary? (Y/N) : ",end="")
			while 1:
				tmp = input().split()
				if tmp[0].lower() != "y" and tmp[0].lower() != "yes" and tmp[0].lower() != "n" and tmp[0].lower() != "no":
					print("invalid input. add it word into dictionary? (Y/N) : ",end="")
					continue
				elif tmp[0].lower() == "y" or tmp[0].lower() == "yes":
					dict.append(new_word)
					print("word added.")
					break
				else:
					print("operation canceled.")
					break
		elif op[0] == "del" or op[0] == "delete" or op[0] == "remove":
			if len(op) >= 3 and (op[2].lower() == "from" or op[2].lower() == "frompr" or op[2].lower() == "using" or op[2].lower() == "usingpr"):
				delword = op[1]
				deltmp = []
				cnt = 0
				for word in dict:
					if word[1] == delword:
						cnt += 1
						print(f"[{cnt}] : {word[0]}({word[1]}) - [{word[2]}] {word[3]}")
						deltmp.append(word)
			elif len(op) == 2:
				delword = op[1]
				deltmp = []
				cnt = 0
				for word in dict:
					if word[0] == delword:
						cnt += 1
						print(f"[{cnt}] : {word[0]}({word[1]}) - [{word[2]}] {word[3]}")
						deltmp.append(word)
			else:
				print("invalid command.")
				continue
			if cnt == 0:
				print("no words deleted.")
			else:
				try:
					print("select which to delete(LIST_TO_DEL/ALL/NONE) : ",end="")
					tmp = input()
					if tmp.lower() == "none" or tmp.lower() == "no":
						print("operation canceled. no words deleted.")
					elif tmp.lower() == "all":
						for word in deltmp : dict.remove(word)
						print(f"{cnt} "+ ("word" if cnt == 1 else "words") + " deleted.")
					else:
						tmp = tmp.split()
						tmp = [int(i) for i in tmp]
						for i in tmp:
							dict.remove(deltmp[i-1])
						print(f"{len(tmp)} "+ ("word" if len(tmp) == 1 else "words") + " deleted.")
				except Exception:
					print("invalid operation. no words deleted.")
		elif op[0] == "clear" or op[0] == "delall" or op[0] == "deleteall" or op[0] == "removeall":
			dict = []
			print("all words removed.")
		elif op[0] == "load" or op[0] == "reload":
			dict_file = open(file="dict.txt",mode="r",encoding="utf-8")
			dict = dict_file.read()
			if len(dict) and dict[-1] == "\n" : dict = dict[:-1]
			dict = dict.split("\n")
			dict_file.close()
			dict = [word.split(" ") for word in dict]
			dict = [word[:-1] if word[-1] == "" else word for word in dict]
			if dict == [[]] : dict = []
			print("dictionary reloaded from file.")
		elif op[0] == "backup" or op[0] == "back" or op[0] == "bkup":
			dict_file = open(file="dict.txt",mode="r",encoding="utf-8")
			dict_bkup_file = open(file="dict_backup.txt",mode="w",encoding="utf-8")
			dict_bkup_file.write(dict_file.read())
			dict_file.close()
			dict_bkup_file.close()
			print("dictionary backuped.")
		elif op[0] == "recover" or op[0] == "rcvr" or op[0] == "recvr" or op[0] == "recov" or op[0] == "re":
			dict_file = open(file="dict.txt",mode="w",encoding="utf-8")
			dict_bkup_file = open(file="dict_backup.txt",mode="r",encoding="utf-8")
			dict_file.write(dict_bkup_file.read())
			dict_file.close()
			dict_bkup_file.close()
			dict_file = open(file="dict.txt",mode="r",encoding="utf-8")
			dict = dict_file.read()
			if len(dict) and dict[-1] == "\n" : dict = dict[:-1]
			dict = dict.split("\n")
			dict_file.close()
			dict = [word.split(" ") for word in dict]
			dict = [word[:-1] if word[-1] == "" else word for word in dict]
			if dict == [[]] : dict = []
			print("dictionary recovered.")
		elif op[0] == "cls":
			os.system("cls")
		elif op[0] == "fuck" or op[0] == "fuckyou":
			print("ah, fuck you man.")
		else:
			print("unknown command!")
	except Exception as e :
		print("command error!")
		continue
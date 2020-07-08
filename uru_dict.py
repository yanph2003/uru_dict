# -*- coding: UTF-8 -*-
import functools

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
# def dict_cmp_modern(x,y)

def dict_cmp_modern(x,y):
	if x[1] < y[1] : return -1
	elif x[1] > y[1] : return 1
	else : return 0

def dict_cmp_explanation(x,y):
	if x[2] < y[2] : return -1
	elif x[2] > y[2] : return 1
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


while 1:
	try :
		op = input().split()
		op[0] = op[0].lower()
		if op[0] == "exit":
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
						print(f"[{i}] : {dict[i][0]}({dict[i][1]}) - {dict[i][2]}")
					print(f"{len(dict)} "+ ("word" if len(dict) == 1 else "words") + " listed.")
		elif op[0] == "find" or op[0] == "query":
			flag = False
			for i in range(len(dict)):
				if (op[1] in dict[i][0]) if (len(op) >= 3 and (op[2] == "inclusive" or op[2] == "included" or op[2] == "include" or op[2] == "in")) else (dict[i][0] == op[1]):
					flag = True
					print(f"{dict[i][0]}({dict[i][1]}) : {dict[i][2]}")
			if not flag:
				print("no explanations found.")
		elif op[0] == "findpronunciation" or op[0] == "querypronunciation" or op[0] == "findpr" or op[0] == "querypr":
			flag = False
			for i in range(len(dict)):
				if (op[1] in dict[i][1]) if (len(op) >= 3 and (op[2] == "inclusive" or op[2] == "included" or op[2] == "include" or op[2] == "in")) else (dict[i][1] == op[1]):
					flag = True
					print(f"{dict[i][1]}({dict[i][0]}) : {dict[i][2]}")
			if not flag:
				print("no explanations found.")
		elif op[0] == "findexp" or op[0] == "queryexp" or op[0] == "findexplanation" or op[0] == "queryexplanation" or op[0] == "findexpl" or op[0] == "queryexpl":
			flag = False
			for i in range(len(dict)):
				if (op[1] in dict[i][2]) if (len(op) >= 3 and (op[2] == "inclusive" or op[2] == "included" or op[2] == "include" or op[2] == "in")) else (dict[i][2] == op[1]):
					flag = True
					print(f"{dict[i][2]} : {dict[i][0]}({dict[i][1]})")
			if not flag:
				print("no words found.")
		elif op[0] == "insert" or op[0] == "add":
			if len(op) >= 4:
				if op[3].lower() == "readas" or op[3].lower() == "as":
					pronunciation = op[4]
			else:
				pronunciation = generate_pronunciation(op[1])
				if "?" in pronunciation:
					print("invalid word.")
					continue
			new_word = [op[1],pronunciation,op[2]]
			print("add:")
			print(f"word - {op[1]}")
			print(f"pronunciation - {pronunciation}")
			print(f"explanation - {op[2]}")
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
			deltmp = []
			cnt = 0
			for word in dict:
				if word[0] == op[1]:
					cnt += 1
					print(f"[{cnt}] : {word[0]}({word[1]}) - {word[2]}")
					deltmp.append(word)
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
		else:
			print("unknown command!")
	except Exception as e :
		print("command error!")
		continue
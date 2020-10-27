
# 1)Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
# dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
import os
import sys
from os import listdir, walk
from os.path import splitext, abspath, realpath, dirname, isfile, isdir, getsize


def get_extensions_rec(directory_name):
	try:
		files_ext = []
		[files_ext.append(splitext(f)[-1][1:]) for (root, directory, files) in os.walk(directory_name) for f in files if splitext(f)[-1][1:] not in files_ext and '' != splitext(f)[-1][1:]]
		files_ext.sort()
		print(files_ext)
	except FileNotFoundError:
		print("Directory Not Found")


def get_extensions_nerec(directory_name):
	try:
		files_ext = []
		[files_ext.append(splitext(f)[-1][1:]) for f in listdir(directory_name) if splitext(f)[-1][1:] not in files_ext and '' != splitext(f)[-1][1:]]
		files_ext.sort()
		print(files_ext)
	except FileNotFoundError:
		print("Directory Not Found")


# 2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută
# a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
# def write_absolute_path(directory, file):
def write_absolute_path_rec(directory_to_walk, file_to_write):
	try:
		abs_paths = [abspath(f) + "\n" for (root, directories, files) in walk(directory_to_walk) for f in files if f.startswith("A")]
		print(len(abs_paths))
		f = open(file_to_write, "w")
		f.writelines(abs_paths)
		f.close()
	except FileNotFoundError:
		print("Directory Not Found")


# 3)Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul
# de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
def file_or_directory(path):
	if isfile(path):
		fd = open(path, "r")
		print(fd.read()[-20:])
		fd.close()
	elif isdir(path):
		extensions = [splitext(f)[1][1:] for (root, directories, files) in walk(path) for f in files]
		extensions_count = [(ext, extensions.count(ext)) for ext in set(extensions)]
		extensions_count.sort(key = lambda x: x[1], reverse=True)
		print(extensions_count)


def unique_extensions():
	"""
	4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument
	la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
	Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista
	finală.
	"""
	try:
		dir_path = sys.argv[1]
		get_extensions_rec(dir_path)
	except:
		print("Please enter the file name")


def find_in_files(target, to_search):
	"""
	5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza
	 o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută
	 doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
	 Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj
	 corespunzator.
	"""
	if isfile(target):
		fd = open(target, 'r')
		file_content = fd.read()
		if to_search in file_content:
			print([target])
		fd.close()
	elif isdir(target):
		contains = []
		[contains.append(abspath(f)) for (root, directories, files) in walk(target) for f in files if f_contains_to_search(f, to_search) if abspath(f) not in contains]
		print(contains)
	else:
		raise ValueError("Valoare pentru target nu corespunde unui director sau fisier")


def f_contains_to_search(f, to_search):
	try:
		fd = open(f, "r")
		file_content = fd.read()
		return True if to_search in file_content else False
	except:
		pass


def find_in_files_2(target, to_search, callback):
	"""
	6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că
	primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută
	în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru
	"""
	if isfile(target):
		fd = open(target, 'r')
		file_content = fd.read()
		if to_search in file_content:
			print([target])
		fd.close()
	elif isdir(target):
		contains = []
		[contains.append(abspath(f)) for (root, directories, files) in walk(target) for f in files if f_contains_to_search(f, to_search) if abspath(f) not in contains]
		print(contains)
	else:
		callback(ValueError("Valoare pentru target nu corespunde unui director sau fisier"))


def file_prop(file_path):
	"""
	7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si
	returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea
	fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca
	se poate citi din/scrie in fisier.
	"""
	try:
		prop = {"full_path" : abspath(file_path), "file_size" : getsize(file_path), "file_extension": splitext(file_path)[1][-1], "can_read": os.access(file_path, os.R_OK), "can_write": os.access(file_path, os.W_OK)}
		print(prop)
	except FileNotFoundError:
		print("File not found")


def abs_paths(directory):
	"""
	Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un
	director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
	Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
	"""
	print([abspath(f) for f in listdir(directory) if isfile(f)])


if __name__ == "__main__":
	#EX1
	get_extensions_rec(dirname(realpath(__file__)))
	get_extensions_nerec(dirname(realpath(__file__)))
	#EX2
	write_absolute_path_rec(dirname(realpath(__file__)), "../absolute_path.txt")
	#EX3
	file_or_directory(dirname(realpath(__file__)))
	#EX4
	# unique_extensions()
	#EX5
	find_in_files("../absolute_path.txt", "a")
	find_in_files(".", "camara")
	# find_in_files("abc", "abc")
	#EX6
	callback = lambda x: print(x)
	find_in_files_2("../absolute_path.txt", "camara", callback)
	find_in_files_2(".", "camara", callback)
	find_in_files_2("abc", "abc", callback)
	#EX7
	file_prop("main.py")
	#EX8
	abs_paths(".")
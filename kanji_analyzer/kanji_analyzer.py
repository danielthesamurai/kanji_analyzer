import collections
import json

with open("kanji_list/n5c.txt",encoding="utf-8") as kln5: 
    n5_kanji = kln5.read()
with open("kanji_list/n4c.txt",encoding="utf-8") as kln4: 
    n4_kanji = kln4.read()
with open("kanji_list/n3c.txt",encoding="utf-8") as kln3: 
    n3_kanji = kln3.read()
with open("kanji_list/n2c.txt",encoding="utf-8") as kln2: 
    n2_kanji = kln2.read()
with open("kanji_list/n1c.txt",encoding="utf-8") as kln1: 
    n1_kanji = kln1.read()

total_dict = {}
n5_dict = {}
n4_dict = {}
n3_dict = {}
n2_dict = {}
n1_dict = {}

n5_counter = 0
n4_counter = 0
n3_counter = 0
n2_counter = 0
n1_counter = 0

def open_file():
    filename = input("enter the name of the file you wish to assess (or press q to quit): ")
    if filename.lower() == "q":
        quit()
    try:
        with open(filename,encoding='UTF-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("file not found, try again!")
        return open_file()
    except UnicodeDecodeError:
        print("please choose a valid file type")
        return open_file()
    else:
        return contents
    
def choose_display():
    choice = input("n1, n2, n3, n4, n5, or overall?: ")
    input_choices = {"n1":n1_dict,"n2":n2_dict,"n3":n3_dict,"n4":n4_dict,"n5":n5_dict,"overall":total_dict}
    try:
        display_list = collections.Counter.most_common(input_choices[choice])
        num1 = int(input("enter a starting place: "))
        num2 = int(input("enter an ending place: "))
        print(display_list[num1:num2:])
    except KeyError:
        print("that's not a valid input. try again.")
        choose_display()

content = open_file()

for kanji in n5_kanji:
    n5_counter += content.count(kanji)
    n5_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n4_kanji:
    n4_counter += content.count(kanji)
    n4_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n3_kanji:
    n3_counter += content.count(kanji)
    n3_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n2_kanji:
    n2_counter += content.count(kanji)
    n2_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n1_kanji:
    n1_counter += content.count(kanji)
    n1_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
    
print(f"n1 kanji amount: {n1_counter}, n2 kanji amount: {n2_counter}, n3 kanji amount: {n3_counter}, n4 kanji amount: {n4_counter}, n5 kanji amount: {n5_counter}")

total_sum = n1_counter+n2_counter+n3_counter+n4_counter+n5_counter

print(f"total amount of kanji: {total_sum}")

if total_sum > 0:
    print(f"{int((n5_counter/total_sum)*100)}% N5, {int((n4_counter/total_sum)*100)}% N4, {int((n3_counter/total_sum)*100)}% N3,{int((n2_counter/total_sum)*100)}% N2, {int((n1_counter/total_sum)*100)}% N1")
else:
    print("please choose a file that has japanese in it!")
    open_file()

choose_display()
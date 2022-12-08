import analyzer_functions as af

#make all the text files into strings
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

#initialize the empty variables to be used later
total_dict:dict = {}
n5_dict:dict = {}
n4_dict:dict = {}
n3_dict:dict = {}
n2_dict:dict = {}
n1_dict:dict = {}

n5_counter:int = 0
n4_counter:int = 0
n3_counter:int = 0
n2_counter:int = 0
n1_counter:int = 0


content = af.open_file()

        
n5_counter, n4_counter, n3_counter, n2_counter, n1_counter = af.load_program(n5k=n5_kanji,n4k=n4_kanji,n3k=n3_kanji,n2k=n2_kanji,n1k=n1_kanji,n5d=n5_dict,n4d=n4_dict,n3d=n3_dict,n2d=n2_dict,n1d=n1_dict,
                n5c=n5_counter,n4c=n4_counter,n3c=n3_counter,n2c=n2_counter,n1c=n1_counter,total=total_dict,filecontent=content)
print(n5_counter)
#display the total percentage per level of kanji
print(f"n1 kanji amount: {n1_counter}, n2 kanji amount: {n2_counter}, n3 kanji amount: {n3_counter}, n4 kanji amount: {n4_counter}, n5 kanji amount: {n5_counter}")

#add and display the total number of kanji overall
total_sum = n1_counter+n2_counter+n3_counter+n4_counter+n5_counter
print(f"total amount of kanji: {total_sum}")

#make sure the file has japanese characters in it
if total_sum > 0:
    print(f"{int((n5_counter/total_sum)*100)}% N5, {int((n4_counter/total_sum)*100)}% N4, {int((n3_counter/total_sum)*100)}% N3,{int((n2_counter/total_sum)*100)}% N2, {int((n1_counter/total_sum)*100)}% N1")
else:
    print("please choose a file that has japanese in it!")
    af.open_file()

af.choose_display(n1_dict,n2_dict,n3_dict,n4_dict,n5_dict,total_dict)
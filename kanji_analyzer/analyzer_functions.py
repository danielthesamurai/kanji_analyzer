import collections

def open_file():
    #check user input for which file to use
    filename = input("enter the name of the file you wish to assess (or press q to quit): ")
    if filename.lower() == "q":
        raise SystemExit
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

def choose_display(dict1,dict2,dict3,dict4,dict5,dict6):
    #ask the user which level of kanji to display
    choice = input("n1, n2, n3, n4, n5, or overall?: ").lower()
    input_choices = {"n1":dict1,"n2":dict2,"n3":dict3,"n4":dict4,"n5":dict5,"overall":dict6}
    try:
        display_list = collections.Counter.most_common(input_choices[choice])
        num1 = int(input("enter a starting place: "))
        num2 = int(input("enter an ending place: "))
        print(display_list[num1:num2:])
    except KeyError:
        print("that's not a valid input. try again.")
        choose_display(dict1,dict2,dict3,dict4,dict5,dict6)
    except ValueError:
        print("that's not a number! try again")
        choose_display(dict1,dict2,dict3,dict4,dict5,dict6)
        
def load_program(n5k,n4k,n3k,n2k,n1k,n5d,n4d,n3d,n2d,n1d,
                 n5c,n4c,n3c,n2c,n1c,total,filecontent):
    #load all the requisite information into the appropriate empty variables
    for kanji in n5k:
        n5c += filecontent.count(kanji)
        n5d[kanji] = filecontent.count(kanji)
        total[kanji] = filecontent.count(kanji)
    for kanji in n4k:
        n4c += filecontent.count(kanji)
        n4d[kanji] = filecontent.count(kanji)
        total[kanji] = filecontent.count(kanji)
    for kanji in n3k:
        n3c += filecontent.count(kanji)
        n3d[kanji] = filecontent.count(kanji)
        total[kanji] = filecontent.count(kanji)
    for kanji in n2k:
        n2c += filecontent.count(kanji)
        n2d[kanji] = filecontent.count(kanji)
        total[kanji] = filecontent.count(kanji)
    for kanji in n1k:
        n1c += filecontent.count(kanji)
        n1d[kanji] = filecontent.count(kanji)
        total[kanji] = filecontent.count(kanji)
    return n5c,n4c,n3c,n2c,n1c
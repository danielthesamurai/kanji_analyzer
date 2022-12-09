import collections as cl

class kanji_analyzer():
    #load the text files with the kanji info into string lists
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
    
    #intialize all necessary empty variables
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
    
    common_n5:list = []
    common_n4:list = []
    common_n3:list = []
    common_n2:list = []
    common_n1:list = []
    common_all:list = []
    
    def open_file(self,entry):
    #check user input for which file to use
        filename = entry
        if filename.lower() == "quit":
            raise SystemExit
        try:
            with open(filename,encoding='UTF-8') as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            print("file not found, try again!")
            return self.open_file(entry)
        except UnicodeDecodeError:
            print("please choose a valid file type")
            return self.open_file(entry)
        else:
            return self.load_program(contents)
    
    def load_program(self,file):
        #load the contents of the selected file into the program
        for kanji in self.n5_kanji:
            self.n5_counter += file.count(kanji)
            self.n5_dict[kanji] = file.count(kanji)
            self.total_dict[kanji] = file.count(kanji)
        for kanji in self.n4_kanji:
            self.n4_counter += file.count(kanji)
            self.n4_dict[kanji] = file.count(kanji)
            self.total_dict[kanji] = file.count(kanji)
        for kanji in self.n3_kanji:
            self.n3_counter += file.count(kanji)
            self.n3_dict[kanji] = file.count(kanji)
            self.total_dict[kanji] = file.count(kanji)
        for kanji in self.n2_kanji:
            self.n2_counter += file.count(kanji)
            self.n2_dict[kanji] = file.count(kanji)
            self.total_dict[kanji] = file.count(kanji)
        for kanji in self.n1_kanji:
            self.n1_counter += file.count(kanji)
            self.n1_dict[kanji] = file.count(kanji)
            self.total_dict[kanji] = file.count(kanji)
        self.common_kanji()
        
    def common_kanji(self):
        #turn the dictionaries of kanji into lists that are arranged by most common
        self.common_n5 = cl.Counter.most_common(self.n5_dict)
        self.common_n4 = cl.Counter.most_common(self.n4_dict)
        self.common_n3 = cl.Counter.most_common(self.n3_dict)
        self.common_n2 = cl.Counter.most_common(self.n2_dict)
        self.common_n1 = cl.Counter.most_common(self.n1_dict)
        self.common_all = cl.Counter.most_common(self.total_dict)
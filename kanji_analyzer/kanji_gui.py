import tkinter as tk
import analyzer_functions as af
import collections as cl

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

def get_text(entry,lbl,btn,frame):
    
    global n5_counter
    global n4_counter
    global n3_counter
    global n2_counter
    global n1_counter
    
    file_entry = entry.get()
    content = af.open_file(file_entry)
    n5_counter, n4_counter, n3_counter, n2_counter, n1_counter = af.load_program(n5k=n5_kanji,n4k=n4_kanji,n3k=n3_kanji,n2k=n2_kanji,n1k=n1_kanji,n5d=n5_dict,n4d=n4_dict,n3d=n3_dict,n2d=n2_dict,n1d=n1_dict,
                n5c=n5_counter,n4c=n4_counter,n3c=n3_counter,n2c=n2_counter,n1c=n1_counter,total=total_dict,filecontent=content)
    total_sum = n1_counter+n2_counter+n3_counter+n4_counter+n5_counter
    result = f"{int((n5_counter/total_sum)*100)}% N5, {int((n4_counter/total_sum)*100)}% N4, {int((n3_counter/total_sum)*100)}% N3,{int((n2_counter/total_sum)*100)}% N2, {int((n1_counter/total_sum)*100)}% N1"
    entry.delete(0,tk.END)
    for widget in frame.winfo_children():
        widget.destroy()
    display_label = tk.Label(root,text=result,font=("arial",15))
    name_label = tk.Label(root,text="breakdown of kanji in "+file_entry,font=("arial",15))
    name_label.pack(pady=(20,0))
    display_label.pack(pady=(20,0))
    lvl_btn = tk.Button(root,text="choose a level",font=("arial",15),command=lambda:choose_level(frame=root))
    new_file_btn = tk.Button(root,text="choose a new file",font=("arial",15),command=lambda:initial_setup(frame=root))
    lvl_btn.pack(side=tk.LEFT,pady=(0,300),padx=(75,0))
    new_file_btn.pack(side=tk.RIGHT,pady=(0,300),padx=(0,75))
    
def choose_level(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    lvl_lbl_1 = tk.Label(root,text="enter your desired level, from n5-n1 or overall: ",font=("arial",15))
    lvl_lbl_entry = tk.Entry(root,width=30,font=("arial",15))
    accept_btn = tk.Button(root,text="display kanji from level",font=("arial",15),command=lambda:display_level(frame=root,entry=lvl_lbl_entry.get()))
    lvl_lbl_1.pack(pady=(50,20))
    lvl_lbl_entry.pack(pady=(0,20))
    accept_btn.pack()

def display_level(frame,entry):
    slice1 = 0
    slice2 = 100
    kanji_dicts = {"n5":n5_dict,"n4":n4_dict,"n3":n3_dict,"n2":n2_dict,"n1":n1_dict,"overall":total_dict}
    for widget in frame.winfo_children():
        widget.destroy()
    lvl_lbl = tk.Label(root,text=cl.Counter.most_common(kanji_dicts[entry])[slice1:slice2:],wraplength=400,font=("arial",15))
    back = tk.Button(root,text="<",font=("arial",15),command=lambda:sub_slice(num1=slice1,num2=slice2,label=lvl_lbl,diction=kanji_dicts,entry=entry))
    forward = tk.Button(root,text=">",font=("arial",15),command=lambda:add_slice(num1=slice1,num2=slice2,label=lvl_lbl,diction=kanji_dicts,entry=entry))
    newfile_btn = tk.Button(root,text="new file",font=("arial",15),command=lambda:initial_setup(frame=root))
    lvl_lbl.pack(pady=(50,0))
    back.pack(side=tk.LEFT,padx=(100,0))
    forward.pack(side=tk.RIGHT,padx=(0,100))
    newfile_btn.pack(pady=(25,0))
    
def add_slice(num1,num2,label,diction,entry):
        num1+=50
        num2+=50
        label.config(text=cl.Counter.most_common(diction[entry])[num1:num2:])

def sub_slice(num1,num2,label,diction,entry):
        num1-=50
        num2-=50
        label.config(text=cl.Counter.most_common(diction[entry])[num1:num2:])
    
def initial_setup(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    label = tk.Label(root,text="enter file you wish to analyze: ",font=("arial",15))
    fileget = tk.Entry(root,width=30,font=("arial",15))
    file_btn = tk.Button(text="Analyze Kanji",font=("arial",15),command=lambda:get_text(entry=fileget,lbl=label,btn=file_btn,frame=root))
    label.pack(pady=(50,20))
    fileget.pack(pady=(0,20))
    file_btn.pack()
    
    

root = tk.Tk()
root.title("kanji analyzer")
root.geometry("500x600")
root.resizable(False,False)
initial_setup(frame=root)



root.mainloop()
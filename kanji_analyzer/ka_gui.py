import tkinter as tk
import kanji_analyzer_class as kac

def get_text(kanji,entry,frame):
    kanji.open_file(entry.get())
    frame.destroy()
    n_frame = tk.Frame(root)
    n_lbl = tk.Label(n_frame,text="What level do you wish to display?")
    v = tk.StringVar()
    v.set("N5")
    n_rdbtn_n5 = tk.Radiobutton(n_frame,text=kanji.n5_results,variable=v,value="N5")
    n_rdbtn_n4 = tk.Radiobutton(n_frame,text=kanji.n4_results,variable=v,value="N4")
    n_rdbtn_n3 = tk.Radiobutton(n_frame,text=kanji.n3_results,variable=v,value="N3")
    n_rdbtn_n2 = tk.Radiobutton(n_frame,text=kanji.n2_results,variable=v,value="N2")
    n_rdbtn_n1 = tk.Radiobutton(n_frame,text=kanji.n1_results,variable=v,value="N1")
    n_rdbtn_all = tk.Radiobutton(n_frame,text=kanji.all_results,variable=v,value="All")
    n_button = tk.Button(n_frame,text="enter",command=lambda:display_level_kanji(kanji,n_frame,v))
    n_frame.pack()
    n_lbl.pack()
    n_rdbtn_n5.pack()
    n_rdbtn_n4.pack()
    n_rdbtn_n3.pack()
    n_rdbtn_n2.pack()
    n_rdbtn_n1.pack()
    n_rdbtn_all.pack()
    n_button.pack()
    
def display_level_kanji(kanji,frame,entry):

    class fwd_bk():
        start = 0
        end = 100
        def fwd(self,label):
            self.start += 100
            self.end += 100
            label.configure(text=k_dict[entry.get()][fb.start:fb.end:])
        def bk(self,label):
            self.start -= 100
            self.end -= 100
            label.configure(text=k_dict[entry.get()][fb.start:fb.end:])

    fb = fwd_bk()
    frame.destroy()
    d_frame = tk.Frame(root)
    dn_frame = tk.Frame(d_frame)
    kanji.common_kanji()
    k_dict = {"N1":kanji.common_n1,"N2":kanji.common_n2,"N3":kanji.common_n3,"N4":kanji.common_n4,"N5":kanji.common_n5,"All":kanji.common_all}
    d_lbl = tk.Label(d_frame,text=k_dict[entry.get()][fb.start:fb.end:],wraplength=400)
    d_btn = tk.Button(dn_frame,text="choose another file",command=lambda:startup_window(kanji,d_frame))
    d2_btn = tk.Button(dn_frame,text="choose a different level",command=lambda:get_text(kanji,entry,d_frame))
    dnl_btn = tk.Button(dn_frame,text="<",command=lambda:fb.bk(d_lbl))
    dnr_btn = tk.Button(dn_frame,text=">",command=lambda:fb.fwd(d_lbl))
    d_frame.pack()
    d_lbl.pack()
    dn_frame.pack()
    dnl_btn.pack(side=tk.LEFT)
    d_btn.pack(side=tk.LEFT)
    d2_btn.pack(side=tk.LEFT)
    dnr_btn.pack(side=tk.LEFT)

def startup_window(kanji,frame):
    if frame:
        frame.destroy()
    s_frame = tk.Frame(root,pady=100)
    entry = tk.Entry(s_frame)
    lbl = tk.Label(s_frame,text="enter the file you wish to analyze",wraplength=300)
    btn = tk.Button(s_frame,text="enter file",command=lambda:get_text(kanji,entry,s_frame))
    s_frame.pack()
    lbl.pack()
    entry.pack()
    btn.pack()

    
kanji = kac.kanji_analyzer()
root = tk.Tk()
root.title("Kanji Analyzer")
root.geometry("400x300")
empty_frame = tk.Frame(root)
startup_window(kanji,empty_frame)
root.mainloop()

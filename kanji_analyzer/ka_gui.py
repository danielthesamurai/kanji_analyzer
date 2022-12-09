import tkinter as tk
import kanji_analyzer_class as kac

def get_text(kanji,entry,frame):
    kanji.open_file(entry.get())
    frame.destroy()
    n_frame = tk.Frame(root)
    n_results = tk.Label(n_frame,text=kanji.display_results())
    n_lbl = tk.Label(n_frame,text="What level do you wish to display?")
    n_entry = tk.Entry(n_frame)
    n_button = tk.Button(n_frame,text="enter",command=lambda:display_level_kanji(kanji,n_entry,n_frame))
    n_frame.pack()
    n_results.pack()
    n_lbl.pack()
    n_entry.pack()
    n_button.pack()
    
def display_level_kanji(kanji,entry,frame):
    entered = entry.get()
    frame.destroy()
    d_frame = tk.Frame(root)
    kanji.common_kanji()
    common_dict = {"n1":kanji.common_n1,"n2":kanji.common_n2,"n3":kanji.common_n3,"n4":kanji.common_n4,"n5":kanji.common_n5,"all":kanji.common_all}
    d_lbl = tk.Label(d_frame,text=common_dict[entered][0:100:],wrap=400)
    d_btn = tk.Button(d_frame,text="choose another file",command=lambda:startup_window(kanji))
    d_frame.pack()
    d_lbl.pack()
    d_btn.pack()

def startup_window(kanji):
    s_frame = tk.Frame(root,pady=100)
    entry = tk.Entry(s_frame)
    lbl = tk.Label(s_frame,text="enter the file you wish to analyze",wrap=300)
    btn = tk.Button(s_frame,text="enter file",command=lambda:get_text(kanji,entry,s_frame))
    s_frame.pack()
    lbl.pack()
    entry.pack()
    btn.pack()

    
kanji = kac.kanji_analyzer()
root = tk.Tk()
root.title("Kanji Analyzer")
root.geometry("400x300")
startup_window(kanji)
root.mainloop()

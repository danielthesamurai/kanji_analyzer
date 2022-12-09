import tkinter as tk
import kanji_analyzer_class as kac

def get_text(entry,label):
    kanji.open_file(entry)
    print(kanji.common_n5)
    label.configure(text=kanji.common_all[0:100:])
    
kanji = kac.kanji_analyzer()
root = tk.Tk()
root.title("Kanji Analyzer")
root.geometry("400x600")
entry = tk.Entry(root)
lbl = tk.Label(root,text=kanji.common_n5,wrap=300)
btn = tk.Button(root,text="enter file",command=lambda:get_text(entry.get(),lbl))
entry.pack()
btn.pack()
lbl.pack()
root.mainloop()

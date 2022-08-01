from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()
common_img = PhotoImage(width = 1, height = 1)

#Properties
font_type_1 = "Times New Roman"


entry_text = StringVar()
correct_word = "Tiger"

a1 = "X"
a2 = "X"
a3 = "X"
a4 = "X"
a5 = "X"

#Def 
def on_change():
    if len(entry_text.get()) > 4:
        user_answer1 = E1.get()
        Box1.config(text=user_answer1[0].upper())
        Box2.config(text=user_answer1[1].upper())
        Box3.config(text=user_answer1[2].upper())
        Box4.config(text=user_answer1[3].upper())
        Box5.config(text=user_answer1[4].upper())
        print(user_answer1)
        InformationBox.config(text="")
    else :
        InformationBox.config(text="The answer is too short. Write 5 characters.")
        

    return True

#Def answer check
def answer_check():
    if E1.get() == correct_word:
        InformationBox.config(text="Well done you win")


#Character Limit Def
def character_limit(entry_text):
    if len(entry_text.get()) > 5:
        entry_text.set(entry_text.get()[:5])

    

entry_text.trace("w", lambda *args: character_limit(entry_text))


Box1 = ttk.Label(frm, background="black", foreground="white", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text=a1)
Box1.grid(column=0, row=0)
Box2 = ttk.Label(frm, background="black", foreground="white", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text=a2)
Box2.grid(column=1, row=0)
Box3 = ttk.Label(frm, background="black", foreground="white", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text=a3)
Box3.grid(column=2, row=0)
Box4 = ttk.Label(frm, background="black", foreground="white", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text=a4)
Box4.grid(column=3, row=0)
Box5 = ttk.Label(frm, background="black", foreground="white", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text=a5)
Box5.grid(column=4, row=0)
#row 1
ttk.Label(frm, background="black", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text="X").grid(column=0, row=1)
ttk.Label(frm, background="black", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text="X").grid(column=1, row=1)
ttk.Label(frm, background="black", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text="X").grid(column=2, row=1)
ttk.Label(frm, background="black", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text="X").grid(column=3, row=1)
ttk.Label(frm, background="black", borderwidth=2, padding=20, relief="ridge", font=(font_type_1,22), text="X").grid(column=4, row=1)


#Information Box
InformationBox = ttk.Label(root, text = "information Text", font=(font_type_1,12))
InformationBox.grid(column=0, row=96)

#EntryBox
E1 = Entry(root, textvariable = entry_text, font=(font_type_1,22))
E1.grid(column=0, row=97)

#old Entrybox below
#E1 = Entry(root, validate='key', validatecommand=on_change, font=(font_type_1,22))

#Submit button
submitButton = Button( text="Submit", command=lambda:[on_change(),answer_check()], image= common_img, width = 90, height = 30,
compound = 'c', bg="darkblue", fg="white", font="helvetica", activebackground="lightyellow", activeforeground="black", relief=GROOVE).grid(column=0, row=98)

#Quit Button
ttk.Button( text="Quit", command=root.destroy).grid(column=0, row=100)

root.mainloop()
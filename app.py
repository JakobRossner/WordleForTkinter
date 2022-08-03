from posixpath import split
from tkinter import *
from tkinter import ttk
from webbrowser import BackgroundBrowser
root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()
common_img = PhotoImage(width = 1, height = 1)


#Properties
font_type_1 = "Times New Roman"
entry_text = StringVar()



correct_word = "Tiger"
correct_word = correct_word.upper()



a1 = "X"
a2 = "X"
a3 = "X"
a4 = "X"
a5 = "X"

#Information Box
InformationBox = ttk.Label(root, text = "information Text", font=(font_type_1,12))
InformationBox.grid(column=0, row=96)




#Def 
def on_change():
    if len(entry_text.get()) > 4:
        user_answer1 = E1.get()
        user_answer1 = user_answer1.upper()
        Box1.config(text=user_answer1[0].upper())
        Box2.config(text=user_answer1[1].upper())
        Box3.config(text=user_answer1[2].upper())
        Box4.config(text=user_answer1[3].upper())
        Box5.config(text=user_answer1[4].upper())
        print(user_answer1)
        InformationBox.config(text="")
    else :
        InformationBox.config(text="The answer is too short. Write 5 characters.")
        
    #return True

#Def Find a certain letter and color label
def find_letter(event = None):
    split_word = E1.get()
    split_word = split_word.upper()
    
    
    if (len(split_word) != 5):
        print("Finder letter: Length is not okay")

    elif (len(split_word) >= 5):
        n1 = split_word[0]
        n2 = split_word[1]
        n3 = split_word[2]
        n4 = split_word[3]
        n5 = split_word[4]
        print("Finder letter: Length is okay!")
        if (n1 in correct_word):
            print("n1 is in the correct word")
            if (n1 == correct_word[0]):
                Box1.config(background="green")
                print(correct_word[0])
            elif (n1 in correct_word):
                Box1.config(background="gold2")
                print(correct_word[0])
            else:
                Box1.config(background="red")
                print(correct_word[0])

        else:
            print("n1 is NOT in correct word")
            Box1.config(background="black")
            Box2.config(background="black")
            Box3.config(background="black")
            Box4.config(background="black")
            Box5.config(background="black")
            
    
    elif("bla" in correct_word):
        print('Found')
    
    else :
        print('Not found')
        print(split_word)
        print(len(split_word))
#root.bind('<Return>', find_letter)


#Def answer check
def answer_check():
    if 1 == True:
        print()
    elif E1.get() == correct_word :
        InformationBox.config(text="Well done you win")

#root.bind('<Return>', answer_check)
    


#Character Limit Def
def character_limit(entry_text):
    if len(entry_text.get()) > 5:
        entry_text.set(entry_text.get()[:5])

def combined(*bla,**bla2):
    find_letter(*bla)
    character_limit(**bla2)
    answer_check()

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

#EntryBox
E1 = Entry(root, textvariable = entry_text, font=(font_type_1,22))
E1.grid(column=0, row=97)
E1.focus_set()


#old Entrybox below
#E1 = Entry(root, validate='key', validatecommand=on_change, font=(font_type_1,22))

#Submit button
submitButton = Button( text="Submit", command=lambda:[on_change(),answer_check(),find_letter()], image= common_img, width = 90, height = 30,
compound = 'c', bg="darkblue", fg="white", font="helvetica", activebackground="lightyellow", activeforeground="black", relief=GROOVE).grid(column=0, row=98)

root.bind('<Return>', [on_change(),answer_check(),find_letter()])
#root.bind('<Return>', lambda event=None: submitButton.invoke())

#Quit Button
ttk.Button( text="Quit", command=root.destroy).grid(column=0, row=100)

root.mainloop()
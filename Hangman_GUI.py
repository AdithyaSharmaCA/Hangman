from tkinter import *
root=Tk()                                                         
root.title('HANGMAN : THE GAME')                                  
root.config(bg="Black")
root.geometry("1000x800")
"""
Welcome to the code of the game , Hangman.
In the above few lines of code we are creating a user interface window using Tkinter.
we also add the title of the gui window using the root.title() function
Please proceed to the start() to trace the control flow.
"""  
#-----------------------------------------------------------------------------------------------------#
def onclick():                                                    
    global guessing_box_1,guessing_box_2,guessing_box_3,guessing_box_4,guessing_box_5,guessing_box_6,guessing_box_7,guessing_box_8,guessing_box_9,guessing_box_10,letters
    l1.config(text="LET THE GUESSING BEGIN!!!",bg="green yellow")
    clue.destroy()                                                
    helpclue=Label(root,text="CLUE: "+clue_box.get(),font="BOLD",bg="firebrick2")
    helpclue.pack()
    clue_box.destroy()
    if len(word.get())<=5 or len(word.get())>10:                  
        clue.after(100,lambda : l1.config(text="Please enter a new word with more than 5 letters"))
        helpclue.destroy()                                        
        click.destroy()                                           
        word.destroy()
        l1.destroy()
        start()
    else:                                                         
        guessing_box_1=Entry(root,width=2,font=("Ariel",25))      
        guessing_box_2=Entry(root,width=2,font=("Ariel",25))
        guessing_box_3=Entry(root,width=2,font=("Ariel",25))
        guessing_box_4=Entry(root,width=2,font=("Ariel",25))
        guessing_box_5=Entry(root,width=2,font=("Ariel",25))
        guessing_box_6=Entry(root,width=2,font=("Ariel",25))
        guessing_box_7=Entry(root,width=2,font=("Ariel",25))
        guessing_box_8=Entry(root,width=2,font=("Ariel",25))
        guessing_box_9=Entry(root,width=2,font=("Ariel",25))
        guessing_box_10=Entry(root,width=2,font=("Ariel",25))
        guessing_box_1.pack(side=LEFT,expand=True)
        guessing_box_2.pack(side=LEFT,expand=True)
        guessing_box_3.pack(side=LEFT,expand=True)
        guessing_box_4.pack(side=LEFT,expand=True)
        guessing_box_5.pack(side=LEFT,expand=True)
        guessing_box_6.pack(side=LEFT,expand=True)
        if len(word.get())==7:
            guessing_box_7.pack(side=LEFT,expand=True)
        if len(word.get())==8:
            guessing_box_7.pack(side=LEFT,expand=True)
            guessing_box_8.pack(side=LEFT,expand=True)
        if len(word.get())==9:
            guessing_box_7.pack(side=LEFT,expand=True)
            guessing_box_8.pack(side=LEFT,expand=True)
            guessing_box_9.pack(side=LEFT,expand=True)
        if len(word.get())==10:
            guessing_box_7.pack(side=LEFT,expand=True)
            guessing_box_8.pack(side=LEFT,expand=True)
            guessing_box_9.pack(side=LEFT,expand=True)
            guessing_box_10.pack(side=LEFT,expand=True)        
        letters=word.get()
        click.destroy()
        word.destroy()
        aftersubmission()
"""
Next,
the control flow from the start() is taken to the onclick()
In this function we make use of an if statement to check for the length of the word (ie...if in range(5,10))
All of the widgets inside the if statement are destoryed to make room for the widgets that get repeated from the start()
Once the length of the word is optimal for the code we proceed further
Next for a few lines we create entry boxes with reference to the length of the word
The function onclick() terminantes with a function call to aftersubmission()
"""


#------------------------------------------------------------------------------------------------------------#
def start():                                                      
    global l1,word,clue,clue_box,click
    l1=Label(root,text="Enter a word for the game to begin",font="BOLD",bg="Orange")
    l1.pack()
    word=Entry(root)
    word.pack()
    clue=Label(root,text="Enter a clue for the word put up",font="BOLD",bg="Green")
    clue.pack()
    clue_box=Entry(root)
    clue_box.pack()
    click=Button(root,text="SUBMIT",command=onclick,bg="cyan")    
    click.pack()                                                  
start()                                                           
"""
Welcome the code of hangman the game
The start() is the function where the code begins with a function call outside the function body.
The function in the argument , command leads us to a new function named onclick() ,
the function call happens due to clicking the submit button.
We set the environment by creating a few labels and entry boxes for the user to enter.
"""
#-------------------------------------------------------------------------------------------------------------#

def aftersubmission():                                             
    global letterentrylabel
    letterentrylabel=Label(root,text="Enter the letters one by one",font="BOLD",bg="yellow")
    letterentrylabel.pack()
    keyboard()
"""
Once the word has been set into the entry box by the user a clue is added , upon clicking the submit button
we come a small function named aftersubmission()
This function is used to create a label just on top of our virtual keyboard in order to aid the user
through the guessing process.
Upon executing the body of the function,we make a function call to the virtual keyboard part of out code.
"""   
#---------------------------------------------------------------------------------------------------------------#                                                   
count=7                                                          
def keyboard():                                                   
    global l,displaycount
    A=Button(root,text='A',command=lambda:keyonclick("A"))        
    B=Button(root,text='B',command=lambda:keyonclick("B"))        
    C=Button(root,text='C',command=lambda:keyonclick("C"))        
    D=Button(root,text='D',command=lambda:keyonclick("D"))
    E=Button(root,text='E',command=lambda:keyonclick("E"))
    F=Button(root,text='F',command=lambda:keyonclick("F"))
    G=Button(root,text='G',command=lambda:keyonclick("G"))
    H=Button(root,text='H',command=lambda:keyonclick("H"))
    I=Button(root,text='I',command=lambda:keyonclick("I"))
    J=Button(root,text='J',command=lambda:keyonclick("J"))
    K=Button(root,text='K',command=lambda:keyonclick("K"))
    L=Button(root,text='L',command=lambda:keyonclick("L"))
    M=Button(root,text='M',command=lambda:keyonclick("M"))
    N=Button(root,text='N',command=lambda:keyonclick("N"))
    O=Button(root,text='O',command=lambda:keyonclick("O"))
    P=Button(root,text='P',command=lambda:keyonclick("P"))
    Q=Button(root,text='Q',command=lambda:keyonclick("Q"))
    R=Button(root,text='R',command=lambda:keyonclick("R"))
    S=Button(root,text='S',command=lambda:keyonclick("S"))
    T=Button(root,text='T',command=lambda:keyonclick("T"))
    U=Button(root,text='U',command=lambda:keyonclick("U"))
    V=Button(root,text='V',command=lambda:keyonclick("V"))
    W=Button(root,text='W',command=lambda:keyonclick("W"))
    X=Button(root,text='X',command=lambda:keyonclick("X"))
    Y=Button(root,text='Y',command=lambda:keyonclick("Y"))
    Z=Button(root,text='Z',command=lambda:keyonclick("Z"))
    l=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]       
    for button in l:
        button.pack(side=TOP,fill=BOTH)
    displaycount=Label(root,text=count,font="BOLD",bg="lawn green")
    displaycount.pack()
"""
We invoke this function from within the aftersubmission()
This is the virtual keyboard part of our code.
It has a series of buttons for all the letters from A-Z in order to guess the letters
one by one.
Each button makes use of a lambda function in order to make a function call to keyonclick() ,
where the logic of the game lies.
We tried using a for loop to create all the buttons but we were unable to access each text on the button
without assingning them to a new variable.
Next,
we created a list of all the buttons which helps us in the rest of the code.
lambda functions help us define a function in a single line for each letter
"""
#--------------------------------------------------------------------------------------------------#
def display():                                                   
    for boxes in guessingboxes:
        boxes.destroy()
    for let in l:                                                
        let.destroy()                                            
    victory=Label(root,text="CONGRATS YOU HAVE FOUND THE WORD!!!!",font="BOLD",bg="gold")
    if count!=0:
        victory.pack()
    Label(root,text="The correct word was "+letters.upper(),font="BOLD",bg="dodger blue").pack()
    l1.destroy()
    letterentrylabel.destroy()                                   
c=0
"""
Once all the guessings have been completed or the word is not found even after 7 wrong attempts
The final answer comes on to the screen where its seen bold capital letters.
Hence signalling that the game has ended. 
""" 
#--------------------------------------------------------------------------------------------------#
alphabetlist=[str(chr(alphabet)) for alphabet in range(65,91)]    
def keyonclick(text):                                             
    l1=list(letters.upper())                                     
    for button in l:
        if button.cget('text')==text:                            
            if button.cget('text') in l1:
                button.config(bg="deep sky blue")                 
            else:
                button.config(bg='orange red')                   
    global guessingboxes,c,count
    if text in l1:                                                
        if text in l1[0] and len(guessing_box_1.get())!=1:        
            guessing_box_1.insert(0,text)
            c=c+1
        if text in l1[1] and len(guessing_box_2.get())!=1:
            guessing_box_2.insert(0,text)
            c=c+1
        if text in l1[2] and len(guessing_box_3.get())!=1:
            guessing_box_3.insert(0,text)
            c=c+1
        if text in l1[3] and len(guessing_box_4.get())!=1:
            guessing_box_4.insert(0,text)
            c=c+1
        if text in l1[4] and len(guessing_box_5.get())!=1:
            guessing_box_5.insert(0,text)
            c=c+1
        if text in l1[5] and len(guessing_box_6.get())!=1:
            guessing_box_6.insert(0,text)
            c=c+1
        if len(l1)>=7 and text in l1[6] and len(guessing_box_7.get())!=1:
            guessing_box_7.insert(0,text)
            c=c+1
        if len(l1)>=8 and text in l1[7] and len(guessing_box_8.get())!=1:
            guessing_box_8.insert(0,text)
            c=c+1
        if len(l1)>=9 and text in l1[8] and len(guessing_box_9.get())!=1:
            guessing_box_9.insert(0,text)
            c=c+1
        if len(l1)==10 and text in l1[9] and len(guessing_box_10.get())!=1:
            guessing_box_10.insert(0,text)
            c=c+1
    else:                                                         
        if text in alphabetlist:                                 
            count=count-1
        displaycount.config(text=count)
        if text in alphabetlist:
            alphabetlist.pop(alphabetlist.index(str(text)))
    if c==len(l1) or count==0:                                    
        guessingboxes=[guessing_box_1,guessing_box_2,guessing_box_3,guessing_box_4,guessing_box_5,guessing_box_6,guessing_box_7,guessing_box_8,guessing_box_9,guessing_box_10]
        display()                                                 
root.mainloop()
"""
LOGIC: if all entry boxes have anyword in them then its confirmed that the word is complete.
The logic part of the code is in the above defined function(ie...keyonclick(text))
This function is executed once the user clicks the button from the virtual keyboard.
We make use of a parameter text which is the nothing but the letter present on the button.
Right after this we create a list of letters of the word where the index of each of these letters are retained.
If the letter on the button is in the list of the letters of the word , we colour it with blue.
And if its missing we go on to color it red.
Next,
We have a bunch of if statements which check if the letter that is passed on from the buttton, is present on the
assigned idex of the lettter in the list.If present it gets entered into the guessing boxes with indexing followed.
Once entered we also have to ensure that the length of letters in each box has to be 1 to complete the game without repition 
of letters in the boxes.
We also have a constant 'c' which keeps track of the the length of the word in the guessing boxes.
Once the value of 'c' becomes equal to the length of the word , it inadvertently means that the word has been guessed.
We also have the live chance counter where we are able to show the user on how many wrong guesses they can make while trying to 
figure out the word.They get a maixmum of 7 wrong guesses.
Following this , 
we have a list of alphabets which keep track of the letters  that have already been guessed and does not make
any changes even if the same button if pressed multiple number of times.This list is generated through list comprehension.
At the very end we make a decision box which helps us decide once the game is over.
If the game is over we make to function call one last time to the display(),which is where the game ends.
"""
#---------------------------------------------------------------------------------------------------------------------------------#

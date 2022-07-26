word=input("enter a word for the opponent to guess ").upper()
clue=input("enter a clue for your opponent ")#to be entered by the opponent
numberofchances=len('HANGMAN')#as per the rules of the game we have 7 trials so the word hangman
wordlist=list(word)#constructor method of forming a list
displaylist=[]
from os import system
def clear():#used to clear the screen has the same functioning of clrscr
	c= system('cls')
clear()
print(clue)
for i in range(len(wordlist)):#this will append the same number of dashes as there is in the original word
    displaylist.append('_')
print(displaylist)
while numberofchances>0:#we are using a while loop as the number of times the player guesses is not finite and depends on the word
    #tkinter part comes here to get added to the program
    if '_' in displaylist:#this ensures that the display list has blanks in it
        letter=input("enter a letter-this can be anything but individual charecters only ").upper()
        if letter in wordlist:
                displaylist[wordlist.index(letter)]=letter
                for i in range(wordlist.index(letter),len(wordlist)):#to have all the letters coming up to be displayed
                    if wordlist[i]==letter:
                        displaylist[i]=letter        
                print(displaylist)
        else:
            print("letter not in word please try a new word")
            numberofchances=numberofchances-1
    else:
        print("CONGRATS YOU'VE FOUND THE WORD!!!")
        numberofchances=0   #we use this statement here as this is used in coming lines to print the correct word
if numberofchances<=0:
    print("the correct word is ",word)#it tells us the original word once the round is complete and when the word is guessed

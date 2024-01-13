#Duncan Craine
#Project 3 - Caesar Cypher
#10-24-22

from graphics import *
 
    
#draws buttons
def drawButton(win, pt1, pt2, label, color):
    button = Rectangle(pt1, pt2)
    button.setFill(color)
    button.draw(win)

    centerX = (pt1.getX() + pt2.getX()) / 2.0
    centerY = (pt1.getY() + pt2.getY()) / 2.0
    label = Text(Point(centerX, centerY), label)
    label.draw(win)

    return button

#checks to see if a button is clicked
def isClicked(button, point):
    
    pt1 = button.getP1()
    pt2 = button.getP2()
    x1 = pt1.getX()
    x2 = pt2.getX()
    y1 = pt1.getY()
    y2 = pt2.getY()
    x3 = point.getX()
    y3 = point.getY()
    if x3 >= x1 and x3 <= x2 and y3 >= y1 and y3 <= y2: #if the point of the click is within the button's perimeter
        return True
    else:
        return False

#encoding gunction
def encode(message, key):
    newSent = ""
    for letter in message:
        if letter.isalpha() == False: #checks to see if it is a letter
            newSent += letter
        else: #checks to see if shift exceeds the alphabet so it can shift
            if (ord(letter)+key > 90 and letter == letter.upper()) or (ord(letter)+key > 122 and letter == letter.lower()):
                newSent += chr(ord(letter)+key-26)#moves to start of alphabet
            else:
                newSent += chr(ord(letter)+key)
    return("Your encoded message is: " + newSent)

#decoding function
def decode(message, key):
    newSent = ""
    for letter in message:
        if letter.isalpha() == False: #checks to see if it is a letter
            newSent += letter
        else: #checks to see if shift exceeds the alphabet so it can shift
            if ((ord(letter)-key < 65) and (letter == letter.upper())) or ((ord(letter)-key < 97) and (letter == letter.lower())):
                newSent += chr(ord(letter)-key+26)#moves it to end of alphabet
            else:
                newSent += chr(ord(letter)-key)
    return("Your decoded message is: " + newSent)
    

def main():
    myWin = GraphWin("Caesar Cypher", 600, 600)#open main screen
    myWin.setBackground("black")
    start = drawButton(myWin, Point(250,250), Point(350,350), "", "green")
    #welcome message
    welcome = Text(Point(300, 200), "Press the green button to start")
    welcome.setTextColor("white")
    welcome.draw(myWin)

    #waits until green start button is clicked
    pt = myWin.getMouse()
    while isClicked(start, pt) == False:
        pt = myWin.getMouse()

    #welcome message
    welcome.setText("Welcome to Caesar Cypher \n \n \n \n \n \n \n Loading...")
    start.undraw()
    
    #loading animation
    outer = Rectangle(Point(100,400), Point(500,450))
    outer.setFill("white")
    outer.draw(myWin)
    percent = Rectangle(Point(110,410), Point(110,440))
    percent.setFill("gray")
    percent.draw(myWin)
    for i in range(380): #redraws percent to seem like its growing
        percent.undraw()
        percent = Rectangle(Point(110,410), Point(110+i,440))
        percent.setFill("gray")
        percent.draw(myWin)
        time.sleep(.001)
    time.sleep(.1)

    #start of the caesar cypher part - end of opening part
    start.undraw()
    outer.undraw()
    percent.undraw()
    myWin.setBackground("white")

    encButton = drawButton(myWin, Point(50,450), Point(150,500), "ENCODE", "light blue")
    decButton = drawButton(myWin, Point(450,450), Point(550,500), "DECODE", "yellow")
    
    mainText = Text(Point(300, 300), "A Caesar cipher is a simple substitution cipher based on \n\
the idea of shifting each letter of the plaintext message \n\
a fixed number of positions in the alphabet.")
    mainText.setFill('black')
    mainText.draw(myWin)

    #sentence entry box
    sentEnt = Entry(Point(300, 75), 60)
    sentEnt.setText('')
    sentEnt.draw(myWin)
    label1 = Text(Point(300, 25), "Enter message below to be encode/decode. \n Leave the text file name box as is, if you don't want to input a file")
    label1.draw(myWin)

    #text file entry box
    textEnt = Entry(Point(300, 175), 30)
    textEnt.setText('.txt')
    textEnt.draw(myWin)
    label2 = Text(Point(300, 125), "Enter the name of the text file below.\n Make sure to keep the sentence entry box clear.\n Keep the .txt at the end.")
    label2.draw(myWin)


    #key entry box
    keyEnt = Entry(Point(300, 250), 5)
    keyEnt.setText('')
    keyEnt.draw(myWin)
    label3 = Text(Point(300, 225), "Enter key below to be encode/decode")
    label3.draw(myWin)
    
    pt = myWin.getMouse()
    while isClicked(encButton, pt) == False and isClicked(decButton, pt) == False:
        pt = myWin.getMouse()
    if isClicked(encButton, pt) == True:
        if textEnt.getText() != ".txt": #if a text file name is entered
            inText = open(textEnt.getText(), "r", encoding = "utf-8") #opens text file
            text = inText.read() #converts text file into string
            enc = encode(text, int(keyEnt.getText()))
        else:
            enc = encode(sentEnt.getText(), int(keyEnt.getText()))
        mainText.setText(enc) 
        output = open("encoded.txt","w")
        output.write(enc)
        output.close()
    
    else:
        if textEnt.getText() != ".txt": #if a text file name is entered
            inText = open(textEnt.getText(), "r", encoding = "utf-8") #opens text file
            text = inText.read() #converts text file into string
            dec = deccode(text, int(keyEnt.getText()))
        else:
            dec = decode(sentEnt.getText(), int(keyEnt.getText()))
        mainText.setText(dec)
        output = open("decoded.txt","w")
        output.write(dec)
        output.close()
        
    time.sleep(3)#time to read output
    myWin.close()

main()



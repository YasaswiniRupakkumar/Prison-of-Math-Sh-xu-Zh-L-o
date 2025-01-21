#Importing libraries and modules
import random
import sys
import app
from datetime import datetime
from DB import modeData as md
from DB import DataCollection as dc
from TextFile import File_commands as tf
import FileOpenner
from Story import BackStory as bs
from Story import Menu as m
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt




#Data regarding the different modes
def gettingConsole():
    while True:
    
        if not(len(sys.argv)<3):
            print("<-e|-m|-h>")
            break
            
        if len(sys.argv)==2:
            if not(sys.argv[1]=="-e" or sys.argv[1]=="-m" or sys.argv[1]=="-h"):
                print("<-e|-m|-h>")
                break

        if len(sys.argv)==1:
            #mode=None#There is an error here
            return None
        else:
            if sys.argv[1]=="-e":
                return "-e"
            elif sys.argv[1]=="-m":
                return "-m"
            elif sys.argv[1]=="-h":
                return "-h"
    mode=modeSelection()
    return mode


#Question generator
def gameSums(modeKey=None):
    
    modeId, level, numRangeMin, numRange, maxNoOfNums, noOfQs, arithOperands=md.importModeData(modeKey)

    #print(numRange, maxNoOfNums, noOfQs, arithOperands, level)
    
    NumList=[*range(numRangeMin, numRange+1)]
    numberOfDigits=[*range(2, maxNoOfNums+1)]
    aswList=[]
    numList=[]
    operList=[]
    
    for i in range(0, noOfQs):
        
        numSubList=[]
        operSubList=[]
        "assumption: they are randomly selected"
        SelectedNumOfDigits=random.choice(numberOfDigits)
        
        for i in range(0, SelectedNumOfDigits-1):
            random.shuffle(NumList)
            selectedNum=random.choice(NumList)
            numSubList.append(selectedNum)
            selectedOperand=random.choice(arithOperands)
            operSubList.append(selectedOperand)
            #print(selectedNum,selectedOperand, end="")
            
        random.shuffle(NumList)
        selectedNum=random.choice(NumList)
        numSubList.append(selectedNum)
        #print(selectedNum, " = ", end="")
        #while True:
        #    try:
        #        asw=int(input())
        #        break
        #    except KeyboardInterrupt or TypeError:
        #        print("Invalid input")
        #aswList.append(asw)"Use this in the later part"
        numList.append(numSubList)
        operList.append(operSubList)

    questionList=strConcatQuestion(numList, operList)

    

    console = Console()

    for i, question in enumerate(questionList):
        while True:
            try:
                # Display the puzzle title in a styled panel
                console.print(Panel.fit(
                    f"[bold magenta]Mathematical Puzzle {i + 1}[/bold magenta]",
                    style="bold green"
                ))

                # Print the question and take input inline
                asw = int(input(f"{question} "))
                
                # Add the answer to the list and break
                aswList.append(asw)
                break
            except (TypeError, ValueError):
                console.print("[bold red]Invalid Input. Please enter a valid integer.[/bold red]")
            except KeyboardInterrupt:
                console.print("\n[bold red]Input interrupted. Please enter a valid integer.[/bold red]")

            
    #print(f'{modeId}, {aswList}, {numList}, {operList}, {level}, {questionList}')
    return modeId, aswList, numList, operList, level, questionList



#Storing the question in String Format (file writing, console writing, database)
def strConcatQuestion(numList, operList):
    
    questionList=[]
    question=""
    
    for i in range (0, len(operList)):
        printOperList=operList[i].copy()
        printOperList.append(" = ")
        question=""
        #operList[i]=operSubList
        
        for x in range (0, len(printOperList)):
            question+=f"{numList[i][x]} {printOperList[x]} "
            
        questionList.append(question)
        
    return questionList
    

#Calculating the answer according to BODMAS
def calculatingBODMAS(operList, numList):
    #print(operList)
    #print(numList)
    dupOperList=operList.copy()
    dupNumList=numList.copy()
    #print(dupOperList)
    i=0
    
    while i < len(dupOperList):
        if dupOperList[i]=="*":
            x=i
            repNum=dupNumList[x]*dupNumList[x+1]
            del dupOperList[i]
            dupNumList[x]=repNum
            del dupNumList[x+1]
            i-=1
        i+=1
        
    repNum=dupNumList[0]
    
    for i in range(1, len(dupOperList)+1):
        #print(i)
        if dupOperList[i-1]=="+":
            #print(repNum, dupOperList[i-1], " = ", dupNumList[i])
            repNum+=dupNumList[i]
        else:
            #print(repNum, dupOperList[i-1], " = ", dupNumList[i])
            repNum-=dupNumList[i]
        #print(repNum)
            
    asw=repNum
    
    return asw


#Calculating the right asw list for one game play in one session
def findRightAsw(numList, operList):
    
    rightAswList=[]
    
    for i in range(0, len(numList)):
        operators, numbers=operList[i], numList[i]
        rightasw=calculatingBODMAS(operators, numbers)
        rightAswList.append(rightasw)
        
    return rightAswList


#Checking for the right answer and generate the error correcting printing list
def correction(aswList, rightAswList):
    
    aswToShow=[]
    
    for i in range(0, len(aswList)):
        if aswList[i]==rightAswList[i]:
            aswToShow.append("")
        else:
            toShow="Correct answer is : "+str(rightAswList[i])
            aswToShow.append(toShow)
            
    return aswToShow


#Printing the results
def preparingPrintString(aswList, aswToShow, numList, operList, rightAswList, level):

    print("\n")
    
    printString=""
    
    rCount=0
    questionList=strConcatQuestion(numList, operList)
    for i in range(0, len(aswToShow)):
        
        if aswToShow[i]=="":
            mark="✓"
            rCount+=1
        else:
            mark="✕"
        printString+=str(mark)+ "\t"
        thisNumList=numList[i]

        "Printing the questions--- here you can even import the data from the database"
        #questionList=strConcatQuestion(numList, operList)
        printString+=str(questionList[i])
        printString+=str(aswList[i])+'\t'+str(aswToShow[i])+'\n\n'
        
    
    printString+="Total Questions : "+str(len(rightAswList))+'\n'
    printString+="Correct Questions : "+ str(rCount)+'\n'
    markPercent=(rCount*100)/len(rightAswList)
    printString+="Marks : "+str(format(markPercent, '.2f'))+"%"+'\n'
    printString+="Level : "+ level+'\n'

    return printString



console = Console()

def center_text(text, width):
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)


def printingTheResultsConsole(aswList, aswToShow, numList, operList, rightAswList, level):
    rCount = 0
    questionList = strConcatQuestion(numList, operList)

    # Create a table for results
    table = Table(title="[bold red]Puzzle score board[/bold red]", border_style="bold green", show_header=True, header_style="bold green", expand=True)
    table.add_column("Puzzle", justify="left", style="cyan", no_wrap=True)
    table.add_column("Your Solution", justify="center", style="yellow", no_wrap=True)
    table.add_column("Correct Solution", justify="center", style="green", no_wrap=True)
    table.add_column("Outcome", justify="center", style="bold white", no_wrap=True)

    for i in range(len(aswToShow)):
        if aswToShow[i] == "":
            mark = "✓"
            rCount += 1
            result_style = "bold green"
        else:
            mark = "✕"
            result_style = "bold red"

        # Add a row to the table
        table.add_row(
            questionList[i],
            str(aswList[i]),
            str(aswToShow[i]),
            Text(mark, style=result_style)
        )

    # Calculate results
    total_questions = len(rightAswList)
    correct_questions = rCount
    mark_percent = (rCount * 100) / total_questions

    # Create a summary panel
    summary_text = (
            f"[bold yellow]Total number of puzzles:[/bold yellow] {total_questions}\n"
            f"[bold yellow]Correctly solved puzzles:[/bold yellow] {correct_questions}\n"
            f"[bold yellow]Final puzzle quest Mark:[/bold yellow] {format(mark_percent, '.2f')}%\n"
            f"[bold yellow]Puzzle Quest Level:[/bold yellow] {level}"
        )

    summary = Panel(
        Align.center(summary_text, vertical="middle"),
        title="[bold red]Puzzle Quest Summary[/bold red]",
        width=console.width
    )

    # Print the results
    console.print(table)
    console.print(summary)

    # Call the motivation function based on the level
    if level == "demo":
        bs.lineMotivationDemo(mark_percent)
    elif level == "easy":
        bs.lineMotivationEasy(mark_percent)
    elif level == "medium":
        bs.lineMotivationMedium(mark_percent)
    elif level == "hard":
        bs.lineMotivationHard(mark_percent)



def modeSelection():
    
    while True:
        try:
            mode=input("What mode do you prefer : ") or None
            
            if not(mode==None or mode=="-e" or mode=="-m" or mode=="-h"):
                raise ValueError
            
            return mode
        
        except(TypeError, ValueError):
            print("< |-e|-m|-h>")
        except KeyboardInterrupt:
                print("\n< |-e|-m|-h>")



def contSelection():
    
    while True:
        try:
            mgameStatQ=input("Do you want to keep playing (y/n) : ")
            mgameStatQ=mgameStatQ.lower()
            
            if not(mgameStatQ=="y" or mgameStatQ=="n"):
                raise ValueError
            
            return mgameStatQ
        
        except(TypeError, ValueError):
            print("<y|n>")
        except KeyboardInterrupt:
                print("\n<y|n>")


def viweHistorySelection():

    historySelection=0

    
    while True:
        try:
            historySelection=input("Do you want to view past game quests (y/n) : ")
            historySelection=historySelection.lower()
            
            if not(historySelection=="y" or historySelection=="n"):
                raise ValueError

            break
        except(TypeError, ValueError):
            print("<y|n>")
        except KeyboardInterrupt:
                print("\n<y|n>")

    if historySelection=="y":
        
        "This did not exist before, there is an error here as the existance of the history directory was not checked"
        exist=FileOpenner.CheckHistoryDir()
        if exist==False:
            return

        while True:
            try:
                
                viewMethod=input("Do you want to view it in a text file (t) or in a web page (w) (t/w) : ")

                viewMethod=viewMethod.lower()
                
                if not(viewMethod=="t" or viewMethod=="w"):
                    raise ValueError
                break
                
            except(TypeError, ValueError):
                print("<t|w>")
            except KeyboardInterrupt:
                    print("\n<t|w>")

        if viewMethod=="t" :
            FileOpenner.HistoryFileLoc()
        elif viewMethod=="w":
            app.run()
        
        

            
#Main Game
def playGame():

    sesStartTime=datetime.now()
    
    mode=gettingConsole()

    bs.backStory()

    
    
    while True:

        gamePlayStartTime=datetime.now()
        
        "Generating questions and reading input"
        modeId, aswList, numList, operList, level, questionList=gameSums(mode)

        "Preparing answer list"
        rightAswList=findRightAsw(numList, operList)

        "Final mark sheet - answers for wrong qs"
        aswToShow=correction(aswList, rightAswList)

        "Printing complete marksheet"
        printString=preparingPrintString(aswList, aswToShow, numList, operList, rightAswList, level)

        printingTheResultsConsole(aswList, aswToShow, numList, operList, rightAswList, level)

        gamePlayEndTime=datetime.now()

        #gameplayId=md.exportGameplayData(sessionId, modeId, gamePlayStartTime, gamePlayEndTime)

        #md.exportQuestionData(gameplayId, questionList, aswList, rightAswList)

        viweHistorySelection()
        
        "Option to continue the game"
        mgameStatQ=contSelection()
        
        if mgameStatQ=="n":
            modeIdList, gamePlayStartTimeList, gamePlayEndTimeList, questionListList, aswListList, rightAswListList, printStringList=dc.gameplayDataCollection(modeId, gamePlayStartTime, gamePlayEndTime, questionList, aswList, rightAswList, printString)
            bs.selectingSuccessStandard(aswListList, rightAswListList)
            sesEndTime=datetime.now()
            md.exportSessionData(sesStartTime, sesEndTime)
            sessionId=md.importSessionId()
            #gameplayId=md.exportGameplayData(sessionId, modeIdList, gamePlayStartTimeList, gamePlayEndTimeList)
            md.exportGameplayData(sessionId, modeIdList, gamePlayStartTimeList, gamePlayEndTimeList, questionListList, aswListList, rightAswListList)
            #md.exportQuestionData(gameplayId, questionListList, aswListList, rightAswListList)
            tf.textFileHistory(sesStartTime, sessionId, printStringList)
            break;

        dc.gameplayDataCollection(modeId, gamePlayStartTime, gamePlayEndTime, questionList, aswList, rightAswList, printString)
        m.showMenu()
        "Option to select mode"
        mode=modeSelection()


#Running the program
playGame()

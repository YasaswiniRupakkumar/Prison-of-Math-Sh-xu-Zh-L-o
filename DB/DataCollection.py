#Initializing data collection variables
modeIdList=[]
gamePlayStartTimeList=[]
gamePlayEndTimeList=[]
questionListList=[]
aswListList=[]
rightAswListList=[]
printStringList=[]
    
def gameplayDataCollection(modeId, gamePlayStartTime, gamePlayEndTime, questionList, aswList, rightAswList, printString): 

    modeIdList.append(modeId)
    gamePlayStartTimeList.append(gamePlayStartTime)
    gamePlayEndTimeList.append(gamePlayEndTime)
    questionListList.append(questionList)
    aswListList.append(aswList)
    rightAswListList.append(rightAswList)
    printStringList.append(printString)

    #print(f'{modeIdList}\n {gamePlayStartTimeList}\n {gamePlayEndTimeList}\n {questionListList}\n {aswListList}\n {rightAswListList}')

    return modeIdList, gamePlayStartTimeList, gamePlayEndTimeList, questionListList, aswListList, rightAswListList, printStringList

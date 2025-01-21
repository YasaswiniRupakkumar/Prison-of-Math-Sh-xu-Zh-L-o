import mariadb
import sys
from rich.console import Console

# Create a Console instance
console = Console()

# Importing data from mode table
def importModeData(mode):
    if mode is None:
        mode = ""
    
    mode = mode.strip()
    
    conDict = {"host": "localhost", "user": "root", "database": "prisonofmath", "password": ""}

    try:
        # Attempt to connect to the database
        db = mariadb.connect(**conDict)
    except mariadb.Error as e:
        console.print("[bright_red]Sorry! There is an error in your database connection, please check to proceed with the gameplay.[/bright_red]")
        # Uncomment the next line to show error details for debugging
        # print(f"Error details: {e}")
        sys.exit()  # Terminate the program

    cursor = db.cursor()

    query = '''SELECT mode_id, modeName, numRangeMin, numRangeMax, maxNoOfNums, noOfQs, arithOperands
               FROM `mode`
               WHERE modeKey=%s'''
    
    try:
        cursor.execute(query, (mode,))
        data = cursor.fetchall()
    except mariadb.Error as e:
        console.print("[bright_red]Sorry! An error occurred while executing the query.[/bright_red]")
        # Uncomment the next line to show error details for debugging
        # print(f"Error details: {e}")
        db.close()
        sys.exit()  # Terminate the program

    # Extract data
    modeId = data[0][0]
    level = data[0][1]
    numRangeMin = data[0][2]
    numRange = data[0][3]
    maxNoOfNums = data[0][4]
    noOfQs = data[0][5]
    arithOperands = list(map(str.strip, data[0][6].split(',')))

    db.close()

    return modeId, level, numRangeMin, numRange, maxNoOfNums, noOfQs, arithOperands

#Exporting session data
def exportSessionData(sesStartTime, sesEndTime):
    conDict={"host":"localhost", "user":"root", "database":"prisonofmath", "password":""}

    db=mariadb.connect(**conDict)

    cursor=db.cursor()

    #Inserting data into the database
    query='''INSERT INTO session (endTime, startTime)
    VALUES (%s, %s)'''
    record=(sesEndTime, sesStartTime)
    cursor.execute(query, record)

    db.commit()
    
    db.close()

#Importing sessionId of the previous session and returning current
def importSessionId():
    conDict={"host":"localhost", "user":"root", "database":"prisonofmath", "password":""}

    db=mariadb.connect(**conDict)

    cursor=db.cursor()
    
    cursor.execute("SELECT MAX(session_id) FROM `session`;")

    sessionId=cursor.fetchall()
    
    db.close()

    return sessionId[0][0]
    
    
#Exporting gameplay data and question data
def exportGameplayData(sessionId, modeIdList, gamePlayStartTimeList, gamePlayEndTimeList, questionListList, aswListList, rightAswListList):
    conDict={"host":"localhost", "user":"root", "database":"prisonofmath", "password":""}

    db=mariadb.connect(**conDict)

    cursor=db.cursor()

    #Inserting data into the database
    for i in range(0, len(modeIdList)):
        query='''INSERT INTO gameplay (session_id, mode_id, start_time, end_time)
        VALUES (%s, %s, %s, %s)'''
        record=(sessionId, modeIdList[i], gamePlayStartTimeList[i], gamePlayEndTimeList[i])
        cursor.execute(query, record)

        #db.commit()

        cursor.execute("SELECT MAX(gameplay_id) FROM `gameplay`;")

        gameplayId=cursor.fetchall()

        #print(gameplayId)

        gameplayId=gameplayId[0][0]

        for x in range(0, len(aswListList[i])):
            #Inserting data into teh database dynamically (Note:- in '%s', s should be simple)
            query='''INSERT INTO question (gameplay_id, question_text, user_answer, correct_answer)
            VALUES (%s, %s, %s, %s)'''
            record=(gameplayId, questionListList[i][x], aswListList[i][x], rightAswListList[i][x])
            #print(record)
            cursor.execute(query, record)

    db.commit()
    
    db.close()



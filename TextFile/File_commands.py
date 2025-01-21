import os
import datetime
import random

def generateFileName():
    now = datetime.datetime.now()
    date_str = now.strftime('%Y%m%d')
    time_str = now.strftime('%H%M')
    
    while True:
        random_number = random.randint(100, 999)
        file_name = f"{date_str}_{time_str}_{random_number}.txt"
        # Check if the file exists
        if not os.path.exists(file_name):
            return file_name


def textFileHistory(sesStartTime, sessionId, printStringList):
    
    folder_path = "History"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate the full file path
    file_name=generateFileName()
    full_path = os.path.join(folder_path, file_name)
    
    with open(full_path, 'w', encoding="utf-8") as file:
        # Write session details
        file.write(f"Session Date: {sesStartTime.date()}\n")
        file.write(f"Session Time: {sesStartTime.time()}\n")
        file.write(f"Session : {sessionId}\n\n")
        
        # Write each game play
        for printString in printStringList:
            file.write(printString)
            file.write("\n")

    



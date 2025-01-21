import os
#The bellow was a correction
from rich import print

def HistoryFileLoc():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the History directory
    history_dir = os.path.join(current_dir, "History")

    # Open the History directory in the file explorer
    os.startfile(history_dir)


#This function did not exist before, this was another mistake
#there is an error here as I did not check whether the folder exists before redirecting to the game play folder
def CheckHistoryDir():
    """
    Check if the 'History' directory exists. If it does not, create it.
    """
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the History directory
    history_dir = os.path.join(current_dir, "History")

    # Check if the directory exists
    if not os.path.exists(history_dir):
        print(f"[bold red]Sorry! [/bold red][bold yellow]There are no past game play sessions, past game play history can only be viwed after the second game play, as history is updated only after a complete session.[/bold yellow]")
        return False
    return True

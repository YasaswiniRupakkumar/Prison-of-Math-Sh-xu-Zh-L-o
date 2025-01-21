import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def backStory():
    console.print(Panel.fit("[bold yellow]In the Song Dynasty...[/bold yellow]"), style="bold red")
    time.sleep(1)
    console.print("There once lived a warrior called [bold cyan]Shu Yin[/bold cyan]...", style="italic")
    time.sleep(1)
    console.print("He was [bold green]loved by the town folks[/bold green]...")
    time.sleep(0.5)
    console.print("The man of their dreams for all the beauties in town...", style="italic")
    time.sleep(1)
    console.print("[bold cyan]His fame spread[/bold cyan] not just around Shoung Hai but the entire [bold blue]Zhōngguó[/bold blue]...")
    time.sleep(1.5)
    console.print("He was the [bold yellow]general[/bold yellow] of the kingdom of Sòng Cháo...")
    time.sleep(0.5)
    console.print("Had the capability [bold magenta]rescuing the gods from heaven[/bold magenta]...")
    time.sleep(1)
    console.print("[bold red]The great mind but ... hated maths...[/bold red]")
    time.sleep(1)
    console.print("[italic]Now...[/italic]", style="italic bold yellow")
    time.sleep(2)
    console.print("He is given the task to save the emperor Zhao Kuangyin from the dangerous.....", style="bold red")
    time.sleep(4)
    console.print("Prison of Math.........", style="bold red")
    time.sleep(1.5)
    console.print("[bold yellow]Can you help the emperor and Yin out of this misery..?[/bold yellow]")
    time.sleep(2)
    console.print("[bold green]Now fate is in your hands...[/bold green]")
    time.sleep(2.5)
    console.print("[bold magenta]Let’s delve into the Prison of Math: Shùxué Zhī Láo![/bold magenta]")


console = Console()

def center_text(text, width):
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def lineMotivationDemo(grade):
    if grade == 100:
        message = (
            "Amazing! Your skills shine brighter than ever!\n"
            "Shu Yin is impressed, and the emperor’s hope grows with every puzzle you solve."
        )
        console.print(Panel(center_text(message, console.width), style="bold green", padding=(1, 2), width=console.width))
    elif grade > 50:
        message = (
            "Great progress! You're showing the makings of a true hero.\n"
            "Keep going—each answer brings the emperor closer to safety."
        )
        console.print(Panel(center_text(message, console.width), style="bold cyan", padding=(1, 2), width=console.width))
    elif grade > 0:
        message = (
            "You're making strides, but there’s still a journey ahead.\n"
            "Focus and keep trying; Shu Yin believes you can overcome this!"
        )
        console.print(Panel(center_text(message, console.width), style="bold yellow", padding=(1, 2), width=console.width))
    elif grade == 0:
        message = (
            "Don’t worry, brave one! Even the greatest heroes start somewhere.\n"
            "Learn, adapt, and try again—the emperor and Shu Yin are counting on you!"
        )
        console.print(Panel(center_text(message, console.width), style="bold red", padding=(1, 2), width=console.width))

def lineMotivationEasy(grade):
    if grade == 100:
        message = (
            "Tài bàng le! Gàn de hǎo!\n"
            "Your brain is sharp as Shu Yin's blade! The emperor's hope grows stronger with your brilliance!"
        )
        console.print(Panel(center_text(message, console.width), style="bold green", padding=(1, 2), width=console.width))
    elif grade > 50:
        message = (
            "Great work! You're cutting through the puzzles like a seasoned warrior.\n"
            "The emperor can sense your progress—stay sharp!"
        )
        console.print(Panel(center_text(message, console.width), style="bold cyan", padding=(1, 2), width=console.width))
    elif grade > 0:
        message = (
            "You're making progress, but danger looms near!\n"
            "Focus harder, and don't let the Prison of Math hold you back. The emperor is counting on you!"
        )
        console.print(Panel(center_text(message, console.width), style="bold yellow", padding=(1, 2), width=console.width))
    elif grade == 0:
        message = (
            "Don't lose hope, brave one! Even the sharpest warriors stumble.\n"
            "Remember, Shu Yin believes in your strength—try again and rise!"
        )
        console.print(Panel(center_text(message, console.width), style="bold red", padding=(1, 2), width=console.width))

def lineMotivationMedium(grade):
    if grade == 100:
        message = (
            "Incredible! Shu Yin is unstoppable with your wisdom guiding him!\n"
            "The emperor's confidence soars as every puzzle you conquer brings him closer to freedom."
        )
        console.print(Panel(center_text(message, console.width), style="bold green", padding=(1, 2), width=console.width))
    elif grade > 50:
        message = (
            "You're moving through the trials like a determined warrior.\n"
            "The emperor feels the tides of fate shifting in his favor—stay resolute and press on!"
        )
        console.print(Panel(center_text(message, console.width), style="bold cyan", padding=(1, 2), width=console.width))
    elif grade > 0:
        message = (
            "You're holding your ground in this battle of wits, but the danger grows.\n"
            "Steel your mind, and push forward; the emperor's life depends on your success!"
        )
        console.print(Panel(center_text(message, console.width), style="bold yellow", padding=(1, 2), width=console.width))
    elif grade == 0:
        message = (
            "The challenge is fierce, but every warrior has moments of doubt.\n"
            "Remember, the greatest battles are won with perseverance. Try again and show the Prison of Math your strength!"
        )
        console.print(Panel(center_text(message, console.width), style="bold red", padding=(1, 2), width=console.width))

def lineMotivationHard(grade):
    if grade == 100:
        message = (
            "Unbelievable! Your mastery of the impossible rivals the gods themselves!\n"
            "Shu Yin marches forward, fearless and unstoppable, as the emperor’s rescue nears completion."
        )
        console.print(Panel(center_text(message, console.width), style="bold green", padding=(1, 2), width=console.width))
    elif grade > 50:
        message = (
            "The Prison of Math trembles under the might of your intellect.\n"
            "Shu Yin draws courage from your progress, and the emperor clings to hope—victory is within reach!"
        )
        console.print(Panel(center_text(message, console.width), style="bold cyan", padding=(1, 2), width=console.width))
    elif grade > 0:
        message = (
            "Every step forward is a triumph, but the shadows of defeat still linger.\n"
            "Focus your mind, and let your brilliance shine through the darkness. The emperor’s fate is in your hands!"
        )
        console.print(Panel(center_text(message, console.width), style="bold yellow", padding=(1, 2), width=console.width))
    elif grade == 0:
        message = (
            "The challenge is at its peak, but no warrior succeeds without struggle.\n"
            "Even Shu Yin stumbled before rising stronger. Harness your determination, and fight on! The emperor cannot wait forever."
        )
        console.print(Panel(center_text(message, console.width), style="bold red", padding=(1, 2), width=console.width))

def center_text(text, width):
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def selectingSuccessStandard(aswListList, rightAswListList):
    count = 0
    countr = 0
    for x in range(len(aswListList)):
        for y in range(len(aswListList[x])):
            if rightAswListList[x][y] == aswListList[x][y]:
                countr += 1
            count += 1

    success_standard = random.randint(50, 90)
    success = countr >= ((count * success_standard) / 100)

    console.print(
        Panel(
            center_text(f"You are required to solve at least [bold yellow]{success_standard}%[/bold yellow] of puzzles to save the emperor.", console.width),
            title="[bold red]Success Requirement[/bold red]",
            border_style="bold green",
            padding=(1, 2),
            width=console.width
        )
    )

    gameEndPlot(success)

def gameEndPlot(success):
    if success:
        message = (
            "[bold green]Congratulations, brave one![/bold green] The Prison of Math has been conquered.\n"
            "Shu Yin stands tall beside the emperor, who declares with gratitude:\n"
            "'Your brilliance and courage have saved me and the kingdom.\n"
            "The Song Dynasty owes its future to your heroism.'\n\n"
            "[bold yellow]The kingdom rejoices,[/bold yellow] and your name will be remembered for generations!"
        )
        console.print(Panel(center_text(message, console.width), title="[bold yellow]Victory![/bold yellow]", border_style="bold green", padding=(1, 2), width=console.width))
    else:
        message = (
            "[bold red]The Prison of Math proved to be a formidable challenge.[/bold red]\n"
            "Shu Yin, though weary, stands resolute:\n"
            "'A true warrior does not give up. We learn, we adapt, and we rise again!'\n\n"
            "The emperor’s fate still hangs in the balance. Sharpen your wits, and return to face the challenge anew.\n"
            "[bold yellow]The kingdom is counting on you![/bold yellow]"
        )
        console.print(Panel(center_text(message, console.width), title="[bold red]Defeat[/bold red]", border_style="bold yellow", padding=(1, 2), width=console.width))

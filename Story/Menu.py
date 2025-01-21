from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def center_text(text, width):
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def showMenu():
    # Title Panel
    title = Panel.fit(
        center_text(
            "⚔️ [bold yellow]Shùxué Zhī Láo: Prison of Math[/bold yellow] ⚔️\n"
            "[italic]Choose your path wisely, brave warrior![/italic]",
            console.width - 4
        ),
        border_style="bold red",
        padding=(1, 1),
    )
    console.print(title)
    
    # Menu Table
    table = Table(title="[bold green]Game Modes[/bold green]", border_style="bold blue")
    table.add_column("No", justify="center", style="bold yellow")
    table.add_column("Console Command", justify="left", style="cyan")
    table.add_column("Description", justify="left", style="white")
    
    # Adding rows
    table.add_row(
        "1",
        "mathbro",
        "This is the demo mode. Game will display 3 arithmetic questions with additions (+) only.\n"
        "Operands range from 0 to 5."
    )
    table.add_row(
        "2",
        "mathbro -e",
        "This is the easy mode. Game will display 5 arithmetic questions with addition (+) and subtraction (-).\n"
        "Operands range from 0 to 10."
    )
    table.add_row(
        "3",
        "mathbro -m",
        "This is the medium mode. Game will display 10 arithmetic questions with addition (+) and subtraction (-).\n"
        "Operands range from 0 to 10."
    )
    table.add_row(
        "4",
        "mathbro -h",
        "This is the hard mode. Game will display 10 arithmetic questions with addition (+), subtraction (-), and multiplication (*).\n"
        "Operands range from 0 to 20."
    )
    
    console.print(table)
    
    # Footer Panel
    footer = Panel(
        center_text(
            "[bold yellow]Embark on your journey now![/bold yellow]\n"
            "Use the console commands to select a mode and rescue the emperor.\n"
            "[italic]May your mind be as sharp as Shu Yin's blade![/italic]",
            console.width - 4
        ),
        border_style="bold green",
        padding=(1, 1),
    )
    console.print(footer)



from adventure.utils import read_events_from_file
import random

from rich import print


def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')



    print("[bold bright_cyan]You wake up in a dark forest. You can go [green]left[/green] or [yellow]right[/yellow].[/bold bright_cyan]")
    print("[bold]Which direction do you choose?[/bold] ([green]left[/green]/[yellow]right[/yellow]/[purple]exit[/purple])")
    while True:
        choice = input("Which direction do you choose? (left/right/exit): ")
        choice = choice.strip().lower()
        
        if choice == 'exit':
            print("[purple]You decided to exit. Goodbye![/purple]")
            break
        
        result = step(choice, events)





        if choice == "left":
            print(f"[bright_green]{result}[/bright_green]")
        elif choice == "right":
            print(f"[bright_yellow]{result}[/bright_yellow]")
        else:
            print(f"[bright_red]{result}[/bright_red]")
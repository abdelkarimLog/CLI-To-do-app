import typer, json
from rich import print
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)

with open('tasks.json', "r") as f:
    tasks = json.load(f)

def save():
    with open('tasks.json', "w") as f:
        json.dump(tasks, f, indent=2)

@app.command()
def add(task: str):
    """Add a new task"""
    
    tasks.append({"name": task, "is_done": False})
    save()
    print(f"[green]Task added[/green]: {task}")

@app.command()
def done(task_num: int):
    """Mark a task as done"""
    
    try:
        tasks[task_num-1]["is_done"] = True
        print("[green]Task marked as done[/green]")
    except IndexError:
        print("[red]Invalid task number[/red]")
        print("[grey]run [i]python3 main.py [b]list[/b][/i] to see each task with its number[/grey]")
    save()

@app.command()
def delete(task_num: Annotated[int, typer.Argument(help="Task to delete (by number, not name)")]=None, 
           all: Annotated[bool, typer.Option(help="Delete all tasks")]=False):
    """Delete a task by its number"""

    if all:
        tasks.clear()
        print("[red]All tasks were deleted[/red]")
    elif task_num:
        try:
            tasks.pop(task_num-1)
            print("[red]Task deleted[/red]")
        except IndexError:
            print("[red]Invalid task number[/red]")
            print("[grey]run [i]python3 main.py [b]list[/b][/i] to see each task with its number[/grey]")
    else:
        print("No valid option")
    save()

@app.command()
def list():
    """Display all tasks"""
    
    if tasks == []:
        print("No tasks")
    else:
        for num, task in enumerate(tasks, start=1):
            if task["is_done"]:
                color = "green"
                decoration = "strike"
            else:
                color = "yellow"
                decoration = "none"
            print(f"[{color}][{num}] [{decoration}]{task['name']}[/{decoration}][/{color}]")

if __name__ == "__main__":
    app()


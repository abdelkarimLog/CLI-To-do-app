# 📝 CLI To-Do App

A simple command-line todo list manager built with Python using [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).  

› You can make, preview, complete, and delete tasks - all from your terminal ⌨️.

---

## 🛠 Requirements

› Python 3.8+

› Typer

› Rich

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/abdelkarimLog/cli_todo.git
cd cli_todo
```

2. Install Typer (Rich will come with it):
```bash
pip3 install typer
```


## ⚡ Usage

Run with Python:
```bash
python3 main.py --help
```

➕ Add a task:
```bash
python3 main.py add Study
```
```bash
python3 main.py add "Learn Bash"
```

📃 List tasks:
```bash
python3 main.py list
```
📑 List in table view:
```bash
python3 main.py list --table #or -t for short
```

✔️ Mark tasks as done:
```bash
python3 main.py done 1 #choose tasks by their number
```
```bash
python3 main.py done --all #or -a
```

🗑️ Delete tasks
```bash
python3 main.py delete 2 #use --all instead of the number to delete all tasks
```
```bash
python3 main.py delete --all #or -a
```

---

This is a learning / practice project 

More features will be added soon ...

---

## project init

```
$ mkdir pytermgui
$ cd pytermgui/
$ python3 -m venv gui
$ source ./gui/bin/activate
(gui) /pytermgui$ pip list
```

## updating all pip packages

pip list --outdated

### update with grep

pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

### update with awk

pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U

### updage packages with requirements.txt present

pip3 list -o
pip freeze > requirements.txt
pip install -r requirements.txt --upgrade

## md format cheatsheet
>
> <https://www.markdownguide.org/basic-syntax/>

## pytermgui
>
> <https://github.com/bczsalba/pytermgui>

### **IMPORTANT**

install PyYAML
pip3 install PyYAML

## pytermgui moving forward as shade40 project **NO RELEASE YET**
>
> <https://github.com/shade40>

### для понимания Hypermedia As The Engine Of Application State
>
> <https://habr.com/ru/articles/483328/>

## pytermgui refrence with list of gui frameworks
>
> <https://ptg.bczsalba.com/>

## tui framework - BubbleTea
>
> <https://github.com/charmbracelet/bubbletea>

### video tutorial for Building a CLI Kanban Board with Bubble Tea
>
> <https://youtu.be/ZA93qgdLUzM?si=eg_i9FF35EZe9QSh>

## textual TUI python framework
>
> <https://github.com/Textualize/textual>

### updating req... file with textual textual-dev

### following textual tutorial
>
> <https://textual.textualize.io/tutorial/>

### git magic

#### after staging too much and editing out unnecessary files cleaning staging area

git diff --name-only --cached
git restore --staged ./pytermgui/gui/*

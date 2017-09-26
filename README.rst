Kotahi
======

This project allows different board game strategies to be exercised and the results recoded


Useful Resources
====
 - https://en.wikipedia.org/wiki/Template:Monopoly_board_layout
 - http://monopoly.wikia.com/wiki/Game_Board_(UK)
 - http://open-site.org/Games/Board_Games/Monopoly/British_Version/
 - https://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-grid-system.php
 - https://github.com/wbond/pybars3

Memory Jogger
====
Run a local web server in Python 3 like this :
```
    python3 -m http.server
```

Run the job which actually simulates the game player:
```
    python core.py
```

Run the job which produces the visulisation files:
```
python monitormaker.py -i /tmp/tmpnzsw1t1b -o /tmp -t .
```

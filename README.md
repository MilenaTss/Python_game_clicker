Для того чтобы программа могла функционировать необходимо установить необходимую библиотеку
```
pip3 install pygame
```

Для того чтобы запустить игру, необходимо запустить
```
python3 game_clicker.py
```

В данной проекте реализован функционал игры кликер. 
Можно зарабатывать клики, нажимая на пробел. Также можно нажимать на кнопки, которые есть на экране.
Реализованы кнопки, которые отвечают за автоматическое получение кликов.
Если купить какой-либо из этих функционалов, то далее в течение каждой секунды к общему количеству кликов будет прибавляться определённое число.
Для того чтобы создать кнопки был реализован собственный класс Button.
Также есть некая подсветка кнопки, если на неё навести мышкой, чтобы было понятно что эту кнопку можно нажать.

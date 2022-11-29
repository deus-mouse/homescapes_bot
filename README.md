Bot resolving pazzles in game Homescapes (Playrix)


Порядок написания:

1) научиться определять координаты на экране -> coordinates_finder

2) найти центр игрового поля   
   
3) определить область в которой нужно сделать скриншот игрового поля
   
4) сделать скриншот всего экрана. открыть в paint, найти координаты. -> take_screenshot
- найти истинный центр игрового поля = 1763*
- найти размеры одной клетки = 126 пкс

5) нарезать экран на сектора -> cropper

6) создание матрицы -> matrix_setter + find_items
- перебрать нарезки с паттернами. найти совпадения, играя значением threshold
    туториал на youtube
    https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&index=2)
      opencv docs Template Matching = TM_CCOEFF_NORMED
      https://docs.opencv.org/4.5.1/d4/dc6/tutorial_py_template_matching.html
- cv.matchTemplate(img_for_searching, pattern_img, method) чувствителен к глубине цвета (24!/32 бит). 
  Потому что скриншот который делает opencv от 24 битовый, а который делает ОС он 32 битовый.
  Кропы должны бить тех же параметров что и скриншот на котором ищем. 
  Делая скриншот области может получится 32 бита.
  А обрезая скриншот полного экрана можем получить искомы 24 бита.
  
7) определить цели на боковой панели -> find_priority + find_items

8) обнаружить бонусы, цели, пары на поле -> matched


   
TODO в методе matched мы ищем пары. но почему только по горизонтали? возможно так же стоит применить reverse_matrix.
Разобрать как работает searching_best_match
# TODO вспомнить алгоритм поиска совпадений в методах find_five, / find_square / find_three
# TODO описать метод определения совпадения на 5 по вертикали. find_five_matches_in_column (для приоритетных и нет)
# TODO find_three_matches_in_column понять как работает. Возможно нужно разделить на поиск по приоритетам и нет.

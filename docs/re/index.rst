Конспекты по регулярным выражениями
===================================

* . - точка, любой символ

* \\w - буква, цифра, подчеркивание [0-9A-Za-z]

* \\W - не буква, не цифра, не подчеркивание [^0-9A-Za-z]

* \\d - цифра, [0-9]

* \\D - не цифра, [^0-9]

* \\s - пробельный символ (пробел, табуляция)

* \\S - не пробельный символ (не пробел, не табуляция)

* \\b - начало или конец слова

* \\B - не начало и не конец слова

* ^, \\A - начало строки

* $, \\Z - конец строки

* [символы] - любой символ из набора

* [^символы] - отрицание, любой символ из набора не должен быть

* символА|символБ - вертикальная черта, или

* \* - предыдущий символ может быть сколько угодно или вовсе не быть

* \+ - предыдущий символ должен быть один или несколько

* ? - предыдущий символ должен быть один раз или не быть вовсе

* {3} - предыдущий символ должен присуствовать 3 раза

* {3,5} - предыдущий символ должен присуствовать от 3 до 5 раз

* () - скобки используются для группировки

.. code-block:: py

    # цвет 16-х
    "#[0-9A-Fa-f]"

    # число от 13 до 16
    "[0-9]{13,16}"

    # веб адрес
    "^(http|https|ftp)\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]*"
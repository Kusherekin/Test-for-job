Разработать программу с графическим интерфейсом на языке Python которая может считывать данные из именованной разделяемой памяти (named shared memory) и способна их визуализировать.

Графический интерфейс программы состоит из следующих элементов:
1. Имя разделяемой памяти (строка) - далее NAME
2. Количество данных для отображения (целое число) - далее LEN
3. Смещение данных для чтения (целое число) - далее SHIFT
4. Тип данных одного элемента (выбор из двух вариантов int или float). Int целочисленное 32битное число, float стандартное число с плавющей точкой 32 бита (стандарт  IEEE-754). Int и float соотвествуют данным типам в С++
5. Окно для вывода графика
6. Кнопка для запуска

При нажатии на кнопку (п.6 интерфейса) программа должна считать из разделяемой памяти с именем "NAME" LEN элементов смещенных относительно начала памяти на SHIFT элементов. 
Тип одного элемента указан в п.4 интерфейса. Далее считанные данные необходимо отобразить в виде графика.
Значения абсцисс (по оси X) - индекс элемента (порядковый номер). Значения ординат (по оси Y) - значения элемента.

Операционная система из семейства Unix. Ограничений на использование сторонних библиотек нет.

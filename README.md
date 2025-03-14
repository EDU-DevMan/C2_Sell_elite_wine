# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код проекта:

[C2_Sell_elite_wine](https://github.com/EDU-DevMan/C2_Sell_elite_wine.git)

- Создайте виртальное окружение для вашего проекта.

`Пример для  Windows`

```python3 -m venv --copies C:\DevMan\Course_2\Layout\venv_wine\```

, где `venv_wine` - папка виртуального окружения

- Активируйте ваше виртальное окружение:

```..\venv_wine\Scripts\activate.bat```

- Важно, если используется VS Code, активацию виртального окружения можно провести следующим образом:

Нажать `ctrl+shift+p`, из списка Выбрать:

 `Python Selected Interpreter > Create Virtusl Enviroment > venv >`
 
 `> Find C:\DevMan\Course_2\Layout\venv_wine\Scripts\python.exe`

Обязательно перезапустить терминал 

`Terminal > New Terminal`

[`Пример для Windows`](https://dvmn.org/encyclopedia/pip/pip_virtualenv/)

- Установите зависимости

`Пример для Windows`

```py -m pip install -r requirements.txt```

[`Пример для Unix/macOS`](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

- В корне проекта создайте файл `.env`, и заведите переменную `FILE_PATH=`, 
в этой переменной будет храниться путь к файлу (.xlsx) с набором данных о вине `FILE_PATH='wine.xlsx'`

Пример файла с набором данных в формате .xlsx:

|Категория|Название|Сорт|Цена|Картинка|Акция|
| --- | --- | --- | --- | --- | --- |
|Белые вина|Белая леди|Дамский пальчик|399|belaya_ledi.png|Выгодное предложение|
|Напитки|Коньяк классический|`-`|350|konyak_klassicheskyi.png|
|Белые вина|Ркацители|Ркацители|499|rkaciteli.png|
|Красные вина|Черный лекарь|Качич|399|chernyi_lekar.png|
|Красные вина|Хванчкара|Александраули|550|hvanchkara.png|
|Белые вина| Кокур| Кокур|450|kokur.png|
|Красные вина| Киндзмараули|Саперави|550|kindzmarauli.png|
|Напитки|Чача|`-`|299|chacha.png|Выгодное предложение|
|Напитки|Коньяк кизиловый|`-`|350|konyak_kizilovyi.png|

- Запустить сайт можно командой 

```python3 main.py```

В таком случае, сайт запуститься с демо-данными из файла wine.xlsx

- Вы можете не указывать имя файла в переменной `FILE_PATH`,
а указать имя и путь при запуске программы, для этого воспользуйтесь подсказкой -h (--help):

```python3 main.py -h```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

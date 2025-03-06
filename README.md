# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код

- В корне проекта создать файл `.env`, завести переменную `FILE_PATH=`, 
в этой переменной будет храниться путь к файлу (.xlsx) с набором данных о вине 
(файл для проекта предоставляется - `wine3.xlsx`).

Пример: `FILE_PATH='wine3.xlsx'`

Пример файла с набором данных в формате .xlsx:

|Категория|Название|Сорт|Цена|Картинка|Акция|
| --- | --- | --- | --- | --- | --- |
|`Белые вина`|Белая леди|Дамский пальчик|399|belaya_ledi.png|Выгодное предложение|
|`Напитки`|Коньяк классический|`-`|350|konyak_klassicheskyi.png|
|`Белые вина`|Ркацители|Ркацители|499|rkaciteli.png|
|`Красные вина`|Черный лекарь|Качич|399|chernyi_lekar.png|
|`Красные вина`|Хванчкара|Александраули|550|hvanchkara.png|
|`Белые вина`| Кокур| Кокур|450|kokur.png|
|`Красные вина`| Киндзмараули|Саперави|550|kindzmarauli.png|
|`Напитки`|Чача|`-`|299|chacha.png|Выгодное предложение|
|`Напитки`|Коньяк кизиловый|`-`|350|konyak_kizilovyi.png|

- Запустить сайт можно командой 

```python3 main.py```
В таком случае, сайт запуститься с демо-данными из файла wine3.xlsx

- Для запуска, с указанием своего файла достаточно вывести подсказку с примером -h (--help):

```python3 main.py -h```


- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

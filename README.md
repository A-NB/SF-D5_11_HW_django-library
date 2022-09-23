## <center>Небольшой учебный django-проект сайта библиотеки</center>
Сайт использует данные из базы `db.sqlite3`, которая содержит информацию о книгах, их авторах, издательствах и читателях, записанных в библиотеку. Описание моделей ***Book***, ***Author***, ***Publisher***, ***Reader*** и ***BookReader*** содержится в файле **models.py**.

Навигация по сайту осуществляется при помощи меню в верхней части каждой страницы.
На главной странице сайта (за её отображение отвечает шаблон **index.html**), доступной обычно по адресу `http://localhost:8000/`, отбражается приветствие.

Страница `books/` (**books_list.html**) содержит полную информацию обо всех книгах библиотеки, включая количество имеющихся в наличии копий (количество копий можно изменять при помощи кнопок &#8722; и &#43;). При этом программно реализован алгоритм, при котором количество копий книги не может быть меньше 1, а также меньше количества копий, которые находятся у читателей на руках.

На странице `authors/` (**authors_list.html**) отображается информация об авторах книг, представленных в библиотеке.

На странице `publishers/` (**publishers_list.html**) отображается информация о издательствах, чьи книги представлены в библиотеке.

На странице `readers/` (**readers_list.html**) отображается информация о читателях, записанных в библиотеку.

Все названия книг, имена авторов, названия издательств и имена читателей кликабельны и позволяют перейти на страницу просмотра детальной информации по адресу вида `xxx/<int:pk>/` (шаблоны вида **xxx_detail.html**) либо на страницу редактирования записи по адресу `xxx/<int:pk>/edit/` (**form_edit.html**).

Реализована возможность наполнения БД пользователем путём выбора пункта меню вида ***"+книга"*** . При этом осуществляется переход на адрес вида `xxx/create/` (используется тот же шаблон, что и при редактировании **form_edit.html**).

В базе данных в ознакомительных целях созданы два пользователя - администратор с правами superuser (`admin` с паролем `1`) и обычный пользователь (`user_1` с паролем `password_1`). Разграничение прав пользователей (в нашем случае - предоставление прав пользователю `user_1`) сделано через административную панель стандартным способом путём добавления пользователя в группу &#171;Общая&#187;. Разрешения для группы предварительно настроены также через панель администратора. Панель администратора доступна по адресу `admin/`.

Работа через админку с объектами, описание которых содержат модели ***Book***, ***Author***, ***Publisher***, ***Reader*** и ***BookReader***, организована в виде отдельных панелей администратора. Пользователи с правами администратора могут создавать, удалять, модифицировать (изменять значения полей, устанавливать или удалять связи между моделями) объекты базы данных, используя функционал административной панели. Для остальных пользователей доступны действия в соответствии с заданными администратором разрешениями.

В учебных целях описанные выше действия (за исключением удаления объектов БД) может совершить любой пользователь в полном объёме, не заходя в административную панель, используя меню либо элементы управления на странице. 

Для стилизации элементов страниц используется bootstrap, который подключён стандартным способом в теге `<link>` базового шаблона **base.html**. Остальные шаблоны наследуют шаблон **base.html** (в котором также содержится блок меню) при помощи тега `{% extends 'base.html' %}`.

### <center>Установка и запуск</center>
Склонируйте репозиторий на локальный компьютер, введя в консоли команду:
```
git clone https://github.com/A-NB/SF-D5_11_HW_django-library.git
```
Затем необходимо перейти в папку проекта и создать для него виртуальное окружение:
```
cd SF-D5_11_HW_django-library
python -m venv venv
```
Дождитесь завершения операции, после чего активируйте виртуальное окружение:
```
.\venv\Scripts\activate
```
Зависимости, необходимые для проекта, установите, используя файл `requirements.txt`:
```
pip install -r requirements.txt
```
После установки зависимостей запустите сервер командой:
```
python manage.py runserver
```
При успехе Вы увидите в консоли сообщение:
```
Starting development server at http://127.0.0.1:8000/
```
Если порт :8000 занят другим приложением, номер порта может отличаться. Перейдите в своём браузере по адресу, указанному в консоли, чтобы попасть на главную страницу сайта.

<!-- *Поскольку проект **учебный**, в настройках приложения в файле **settings.py** содержится в открытом виде SECRET_KEY, а параметр DEBUG = True.* -->
<p align="center">
    <img src="https://i.ibb.co/mhKtxrW/1-Qx47-Gs7-VSo.png" alt="ProjectLogo" width="300">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/framework-Django%204.2.5-green" alt="Django">
   <img src="https://img.shields.io/badge/framework-torch%202.0.1-orange" alt="torch">
   <img src="https://img.shields.io/badge/library-numpy%201.25.2-blue" alt="numpy">
</p>

## О проекте

Данное веб-приложение генерирует три варианта продолжения вашего текста и позволяет сохранить результат на Ваше устройство в текстовом файле. Список языков, которые нейронная сеть способна воспринимать:

- русский
- английский (в планах)
- французский (в планах)
- испанский (в планах)

### Состав

Состав приложения:

- Страница "Главная"
- Форма feedback'а
- Страница "FAQs"
- База данных
- Нейронная сеть

#### Страница "Главная"

Главная страница содержит шапку сайта, анимированное название "3Paths", поле для ввода текста (максимальная длина текста - 400 символов), кнопку для генерации текста и форму для отправки feedback. После нажатия на кнопку "Сгенерировать текст" появляются три варианта продолжения текста и кнопка "Сохранить результаты", которая позволяет сохранить результаты в txt-файле и скачать их на Ваше устройство.

#### Форма feedback'а

Форма содержит поля для ввода имени, Email-адресса и комментария. В форме проводится проверка на заполнение всех полей, а также на корректность введённого Email-адресса. При нажатии на кнопку "Отправить" данные отправляются в базу данных SQLite.

#### Страница "FAQs"

Данная страница содержит ответы на часто задаваемые вопросы.

#### База данных

Для доступа к базе данных перейдите по адресу: http://127.0.0.1:8000/admin  
Данные для входа:

- имя пользователя: **admin**
- пароль: **admin**

База данных содержит одну таблицу "Обратная связь". Таблица содержит имена пользователей, Email-адресса и их комментарии. Имеется одна строчка с тестовыми данными.

#### Нейронная сеть

Нейросеть обучена на наборе данных из фрагментов текстов русской литературы различных авторов. Длины текстов находятся в диапазоне от 2000 до 2100 символов. Всего выборка содержит 65845 уникальных текстов. Набор данных доступен по следующему адресу: https://www.kaggle.com/datasets/tatianafofanova/authorstexts?select=val_data.csv  
Нейросеть может воспринимать текст, введенный с ошибками при условии, что текст на русском языке.

## Установка

Клонируйте репозиторий в PyCharm. Откройте терминал (Alt + F12) и пропишите следующие команды:

- pip install -r requirements.txt
- cd Web
- python manage.py runserver

После выполнения данных команд у Вас запустится сервер по адресу: http://127.0.0.1:8000/

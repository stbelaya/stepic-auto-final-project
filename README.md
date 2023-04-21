# stepic-auto-final-project
Final project for Selenium AT course

Добро пожаловать в мой репозиторий с финальным проектом курса Автоматизация тестирования с помощью Selenium и Python! 

Ссылка на курс: https://stepik.org/course/575/

В данном курсе используются:

<img src="https://user-images.githubusercontent.com/125028645/231808880-8c86c010-a3f9-48d0-ac04-f059afa9efc8.png" width="40" title="Python"><img src="https://user-images.githubusercontent.com/125028645/231809848-5fc170d4-2ed5-488b-8d46-b957abc3ee99.png" width="40" title="Selenium"><img src="https://user-images.githubusercontent.com/125028645/231810036-e2c7d063-3355-4c3f-9fd4-eb1f1fbd5bc7.png" width="40" title="PyCharm">

**Instructions:**

По умолчанию для запускаемых тестов выставлен английский язык.

Установить зависимости можно с помощью команды:

`pip install -r requirements.txt`

Запустить все тесты с маркой need_review можно с помощью команды: 

`pytest -v --tb=line -m need_review`

Запустить все тесты для main page можно с помощью команды: 

`pytest -v --tb=line test_main_page.py`

Запустить все тесты для product page можно с помощью команды: 

`pytest -v --tb=line test_product_page.py`

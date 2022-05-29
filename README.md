# Создание задач в Bitrix24 за 3 дня до государственных праздников

Написать программу(скрипт) на языке Python, которая будет создавать задачи в системе Bitrix24 
за три дня до наступления государственных праздников.

## Использование Docker

### Установка Docker.
Установите Docker, используя инструкции с официального сайта:
* для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
* для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

* скачайте проект к себе на компьютер 
```bash
    git clone https://github.com/ivbbest/create_task_bitrix24.git
```
* Установите Docker 
```bash
    https://www.docker.com/get-started
```

## Настройка виртуального окружения 

* установите виртуальное окружение
```bash
    python -m venv .venv
```
* Активируйте виртуальное окружение:

### Windows
```bash
    source .venv/Scripts/activate
```

### Linux
```bash
    source .venv/bin/activate
```


* Создайте Docker образ
```bash
    docker build -t test .
```

* Запустите контейнер из образа
```bash
    docker run --name test -it test
```

* В новом терминале выполните команду:
```bash
    docker exec -it test bash
```
* это запустит терминал внутри контейнера

* Запустите  скрипт
```bash
    python tasks_bitrix24.py
```
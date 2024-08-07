# Интернет-магазин на Django

## Описание проекта

В эпоху цифровых технологий интернет-магазины стали неотъемлемой частью торговли, предоставляя пользователям удобный способ приобретения товаров онлайн. Цель данного дипломного проекта — разработка функционального и удобного интернет-магазина с использованием фреймворка Django. Интернет-магазин будет включать все основные функции, такие как каталог товаров, корзина, оформление заказа, и панель администратора для управления магазином.

## Основные функции

- **Каталог товаров:** Просмотр и фильтрация товаров по категориям.
- **Страница товара:** Подробная информация о товаре, включая описание, цену и наличие на складе.
- **Корзина:** Добавление и удаление товаров, просмотр общей стоимости.
- **Оформление заказа:** Ввод данных для доставки и оплата.
- **Панель администратора:** Управление товарами, заказами и пользователями.

## Установка и запуск проекта

Следуйте этим шагам для установки и запуска проекта на вашем локальном компьютере.

### Предварительные требования

- Python 3.11
- pip (Python package installer)
- virtualenv (рекомендуется)

### Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/Pavel7334/click_shop.git
   cd your-repo-name

2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # для Windows используйте `venv\Scripts\activate`

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt   
   
4. **Выполните миграции базы данных:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
5. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver
   
## Завершение

Мы создали этот интернет-магазин на Django с любовью к деталям и стремлением к идеальной функциональности. Надеемся, что наш проект вдохновит вас на создание собственных инновационных решений в мире электронной коммерции.

Если у вас есть вопросы, предложения или вы хотите внести свой вклад в развитие проекта, не стесняйтесь связаться с нами. Мы всегда готовы к диалогу и новым идеям!

Спасибо, что выбрали наш интернет-магазин. Приятных покупок!
from data import db_session
from data.news import News
from data.users import User

db_session.global_init("blogs.sqlite")

session = db_session.create_session()

user_1 = User()
user_1.name = "Пользователь 1"
user_1.about = "биография пользователя 1"
user_1.email = "user_1@email.ru"
session.add(user_1)

user_2 = User()
user_2.name = "Пользователь 2"
user_2.about = "биография пользователя 2"
user_2.email = "user_2@email.ru"
session.add(user_2)

session.commit()

print('Запрос одного (произвольного) пользователя:')
user = session.query(User).first()
print(user.name)

print('Запрос всех пользователей:')
for user in session.query(User).all():
    print(user.name)

print('Пользователи с id > 1 И email НЕ содержащим символ "1":')
for user in session.query(User).filter(User.id > 1, User.email.notilike("%1%")):
    print(user.name)

news_1 = News(title="Первая новость", content="Привет блог!",
            user=user_1, is_private=False)
session.add(news_1)

news_2 = News(title="Вторая новость", content="Уже вторая запись!",
            user=user_1, is_private=False)
session.add(news_2)

session.commit()

news_3 = News(title="Личная запись", content="Эта запись личная",
            is_private=True)
user.news.append(news_3)

session.commit()
from faker import Faker

fake = Faker("ru_RU")

#Создаёт уникальные данные нового курьера
def register_new_courier():
    fake = Faker("ru_RU")
    return {
        "login": fake.unique.user_name(),
        "password": fake.password(length=12),
        "firstName": fake.first_name()
    }

#Создаёт данные курьера без обязательного логина
def register_new_courier_without_login():
    courier = register_new_courier()
    courier.pop("login")
    return courier

#Создаёт данные курьера без обязательного пароля
def register_new_courier_without_password():
    courier = register_new_courier()
    courier.pop("password")
    return courier

#Генерирует данные для создания заказа
def generate_order_data():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address().replace("\n", ", "),
        "metroStation": fake.random_int(min=1, max=10),
        "phone": f"+7{fake.numerify(text='9#########')}",
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.future_date().isoformat(),
        "comment": fake.sentence(nb_words=4),
        "color": ["BLACK"]
    }
class Users:
    WRONG_PASSWORD = "WrongPassword123"
    NONEXISTENT_LOGIN = "courier_does_not_exist_987654"

class Messages:
    COURIER_ALREADY_EXISTS = "Этот логин уже используется. Попробуйте другой."
    COURIER_DATA_REQUIRED = "Недостаточно данных для создания учетной записи"
    LOGIN_NOT_FOUND = "Учетная запись не найдена"
    LOGIN_DATA_REQUIRED = "Недостаточно данных для входа"

class Orders:
    COLORS = [
        [],
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ]
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def is_valid_email(self):
        """Проверяет, содержит ли email @ и ."""
        return '@' in self.email and '.' in self.email

    def change_username(self, new_name):
        """
        Меняет имя пользователя.

        Args:
            new_name: новое имя (минимум 3 символа)

        Raises:
            ValueError: если новое имя короче 3 символов
        """
        if len(new_name) < 3:
            raise ValueError("Username must be at least 3 characters long")
        self.username = new_name
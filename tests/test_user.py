import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Настройка тестового пользователя"""
        self.valid_user = User("testuser", "test@example.com")
        self.invalid_user = User("baduser", "bademail")

    def test_valid_email(self):
        """Тест валидного email"""
        self.assertTrue(self.valid_user.is_valid_email())

    def test_invalid_email(self):
        """Тест невалидного email"""
        self.assertFalse(self.invalid_user.is_valid_email())

    def test_change_username_valid(self):
        """Тест корректной смены имени"""
        new_name = "newuser"
        self.valid_user.change_username(new_name)
        self.assertEqual(self.valid_user.username, new_name)

    def test_change_username_too_short(self):
        """Тест смены имени на слишком короткое"""
        with self.assertRaises(ValueError):
            self.valid_user.change_username("ab")

    def test_change_username_exact_min_length(self):
        """Тест смены имени на минимально допустимую длину"""
        min_length_name = "abc"
        self.valid_user.change_username(min_length_name)
        self.assertEqual(self.valid_user.username, min_length_name)


if __name__ == "__main__":
    unittest.main()
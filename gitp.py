import string


class CaesarsCipher:
    """
    Класс, реализующий шифр Цезаря для шифрования и расшифровки.
    """

    def __init__(self):
        # Определяем алфавит для шифрования
        self.alphabet = string.ascii_letters + string.digits + " !?."

    def decrypt(self, message: str, key: int) -> str:
        """
        Расшифровывает сообщение с использованием алгоритма шифра Цезаря.

        Args:
            message (str): Зашифрованное сообщение.
            key (int): Ключ для расшифровки.

        Returns:
            str: Расшифрованное сообщение.
        """
        decrypted = []
        for char in message:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - key) % len(self.alphabet)
                decrypted.append(self.alphabet[index])
            else:
                decrypted.append(char)
        return ''.join(decrypted)

    def encrypt(self, message: str, key: int) -> str:
        """
        Шифрует сообщение с использованием алгоритма шифра Цезаря.

        Args:
            message (str): Исходное сообщение.
            key (int): Ключ для шифрования.

        Returns:
            str: Зашифрованное сообщение.
        """
        encrypted = []
        for char in message:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + key) % len(self.alphabet)
                encrypted.append(self.alphabet[index])
            else:
                encrypted.append(char)
        return ''.join(encrypted)


def save_to_file(filepath: str, content: str) -> None:
    """
    Сохраняет переданный контент в указанный файл.

    Args:
        filepath (str): Путь к файлу.
        content (str): Контент для записи.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Результаты успешно сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")


if __name__ == "__main__":
    cipher = CaesarsCipher()
    encrypted_message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    results = []

    # Перебор ключей
    for key in range(len(string.ascii_letters + string.digits + " !?.") + 1):
        result = cipher.decrypt(encrypted_message, key)
        print(f"{key}: {result}")  # Вывод ключей и соответствующих сообщений

    # Условие: если результат выглядит осмысленно,
    # например, содержит часть ожидаемого текста,
    # можно вручную добавить проверку. Здесь же
    # просто добавим последний результат:
        if " " in result:  # Пример проверки, можно добавить точное условие
            final_key = key
            final_message = result

    # Финальный вывод (по результатам последнего найденного ключа):
    print(f"\nПодобранный ключ: {final_key}")
    print(f"Расшифрованное сообщение: {final_message}")

    # Запрос пути к файлу у пользователя
    file_path = input("Введите путь для сохранения результатов: ").strip()
    save_to_file(file_path, '\n'.join(results))

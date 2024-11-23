import unittest
from gitp import CaesarsCipher



class TestCaesarsCipher(unittest.TestCase):

    def test_encrypt(self):
        cipher = CaesarsCipher()
        original_message = "The vacation was a success"
        key = 3
        encrypted_message = "Wkh.ydfdwlrq.zdv.d.vxffhvv"
        self.assertEqual(cipher.encrypt(original_message, key), encrypted_message)

    def test_decrypt(self):
        cipher = CaesarsCipher()
        encrypted_message = "Wkh.ydfdwlrq.zdv.d.vxffhvv"
        original_message = "The vacation was a success"
        key = 3
        self.assertEqual(cipher.decrypt(encrypted_message, key), original_message)

    def test_no_change_with_key_zero(self):
        cipher = CaesarsCipher()
        original_message = "Hello World"
        self.assertEqual(cipher.encrypt(original_message, 0), original_message)
        self.assertEqual(cipher.decrypt(original_message, 0), original_message)


if __name__ == "__main__":
    unittest.main()

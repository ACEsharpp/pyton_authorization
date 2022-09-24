import unittest
from enter import menu, Users_auth,User_lib
#to be honest i dont inderstand how to test
class TestEnterUser(unittest.TestCase):
    def test_menu(self):
        self.assertEqual(menu("1"),Users_auth.user_reg())
        self.assertEqual(menu("2"),Users_auth.user_reg())
        self.assertEqual(menu("3"),Users_auth.user_reg())

    def test_hash_password(self, hash_password=None):
        self.assertTrue(hash(hash_password))
    iin_person=User_lib("030726551436")
    if User_lib.test_username(iin_person,"IIN"):
        print("test pass")
    else:
        print("test fail")
def main():
    TestEnterUser()


if __name__ == "__main__":
    main()




import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class TestLogin(unittest.TestCase):
    def setUp(self) :
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_sukses_login(self):
        #step
        browser = self.browser   
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("putristp23@gmai.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("Stp123")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click

        #Validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_gagal_login_empty(self):
        #step
        browser = self.browser   
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click

        #Validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_c_gagal_login(self):
        #step
        browser = self.browser   
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("putristp23@gmai.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click

        #Validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def signup_a(self):
        #step
        browser = self.browser   
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"name_register").send_keys("seokjin")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("seokjin23@gmai.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("Jin123")
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click

        #Validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'Created user!')

    def tearDown(self): 
        self.browser.close() 



if __name__ == "__main__": 
    unittest.main()

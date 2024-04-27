import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_succ_registration(driver):
    driver.get('http://localhost:5000/register')
    driver.find_element(By.Name, 'username').send_keys('test_new')
    driver.find_element(By.Name, 'password').send_keys('pass_new')
    driver.find_element(By.XPATH, '//button').click()
    WebDriverWait(driver, 10).until(driver.find_element(By.ID, 'msg').text == 'SUCCESS')
    assert 'test successfully' in driver.page_source

def test_faild_registration(driver):
    driver.get('http://localhost:5000/register')
    driver.find_element(By.Name, 'username').send_keys('test_new')
    driver.find_element(By.Name, 'password').send_keys('pass_new')
    driver.find_element(By.XPATH, '//button').click()
    WebDriverWait(driver, 10).until(driver.find_element_by_id('msg').text == 'Username aleady exist')
    assert 'test falid' in driver.page_source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Constants
URL = "https://ecspro-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
driver.maximize_window()

def login():
    """Logs into the application."""
    driver.get(URL)
    time.sleep(3)  # Wait for page to load

    driver.find_element(By.ID, "email").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(5)  # Wait for login process

def logout():
    """Logs out from the application."""
    driver.find_element(By.ID, "logout_button").click()
    time.sleep(3)

def add_package():
    """Adds a package with a random dimension."""
    login()

    # Navigate to Package Types
    driver.find_element(By.XPATH, "//a[contains(text(),'Package Types')]").click()
    time.sleep(3)

    # Click 'Add Manually' button
    driver.find_element(By.XPATH, "//button[contains(text(),'Add Manually')]").click()
    time.sleep(2)

    # Fill package details
    first_name = "John"  # Replace with dynamic values if needed
    last_name = "Doe"
    package_name = f"{first_name}_{last_name}"
    dimension = random.randint(1, 19)

    driver.find_element(By.ID, "package_name").send_keys(package_name)
    driver.find_element(By.ID, "dimension").send_keys(str(dimension))
    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
    time.sleep(3)  # Wait for the package to be added

    logout()
    return package_name  # Return package name for deletion later

def delete_package(package_name):
    """Deletes the package."""
    login()

    # Navigate to Package Types
    driver.find_element(By.XPATH, "//a[contains(text(),'Package Types')]").click()
    time.sleep(3)

    # Find and delete package
    package_xpath = f"//td[contains(text(), '{package_name}')]/following-sibling::td/button[contains(text(),'Delete')]"
    driver.find_element(By.XPATH, package_xpath).click()
    time.sleep(2)

    # Confirm delete action
    driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
    time.sleep(3)

    logout()

# Run tests
package_name = add_package()
delete_package(package_name)

# Close browser
driver.quit()

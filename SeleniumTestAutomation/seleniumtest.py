from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_remove_cart():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")  # Yerel sunucu URL'si

    try:
        # 'Sepete Ekle'
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        )
        add_to_cart_button.click()

        # Kontrol et
        cart_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cart-item"))
        )
        assert cart_item.text.startswith("Laptop"), "Sepet öğesi eklenemedi!"

        # 'Çıkar' Ekle
        remove_button = cart_item.find_element(By.TAG_NAME, "button")
        remove_button.click()

        # Sepetin boş olduğunu kontrol et
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.ID, "cart-item"))
        )
        print("Test Başarılı!")
    finally:
        driver.quit()

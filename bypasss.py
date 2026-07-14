# bypass.py
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_driver_autorizado(url, timeout=15):
    """
    Inicializa un navegador undetected_chromedriver, navega a la URL,
    resuelve el reto de Cloudflare si aparece y devuelve el objeto driver listo.
    """
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    
    # Inicializar driver
    driver = uc.Chrome(options=options)
    # Solución definitiva para evitar WinError 6 al cerrar
    driver.keep_user_data_dir = True 

    try:
        print(f"Abriendo: {url}")
        driver.get(url)
        
        print("Esperando a que cargue la protección de Cloudflare...")
        wait = WebDriverWait(driver, timeout)
        
        try:
            # 1. Localizar el iframe de Cloudflare Turnstile
            iframe_selector = (By.CSS_SELECTOR, "iframe[src*='challenges.cloudflare.com']")
            cf_iframe = wait.until(EC.presence_of_element_located(iframe_selector))
            
            print("Iframe de Cloudflare detectado. Cambiando de contexto...")
            driver.switch_to.frame(cf_iframe)
            
            # 2. Esperar el checkbox
            checkbox_selector = (By.CSS_SELECTOR, "label.cb-lb, input[type='checkbox']")
            checkbox = wait.until(EC.element_to_be_clickable(checkbox_selector))
            
            print("Checkbox interactuable encontrado. Simulando click...")
            time.sleep(2)
            checkbox.click()
            print("Click en el checkbox realizado con éxito.")
            
            driver.switch_to.default_content()
            
        except Exception:
            # Si no hay iframe o se resuelve solo
            driver.switch_to.default_content()
            print("El reto de Cloudflare no requirió interacción manual (se resolvió solo).")

        # Esperar a que cargue el body de la página destino
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        print("¡Acceso concedido exitosamente!")
        return driver

    except Exception as e:
        print(f"Error durante el bypass: {e}")
        try:
            driver.quit()
        except:
            pass
        raise e
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Définir les sélecteurs de bouton
xpathButton = '//*[@class="cky-btn cky-btn-accept"]'  # XPATH avec guillemets correctement échappés
nameButton = ''
idButton =''

url = 'https://www.luminis-films.com/?gad_source=1&gclid=EAIaIQobChMI2q2N4q6zhwMV-FhBAh0GaAuvEAAYASAAEgLBYvD_BwE'

response = requests.get(url)

try:
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')  # Utiliser response.content et spécifier le parser
        print("Page chargée et analysée avec succès")

        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        run = webdriver.Chrome(service=service, options=options)
        run.get(url)
        print("Navigateur lancé et page chargée")

        # Attendre que le bouton soit présent
        wait = WebDriverWait(run, 3)

        if not nameButton and not idButton :
            button = wait.until(EC.presence_of_element_located((By.XPATH, xpathButton)))
        elif not xpathButton and not idButton : 
            button = wait.until(EC.presence_of_element_located((By.NAME, xpathButton)))
        else : 
            button = wait.until(EC.presence_of_element_located((By.ID, xpathButton)))
        
        if button:
            print("Bouton trouvé")
            button.click()
            print("Bouton cliqué")
        else:
            print("Bouton non trouvé")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête HTTP : {e}")
except Exception as e:
    print(f"Quelque chose a mal tourné : {e}")

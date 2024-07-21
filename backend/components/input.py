from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Définir les sélecteurs de lien
xpathInput = '//*[@class="recherche_champ"]'  # XPATH avec guillemets correctement échappés
idInput = ''
nameInput = ''

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

        # Attendre que le input soit cliquable
        wait = WebDriverWait(run, 10)

        if not idInput and not nameInput:  
            input = wait.until(EC.element_to_be_clickable((By.XPATH, xpathInput)))
        elif not idInput and not xpathInput:
            input = wait.until(EC.element_to_be_clickable((By.NAME, xpathInput)))
        else : 
            input = wait.until(EC.element_to_be_clickable((By.ID, idInput)))

        
        if input:
            print("input trouvé")
            # Faire défiler jusqu'à l'élément
            run.execute_script("arguments[0].scrollIntoView();", input)
            # Utiliser JavaScript pour cliquer sur l'élément
            run.execute_script("arguments[0].click();", input)
            print("input cliqué")
        else:
            print("input non trouvé")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête HTTP : {e}")
except Exception as e:
    print(f"Quelque chose a mal tourné : {e}")

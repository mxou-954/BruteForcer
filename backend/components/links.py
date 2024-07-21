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
xpathLink = '//*[@class="sal-animate"]'  # XPATH avec guillemets correctement échappés
idLink = ''
nameLink = ''

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

        # Attendre que le lien soit cliquable
        wait = WebDriverWait(run, 10)

        if not idLink and not nameLink:  
            lien = wait.until(EC.element_to_be_clickable((By.XPATH, xpathLink)))
        elif not idLink and not xpathLink:
            lien = wait.until(EC.element_to_be_clickable((By.NAME, xpathLink)))
        else : 
            lien = wait.until(EC.element_to_be_clickable((By.ID, idLink)))

        
        if lien:
            print("Lien trouvé")
            # Faire défiler jusqu'à l'élément
            run.execute_script("arguments[0].scrollIntoView();", lien)
            # Utiliser JavaScript pour cliquer sur l'élément
            run.execute_script("arguments[0].click();", lien)
            print("Lien cliqué")
        else:
            print("Lien non trouvé")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête HTTP : {e}")
except Exception as e:
    print(f"Quelque chose a mal tourné : {e}")


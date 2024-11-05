import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Predvolená URL a časový interval
default_url = 'https://open.spotify.com/embed/episode/03zjfbCqATVp3Iwko9dNyE?utm_source=generator&t=1'
default_interval = 30  # minúty

# Dotaz na URL od operátora s predvolenou hodnotou
spotify_url = input(f"Zadajte URL epizódy Spotify (predvolená: {default_url}): ") or default_url

# Dotaz na časový interval od operátora s predvolenou hodnotou
try:
    interval = int(input(f"Zadajte interval (v minútach) pre spustenie (predvolený: {default_interval} min): ") or default_interval)
except ValueError:
    print(f"Neplatný vstup, používa sa predvolený interval {default_interval} minút.")
    interval = default_interval

def play_spotify_in_incognito(url, interval):
    # Nastavenie možností pre Chrome, aby sa otvoril v inkognito režime
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Inicializácia Chrome driveru (predpokladá sa, že chromedriver je v PATH)
    driver = webdriver.Chrome(options=chrome_options)

    # Otvorenie URL Spotify
    driver.get(url)
    print(f"Otvorená epizóda Spotify: {url}")

    try:
        # Počkáme na tlačidlo Play a klikneme naň
        play_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='play-pause-button']"))
        )
        play_button.click()
        print("Kliknuté na tlačidlo Play.")
    except Exception as e:
        print(f"Tlačidlo Play sa nenašlo alebo automatické spustenie zlyhalo: {e}")

    # Čaká na zadaný interval (v sekundách)
    time.sleep(interval * 60)

    # Zavrie aktuálne okno
    driver.quit()

# Neustále spúšťanie zadanej URL
while True:
    play_spotify_in_incognito(spotify_url, interval)
    print("Reštartovanie prehrávania od začiatku...")

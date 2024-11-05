import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Spotify URL to play
spotify_url = 'https://open.spotify.com/embed/episode/03zjfbCqATVp3Iwko9dNyE?utm_source=generator&t=1'

def play_spotify_in_incognito(url):
    # Set up Chrome options to open in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Initialize Chrome driver (assumes chromedriver is in PATH)
    driver = webdriver.Chrome(options=chrome_options)

    # Open the Spotify URL
    driver.get(url)
    print(f"Opening Spotify episode: {url}")

    try:
        # Wait for the Play button and click it
        play_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='play-pause-button']"))
        )
        play_button.click()
        print("Play button clicked.")
    except Exception as e:
        print(f"Play button not found or auto-play failed: {e}")

    # Wait for 35 minutes (35 * 60 seconds)
    time.sleep(35 * 60)

    # Close the current session
    driver.quit()

# Continuously play the specified Spotify URL
while True:
    play_spotify_in_incognito(spotify_url)
    print("Restarting playback from the beginning...")

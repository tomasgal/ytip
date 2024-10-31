def play_video_in_incognito(video_url):
    # Set up Chrome options to open in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Specify the path to ChromeDriver using Service
    chrome_service = Service(r'C:\chromedriver\chromedriver.exe')

    # Initialize Chrome driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Open the video URL
    driver.get(video_url)
    print(f"Playing video: {video_url}")

    try:
        # Wait for the cookie banner and click "Prijať všetko" if it appears
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.='Prijať všetko']"))
        )
        accept_button.click()
        print("Cookies accepted.")
    except:
        print("No cookie banner found or auto-accept failed.")

    # Wait for 35 minutes (35 * 60 seconds)
    time.sleep(35 * 60)

    # Close the current session
    driver.quit()

# ytip : YouTube Video Auto-Play Script with Cookie Acceptance

This Python script automates the process of opening YouTube videos in an incognito Chrome browser, accepting the cookie banner (in Slovak), and playing each video for a specified duration. It loops through a list of video URLs, restarting the playlist after each cycle.

## Features

- Opens videos in an incognito Chrome browser window
- Automatically clicks the "Prijať všetko" button to accept cookies on YouTube
- Plays each video for 35 minutes before moving to the next
- Loops through the provided list of YouTube URLs indefinitely

## Requirements

- Python 3.7+
- Selenium package for Python
- Chrome browser and the matching version of ChromeDriver

## Installation

1. **Clone the repository** or download the script file.
2. **Install Selenium** by running:
   ```bash
   pip install selenium

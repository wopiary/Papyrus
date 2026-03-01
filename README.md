Papyrus is a lightweight Python utility designed to streamline the process of finding and downloading PDF versions of your favorite books.

	Disclaimer: This tool does not own or host any of the materials provided. Papyrus is a scraping utility that aggregates 	publicly available links from the web for research and personal use.
=====================================
:: 🛠 Prerequisites ::
To ensure Papyrus runs smoothly, you’ll need to have the following installed on your system:
-Python 3.x: Ensure Python is added to your system PATH during installation.
-Google Chrome: (Required for the Selenium WebDriver).
-Essential Libraries
	The tool relies on || Selenium, BeautifulSoup4, and Curses ||. You can install all dependencies at once by running the following 	command in your terminal
		Installation Guide:
		Bash
		pip install selenium beautifulsoup4 windows-curses
		(Note: windows-curses is required specifically for Windows users; Linux/Mac users generally have curses built-in.)
=====================================
:: 🚀 Getting Started  ::
Follow these steps to get Papyrus up and running:
Download the Project: Download the repository as a ZIP file and extract it to your preferred location.
Open in Editor: Launch the extracted folder in VSCode (or your preferred IDE).
Open Terminal: * In VSCode, go to Terminal > New Terminal.
Alternatively, use your operating system's native Terminal/Command Prompt and navigate to the folder.
Run the Tool: Execute the script using:
	Bash
	python run_papyrus.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def fetch_case_data(case_type, case_number, filing_year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    html = ""
    parsed_data = None

    try:
        driver.get(url)
        print("✅ Step 1: Opened eCourts home")
        time.sleep(5)

        # Step 2: Click 'District Court Services'
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "District Court Services"))
        ).click()
        print("✅ Step 2: Clicked District Court Services")
        time.sleep(5)

        # Step 3: Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        print("✅ Step 3: Switched to new tab")

        # Step 4: Click on 'Case Status'
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Case Status"))
        ).click()
        print("✅ Step 4: Clicked Case Status")
        time.sleep(5)

        # Optional: Click 'By Case Number' tab if not selected by default
        WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "By Case Number"))
).click()
        print("✅ Step 4.1: Clicked on 'By Case Number' tab")
        time.sleep(5)

        # Step 5: Fill in form fields
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "ds_caseType"))
        ).send_keys(case_type)
        driver.find_element(By.NAME, "ds_caseNumber").send_keys(case_number)
        driver.find_element(By.NAME, "ds_caseYear").send_keys(filing_year)
        print("✅ Step 5: Form fields filled")

        print("🧠 Please solve the CAPTCHA manually.")
        input("Press Enter here after solving CAPTCHA and clicking Search...")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table"))
        )
        print("✅ Step 6: Results loaded")

        # Parsing...
        html = driver.page_source
        # [ ... continue with BeautifulSoup ... ]

    except Exception as e:
        print("❌ Error occurred during scraping:", e)

    finally:
        time.sleep(40)
        driver.quit()
        return html, parsed_data

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
from selenium.webdriver.common.keys import Keys
import urllib.parse
import webbrowser
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse, parse_qs



columns = ['Carte', 'Date exp', 'CVV2', 'mot de passe', 'Statut']

# Manually enter the data (as a list of lists, each sublist is a row)
data = [
    ['6280580610061011', '01/25', '341', '123456', 'Valide'],
    ['6280581110006712', '01/25', '757', '123456', 'TEMPRORARY BLOCK'],
    ['6280581110006316', '01/25', '902', '123456', 'LOST'],
    ['6280581110006415', '01/25', '296', '123456', 'STOLEN'],
    ['6280581110006613', '01/25', '649', '123456', 'Saisie erronée de Date d’expiration'],
    ['6280581110003927', '01/25', '834', '123456', 'Carte n’existe plus sur le serveur de l’émetteur AUTORISEUR'],
    ['6280580610061219', '01/25', '760', '123456', 'Plafond Carte Dépassé'],
    ['6280580610061110', '01/25', '410', '123456', 'solde Carte insuffisant'],
    ['6280581110006514', '01/25', '526', '123456', 'Erronée du CVV2'],
    ['6280580610061318', '01/25', '406', '666666', 'Dépassement Nb autorisé des PASSWORD (3 codes faux)'],
    ['6280581110007017', '01/25', '517', '123456', 'Carte Non Autorisée pour le Service Paiement en ligne'],
    ['6280581110007116', '01/25', '790', '123456', 'Carte Non Active et valide pour le Service Paiement en ligne'],
    ['6280581110007215', '01/25', '776', '123456', 'Carte Non Acceptée par le commerçant (Négative CGW)'],
    ['6280581110007314', '01/25', '541', '123456', 'Dépassement Montant Plafond Terminal / TRX (MAX FLOOR LMT / AMT'],
    ['6394131100000417', '06/20', '214', '123456', 'carte expirée'],
]
df = pd.DataFrame(data, columns=columns)
df[['month', 'year']] = df['Date exp'].str.split('/', expand=True)

# Convert 'month' and 'year' columns to integer types if needed
df['month'] = df['month'].astype(int)
df['year'] = df['year'].astype(int)
df.drop(columns=['Date exp'], inplace=True)

###################################################


# Function to check for the presence of any keyword
def contains_keywords(page_source, keywords):
    for keyword in keywords:
        if re.search(keyword, page_source, re.IGNORECASE):
            return True
        return False

def is_https(driver, url):
    try:
        driver.get(url)
        return driver.current_url.startswith('https://')
    except WebDriverException as e:
        print(f"An error occurred: {e}")
        return False


driver = webdriver.Chrome()
url = "https://naviguih.com/SignIn"

if is_https(driver, url):
    print(f"The site {url} uses HTTPS.")

else:
    print(f"The site {url} does not use HTTPS or could not be accessed.")

# Path to the ChromeDriver executable
service = Service(executable_path="chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the page you want to scrape
driver.get("https://www.naviguih.com/SignIn")


driver.maximize_window()


time.sleep(5)

email_input = driver.find_element(By.ID, "email")  # Replace with actual field name
password_input = driver.find_element(By.ID, "password")  # Replace with actual field name

#Fill in the login credentials
email_input.send_keys('anis.cheklat@satim.dz')
password_input.send_keys('Anis.Cheklat123@')
password_input.send_keys(Keys.RETURN)

time.sleep(5)


driver.get("https://www.naviguih.com/plans")

time.sleep(5)
pyautogui.moveTo(850, 680)
pyautogui.scroll(-800)

time.sleep(1)

pyautogui.moveTo(850, 680)

time.sleep(1)

pyautogui.click()

time.sleep(1)




# Wait for a certain element or the whole page to load completely (adjust timeout if needed)
try:
    # Adjust the selector below based on a reliable element on the page to wait for
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))  # Example: wait for the body tag to load
    )

    # Once the page is fully loaded, print the page source (HTML)
    page_source = driver.page_source

except Exception as e:
    print(f"Error: {e}")

finally:
    #Close the browser
    driver.quit()


# Open Chrome and navigate to the login page
webbrowser.open('https://www.naviguih.com/SignIn')
time.sleep(3)  # Wait for the browser to load

# Move to the email input field and type email (you need to replace with actual coordinates)
email_field_coords = (1175, 502)  # Use pyautogui.position() to get these coordinates

pyautogui.click(email_field_coords)

# Copy email address to the clipboard
pyperclip.copy('anis.cheklat@satim.dz')
# Paste it using pyautogui
pyautogui.hotkey('ctrl', 'v')  # Pasting from clipboard

time.sleep(1)

# Move to the password input field and type password (you need to replace with actual coordinates)
password_field_coords = (1190, 625)  # Use pyautogui.position() to get these coordinates
pyautogui.click(password_field_coords)

# Copy email address to the clipboard
pyperclip.copy('Anis.Cheklat123@')
# Paste it using pyautogui
pyautogui.hotkey('ctrl', 'v')  # Pasting from clipboard

time.sleep(1)

# Press Enter to submit the form
pyautogui.press('enter')
time.sleep(5)


for i in range(15):
    webbrowser.open('https://www.naviguih.com/plans')

    # Wait for the page to load (Adjust this delay based on your internet speed)
    time.sleep(3)

    pyautogui.moveTo(850, 680)
    pyautogui.scroll(-800)

    time.sleep(1)

    pyautogui.moveTo(932, 608)

    time.sleep(1)

    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(850, 680)
    pyautogui.scroll(-2300)

    pyautogui.moveTo(510,400)

    pyautogui.click()
    time.sleep(5)



    # List of keywords for CIB and EDAHABIA
    card_keywords = [
        'CIB','EDAHABIA'
    ]

    # List of keywords for terms and conditions and privacy policy
    logo_keywords = [
        r'\bcib_logo?\b',
        r'\bCIB\s+LOGO\b'
    ]

    # List of keywords for terms and conditions and privacy policy
    terms_keywords = [
        r'\bterms?\s+and\s+conditions?\b',
        r'\bprivacy\s+policy\b',
        r'\buser\s+agreement\b',
        r'\bterms\s+of\s+service\b',
        r'\baccept\s+the\s+terms\b'
    ]
    # List of keywords for terms and conditions and privacy policy
    captcha_keywords = [
        r'\bLemin?',
        r'\bCapsolver?',
        r'\bYandex\s+SmartCaptcha\b',
        r'\bAmazon\s+CAPTCHA\b',
        r'\bCloudflare?',
        r'\bGoogle\s+reCAPTCHA\b',
        r'\bhCaptcha?',
        r'\bArkose\s+Labs\b',
        r'\bBotDetect\s+Captcha\b','cloudflare'
    ]


    # Check for Terms and Conditions or similar agreements
    terms_condition_present = contains_keywords(page_source, terms_keywords)
    captcha_present = contains_keywords(page_source, captcha_keywords)
    card_selected_present = contains_keywords(page_source,card_keywords)
    CIB_LOGO_present = contains_keywords(page_source,logo_keywords)


    if card_selected_present:
        print("CID AND/OR EDAHABIA Selected Condition Exists")
    else:
        print("CID AND/OR EDAHABIA Condition Does Not Exists")

    if CIB_LOGO_present:
        print("CID LOGO Condition Exists")
    else:
        print("CID LOGO Condition Does Not Exists")

    if terms_condition_present:
        print("terms and conditions exist!")
    else:
        print("terms and conditions do not exist..")

    if captcha_present:
        print("Captcha Exists!")
    else:
        print("Captcha Does Not exist...")



    pyautogui.moveTo(760, 900, duration=2)
    pyautogui.click()
    time.sleep(2)

    for _ in range(4):
        pyautogui.press('tab')
        time.sleep(0.1)  # Slight delay between presses

    pyautogui.press('space')

    for _ in range(2):
        pyautogui.press('tab')
        time.sleep(0.1)  # Slight delay between presses

    pyautogui.press('space')

    ##########################################################################################################

    time.sleep(6)
    pyautogui.hotkey('ctrl', 'l')  # This usually selects the URL bar
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait a moment for the clipboard to update
    payment_url = pyperclip.paste()

    pyautogui.moveTo(100,280)
    pyautogui.click()


    # Set up Chrome WebDriver
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)

#payment_url = 'https://test.satim.dz/payment/merchants/merchant1/payment_en.html?mdOrder=iR5bwd3ho94PLIAAE5H7'

# Open the website
    driver.get(payment_url)

    # Extract data from the first row of the DataFrame
    card = df.iloc[i]
    card_number = card['Carte']
    cvv2 = card['CVV2']
    name = 'TEEST ZEEEEST'
    month = card['month']  # Assuming 1 for January, 12 for December
    year = card['year'] + 2000  # Adjusting year as per the requirement
    password = card['mot de passe']

    # Wait for elements to load and fill the form
    card_number_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'iPAN'))
    )
    card_number_field.send_keys(card_number)

    driver.find_element(By.ID, 'iCVC').send_keys(cvv2)
    driver.find_element(By.ID, 'iTEXT').send_keys(name)

    # Handle the month dropdown selection by index
    month_dropdown = Select(driver.find_element(By.ID, 'month'))
    month_dropdown.select_by_index(month - 1)  # month is 1-indexed, Select uses 0-index

    # Handle the year dropdown selection
    year_dropdown = Select(driver.find_element(By.ID, 'year'))
    year_dropdown.select_by_value(str(year))  # Select the year by value, e.g., '2024'

    # Submit the form
    driver.find_element(By.ID, 'buttonPayment').click()

    password_field = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.NAME, 'j_idt39'))
    )

    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)


    time.sleep(15)

    page_source2 = driver.page_source
    print(page_source2)

# List of keywords for terms and conditions and privacy policy
print_keywords = [
    'print'
]

download_keywords = [
    'Download'
]


email_keywords = [
    'email'
]


# Function to check for the presence of any keyword
def contains_keywords(page_source, keywords):
    for keyword in keywords:
        if re.search(keyword, page_source, re.IGNORECASE):
            return True
    return False

# Check for Terms and Conditions or similar agreements
print_present = contains_keywords(page_source, print_keywords)
download_present = contains_keywords(page_source, download_keywords)
email_present = contains_keywords(page_source,email_keywords)


if print_present:
    print("Print Option Condition Exists")
else:
    print("Print Option Condition Does Not Exists")
    

    

if download_present:
    print("Download Option Condition Exists")
else:
    print("Download Option Condition Does Not Exists")
    

    

if email_present:
    print("Send Via Email Option Condition Exists")
else:
    print("Send Via Email Option Condition Does Not Exists")

if is_https(driver, url):
    print(f"The site {url} uses HTTPS.")

else:
    print(f"The site {url} does not use HTTPS or could not be accessed.")
    
    # Close the browser
    driver.quit()       

##### Response treatment from SATIM [get JSON Packet] code: READY.   Tested: Not Yet  #######


# from urllib.parse import urlparse, parse_qs
# import requests

# current_url = driver.current_url

# parsed_url = urlparse(current_url)
# order_id = parse_qs(parsed_url.query).get('orderId', [None])[0]  # Extract 'orderId' from the query string

# if order_id:
#     # Construct the confirmation URL
#     confirmation_url = f'https://test.satim.dz/payment/rest/confirmOrder.do?language=EN&orderId={order_id}&password=satim120&userName=SAT2408280995'

# Send a GET request to fetch the JSON response
#     response = requests.get(confirmation_url)

#     if response.status_code == 200:
#         # Convert the JSON response to a Python dictionary
#         confirmation_data = response.json()
#         print(confirmation_data)  # Display the JSON data or use it in your program
#     else:
#         print(f"Failed to fetch confirmation. Status code: {response.status_code}")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

#Datasheet settings:

df=pd.read_excel('ZEYAN CHECKED.xlsx')
dfs=df.drop(columns=['ADDRESS','Unnamed: 0','CITY','PHONE NUMBER'])

# Setup
options = Options()
options.add_argument("--disable-notifications")  # ✅ prevent popup
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    # service=Service(ChromeDriverManager().install()),
    options=options
)

# 🚀 Step 1: Go to login page
driver.get("https://dashboard.tms.partners/#/")

wait = WebDriverWait(driver, 30)


username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys("msmrichard@gmail.com")

password_input = wait.until(EC.presence_of_element_located((By.ID, "pwd")))
password_input.send_keys("MSMAgent593%")

# 🚀 Step 4: Click Sign In button
driver.find_element(By.CLASS_NAME, "btn-safespace").click()

# 🚀 Step 5: Optional wait to confirm login success
# time.sleep(10)

print("✅ Logged in successfully")

# driver.save_screenshot("after_login.png")
# print("📸 Screenshot saved after login.")

# Wait for and click the "Create case" button by text

# wait=WebDriverWait(driver,30)
# try:
#     create_case_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create case')]"))
#     )
#     create_case_button.click()
#     print("✅ 'Create case' button clicked.")
# except Exception as e:
#     print("❌ Failed to click 'Create case' button:", e)

# Wait for and click the "Create case" button

wait = WebDriverWait(driver,60)

try:
    create_case_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[8]/div[2]/div/div[2]/div[1]/div[2]/button"))
    )
    create_case_button.click()
    print("✅ 'Create case' button clicked.")
except Exception as e:
    print("❌ Failed to click 'Create case' button:", e)
    # driver.save_screenshot("error_create_case.png")



# # ✅ Step 1: Click the value container to focus the dropdown
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sp-select__value-container"))).click()

# # ✅ Step 2: Find the input field and type
# dropdown_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-8-input")))
# dropdown_input.send_keys("Genetics")  # 🔁 change to your option
# dropdown_input.send_keys(Keys.ENTER)

# print("✅ Selected business.")

# # For Vertical dropdown (react-select-9-input)
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sp-select__value-container"))).click()
# vertical_input = wait.until(EC.presence_of_element_located((By.ID, "react-select-9-input")))
# vertical_input.send_keys("Genetic Testing")  # change as needed
# vertical_input.send_keys(Keys.ENTER)

# print("✅ Selected vertical.")



# from selenium.webdriver.common.keys import Keys

# # --- STEP 1: Find and click Business dropdown ---
# containers = wait.until(EC.presence_of_all_elements_located(
#     (By.CSS_SELECTOR, ".sp-select__value-container")
# ))

# containers[0].click()  # Business dropdown
# print("🔽 Clicked Business dropdown")

# # --- STEP 2: Wait and Click specific Business option ---
# business_option = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//div[contains(@class, 'sp-select__option') and text()='Genetics']")
# ))
# business_option.click()
# print("✅ Business selected: Genetics")

# # --- STEP 3: Click Vertical dropdown ---
# containers[1].click()  # Vertical dropdown
# print("🔽 Clicked Vertical dropdown")

# # --- STEP 4: Wait and Click specific Vertical option ---
# vertical_option = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//div[contains(@class, 'sp-select__option') and text()='Genetic Testing']")
# ))
# vertical_option.click()
# print("✅ Vertical selected: Genetic Testing")


# 🚀 Step: Click the business dropdown input field
business_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-8-input")))
business_input.send_keys("Genetics")  # ⬅️ Replace with actual visible option text
business_input.send_keys(Keys.ENTER)
print('✅ Business selected')


# 🚀 Step: Click the vertical dropdown
vertical_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-9-input")))
vertical_input.send_keys("Genetic Testing")  # ⬅️ Replace with actual visible option text
vertical_input.send_keys(Keys.ENTER)
print('✅ Vertical selected')


# # Click pen icon
# pen_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'fa-pen')]")))
# pen_icon.click()

# # Update the agent name
# agent_input = wait.until(EC.element_to_be_clickable((By.ID, "sales_agent_name")))
# agent_input.clear()
# agent_input.send_keys("Richard Test")  # Change name here
# print('✅ Agent selected')

# # ✅ 1. Click the pen icon (SVG)
# pen_icon = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//svg[contains(@class, 'fa-pen')]"))
# )
# pen_icon.click()
# print("✅ Pen icon clicked")

# # ✅ 2. Wait until the input field appears
# agent_input = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.ID, "sales_agent_name"))
# )

# # ✅ 3. Clear the existing name and type a new one
# agent_input.clear()
# agent_input.send_keys("Test Agent")
# print("✅ Agent name changed to 'Test Agent'")


# # STEP 1: Click the "Test Type" dropdown container (visible part)
# dropdowns = WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "sp-select__value-container"))
# )
# dropdowns[2].click()  # Assuming this is the 3rd select box (after Business and Vertical)

# # STEP 2: Wait for dropdown menu to appear and select an option
# test_type_option = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'PCR')]"))  # Change to your value
# )
# test_type_option.click()

# print("✅ Selected test type: PCR")

# time.sleep(5)

# # STEP: Select Test Type using input ID (react-select-11-input)
# test_type_input = WebDriverWait(driver, 40).until(
#     EC.presence_of_element_located((By.ID, "react-select-11-input"))
# )
# test_type_input.send_keys("Immunodeficiency")  # 🔁 Replace "PCR" with your actual test type
# test_type_input.send_keys(Keys.ENTER)
# print("✅ Test Type selected successfully.")

# Step 1: Type into the select input
test_type_input = WebDriverWait(driver, 60).until(  #wait is 60 bcz it can take soome time to find immunodeficiency
    EC.presence_of_element_located((By.ID, "react-select-11-input"))
)
test_type_input.clear()
test_type_input.send_keys("Immunodeficiency")
# Step 2: Wait for the dropdown option to appear
dropdown_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'select__option') and text()='Immunodeficiency']"))
)
# Step 3: Click the option directly
dropdown_option.click()
print("✅ Test Type selected successfully.")

# time.sleep(5)

# # STEP: Select Lab using input ID (react-select-13-input)
# lab_input = WebDriverWait(driver, 25).until(
#     EC.presence_of_element_located((By.ID, "react-select-12-input"))
# )
# lab_input.send_keys("Immunology - Precision Genetics")  
# lab_input.send_keys(Keys.ENTER)

# print("✅ Lab selected successfully.")

# Type in the Lab input
lab_input = WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.ID, "react-select-12-input"))
)
lab_input.clear()
lab_input.send_keys("Immunology - Precision Genetics")
# Wait for the dropdown to show up and click
dropdown_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//div[contains(@class, 'select__option') and text()='Immunology - Precision Genetics']"
    ))
)
dropdown_option.click()
print("✅ Lab selected successfully.")


# STEP: Select First name using input ID 
fname_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "eu9k5i-patient_first_name"))
)

fname_input.send_keys("Sandi")  
fname_input.send_keys(Keys.ENTER)

print("✅ F name entered successfully.")


# STEP: Select Last name using input ID 
lname_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "emb0a8-patient_last_name"))
)
lname_input.send_keys("Haberland")  
lname_input.send_keys(Keys.ENTER)
print("✅ L name entered successfully.")

# # Wait for the DOB input to be visible
# dob_input = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text'].form-control"))
# )
# # Clear existing value if needed
# dob_input.click()
# dob_input.send_keys(Keys.CONTROL + "a")
# dob_input.send_keys(Keys.BACKSPACE)
# # Send the date (check format needed by your form: "MM/DD/YYYY" or "YYYY-MM-DD")
# dob_input.send_keys("01/01/1990")  # Change to desired date
# dob_input.send_keys(Keys.ENTER)
# print("✅ Date of Birth entered successfully.")

# # Wait until DOB input is clickable
# dob_input = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text'].form-control"))
# )
# # Click and clear if necessary
# dob_input.click()
# # dob_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
# # ✅ Send MMDDYYYY — slashes will be auto-added
# dob_input.send_keys("01011990")  # for January 1, 1990
# # Optional: press Enter to close calendar
# dob_input.send_keys(Keys.ENTER)
# print("✅ Date of Birth entered successfully.")

# # Wait for the date input
# dob_input = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[8]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div[1]/div/input[2]"))
# )
# # Click, clear and send date
# dob_input.click()
# dob_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
# dob_input.send_keys("01011990")  # MMDDYYYY (slashes may auto-fill)
# dob_input.send_keys(Keys.ENTER)
# print("✅ DOB entered.")

# STEP 1: Wait for the correct DOB field
dob_input = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='e45d6bf']/div[1]/div/input[2]"))
)
# STEP 2: Click to focus the field
dob_input.click()
# one='2/1/1944'
# x,y,z=one.split('/')
# if len(x)!=2:
#     x='0'+x
# if len(y)!=2:
#     y='0'+y
# print(y)    
# ones=x+'/'+y+'/'+z
# print(ones)
one = '4/26/1954'
x, y, z = one.split('/')
x = x.zfill(2)
y = y.zfill(2)
ones = f"{x}/{y}/{z}"
print(ones)
# STEP 3: Clear existing text and enter DOB
#dob_input.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)  #no need to clear existing if there isnt .right ?HAHA
dob_input.send_keys(ones)  # MMDDYYYY (auto adds slashes)
dob_input.send_keys(Keys.TAB)  # or Keys.ENTER
print("✅ DOB filled successfully.")

# # STEP: Select Patient MI using input ID 
# pmi_input = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "eo348c7-patient_mi"))
# )
# pmi_input.send_keys("5.4")  
# pmi_input.send_keys(Keys.ENTER)
# print("✅ Patient M.I entered successfully.")


st1=93422
if len(str(st1))==4:
    st1=str(st1)+'12345'
elif len(str(st1))==5:
    st1=str(st1)+'1234'    
# STEP: Select Zip code using input ID 
pmi_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "esclpyj-patient_zip_code"))
)
pmi_input.send_keys(st1)  
pmi_input.send_keys(Keys.ENTER)
print("✅ Zip code entered successfully.")


# STEP: Select Patient State using input ID 
pmi_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "emef2hq-patient_state"))
)
pmi_input.send_keys("CA")  
pmi_input.send_keys(Keys.ENTER)
print("✅ Patient State entered successfully.")

# # STEP: Select "Medicare" radio button for Patient Primary Insurance
# medicare_radio = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.ID, "ediqf1-eloc86n--Medicare"))
# )
# medicare_radio.click()
# print("✅ Medicare radio button clicked via JavaScript.")

# medicare_radio2= WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "ediqf1-eloc86n--Medicare"))
# )
# medicare_radio2.click()
# print("✅ Medicare radio button clicked via JavaScript.")

# medicare_label = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//label[@for='ediqf1-eloc86n--Medicare']"))
# )
# medicare_label.click()
# print("✅ Clicked on the 'Medicare' label instead.")

# medicare_label = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='e2onqa-eloc86n--Medicare']/parent::label"))
# )
# medicare_label.click()
# print("✅ Clicked 'Medicare' by selecting its label.")

# medicare_label = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='e2onqa-eloc86n--Medicare']/parent::label"))
# )
# driver.execute_script("arguments[0].scrollIntoView(true);", medicare_label)
# medicare_label.click()

# medicare_radio = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='e2onqa-eloc86n--Medicare']"))
# )
# driver.execute_script("arguments[0].scrollIntoView(true);", medicare_radio)
# driver.execute_script("arguments[0].click();", medicare_radio)
# print("✅ Clicked 'Medicare' using ID XPath and JavaScript.")

# # Find the element that has visible text "Medicare"
# medicare_button = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.XPATH, "//*[text()='Medicare']"))
# )
# medicare_button.click()
# print("✅ Clicked visible element labeled 'Medicare'.")

# # Click the closest ancestor with a role or class that behaves like a button
# medicare_button = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@id='e2onqa-eloc86n--Medicare']/ancestor::label"))
# )
# medicare_button.click()
# print("✅ Clicked Medicare via its ancestor label.")

# Locate the "Medicare" radio button via value, just like Tricare
medicare_radio = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='Medicare']"))
)
# Click it using JavaScript
driver.execute_script("arguments[0].click();", medicare_radio)
print("✅ Selected 'Medicare' radio option via JavaScript.")


# # STEP: Select Patient primary insurance using input ID 
# pmi_input = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "ex83gsp-patient_primary_name"))
# )
# pmi_input.send_keys("Yes")  
# pmi_input.send_keys(Keys.ENTER)
# print("✅ Patient Primary insurance entered successfully.")


# STEP: Select Patient primary insurance ID /policy no. using input ID 
pmi_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "eadrxvn-patient_primary_insurance_id"))
)
pmi_input.send_keys("4DM5K34JU73")  
pmi_input.send_keys(Keys.ENTER)
print("✅ Patient Primary insurance ID entered successfully.")


# # STEP: Select Patient primary group no. using input ID 
# pmi_input = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "ec7ohl-patient_primary_group"))
# )
# pmi_input.send_keys("33")  
# pmi_input.send_keys(Keys.ENTER)
# print("✅ Patient Primary group no. entered successfully.")

wait = WebDriverWait(driver, 20)
# Wait for the checkbox to be present
checkbox = wait.until(EC.presence_of_element_located(
    (By.NAME, "data[patient_no_secondary_insurance]")
))
# ✅ Check if not already selected, then click
if not checkbox.is_selected():
    checkbox.click()
    print("✅ 'No Secondary Insurance' checkbox selected.")
else:
    print("ℹ️ Checkbox already selected.")



# # STEP: Select Patient Secondary insurance using input ID 
# pmi_input = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "ek9tw8-patient_secondary_name"))
# )
# pmi_input.send_keys("Backlash")  
# pmi_input.send_keys(Keys.ENTER)
# print("✅ Patient Secondary insurance entered successfully.")

# # STEP: Select Patient secondary insurance ID /policy no. using input ID 
# pmi_input = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "exd4nbh-patient_secondary_insurance_id"))
# )
# pmi_input.send_keys("12")  
# pmi_input.send_keys(Keys.ENTER)
# print("✅ Patient Secondary insurance ID entered successfully.")


# # STEP: Select Patient Secondary group no. using input ID 
# pmi_input = WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "ex4z7o6-patient_secondary_group"))
# )
# pmi_input.send_keys("65")  
# pmi_input.send_keys(Keys.ENTER)
# print("✅ Patient Secondary group No. entered successfully.")

# # tricare_radio = driver.find_element(By.ID, "evkezt-eitcdsf--Tricare")
# # driver.execute_script("arguments[0].click();", tricare_radio)
# # print("✅ 'Tricare' clicked using JavaScript fallback.")


# # radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][name*='secondaryInsuranceType']")
# # for r in radios:
# #     print("Radio:", r.get_attribute("value"))
# # # Step 1: Uncheck the 'No Secondary Insurance' checkbox
# # checkbox = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.NAME, "data[patient_no_secondary_insurance]"))
# # )
# # # Only click it if it's currently checked
# # if checkbox.is_selected():
# #     checkbox.click()
# #     print("☑️ Unchecked 'No Secondary Insurance'")
# # else:
# #     print("☑️ Checkbox already unchecked.")
# # # Step 2: Scroll down to make sure radio buttons are visible
# # driver.execute_script("arguments[0].scrollIntoView();", checkbox)
# # time.sleep(1)  # Small delay
# # # Step 3: Wait for Tricare radio to appear
# # tricare_radio = WebDriverWait(driver, 10).until(
# #     EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio'][value='Tricare']"))
# # )
# # # Step 4: Click Tricare using JS (bypass hidden layer issues)
# # driver.execute_script("arguments[0].click();", tricare_radio)
# # print("✅ Selected 'Tricare' radio option.")

# wait = WebDriverWait(driver, 20)
# # Step 1: Force uncheck the "No Secondary Insurance" checkbox using JavaScript
# checkbox = wait.until(EC.presence_of_element_located(
#     (By.NAME, "data[patient_no_secondary_insurance]")
# ))
# driver.execute_script("if(arguments[0].checked){arguments[0].click();}", checkbox)
# print("✅ Unchecked 'No Secondary Insurance' checkbox (via JS)")
# # Optional: wait for UI to react (DOM update)
# time.sleep(2)
# # Step 2: Wait for the "Tricare" radio to appear
# tricare_radio = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "//input[@type='radio' and @value='Tricare']")
# ))
# # Step 3: Force click using JavaScript
# driver.execute_script("arguments[0].click();", tricare_radio)
# print("✅ Selected 'Tricare' radio option via JavaScript")

wait=WebDriverWait(driver,30)
try:
    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ei9x9e"]/button'))
    )
    continue_button.click()
    print("✅ 'Continue' button clicked.")
except Exception as e:
    print("❌ Failed to click 'Continue' button:", e)
    # driver.save_screenshot("error_continue_button.png")


# # try:
# #     # Step 1: Wait for the error icon to appear
# #     WebDriverWait(driver, 5).until(
# #         EC.presence_of_element_located((By.CLASS_NAME, "swal-icon--error"))
# #     )
# #     # Step 2: Get the error message
# #     error_text_element = WebDriverWait(driver, 5).until(
# #         EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
# #     )
# #     # Step 3: Confirm the message text
# #     if "Inactive Insurance or Incorrect Insurance Id" in error_text_element.text:
# #         print("❌ Bad lead detected.")
# #         # Step 4: Click OK button to dismiss
# #         ok_button = WebDriverWait(driver, 5).until(
# #             EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]'))
# #         )
# #         ok_button.click()
# #     else:
# #         print("⚠️ Unrecognized error:", error_text_element.text)
# # except TimeoutException:
# #     print("✅ No error popup. Proceeding.")

# try:
#     # Step 1: Wait for the error icon to appear
#     WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "swal-icon--error"))
#     )

#     # Step 2: Get the error text
#     error_text_element = WebDriverWait(driver, 5).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
#     )
#     error_message = error_text_element.text.strip()

#     # Step 3: Handle based on message content
#     if "Inactive Insurance or Incorrect Insurance Id" in error_message:
#         print("❌ Bad lead detected: Inactive or incorrect insurance.")
#     elif "Medicare Advantage plans cannot be used" in error_message:
#         print("❌ Bad lead detected: Medicare Advantage not allowed.")
#     else:
#         print("⚠️ Unrecognized error:", error_message)
#     # Step 4: Click the OK button to dismiss
#     ok_button = WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]'))
#     )
#     ok_button.click()
# except TimeoutException:
#     print("✅ No error popup. Proceeding.")

# # from selenium.common.exceptions import TimeoutException
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# # try:
# #     # Wait for the error icon
# #     WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.CLASS_NAME, "swal-icon--error"))
# #     )

# #     # Get error message
# #     error_text_element = WebDriverWait(driver, 10).until(
# #         EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
# #     )
# #     error_message = error_text_element.text.strip()
# #     print("⚠️ Error message received:", repr(error_message))  # Debug

# #     # Detect known errors
# #     if "Inactive Insurance" in error_message:
# #         print("❌ Bad lead: Inactive or incorrect insurance.")
# #     elif "Medicare Advantage" in error_message:
# #         print("❌ Bad lead: Medicare Advantage not allowed.")
# #     else:
# #         print("⚠️ Unrecognized error:", error_message)

# #     # Click OK
# #     ok_button = WebDriverWait(driver, 10).until(
# #         EC.element_to_be_clickable((By.XPATH, '//button[text()="OK"]'))
# #     )
# #     driver.execute_script("arguments[0].scrollIntoView(true);", ok_button)
# #     ok_button.click()

# # except TimeoutException:
# #     print("✅ No error popup appeared.")


# try:
#     warning_text = wait.until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
#     )    
#     if "wellness visit" in warning_text.text.lower():
#         ok_button = wait.until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
#         )
#         ok_button.click()
#         print("✅ Warning handled and OK clicked.")
#     else:
#         print("⚠️ Unexpected warning text:", warning_text.text)
# except Exception as e:
#     print("❌ Error while handling the warning:", e)

    
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Wait object (already created with your driver)
# wait = WebDriverWait(driver, 10)

# try:
#     # Wait for alert text to appear
#     alert_text_element = wait.until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
#     )
#     alert_text = alert_text_element.text.lower()

#     # List of known bad lead error messages
#     bad_lead_errors = [
#         "medicare advantage plans cannot be used",
#         "inactive insurance or incorrect insurance id",
#         "medicare coverage is inactive for part b"
#     ]

#     # Handle bad leads (errors)
#     if any(err in alert_text for err in bad_lead_errors):
#         ok_button = wait.until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger"))
#         )
#         ok_button.click()
#         #status[i]='bad lead'
#         print("❌ Bad lead error handled and OK clicked.")
    
#     # Handle good lead warning
#     elif "wellness visit" in alert_text:
#         ok_button = wait.until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
#         )
#         ok_button.click()
#         #status[i]='good lead'
#         print("✅ Good lead warning handled and OK clicked.")
    
#     else:
#         print("⚠️ Unrecognized alert message:", alert_text)

# except Exception as e:
#     print("❌ Exception while handling alert:", e)


wait = WebDriverWait(driver, 20)
try:
    # Try detecting alert popup first
    alert_text_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
    )
    alert_text = alert_text_element.text.lower()

    bad_lead_errors = [
        "medicare advantage plans cannot be used",
        "inactive insurance or incorrect insurance id",
        "medicare coverage is inactive for part b"
    ]

    if any(err in alert_text for err in bad_lead_errors):
        ok_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger"))
        )
        ok_button.click()
        #df['status'][i]='bad lead'
        print("❌ Bad lead error handled and OK clicked.")

    elif "wellness visit" in alert_text:
        ok_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
        )
        ok_button.click()
        #df['status'][i]='good lead'
        print("✅ Good lead warning handled and OK clicked.")

    else:
        print("⚠️ Unrecognized alert message:", alert_text)

except:
    # No alert appeared – check if it's a good lead via page elements
    try:
        # Confirm that we reached the Patient Information page
        patient_heading = wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Patient Information"]'))
        )

        # Check for both green icon and "Active Insurance" text
        icon_present = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "insurance-section-icon-active"))
        )
        text_present = wait.until(
            EC.presence_of_element_located((By.XPATH, '//p[contains(@class,"insurance-section-text") and text()="Active Insurance"]'))
        )

        if patient_heading and icon_present and text_present:
            #df['status'][i]='good lead'
            print("✅ Good lead confirmed: Active Insurance detected on Patient Information page.")
        else:
            print("⚠️ Proceeded but could not confirm all good lead elements.")

    except Exception as e:
        print("❌ No popup and no good lead elements found. Possibly invalid lead or unexpected page.")

driver.refresh()

# wait = WebDriverWait(driver, 30)

# try:
#     # Try detecting alert popup first
#     alert_text_element = wait.until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "swal-text"))
#     )
#     alert_text = alert_text_element.text.lower()

#     bad_lead_errors = [
#         "medicare advantage plans cannot be used",
#         "inactive insurance or incorrect insurance id",
#         "medicare coverage is inactive for part b"
#     ]

#     if any(err in alert_text for err in bad_lead_errors):
#         ok_button = wait.until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger"))
#         )
#         ok_button.click()
       
#         print("❌ Bad lead error handled and OK clicked.")

#     elif "wellness visit" in alert_text:
#         ok_button = wait.until(
#             EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
#         )
#         ok_button.click()
        
#         print("✅ Good lead warning handled and OK clicked.")

#         # After clicking OK, wait for save button and click
#         save_button = wait.until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "button.patient_information-formio-submit-button"))
#         )
#         save_button.click()
#         print("💾 Save button clicked after good lead popup.")

#     else:
#         print("⚠️ Unrecognized alert message:", alert_text)

# except:
#     # No alert appeared – check if it's a good lead via page elements
#     try:
#         # Confirm that we reached the Patient Information page
#         patient_heading = wait.until(
#             EC.presence_of_element_located((By.XPATH, '//span[text()="Patient Information"]'))
#         )

#         # Check for both green icon and "Active Insurance" text
#         icon_present = wait.until(
#             EC.presence_of_element_located((By.CLASS_NAME, "insurance-section-icon-active"))
#         )
#         text_present = wait.until(
#             EC.presence_of_element_located((By.XPATH, '//p[contains(@class,"insurance-section-text") and text()="Active Insurance"]'))
#         )


#         if patient_heading and icon_present and text_present:
#             print("✅ Good lead confirmed: Active Insurance detected on Patient Information page.")

#             # Save button click for good lead without popup
#             save_button = wait.until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "button.patient_information-formio-submit-button"))
#             )
#             save_button.click()
#             print("💾 Save button clicked for good lead without popup.")

#         else:
#             print("⚠️ Proceeded but could not confirm all good lead elements.")

#     except Exception as e:
#         print("❌ No popup and no good lead elements found. Possibly invalid lead or unexpected page.")


# driver.refresh()

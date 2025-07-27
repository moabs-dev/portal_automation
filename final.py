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
from selenium.common.exceptions import StaleElementReferenceException

#Datasheet settings:

df=pd.read_excel('ZEYAN CHECKED.xlsx')
df['status'] = ''  # Create a blank 'status' column
dfs=df.drop(columns=['ADDRESS','Unnamed: 0','CITY','PHONE NUMBER'])
dfs['DOB'] = pd.to_datetime(dfs['DOB'], errors='coerce')  # Converts to datetime object
dfs['DOB'] = dfs['DOB'].dt.strftime('%m/%d/%Y')            # Formats as MM/DD/YYYY
dfs['MEDICARE'] = dfs['MEDICARE'].astype(str).str.upper()

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

print("✅ Logged in successfully")

for i in range(len(dfs)):

    wait = WebDriverWait(driver,90)
    
    try:
        create_case_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[8]/div[2]/div/div[2]/div[1]/div[2]/button"))
        )
        create_case_button.click()
        print("✅ 'Create case' button clicked.")
    except Exception as e:
        print("❌ Failed to click 'Create case' button:", e)
    
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
    
    # # Step 1: Type into the select input
    # test_type_input = WebDriverWait(driver, 60).until(
    #     EC.presence_of_element_located((By.ID, "react-select-11-input"))
    # )
    # test_type_input.clear()
    # test_type_input.send_keys("Immunodeficiency")
    # # Step 2: Wait for the dropdown option to appear
    # dropdown_option = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'select__option') and text()='Immunodeficiency']"))
    # )
    # # Step 3: Click the option directly
    # dropdown_option.click()
    # print("✅ Test Type selected successfully.")
  
#   # Re-find the dropdown parent before selecting an option
#     try:
#         dropdown_button = short_wait.until(
#             EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown-trigger")]'))
#         )
#         dropdown_button.click()
    
#         # Give time for options to load
#         time.sleep(1)  # or better: use WebDriverWait if there's a clear loading indicator
    
#         # Re-locate the dropdown option again before clicking
#         dropdown_option = short_wait.until(
#             EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"dropdown-option") and text()="Immunodeficiency"]'))
#         )
#         dropdown_option.click()
    
#     except StaleElementReferenceException:
#         print("⚠️ StaleElementReferenceException caught. Retrying dropdown selection...")
    
#         # Retry the whole dropdown-click process
#         dropdown_button = short_wait.until(
#             EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown-trigger")]'))
#         )
#         dropdown_button.click()
    
#         dropdown_option = short_wait.until(
#             EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"dropdown-option") and text()="Immunodeficiency"]'))
#         )
#         dropdown_option.click()
    
   

    # wait = WebDriverWait(driver, 10)
    
    # # Step 1: Click on the input block to open the dropdown
    # input_block = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, '//div[contains(@class, "sp-select__value-container")]')
    # ))
    # input_block.click()
    
    # # Step 2: Wait for the dropdown option and click "Immunodeficiency"
    # immuno_option = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, '//div[contains(text(), "Immunodeficiency")]')
    # ))
    # immuno_option.click()

    # dropdown = WebDriverWait(driver, 10).until(
    # EC.element_to_be_clickable((By.CLASS_NAME, "sp-select__value-container"))
    # )
    
    # # Use JavaScript click to bypass overlay issues
    # driver.execute_script("arguments[0].click();", dropdown)
    # # Wait for dropdown options to appear
    # immuno_option = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Immunodeficiency')]"))
    # )
    
    # # Again use JS click if normal click fails
    # driver.execute_script("arguments[0].click();", immuno_option)

    wait = WebDriverWait(driver, 50)
    
    # Step 1: Click the dropdown to open options
    dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="rec-form-select-collapse"]/div/div[5]/div/div/div/div[1]'
    )))
    dropdown.click()

    # Step 2: Wait for options to appear (React-Select often renders them globally in body)
    option = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//div[contains(@class, "sp-select__option") and text()="Immunodeficiency"]'
    )))
    option.click()

    
    
    # # Type in the Lab input
    # lab_input = WebDriverWait(driver, 45).until(
    #     EC.presence_of_element_located((By.ID, "react-select-12-input"))
    # )
    # lab_input.clear()
    # lab_input.send_keys("Immunology - Precision Genetics")
    # # Wait for the dropdown to show up and click
    # dropdown_option = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((
    #         By.XPATH,
    #         "//div[contains(@class, 'select__option') and text()='Immunology - Precision Genetics']"
    #     ))
    # )
    # dropdown_option.click()
    wait = WebDriverWait(driver, 50)

    # Step 1: Click the Lab dropdown to open options
    lab_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="rec-form-select-collapse"]/div/div[6]/div/div/div/div[1]'
    )))
    lab_dropdown.click()
    
    # Step 2: Wait for "Immunology - Precision Genetics" option to appear and click it
    lab_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//div[contains(@class, "sp-select__option") and text()="Immunology - Precision Genetics"]'
    )))
    lab_option.click()
    print("✅ Lab selected successfully.")
    
    # STEP: Select First name using input ID 
    fname_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "eu9k5i-patient_first_name"))
    )
    
    fname_input.send_keys(dfs['FIRST NAME'][i])  
    fname_input.send_keys(Keys.ENTER)
    
    print("✅ F name entered successfully.")
    
    
    # STEP: Select Last name using input ID 
    lname_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "emb0a8-patient_last_name"))
    )
    lname_input.send_keys(dfs['LAST NAME'][i])  
    lname_input.send_keys(Keys.ENTER)
    print("✅ L name entered successfully.")
    
    # STEP 1: Wait for the correct DOB field
    dob_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='e45d6bf']/div[1]/div/input[2]"))
    )
    # STEP 2: Click to focus the field
    dob_input.click()
    
    # one = '4/26/1954'
    # x, y, z = one.split('/')
    # x = x.zfill(2)
    # y = y.zfill(2)
    # ones = f"{x}/{y}/{z}"

    dob_input.send_keys(dfs['DOB'][i])  # MMDDYYYY (auto adds slashes)
    dob_input.send_keys(Keys.TAB)  # or Keys.ENTER
    print("✅ DOB filled successfully.")
    
    # st1=92343
    # if len(str(st1))==4:
    #     st1=str(st1)+'12345'
    # elif len(str(st1))==5:
    #     st1=str(st1)+'1234'    
    # Efficient padding of ZIP code based on its length
    st1 = str(dfs['ZIPCODE'][i])
    st1 += '12345'[:9 - len(st1)] if 4 <= len(st1) <= 5 else ''
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
    pmi_input.send_keys(dfs['STATE'][i])  
    pmi_input.send_keys(Keys.ENTER)
    print("✅ Patient State entered successfully.")
    
    # Locate the "Medicare" radio button via value, just like Tricare
    medicare_radio = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='Medicare']"))
    )
    # Click it using JavaScript
    driver.execute_script("arguments[0].click();", medicare_radio)
    print("✅ Selected 'Medicare' radio option via JavaScript.")
    
    primary_insurance_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "ex83gsp-patient_primary_name"))
    )
    # Clear any existing text and enter a new value
    primary_insurance_input.clear()
    primary_insurance_input.send_keys("Medicare")
    print("Primary insurance input filled successfully.")
    print(dfs["MEDICARE"][i])
    # STEP: Select Patient primary insurance ID /policy no. using input ID 
    pmi_input = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.ID, "eadrxvn-patient_primary_insurance_id"))
    )
    pmi_input.send_keys(dfs['MEDICARE'][i])  
    pmi_input.send_keys(Keys.ENTER)
    print("✅ Patient Primary insurance ID entered successfully.")
    
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
    
    
    element = driver.find_element(By.XPATH, '//*[@id="ei9x9e"]/button')
    driver.execute_script("arguments[0].scrollIntoView();", element)


    wait=WebDriverWait(driver,40)
    try:
        continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ei9x9e"]/button'))
        )
        continue_button.click()
        print("✅ 'Continue' button clicked.")
    except Exception as e:
        print("❌ Failed to click 'Continue' button:", e)
    
    # try:
    #     # Fast check for alert popup (non-blocking)
    #     alert_elements = driver.find_elements(By.CLASS_NAME, "swal-text")
    #     if alert_elements:
    #         alert_text = alert_elements[0].text.lower()
    
    #         bad_lead_errors = [
    #             "medicare advantage plans cannot be used",
    #             "inactive insurance or incorrect insurance id",
    #             "medicare coverage is inactive for part b"
    #         ]
    
    #         if any(err in alert_text for err in bad_lead_errors):
    #             ok_button = short_wait.until(
    #                 EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger"))
    #             )
    #             ok_button.click()
    #             df.loc[i, 'status'] = 'bad lead'
    #             print("❌ Bad lead error handled and OK clicked.")
    
    #         elif "wellness visit" in alert_text:
    #             ok_button = short_wait.until(
    #                 EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
    #             )
    #             ok_button.click()
    #             df.loc[i, 'status'] = 'good lead'
    #             print("✅ Good lead warning handled and OK clicked.")
    
    #         else:
    #             print("⚠️ Unrecognized alert message:", alert_text)
    
    #     else:
    #         raise Exception("No alert popup")
    
    # except:
    #     # No alert or handled already, check for good lead
    #     try:
    #         patient_heading = short_wait.until(
    #             EC.presence_of_element_located((By.XPATH, '//span[text()="Patient Information"]'))
    #         )
    
    #         icon_present = short_wait.until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "insurance-section-icon-active"))
    #         )
    
    #         text_present = short_wait.until(
    #             EC.presence_of_element_located((By.XPATH, '//p[contains(@class,"insurance-section-text") and text()="Active Insurance"]'))
    #         )
    
    #         if patient_heading and icon_present and text_present:
    #             df.loc[i, 'status'] = 'good lead'
    #             print("✅ Good lead confirmed: Active Insurance detected on Patient Information page.")
    #         else:
    #             print("⚠️ Proceeded but could not confirm all good lead elements.")
    
    #     except Exception as e:
    #         print("❌ No popup and no good lead elements found. Possibly invalid lead or unexpected page.")
    
    # finally:
    #     # Refresh page after all status updates are recorded
    #     driver.refresh()
    
    # short_wait = WebDriverWait(driver, 5)
    # long_wait = WebDriverWait(driver, 20)
    
    # lead_status_recorded = False  # Flag to wait for status update
    
    # try:
    #     # Check for alert popup (non-blocking)
    #     alert_elements = driver.find_elements(By.CLASS_NAME, "swal-text")
    #     if alert_elements:
    #         alert_text = alert_elements[0].text.lower()
    
    #         bad_lead_errors = [
    #             "medicare advantage plans cannot be used",
    #             "inactive insurance or incorrect insurance id",
    #             "medicare coverage is inactive for part b"
    #         ]
    
    #         if any(err in alert_text for err in bad_lead_errors):
    #             ok_button = short_wait.until(
    #                 EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger"))
    #             )
    #             ok_button.click()
    #             df.loc[i, 'status'] = 'bad lead'
    #             print("❌ Bad lead error handled and OK clicked.")
    #             lead_status_recorded = True
    
    #         elif "wellness visit" in alert_text:
    #             ok_button = short_wait.until(
    #                 EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
    #             )
    #             ok_button.click()
    #             df.loc[i, 'status'] = 'good lead'
    #             print("✅ Good lead warning handled and OK clicked.")
    #             lead_status_recorded = True
    
    #         else:
    #             print("⚠️ Unrecognized alert message:", alert_text)
    
    #     else:
    #         raise Exception("No alert popup")
    
    # except:
    #     # No alert, check good lead indicators
    #     try:
    #         patient_heading = short_wait.until(
    #             EC.presence_of_element_located((By.XPATH, '//span[text()="Patient Information"]'))
    #         )
    
    #         icon_present = short_wait.until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "insurance-section-icon-active"))
    #         )
    
    #         text_present = short_wait.until(
    #             EC.presence_of_element_located((By.XPATH, '//p[contains(@class,"insurance-section-text") and text()="Active Insurance"]'))
    #         )
    
    #         if patient_heading and icon_present and text_present:
    #             df.loc[i, 'status'] = 'good lead'
    #             print("✅ Good lead confirmed: Active Insurance detected.")
    #             lead_status_recorded = True
    #         else:
    #             print("⚠️ Page loaded but good lead indicators missing.")
    
    #     except Exception as e:
    #         print("❌ No popup and no good lead indicators found.")
    
    # # 🔁 Wait until lead status is set before refresh
    # if not lead_status_recorded:
    #     print("⏳ Waiting before refresh to ensure lead status is recorded...")
    #     time.sleep(2)
    
    # driver.refresh()

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
            dfs.loc[i, 'status'] = 'bad lead'
            print("❌ Bad lead error handled and OK clicked.")
    
        elif "wellness visit" in alert_text:
            ok_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--confirm"))
            )
            ok_button.click()
            dfs.loc[i, 'status'] = 'good lead'
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
                dfs.loc[i, 'status'] = 'good lead'
                print("✅ Good lead confirmed: Active Insurance detected on Patient Information page.")
            else:
                print("⚠️ Proceeded but could not confirm all good lead elements.")
    
        except Exception as e:
            print("❌ No popup and no good lead elements found. Possibly invalid lead or unexpected page.")
    
    driver.refresh()
    print(i)


    if i%10==0:
        dfs.to_excel('Updated.xlsx')  

    
        
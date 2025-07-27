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



def run_automation(file_path: str):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel are allowed.")
    
    
    df['status'] = ''  # Create a blank 'status' column
    dfs=df.drop(columns=['ADDRESS','Unnamed: 0','CITY','PHONE NUMBER'])
    dfs['DOB'] = pd.to_datetime(dfs['DOB'], errors='coerce')  # Converts to datetime object
    dfs['DOB'] = dfs['DOB'].dt.strftime('%m/%d/%Y')            # Formats as MM/DD/YYYY
    dfs['MEDICARE'] = dfs['MEDICARE'].astype(str).str.upper()

    updated_rows = []
    iteration_count = 0

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
    
    wait = WebDriverWait(driver, 40)
    
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_input.send_keys("msmrichard@gmail.com")
    
    password_input = wait.until(EC.presence_of_element_located((By.ID, "pwd")))
    password_input.send_keys("MSMAgent593%")
    
    # 🚀 Step 4: Click Sign In button
    driver.find_element(By.CLASS_NAME, "btn-safespace").click()
    print("✅ Logged in successfully")
    
    for i in range(len(dfs)):
        row = dfs.iloc[i]
    
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
        
        dob_input.send_keys(dfs['DOB'][i])  # MMDDYYYY (auto adds slashes)
        dob_input.send_keys(Keys.TAB)  # or Keys.ENTER
        print("✅ DOB filled successfully.")
    
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
        
        primary_insurance_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "e8bm1gq-patient_primary_name"))
        )
        # Clear any existing text and enter a new value
        primary_insurance_input.clear()
        primary_insurance_input.send_keys("Medicaid")
        print("Primary insurance input filled successfully.")
    
        # STEP: Select Patient primary insurance ID /policy no. using input ID 
        pmi_input = WebDriverWait(driver, 15).until(
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
        
        wait=WebDriverWait(driver,40)
        try:
            continue_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="ei9x9e"]/button'))
            )
            continue_button.click()
            print("✅ 'Continue' button clicked.")
        except Exception as e:
            print("❌ Failed to click 'Continue' button:", e)
        
    
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

        #updated_rows.append(row)
        iteration_count += 1


    driver.quit()

    #updated_df = pd.DataFrame(updated_rows)
    updated_file_path = 'Updated.xlsx'
    dfs.to_excel(updated_file_path, index=False)

    return updated_file_path, iteration_count   

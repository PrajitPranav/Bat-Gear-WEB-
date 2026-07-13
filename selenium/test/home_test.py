from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://localhost:5501/")

wait = WebDriverWait(driver, 10)

print("======================================")
print("      BAT GEAR HOME PAGE TEST")
print("======================================")


expected_title = "Bat Gear | Car Enthusiasts Club"

if driver.title == expected_title:
    print("✅ Test Case 1 Passed : Page Title Verified")
else:
    print("❌ Test Case 1 Failed")
    print("Expected :", expected_title)
    print("Actual   :", driver.title)

# ----------------------------------------------------
# TEST CASE 2 : Verify Logo
# ----------------------------------------------------
logo = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "logo"))
)

if logo.is_displayed():
    print("✅ Test Case 2 Passed : Logo is Visible")
else:
    print("❌ Test Case 2 Failed")

# ----------------------------------------------------
# TEST CASE 3 : Verify Menu Icon
# ----------------------------------------------------
menu = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "menu-icon"))
)

if menu.is_displayed():
    print("✅ Test Case 3 Passed : Menu Icon is Visible")
else:
    print("❌ Test Case 3 Failed")

# ----------------------------------------------------
# TEST CASE 4 : Verify Carousel
# ----------------------------------------------------
carousel = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "carousel"))
)

if carousel.is_displayed():
    print("✅ Test Case 4 Passed : Carousel Loaded")
else:
    print("❌ Test Case 4 Failed")

# ----------------------------------------------------
# TEST CASE 5 : Verify Stories Section
# ----------------------------------------------------
stories = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "stories"))
)

if stories.is_displayed():
    print("✅ Test Case 5 Passed : Stories Section Visible")
else:
    print("❌ Test Case 5 Failed")

# ----------------------------------------------------
# TEST CASE 6 : Verify Discover Section
# ----------------------------------------------------
discover = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "discover"))
)

if discover.is_displayed():
    print("✅ Test Case 6 Passed : Discover Section Visible")
else:
    print("❌ Test Case 6 Failed")

# ----------------------------------------------------
# TEST CASE 7 : Verify Footer
# ----------------------------------------------------
footer = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "footer"))
)

if footer.is_displayed():
    print("✅ Test Case 7 Passed : Footer Visible")
else:
    print("❌ Test Case 7 Failed")

# ----------------------------------------------------
# TEST CASE 8 : Verify Explore Button
# ----------------------------------------------------
explore_button = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "btn-explore"))
)

if explore_button.is_displayed():
    print("✅ Test Case 8 Passed : Explore Button Visible")
else:
    print("❌ Test Case 8 Failed")

# ----------------------------------------------------
# Save Screenshot
# ----------------------------------------------------
driver.save_screenshot("screenshots/home_page.png")
print("📸 Screenshot Saved")

print("\n======================================")
print("     HOME PAGE TEST COMPLETED")
print("======================================")

input("\nPress ENTER to close browser...")

driver.quit()
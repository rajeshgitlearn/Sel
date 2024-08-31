from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Set up the driver (e.g., for Chrome)
driver = webdriver.Chrome()

# Open the web page
driver.get('http://your-webpage-url')

# Find the drop-down menu element
select_element = driver.find_element_by_id('your-select-element-id')

# Create a Select object
select = Select(select_element)

# Get all options
options = select.options

# Loop through the options and print their values
for option in options:
    print(option.get_attribute('value'))
    # If you need the text displayed, use option.text

# Close the driver
driver.quit()
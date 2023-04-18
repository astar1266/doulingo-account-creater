import time
from selenium import webdriver

# create an instance of the Edge driver
# If you use chrome or firefox or any other webbrowser make sure to change webdriver.(your web browser) and use its driver.
driver = webdriver.Edge("#put your edge,firefox or chrome loction here for example:     C:\\Windows\\msedgedriver.exe")

# start the email number at 5
# The number where it starts creating accounts
email_number = 5

# loop 10 times
# the number of how many account u want to be created
for i in range(10):
    # load the login page
    driver.get("https://www.duolingo.com/log-in?isLogging=true&isLoggingIn=true")
    driver.implicitly_wait(60)
    
    # click the signup button
    signup = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/div[2]/button')
    signup.click()
    driver.implicitly_wait(60)
    
    # enter age
    ageinput = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[1]/label/div/input')
    ageinput.send_keys('24')
    driver.implicitly_wait(60)
    
    # increment the email number and use it in the email address
    email_number += 1
    email = "example+{}@hotmail.com".format(email_number)
    
    # enter email address
    emailinput = driver.find_element_by_xpath("//*[@id='overlays']/div[2]/div/div/form/div[1]/div[1]/div[3]/label/div/input")
    emailinput.send_keys(email)
    driver.implicitly_wait(60)
    
    # enter password
    passwordinput = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[4]/label/div/input')
    passwordinput.send_keys("yourepicpasswordthatyouwant")
    driver.implicitly_wait(60)
    
    # click the create account button
    createbutton = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/form/div[1]/button')
    createbutton.click()
    
    # wait for the account to be created
    time.sleep(7)
    

# done :)
print ("Script completed successfully.")

from selenium import webdriver
import getpass
import time

driver=webdriver.Chrome('/home/neeraj/Downloads/chromedriver_linux64/chromedriver') 
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin') 
username=driver.find_element_by_id('username') 
username_=input("Enter email or username: ")
username_="neerajdeshpande55@yahoo.com"
password_ = getpass.getpass(prompt='Enter password: ')
username.send_keys(username_)
password=driver.find_element_by_id('password') 
password.send_keys(password_)
button=driver.find_element_by_class_name('login__form_action_container ') 
button.click()
print("Waiting for it to load the homepage")
time.sleep(6)
driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
for i in range(0,100): 
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
	time.sleep(0.5)
Name=driver.find_elements_by_class_name('mn-connection-card__name  ') 
f= open("connections.txt","w+")
print("Printing connections.................................")
for i in Name:
	print(i.text)
	f.write(i.text)
	f.write('\n')
f.close()
driver.get('https://www.linkedin.com/feed/followers/') 
for i in range(0,100): 
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
	time.sleep(0.5)
Name=driver.find_elements_by_class_name('follows-recommendation-card__name') 
print("Printing followers.................................")
f= open("followers.txt","w+")
for i in Name:
	print(i.text)
	f.write(i.text)
	f.write('\n')
f.close()






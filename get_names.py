from selenium import webdriver
import getpass

driver=webdriver.Chrome('/home/neeraj/Downloads/chromedriver_linux64/chromedriver') 
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin') 
username=driver.find_element_by_id('username') 
username_=input("Enter email or username: ")
password_ = getpass.getpass(prompt='Enter password: ')
username.send_keys(username_)
password=driver.find_element_by_id('password') 
password.send_keys(password_)
button=driver.find_element_by_class_name('login__form_action_container ') 
button.click()
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin') 
Name=driver.find_elements_by_class_name('mn-connection-card__name  ') 
f= open("connections.txt","w+")
print("Printing connections.................................")
for i in Name:
	print(i.text)
	f.write(i.text)
f.close()
driver.get('https://www.linkedin.com/feed/followers/') 
Name=driver.find_elements_by_class_name('follows-recommendation-card__name') 
print("Printing followers.................................")
f= open("followers.txt","w+")
for i in Name:
	print(i.text)
	f.write(i.text)
f.close()






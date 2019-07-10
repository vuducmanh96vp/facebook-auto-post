from datetime import datetime
from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


username = input('Enter your username: ')
password = input('Enter your password: ')
number_time_post = int(input('Enter the number times post: '))
id_target = int(input('Enter the target ID (page, group, user): '))
content = input('Enter the content of the posts: ')

chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs", {'profile.managed_default_content_settings.javascript': 2}
)
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

driver.get("https://m.facebook.com/")
print("Opened facebook")

username_box = driver.find_element_by_id('m_login_email')
username_box.send_keys(username)
print("Email Id entered")

password_box = driver.find_element_by_id('m_login_password')
password_box.send_keys(password)
print("Password entered")

login_box = driver.find_element_by_id('u_0_5')
sleep(1)
login_box.click()

try:
    if driver.find_element_by_id('m_login_email') or \
            driver.find_element_by_id('m_login_password'):
        print("The username or password is incorrect")
        exit(1)
except Exception:
    pass

count = 0
print('Index\t Duration')
start_process = datetime.now()
while number_time_post > 0:
    start = datetime.now()
    count += 1
    driver.get(
        "https://m.facebook.com/{}".format(id_target)
    )
    message_box = None
    try:
        message_box = driver.find_element_by_name('xc_message')
    except Exception:
        message_box = driver.find_element_by_id('u_0_0')
    finally:
        if not message_box:
            print('Something went wrong. Please check it again')
            exit(1)

    message_box.send_keys(
         content + ' \n.\n.\n.\n.\n.\n' + str(datetime.now().timestamp())
    )
    post_btn = driver.find_element_by_name('view_post')
    sleep(1)
    post_btn.click()

    end = datetime.now()
    duration = end - start
    print("{}\t {}".format(count, duration))
    number_time_post -= 1

end_process = datetime.now()
print('Total\t {}'.format(end_process - start_process))
driver.close()

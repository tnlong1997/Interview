from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get("http://google.com")
# url = "http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh"
# driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")

for i in range(0, 10001):
    driver = webdriver.Chrome()
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
    driver.execute_script("window.open('http://hoahoctro.vn/tin-tuc/co-ai-nhu-nai-luong-biet-ro-tieu-lo-la-hoa-hong-co-gai-nhung-van-nguyen-dat-vao-tim-minh');")
# elem = driver.find_element_by_tag_name("body")
    time.sleep(3)
    driver.quit()
# elem.send_keys(Keys.COMMAND+"t")
# time.sleep(2)
# elem.send_keys(Keys.COMMAND+"w")

import requests
import random
import time

url = input("Nhập URL của trang web: ")

proxies = []
with open("proxy.txt", "r") as file:
    proxies = file.read().splitlines()

num_requests = int(input("Nhập số lượng request: "))
interval = float(input("Nhập tần suất giữa các request (giây): "))

for i in range(num_requests):
    proxy = random.choice(proxies)  # Chọn ngẫu nhiên một proxy từ danh sách
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    response = session.get(url)
    print(f"Request {i+1} - Proxy: {proxy} - Status code: {response.status_code}")
    time.sleep(interval)
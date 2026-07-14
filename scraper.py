import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_gmaps(keyword, lokasi, max_results=50): # Batasan dinaikkan ke 50 data
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1200,800")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    search_query = f"{keyword} di {lokasi}"
    url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
    driver.get(url)
    time.sleep(5) # Waktu tunggu awal agar halaman maps benar-benar termuat
    
    results = []
    seen_links = set()
    
    # Mencari panel tempat daftar hasil pencarian berada
    try:
        panel = driver.find_element(By.XPATH, '//div[contains(@role, "feed")]')
    except:
        try:
            panel = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
        except:
            panel = None

    if panel:
        for _ in range(15): # Melakukan scroll down sebanyak 15 kali untuk memuat banyak data
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", panel)
            time.sleep(random.uniform(1.5, 2.5)) # Jeda acak agar tidak diblokir
            
            # Strategi Agresif: Ambil SEMUA tag jangkar (a) yang mengandung pola tautan tempat Google Maps
            all_links = driver.find_elements(By.TAG_NAME, "a")
            
            for el in all_links:
                try:
                    link = el.get_attribute("href")
                    if link and "/maps/place/" in link:
                        if link not in seen_links:
                            seen_links.add(link)
                            
                            # Mengambil nama tempat dari atribut aria-label atau text element
                            name = el.get_attribute("aria-label")
                            if not name:
                                name = el.text.split('\n')[0]
                                
                            if name and name.strip():
                                results.append({
                                    "Nama": name.strip(),
                                    "Link": link
                                })
                                
                            if len(results) >= max_results:
                                break
                except:
                    continue
            if len(results) >= max_results:
                break
                
    driver.quit()
    return results
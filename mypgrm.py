import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

# options = Options()
# # enable headless mode
# options.headless = True

# driver = webdriver.Chrome(
#     options=options, 
#     #...
# )

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
movie_link=[]
try:
    # Navigate to the website
    driver.get("https://in.bookmyshow.com/explore/home/hyderabad")
    time.sleep(10)
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Movies"]'))
    )
    # Click the link
    link.click()

    # time.sleep(10)
     
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="super-container"]/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/div/div[contains(text(), "Telugu")]'))
    )
    
    # Click the element
    # time.sleep(10)
    element.click()

    
    for i in range(4,7):
        for j in range(1,5):
            # time.sleep(5)
            element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="super-container"]/div[2]/div[3]/div[2]/div[{i}]/div/div/div[2]/a[{j}]'))
            )
            href_value = element.get_attribute("href")
            movie_link.append(href_value)
    # time.sleep(10)

    driver.close()



   
    try:
        # sample_link=movie_link[0]
        # driver.get(sample_link)
        # element = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, '//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/h1'))
        # )

    # # Get the text content of the element
    #     movie_name = element.text
    #     element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/div[1]/div[2]'))
    #     )
    #     print(element.text)
        
    #     full_text = element.text

    # # Split the text based on the separator "•"
    #     parts = full_text.split("•")

    # # Extract the different parts
    #     movie_time = parts[0].strip()
    #     genres = [genre.strip() for genre in parts[1].strip().split(",")]
    #     certificate = parts[2].strip()
    #     release_date = parts[3].strip()
    # # Print the extracted values
    #     print("Movie Time:", movie_time)
    #     print("Genres:", genres)
    #     print("Certificate:", certificate)
    #     print("Release Date:", release_date)
    # # Print the extracted values
    #     print(movie_name)
    #     # print("Movie Time:", movie_time)
    #     # print("Certificate:", certificate)
    #     # print("Release Date:", release_date)
    #     # print(movie_link,sample_link)
    #     time.sleep(20)
        csv_file = "movie_details.csv"

# Open CSV file for writing
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
    # Write the header
            writer.writerow(["Movie Name","Movie Time", "Genres", "Certificate", "Release Date"])

            for url in movie_link:
                try:
            # Navigate to the movie page
                    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
                    driver.get(url)
                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/h1'))
                    )
                    movie_name = element.text
            # Wait for the main container to be present
                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/div[1]/div[2]'))
                    )
        
                    full_text = element.text

            
            # Split the text based on the separator "•"
                    parts = full_text.split("•")
            
            # Extract the different parts
                    movie_time = parts[0].strip()
                    genres = [genre.strip() for genre in parts[1].strip().split(",")]
                    certificate = parts[2].strip()
                    release_date = parts[3].strip()
            
            # Print the extracted values (for debugging purposes)
                    print(movie_name)
                    print("Movie Time:", movie_time)
                    print("Genres:", genres)
                    print("Certificate:", certificate)
                    print("Release Date:", release_date)
            
                # Write the data to CSV
                    writer.writerow([movie_name,movie_time, ", ".join(genres), certificate, release_date])
                    driver.close()
        
                except Exception as e:
                    print(f"An error occurred for URL {url}: {e}")
                time.sleep(6)

        # Wait for a few seconds before moving to the next URL
        time.sleep(10)

    finally:
        driver.quit()
finally:
    # Close the browser
    driver.quit()




# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[1]
# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[2]
# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[3]
# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[4]


# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[5]/div/div/div[2]/a[1]
# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[5]/div/div/div[2]/a[2]
# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[5]/div/div/div[2]/a[3]
# //*[@id="super-container"]/div[2]/div[3]/div[2]/div[5]/div/div/div[2]/a[4]
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

# if you dont use snap/Ubuntu you will need to change this
service = FirefoxService("/snap/bin/firefox.geckodriver")

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://careers.cern/alljobs")
data_class_jobs = driver.find_elements(By.CLASS_NAME, "field--item")
print("Looking for fitting jobs")

contract = "-LD" #-LD, -GRAP, ....
grade = "6-7"
partial_matches = [ #all in caps
  "SOFTWARE",
  "DEVELOPER",
  "ENGINEER",
]

print("Contract", contract)
print("Grade", grade)
print("Partial matches in job description", partial_matches)
print("\nMatches found:")

for potential_data_jobs in data_class_jobs:
  try:
    plaintext_jobs = potential_data_jobs.get_attribute("innerText")
    metadata_jobs = potential_data_jobs.get_attribute("innerHTML").split("https://")
  except:
    continue

  for line in plaintext_jobs.split("\n"):
    line = line.upper()
    if contract in line:
      look_into_job = False

      for match in partial_matches:
        if match in line:
          look_into_job = True

      if look_into_job == True:
        id = line.split("(")[1].split(")")[0]

        for metadata_job in metadata_jobs:
          if id in metadata_job:
            job_url = "https://" + metadata_job.split("&quot;")[0]

            if contract == "-LD":
              driver.get(job_url)
              grade_sections = driver.find_elements(By.ID, "st-additionalInformation")
              for grade_section in grade_sections:
                paragraphs = grade_section.find_elements(By.TAG_NAME, "p")
                for paragraph in paragraphs:
                  if grade in paragraph.text:
                    print(line.split("GENEVA")[0], job_url)
            else:
              print(line.split("GENEVA")[0], job_url)
driver.quit()

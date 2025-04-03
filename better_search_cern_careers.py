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

# mandatory
contract = "-LD" #-LD, -GRAP, ....
# Grade of the LD: "3-4" or "6-7" ...
# Either grade or job_title must be given for LDs
grade = "6-7"

# partial matches looks in the title
# applies to LD and other contracts
# if empty, looks for all contracts of type "contract"
# partial_matches = [ #all in caps
#   "SOFT",
#   "DEVEL",
#   "ENGINEER",
#   "DEVOPS",
#   "COMPUT",
#   "AI ",
#   "EXPERT"
# ]
partial_matches = [ ]

# Benchmark Job Title
# Only relevant for LD
# If empty it is ignored
# Either grade or job_title must be given for LDs
job_title = "Computing Engineer"
# job_title = ""
# selected benchmark Job Title
# Computing Engineer
# Applied Physicist
# Mechanical Engineer

print("Contract", contract)
print("Grade", grade)
print("Partial matches in job description", partial_matches)
print("Benchmark Job Title", job_title)
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

      if len(partial_matches) > 0:
        for match in partial_matches:
          if match in line:
            look_into_job = True
      else:
        look_into_job = True

      if look_into_job == True:
        id = line.split("(")[1].split(")")[0]

        for metadata_job in metadata_jobs:
          if id in metadata_job:
            job_url = "https://" + metadata_job.split("&quot;")[0]

            if contract == "-LD":
              correct_grade = False
              correct_job_title = False
              driver.get(job_url)
              grade_sections = driver.find_elements(By.ID, "st-additionalInformation")
              if len(grade) == 0:
                correct_grade = True
              if len(job_title) == 0:
                correct_job_title = True
              for grade_section in grade_sections:
                if correct_grade and correct_job_title:
                  break
                paragraphs = grade_section.find_elements(By.TAG_NAME, "p")
                for paragraph in paragraphs:
                  if len(grade) != 0:
                    if grade in paragraph.text:
                      correct_grade = True
                  if len(job_title) != 0:
                    if job_title in paragraph.text:
                      correct_job_title = True

              if correct_grade and correct_job_title:
                print(line.split("GENEVA")[0], job_url)
            else:
              print(line.split("GENEVA")[0], job_url)
driver.quit()

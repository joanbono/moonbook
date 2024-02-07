from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, requests, datetime
from PIL import Image
from config import cookie_header

RANGE = 0

def generate_book(problem_list):
    #print(problem_list)
    f = open('Moonbook.md', 'a+')
    for i in range(RANGE, len(problem_list),1):
        f.write("""
## %s - `%s`

![](img/%s.png)

***
    """%(problem_list[i]['Name'], problem_list[i]['Grade'], problem_list[i]['Filename']))
    f.close()

def resize_screenshot(filename):
    img = Image.open("img/%s.png"%(filename))
    img2 = img.crop((806, 17, 1228, 667))
    img2.save("img/%s.png"%(filename), optimize=True, quality=100)

def get_benchmarks():
    problem_list = []
    h = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data="sort=Grade-asc&page=1&pageSize=10000&group=&aggregate=Score-sum~MaxScore-sum&filter=setupId~eq~'17'~and~Configuration~eq~1"
    #data="sort=Grade-asc&page=1&pageSize=10&group=&aggregate=Score-sum~MaxScore-sum&filter=setupId~eq~'17'~and~Configuration~eq~1"
    h.update(cookie_header)
    r = requests.post("https://www.moonboard.com/Dashboard/GetBenchmarks", headers=h, data=data)

    for i in range(0,len(r.json()['Data']),1):
        problems = {
            "ProblemId": r.json()['Data'][i]['ProblemId'],
            "Name": r.json()['Data'][i]['Name'],
            "Url": r.json()['Data'][i]['Url'],
            "Grade": r.json()['Data'][i]['Grade'],
        }
        problem_list.append(problems)

    return problem_list

def get_screenshot(url):
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get('%s'%(url))
    time.sleep(3)
    t = browser.title
    title = t.replace('MoonBoard - ','').split(' set by')[0].lower().replace(' ','_')
    browser.get_screenshot_as_file("img/%s.png"%(title))
    browser.close()
    browser.quit()
    return title


if __name__ == "__main__":
    problem_list = get_benchmarks()

    for i in range(RANGE, len(problem_list),1):
        now = datetime.datetime.now()
        print("%s - %d/%d - %s"%(now, i+1, len(problem_list), problem_list[i]['Name']))
        filename = get_screenshot("https://www.moonboard.com/Problems/View/%s/%s"%(problem_list[i]['ProblemId'], problem_list[i]['Url']))
        problem_list[i].update({"Filename": filename})
        resize_screenshot(filename)

    generate_book(problem_list)

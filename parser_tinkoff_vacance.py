import requests
from bs4 import BeautifulSoup
import json


def save_to_json(data, filename):
    with open(f"Jsons/{filename}.json", 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"{filename}.json сохранен в папку Jsons")


def parser_categories_BUSINESS_and_IT():
    links = {
        'IT_parser_result': 'https://www.tinkoff.ru/career/it/?allForSpecialties=back-end-razrabotka&allForSpecialties=analitika&allForSpecialties=infrastruktura-administrirovanie&allForSpecialties=informacionnaya-bezopasnost&allForSpecialties=mobilnaya-razrabotka&allForSpecialties=system-analytics&allForSpecialties=testirovanie',
        'BUSINESS_parser_result': 'https://www.tinkoff.ru/career/back-office/?allForSpecialties=analitika&allForSpecialties=investicii&allForSpecialties=marketing-i-pr&allForSpecialties=prodazhi&allForSpecialties=product-analytics&allForSpecialties=riski&allForSpecialties=upravlenie-proektami&allForSpecialties=back-office&allForSpecialties=hr'   
    }
    for url in links:
        response = requests.get(links[url])
        soup = BeautifulSoup(response.text, 'lxml')
        
        vacance_categories = soup.find('div', class_='deyd61')
        parser_data = []
        for category in vacance_categories:
            title_category = category.find('h3').text
            category_vacancies = category.find('table', class_='c-+mU0F j-+mU0F i-+mU0F n-+mU0F').find_all('tr')
            vacance_data = []

            for vacance in category_vacancies:
                vacance_info = vacance.find_all('td', class_='g-+mU0F')
                vacance_title = vacance_info[0].text
                vacance_level = vacance_info[1].text
                vacance_url = f"https://www.tinkoff.ru/{vacance.find('a')['href']}"

                vacance_data.append({
                    'Вакансия': vacance_title,
                    'Уровень': vacance_level,
                    'Ссылка': vacance_url
                })
            parser_data.append({
                'Группа': title_category,
                'Все вакансии': vacance_data
            })
        save_to_json(parser_data, filename=url)
        

# parser_categories_BUSINESS_and_IT()
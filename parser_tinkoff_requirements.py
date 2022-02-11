from bs4 import BeautifulSoup
import requests
import json

def save_to_json(data, filename):
    with open(f"Jsons/{filename}.json", 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"{filename}.json сохранен в папку Json")


def parse_requirements(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    vacance_info = soup.find_all('section', class_='aA3yDC')[1].find_all('li')
    requirements = []
    for item in vacance_info:
        requirements.append(item.text)
    
    return requirements

def collect_requirements():
    files = {
        'BUSINESS_requirements': 'Jsons/BUSINESS_parser_result.json',
        'IT_requirements': 'Jsons/IT_parser_result.json'
    }
    for file in files:
        vacancies = json.load(open(files[file], 'r'))
        result_data = []

        for group in vacancies:
            group_requirements = []
            for vacance in group['Все вакансии']:
                url = vacance['Ссылка']
                group_requirements += parse_requirements(url)
                
            result_data.append({
                'Группа': group['Группа'],
                'Требования': group_requirements
            })        

        save_to_json(result_data, file)

collect_requirements()
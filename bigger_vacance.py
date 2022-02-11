import json


def definer_bigger_vacance_in_group():
    files = {
        'BUSINESS_bigger_vacance': 'Jsons/BUSINESS_levels.json',
        'IT_bigger_vacance': 'Jsons/IT_levels.json'
    }
    for filename in files:
        file_data = json.load(open(files[filename], 'r'))
        data_with_bigger_vacance = []
        
        for item in file_data:
            max_level = -1
            bigger_vacance = item['Все вакансии'][0]['Вакансия']
            for vacance in item['Все вакансии']:

                if len(vacance['Вакансия']) < len(bigger_vacance):
                    # max_level = int(vacance['Уровень'])
                    bigger_vacance = vacance['Вакансия']
                    print(bigger_vacance)
                
            for vacance in item['Все вакансии']:
                if vacance['Вакансия'] == bigger_vacance:
                    vacance['Вес'] = 1
                else:
                    vacance['Вес'] = 0

        with open(f'Jsons/{filename}.json', 'w') as file:
            json.dump(file_data, file, ensure_ascii=False, indent=2)


definer_bigger_vacance_in_group()
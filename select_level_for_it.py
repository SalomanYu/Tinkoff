import json

def save_result(data):
    with open('Jsons/IT_levels.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def select_level():
    all_data = json.load(open('Jsons/IT_parser_result.json', 'r'))
    for group in all_data:
        for vacance in group['Все вакансии']:
            if vacance['Уровень'] == 'Middle':
                vacance['Уровень'] = 2

            elif vacance['Уровень'] == 'Senior':
                vacance['Уровень'] = 3
    
    save_result(all_data)

select_level()
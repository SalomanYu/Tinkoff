import json
import ru_core_news_lg

nlp = ru_core_news_lg.load()


def save_result(data):
    with open('Jsons/BUSINESS_levels.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def get_hotwords(text):
    global result_data
    levels_dict = { # Стоит ли добавлять сюда: Владелец, Секретаря руководителя относит к 3 категории
        1: ('junior', 'помощник', 'ассистент', 'младший', 'стажёр', 'стажер', 'assistant', 'intern', 'интерн', 'начинать'), # начинающий заменен на начинать с учетом лемматизации
        2: ('middle', 'заместитель', 'старший', 'lead', 'ведущий', 'главный', 'лидер'),
        3: ('senior', 'руководитель', 'head of', 'портфель', 'team lead', 'управлять', 'начальник', 'директор', 'head') # управляющий заменен на управлять с учетом лемматизации
    }

    doc = nlp(text.lower())
    vacance_level = 0
    for token in doc:
        for level in levels_dict:
            if token.lemma_ in levels_dict[level]:
                vacance_level = level
    
    return vacance_level
    

def select_level():
    result_data = []
    all_data = json.load(open('Jsons/BUSINESS_parser_result.json', 'r'))

    for group in all_data:
        for vacance in group['Все вакансии']:
            vacance_level = get_hotwords(vacance['Вакансия'])
            vacance['Уровень'] = vacance_level
            print('Изменен ', vacance['Вакансия'])

    save_result(all_data)

select_level()
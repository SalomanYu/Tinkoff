from base64 import encode
import json
from textwrap import indent
import ru_core_news_lg


all_requirements = json.load(open('Jsons/IT_requirements.json', 'r'))
nlp = ru_core_news_lg.load()

dublicate_list = []
result_data = []
stopwords = ['имеешь опыт работы в сфере','имеете опыт работы с', 'понимание и опыт работы с', 'имеешь опыт работы с', 'опыт работы с', 'опыт работы со',
                'навыки работы с',  'уверенное знание', 'уверенные знания', 'базовые знания' 'отличное знание',  'есть опыт написания', 'опыт разработки',
                'знание принципов', 'знание основ', 'понимание принципов', 'понимаете принципы', 'знаете принципы', 'умеете работать', 'умение работать' 'приветствуется',
                 'навык работы с', 'имеете работы с', 'мышление', 'опыт работы/ знание']

for group in all_requirements:
    requirements = group['Требования']
    for req in range(len(requirements)-1):
        first_req = requirements[req]
        for taby in stopwords:
            if taby in first_req.lower():
                first_req = first_req.lower().replace(taby, '').strip()
                break
        doc1 = nlp(first_req)
        for req2 in range(req+1, len(requirements)):
            second_req = requirements[req2]
            for taby in stopwords:
                if taby in second_req.lower():
                    second_req = second_req.lower().replace(taby, '').strip()

            doc2 = nlp(second_req)
            similary = doc1.similarity(doc2) * 100
            if similary > 90:
                dublicate_list.append(requirements[req2])
                print(f'{first_req} -- {second_req} -- {similary}')
    
    for item in dublicate_list:
        count = 0
        for item2 in requirements:
            if item == item2:
                count += 1
        if count > 1 and item in requirements:
            requirements.remove(item)
    
    result_data.append({
        'Группа': group['Группа'],
        'Требования': requirements
    })

with open('Jsons/IT_NO_DUBLICATE_REQ.json', 'w') as file:
    json.dump(result_data, file, ensure_ascii=False, indent=2)

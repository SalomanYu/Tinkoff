import json


def set_ids():
    all_data = json.load(open('Jsons/AMOUNT_result.json', 'r'))

    count = 0
    for group in all_data:
        group['id'] = count
        count += 1
    
    with open('Jsons/1FinalResult.json', 'w') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

set_ids()
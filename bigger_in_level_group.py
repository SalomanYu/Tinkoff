import json

def definer_bigger_vacance_in_level_group():
    files = {
        'BUSINESS_bigger_in_level_group': 'Jsons/BUSINESS_bigger_vacance.json',
        'IT_bigger_in_level_group': 'Jsons/IT_bigger_vacance.json'
    }

    for filename in files:
        file_data = json.load(open(files[filename], 'r'))
        data_result = []

        for item in file_data:
            group_data = []
            levels = (0, 1, 2, 3)
            for level in levels:
                group_level = []
                for vacance in item['Все вакансии']:
                    if level == vacance['Уровень']:
                        group_level.append(vacance)

                if group_level != []:
                    main_vacance_in_level_group = group_level[0]['Вакансия']
                else:
                    pass
                for vacance in group_level:
                    if len(vacance['Вакансия']) < len(main_vacance_in_level_group):
                        main_vacance_in_level_group = vacance['Вакансия']

                
                # print(main_vacance_in_level_group)
                # for vacance in item['Группа']:
                    # if level == vacance['Уровень'] and len(vacance['Вакансия']) < len(main_vacance_in_level_group):
                    # if level == vacance['Уровень']:

                #         print('Тут меньше')
                #         main_vacance_in_level_group = vacance['Вакансия']

                for vacance in item['Все вакансии']:
                    for level in levels:
                        if level == vacance['Уровень']:
                            if vacance['Вакансия'] == main_vacance_in_level_group:
                                vacance['Вес в уровне'] = 1
                            # else:
                            #     vacance['Вес в уровне'] = 0
        
        with open(f"Jsons/{filename}.json", 'w') as file:
            json.dump(file_data, file, ensure_ascii=False, indent=2)


# definer_bigger_vacance_in_level_group()
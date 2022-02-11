import json
import xlsxwriter


data = json.load(open('Jsons/1FinalResult.json', 'r'))

workbook = xlsxwriter.Workbook('Excel/result_excel.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Соответствия')
worksheet.write(0, 1, 'Вес профессии в соответствии')
worksheet.write(0, 2, 'Уровень должности')
worksheet.write(0, 3, 'Вес профессии в уровне')
worksheet.write(0, 4, 'Наименование професии и различные написания')

vacance_amount = 0
for item in data: vacance_amount +=  len(item['Группа']) # Нужно для цикла 

row_count = 1
for item in data:
    for vacance in item['Все вакансии']:
        try:
            weight_in_level = vacance['Вес в уровне']
        except KeyError:
            weight_in_level = 0
        worksheet.write(row_count, 0, item['id'])
        worksheet.write(row_count, 1, vacance['Вес'])
        worksheet.write(row_count, 2, vacance['Уровень'])
        worksheet.write(row_count, 3, weight_in_level)
        worksheet.write(row_count, 4, vacance['Вакансия'])

        row_count += 1

workbook.close()
import csv


def save_extract(category, path, labels, datas_list):
    # save data to csv file
    file_name = f"{category.replace(' ', '_')}__extract.csv"
    with open(file=f'{path}/{file_name}', mode='w', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in datas_list:
            writer.writerow(elem)

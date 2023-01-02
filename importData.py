def import_data(data, separator):
    with open('telephone_directory.csv', 'a', encoding='utf-8') as file:
        if separator is None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(separator.join(data))
            file.write(f"\n")

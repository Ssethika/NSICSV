import csv

class CSVFileFunctions:
    @staticmethod
    def read_csv_file_to_file(file_name: str):
        with open(file_name, mode="r", newline="") as file:
            reader = csv.DictReader(file, delimiter=";")
            reader = list(reader)
            print(reader)
        return reader

    @staticmethod
    def read_csv_file(file_name: str):
        with open(file_name, mode="r", newline="") as file:
            reader = csv.reader(file)
        return reader

    @staticmethod
    def fuse_csv_files(r1, r2):
        output_file = r1
        for i in r2:
            if not i in r1:
                output_file.append(i)
        return output_file
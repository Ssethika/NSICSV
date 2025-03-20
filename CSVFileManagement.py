from CSVFileFunctions import CSVFileFunctions
import csv

class CSVFileManagement:

    def __init__(self, f1: str, f2: str):
        self.reader1 = CSVFileFunctions.read_csv_file_to_file(f1)
        self.reader2 = CSVFileFunctions.read_csv_file_to_file(f2)
        self.output_reader = CSVFileFunctions.fuse_csv_files(self.reader1, self.reader2)
        self.write_output("output.csv")


    def write_output(self,filename, delimiter=";"):
        """Writes a list of dictionaries to a CSV file with a specified delimiter."""
        if not self.output_reader:
            print("Error: Empty data, nothing to write!")
            return

        # Extract headers from the first dictionary
        headers = self.output_reader[0].keys()

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=delimiter)

            writer.writeheader()  # Write column names
            writer.writerows(self.output_reader)  # Write all rows



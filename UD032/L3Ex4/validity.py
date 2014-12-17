"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
__author__ = 'zaorish'

import csv
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    with open(input_file, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        header = reader.fieldnames

        good = []
        bad = []
        for line in reader:
            uri = line['URI']
            if 'dbpedia.org' in uri:
                production_start_year = line['productionStartYear']
                date_reg_exp = re.compile('\d{4}')
                matches_list = date_reg_exp.findall(production_start_year)
                if matches_list:
                    year_candidate = matches_list[0]
                    if 1886 <= int(year_candidate) <= 2014:
                        line['productionStartYear'] = int(year_candidate)
                        good.append(line)
                    else:
                        bad.append(line)
                else:
                    bad.append(line)

    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        for row in good:
            writer.writerow(row)

    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        for row in bad:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()

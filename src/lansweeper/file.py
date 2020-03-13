import csv
import os


def is_string(variable):
    return isinstance(variable, str)


def extension(filename):
    _, ext = os.path.splittext(filename)
    return ext


class File:

    _default_indent = 2

    def __init__(self):
        pass

    @staticmethod
    def read(filename):
        with open(filename, 'r',) as f:
            return f.read()

    @staticmethod
    def read_csv(filename, encoding='utf-8', delimiter=',', headers=False):
        with open(filename, 'r', encoding=encoding) as f:
            if headers:
                reader = csv.reader(f, delimiter=delimiter)
                n = next(reader)
                results = []
                for line in reader:
                    item = {}
                    for x, y in enumerate(line):
                        item[n[x]] = y

                    results.append(item)

                return results

            else:
                return [i for i in csv.reader(f, delimiter=delimiter)]

    @staticmethod
    def read_json(filename):
        pass

    @staticmethod
    def write(ext, filename, variable):
        if isinstance(variable, str):
            File.write_plain(filename, variable)
        elif ext == '.csv':
            File.write_csv(filename, variable)
        elif ext == '.json':
            File.write_json(filename, variable)
        else:
            File.write_plain(filename, variable)

    @staticmethod
    def write_plain(filename, variable):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(variable + '\n')

    @staticmethod
    def append_plain(filename, variable):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(variable + '\n')

    @staticmethod
    def write_csv(filename, variable, delimiter=','):
        headers = isinstance(variable[0], dict) and list(variable[0].keys())
        with open(filename, 'w', encoding='utf-8') as f:
            w = csv.writer(f, delimiter=delimiter)
            if headers:
                w.writerow(headers)
                for row in variable:
                    if headers:
                        w.writerow([row[i] for i in headers])
                    else:
                        w.writerow(row)

    @staticmethod
    def append_csv(filename, variable):
        with open(filename, 'a') as f:
            w = csv.writer(f)
            w.writerow(variable)

    @staticmethod
    def write_json(filename, variable):
        pass
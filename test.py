import csv
import unittest


class CSVParseTest(unittest.TestCase):

    def setUp(self):
        with open('sample.csv', 'r') as csvfile:
            self.data = [row for row in csv.reader(csvfile.read().splitlines())]

    def test_csv_read_data_headers(self):
        self.assertEqual(
            self.data[0],
            ["header1", "header2", "header3", "header4", "header5", "header6", "header7", "header8", "header9",
             "header10", "header11"]
        )


if __name__ == "__main__":
    unittest.main()

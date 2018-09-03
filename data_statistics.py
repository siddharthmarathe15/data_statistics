from pprint import pprint

import pandas as pd

def get_data_statistics(name):
    """

    :param name: to get the statistics from this name

    To get the total occurrence count of the name.
    To get column-wise count of the name
    To get the column-wise count of all the names present in the file
    """
    data_set = {}
    headers = ["header1", "header2", "header3", "header4", "header5", "header6", "header7", "header8", "header9",
               "header10", "header11"]
    df = pd.read_csv("sample.csv")

    total_count = df[df == name].count().sum()
    column_wise_count = dict(df[df == name].count())

    for header in headers:
        data_set.update(df.groupby(header).agg({header: "count"}).to_dict())

    print "Name: [%s] occurs [%s] times in the file.\n" % (name, total_count)
    print "Column-wise count of [%s] in the file." % name
    pprint(column_wise_count)
    print "\nColumn-wise count of all the names present in the file."
    pprint(data_set)


if __name__ == "__main__":
    """
    List of all the names present in the file
    ["Adam", "Bob", "Claire", "Danny", "Emily", "Frank", "George", "Harry", "Ian", "Jack", "Kathrin"]
    """
    get_data_statistics("Adam")

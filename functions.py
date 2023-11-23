FILEPATH = "Reports.csv"

def get_reports(filepath=FILEPATH):
    """ Read a csv file and return the list of
    reports.
    """
    with open(filepath, "r", encoding="utf-8") as file_local:
        reports_local = file_local.readlines()
    return reports_local


def write_reports(reports_arg, filepath=FILEPATH):
    """Write report in the csv file"""
    with open(filepath, 'w', encoding="utf-8") as file:
        file.writelines(reports_arg)
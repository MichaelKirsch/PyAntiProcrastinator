from tempfile import NamedTemporaryFile
import shutil
import csv
import datetime




def add_time_to_today(bad_add, good_add):

    filename = 'data/data.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

    with open(filename, 'r', newline='') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quotechar='"')

        rows = []

        for row in reader:
            if row:
                rows.append(row)

        if not (rows[-1][0] == str(datetime.datetime.now()).split()[0]):
            rows.append([str(datetime.datetime.now()).split()[0], 0, 0])

        old_time_good = int(rows[-1][1])
        old_time_bad = int(rows[-1][2])
        old_time_bad += bad_add
        old_time_good += good_add

        print('addming time')
        print(good_add,bad_add)

        rows[-1] = [rows[-1][0], old_time_good, old_time_bad]
        for t in rows:
            writer.writerow(t)

    shutil.move(tempfile.name, filename)

    return old_time_bad>old_time_good

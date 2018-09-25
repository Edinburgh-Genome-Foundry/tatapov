import os
import urllib.request

import appdirs
import pandas
import flametree

DATA_FILES = {
    "25C": {
        "01h": "FileS1_01h_25C.xlsx",
        "18h": "FileS3_18h_25C.xlsx"
    },
    "37C": {
        "01h": "FileS2_01h_37C.xlsx",
        "18h": "FileS4_18h_37C.xlsx",
    }
}

DATA_PATH = os.environ.get('TATAPOV_DATA_DIR',
                           os.path.join(appdirs.user_data_dir(), 'tatapov'))

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

def list_missing_files():
    return [fname for data in DATA_FILES.values()
                  for fname in data.values()
                  if not os.path.exists(os.path.join(DATA_PATH, fname))]

def download_missing_files():
    response = urllib.request.urlopen(
        "https://www.biorxiv.org/highwire/filestream/98810/"
        "field_highwire_adjunct_files/1/322297-2.zip")
    zip_root = flametree.file_tree(response.read())
    data_root = flametree.file_tree(DATA_PATH)
    for fname in missing_files:
        zip_root[fname].copy(data_root._file(fname))

# This should only run once, at first use, to download the data files
missing_files = list_missing_files()
if missing_files != []:
    print ("Downloading missing data files for tatapov...", end=" ")
    download_missing_files()
    print ("Done.")
assert list_missing_files() == []


annealing_data = {
    temperature: {
        duration: pandas.read_excel(os.path.join(DATA_PATH, fname),
                                    index_col='Overhang')
        for duration, fname in data.items()
    }
    for temperature, data in DATA_FILES.items()
}
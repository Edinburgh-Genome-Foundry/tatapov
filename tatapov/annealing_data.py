import os
import urllib.request

import appdirs
import pandas

DATA_FILES = {
    "25C": {"01h": "FileS1_01h_25C.xlsx", "18h": "FileS3_18h_25C.xlsx"},
    "37C": {
        "01h": "FileS2_01h_37C.xlsx",
        "18h": "FileS4_18h_37C.xlsx",
        "2020_01h_BsaI": "pone.0238592.s001.xlsx",
        "2020_01h_BsmBI": "pone.0238592.s002.xlsx",
        "2020_01h_Esp3I": "pone.0238592.s003.xlsx",
        "2020_01h_BbsI": "pone.0238592.s004.xlsx",
    },
}

DATA_PATH = os.environ.get(
    "TATAPOV_DATA_DIR", os.path.join(appdirs.user_data_dir(), "tatapov")
)

if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)


def list_missing_files():
    return [
        fname
        for data in DATA_FILES.values()
        for fname in data.values()
        if not os.path.exists(os.path.join(DATA_PATH, fname))
    ]


def download_missing_files():
    # 2020 PLoS One paper:
    # An EGF repository was made for the data because weblinks are unreliable.
    datafiles_2020 = [
        "pone.0238592.s001.xlsx",
        "pone.0238592.s002.xlsx",
        "pone.0238592.s003.xlsx",
        "pone.0238592.s004.xlsx",
    ]
    link = (
        "https://github.com/Edinburgh-Genome-Foundry/tatapov_data/blob/main/pryor2021/"
    )
    for datafile in datafiles_2020:
        if datafile in missing_files:
            urllib.request.urlretrieve(
                link + datafile + "?raw=true",
                os.path.join(DATA_PATH, datafile),
            )  # "?raw=true" ensures retrieving the file rather than the website
            missing_files.remove(datafile)  # loop below goes through all for 2018 data

    # 2018 bioRxiv paper:
    # Original link cannot be downloaded anymore:
    # link = "https://www.biorxiv.org/highwire/filestream/98810/field_highwire_adjunct_files/1/322297-2.zip"
    # response = urllib.request.urlopen(link)
    # zip_root = flametree.file_tree(response.read())
    # data_root = flametree.file_tree(DATA_PATH)
    # for fname in missing_files:
    #     zip_root[fname].copy(data_root._file(fname))

    datafiles_2018 = [
        "FileS1_01h_25C.xlsx",
        "FileS3_18h_25C.xlsx",
        "FileS2_01h_37C.xlsx",
        "FileS4_18h_37C.xlsx",
    ]
    link = "https://github.com/Edinburgh-Genome-Foundry/tatapov_data/blob/main/potapov2018/"

    for datafile in datafiles_2018:
        if datafile in missing_files:
            urllib.request.urlretrieve(
                link + datafile + "?raw=true",
                os.path.join(DATA_PATH, datafile),
            )
            missing_files.remove(datafile)  # loop below goes through all for 2018 data


# This should only run once, at first use, to download the data files
missing_files = list_missing_files()
if missing_files != []:
    print("Downloading missing data files for tatapov...", end=" ")
    try:
        download_missing_files()
        print("Done.")
        assert list_missing_files() == []
    except urllib.request.HTTPError:
        print("Warning: unable to download data files for Tatapov")


try:
    annealing_data = {
        temperature: {
            duration: pandas.read_excel(
                os.path.join(DATA_PATH, fname), index_col="Overhang", engine="openpyxl"
            )
            for duration, fname in data.items()
        }
        for temperature, data in DATA_FILES.items()
    }
except:
    print("Warning: unable to find data files for Tatapov")
    annealing_data = {}

# -*- coding: utf-8 -*-
# Hugo Meinhof, 815220
# Date: 2023-07-26
"""installation script for the default word lists

provides a function for downloading and processing the two default word lists,
that are used in the quordle and sequence games. the funciton is also
executed, if this file is run.
"""
import os
import zipfile
import io
import requests
from process_wordlist import process_DeReWo_wordlist_2012


def download_and_process_data():
    # make the folder if it doesnt exist yet
    try:
        os.mkdir(os.path.join(os.curdir, "data"))
    except:
        pass

    # download the zip archive
    r = requests.get(
        "https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-ww-bll-320000g-2012-12-31-1.0.zip"
    )

    # create the zip object from the downloaded data
    z = zipfile.ZipFile(io.BytesIO(r.content))

    # make sure to only extract the one file we want
    member = None
    for name in z.namelist():
        if name.endswith(".txt"):
            member = [name]

    # now finally extract the file and save it
    z.extractall(os.path.join(os.curdir, "data"), members=member)

    # process the file we downloaded in a way that the game can use it
    process_DeReWo_wordlist_2012()

    # remove the old file we dont need anymore
    os.system("rm data/derewo-v-ww-bll-320000g-2012-12-31-1.0.txt")


if __name__ == "__main__":
    download_and_process_data()

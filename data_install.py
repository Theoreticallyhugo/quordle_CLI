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
    """installation script for the default word lists

    creates data folder if necessary, downloads data, unpacks and processes it,
    and removes leftver files from the process
    """
    # make the folder if it doesnt exist yet
    try:
        os.mkdir(os.path.join(os.curdir, "data"))
    except:
        pass

    # download the zip archive and handle errors
    try:
        response = requests.get(
            "https://www.ids-mannheim.de/fileadmin/kl/derewo/"
            + "derewo-v-ww-bll-320000g-2012-12-31-1.0.zip"
        )
    except requests.exceptions.Timeout as e:
        raise e(
            "the connection could not be established. Either you are not "
            + "connected to the internet or the server is down. "
            + f"code: {response.status_code}"
        )
    except requests.exceptions.ConnectionError as e:
        raise e(
            "the connection could not be established. there seems to be "
            + f"a network problem. code: {response.status_code}"
        )
    except requests.exceptions.TooManyRedirects as e:
        raise e(
            "the connection could not be established. request was "
            + f"redirected too many times. code: {response.status_code}"
        )
    except requests.exceptions.HTTPError as e:
        raise e(
            "the connection could not be established. invalid HTTP-"
            + f"response. code: {response.status_code}"
        )
    except requests.exceptions.RequestsException as e:
        raise e(
            "the connection could not be established. something very"
            + f"unexpected happened. code: {response.status_code}"
        )

    # if the status code isnt OK/ success, and yet it slipped through the cracks
    # of the previous error handling, raise an error
    assert (
        response.status_code == 200
    ), f"bad status code of response, code: {response.status_code}"

    # create the zip object from the downloaded data
    zip_data = zipfile.ZipFile(io.BytesIO(response.content))

    # make sure to only extract the one file we want
    member = None
    for name in zip_data.namelist():
        if name.endswith(".txt"):
            member = [name]

    # now finally extract the file and save it
    zip_data.extractall(os.path.join(os.curdir, "data"), members=member)

    # process the file we downloaded in a way that the game can use it
    process_DeReWo_wordlist_2012()

    # remove the old file we dont need anymore
    if os.path.isfile("data/derewo-v-ww-bll-320000g-2012-12-31-1.0.txt"):
        os.remove("data/derewo-v-ww-bll-320000g-2012-12-31-1.0.txt")
    # os.system("rm data/derewo-v-ww-bll-320000g-2012-12-31-1.0.txt")


if __name__ == "__main__":
    download_and_process_data()

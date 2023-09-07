# FEEDBACK a header would be nice :)
# FEEDBACK general thoughts: I like the detailed commentary and how you taught
# yourself to deal with zip-folders
import os
import requests, zipfile, io
from process_wordlist import process_DeReWo_wordlist_2012

def download_and_process_data():  # FEEDBACK missing docstring
    # make the folder if it doesnt exist yet
    try:
        os.mkdir(os.path.join(os.curdir, "data"))
    except:  # do not use bare except
        pass

    # download the zip archive

    # FEEDBACK If you don't want to have this gigantic link, you could use tinyurl/...
    # and set allow_redirects=True
    # Also, you could think about adding some error handling in case the
    # requests.get() doesn't work (no internet connection, ...)
    r = requests.get("https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-ww-bll-320000g-2012-12-31-1.0.zip")  # FEEDBACK maybe more descriptive variable names?

    # create the zip object from the downloaded data
    z = zipfile.ZipFile(io.BytesIO(r.content))  # FEEDBACK maybe more descriptive variable names?

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

    # FEEDBACK I know this info won't change any time soon but you could try to
    # find a way not to hardcode this part; the following worked:
    # os.remove(os.path.join(os.curdir, "data", member[0]))
    os.system('rm data/derewo-v-ww-bll-320000g-2012-12-31-1.0.txt')


if __name__ == "__main__":
    download_and_process_data()

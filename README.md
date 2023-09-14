# quordle_CLI
this game is a command line based quordle clone, 
written by:
Hugo Meinhof, 815220, me@theoreticallyhugo.de

### differences to the original quordle
- this game does not allow the player to input the same word twice, as it would not benefit the player. This is a conscious decision and not a mistake.
- just like with the original quordle, the player can cheat. instead of going online and googling todays quordle results, the player can enter ```!cheat``` which will display the words to be guessed.
## requirements
- python 3.10
- colorama
- requests
## data installation
**as data, the program needs two files: ```rate_worte.txt``` and ```ziel_worte.txt```. the following describes methods for getting the two default files, but they can be replaced by any other file with the same name and format.**
the process has been tested on MacOS and Linux Arch

- **AUTOMATIC**:
	- run `python data_install.py
	- if for some reason, this doesn't create a data folder within the games project folder, which contains two txt files, go through the steps for the manual installation process
- **MANUAL**: 
	- save the file located at:
		- https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-ww-bll-320000g-2012-12-31-1.0.zip
	- OR go to:
		- https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/
		- and manually download:
			- derewo-v-ww-bll-320000g-2012-12-31-1.0, Grundformliste, 326.946, 31. Dezember 2012
	- the obtained zip folder needs to be unpacked
	- a ```data``` folder needs to be created within the repositories folder, which by default is ```quordle_CLI``` and the txt file from the zip folder needs to be placed within said folder
	- to complete the installation, run `python process_wordlist.py

## running quordle_cli 
in order to run quordle_cli, you must always give it the flag for the game mode to be played. the simplest calls for the game therefore are `python main.py -q`and `python main.py -s`. the game uses two .txt files to source wordlists from. it can download, process and provide two default files, greatly simplifying the user experience. if no files are specified and the installation script hasnt run yet, the user is prompted, to run the installation script. getting the game ready is as simple as pressing enter. 
if a non default experience is desired though, the necessary files can be provided in two ways.
option 1:
- call the two files ziel_worte.txt and rate_worte.txt respectively, and put them in one folder.
- when running quordle provide either the absolute or relative path to that folder with the flag -f, like so: `python main.py -q -f <path_to_folder_with_the_two_.txt_files>
- this works for both game modes
option 2:
- provide the relative or absolute paths to the two files individually.
- `-r <path>` takes the path to the file of words that the user can enter for guessing
- `-z <path>` takes the path to the file of words that may become the words to be guessed
- both flags need to be provided simultaneously, in order to provide one full usable dataset. otherwise undefined behaviour may occur.

## tested on:
- MacOS Ventura
	- 13.5.2 (22G91), arm64, apple M1
	- 13.4.1 (c) (22F770820d), x86_64, intel I7
- Arch Linux 14th sept 2023 (rolling release), x86_64, intel I5
- Ubuntu 22.04.3 LTS, x86_64, intel I9
- Manjaro Uranos 23.0.0 (rolling release), x86_64, intel I9
- Raspbian GNU/ Linux 11 (bullseye), arm32, Cortex-A72
- Windows 11 home 22H2, x86_64, intel I9
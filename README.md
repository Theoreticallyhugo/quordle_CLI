# quordle_CLI
a command line based quordle clone
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
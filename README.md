# quordle_CLI
a command line based quordle clone
## data installation
**as data, the program needs two files: ```rate_worte.txt``` and ```ziel_worte.txt```. the following describes methods for getting the two default files, but they can be replaced by any other file with the same name and format.**
the process has been tested on MacOS and Linux Arch

- **POSIX**: on posix compliant systems (generally MacOS and Linux distros)
	- make sure that the cli commands "curl" and "unzip" are installed
		- if not installed, use the package manager of your choice, eg:
			- MacOS: `brew install curl
			- Linux Ubuntu: `sudo apt install curl
			- Linux Arch: `sudo packman -S curl
	- then ensure that you have a working internet connection and run the data_install.py script, eg: `python data_install.py
- **WINDOWS**: if you are running windows, the necessary commands may be installed, or possibly obtained through chocolatey, cygwin or WSL. otherwise, follow the manual installation steps.
- **MANUAL**: 
	- save the files located at:
		- https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-100000t-2009-04-30-0.1.zip
		- https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-ww-bll-320000g-2012-12-31-1.0.zip
	- OR go to:
		- https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/
		- and manually download:
			- derewo-v-100000t-2009-04-30-0.1, Wortformliste, 100.000,12. Mai 2009
			- derewo-v-ww-bll-320000g-2012-12-31-1.0, Grundformliste, 326.946, 31. Dezember 2012
	- the two obtained zip folders need to be unpacked, and two files need to be renamed like so:
		- ```derewo-v-100000t-2009-04-30-0.1``` becomes ```rate_worte.txt```
		- ```derewo-v-ww-bll-320000g-2012-12-31-1.0.txt``` becomes ```ziel_worte.txt```
	- a ```data``` folder needs to be created within the repositories folder, which by default is ```quordle_CLI``` and the two txt files need to be placed within said folder
	- with that the installation is complete (please just run something POSIX compliant...)
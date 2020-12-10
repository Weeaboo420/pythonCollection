Installation:

	#ADDITIONAL INFORMATION#
	<your path> means a directory or path of your choosing.
	You must use curl or alternatively wget to download the
	debian package, where the file ends up and what it is called
	is entirely up to you.


	Installation (using curl):

	curl -L tiny.cc/gd-debian -o <your path>/gd.deb
	sudo apt install <your path>/gd.deb

	Example:
		curl -L tiny.cc/gd-debian -o ~/Desktop/gd.deb
		sudo apt install ~/Desktop/gd.deb


	Installation (using wget):
	
	wget tiny.cc/gd-debian -O <your path>/gd.deb
	sudo apt install <your path>/gd.deb
	
	Example:
		wget tiny.cc/gd-debian -O gd.deb
		sudo apt install ./gd.deb

Uninstallation:

	To uninstall, simply issue one of the following commands:
	
	sudo apt remove gd

	OR

	apt remove gd

Updating:
	
	To update to the newest version you have to uninstall the current version of gd
	and then download the latest version. Simply follow the instructions inside the "Uninstallation"
	and "Installation" sections of this document in that order.


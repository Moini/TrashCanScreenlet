# TrashCanScreenlet
Desktop Screenlet that can read garbage collection dates from an ics file and reminds you when to bring out the trash cans. Images and parsing are preconfigured for German garbage types in combination with the ics file as given by [awr.de](https://www.awr.de/startseite/).

Requires the packages 'screenlets' and 'python-icalendar' to be installed. Screenlets package isn't available yet for Ubuntu 16.04, but you can download the [deb for trusty](http://launchpadlibrarian.net/116382997/screenlets_0.1.6-0ubuntu2_all.deb) and it will work.

If you would like to use it:
- copy the directory from this repository into ~/.screenlets
- if you're not using the ics file from awr, you probably need to adapt the screenlet. Instructions are inside the .py file, but you can also open an issue here if you need help.
- copy the ics file into the folder with the .py file.
- activate autostart for the screenlet.

Tested on LM18 Xfce.

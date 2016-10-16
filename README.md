# TrashPlanScreenlet
Desktop Screenlet that can read garbage collection dates from an ics file and reminds you when to bring out and fetch the trash cans. 

Images and parsing are preconfigured for German garbage types ('Papier' = Blue can (paper), 'Restmüll' = Black can (everything that doesn't fit into the other categories and is not glass or old clothes, or dangerous), 'Gelber Sack' = Yellow bag (packaging), 'Biomüll' = Brown Can (organic waste), 'Sperrmüll' = Bulky refuse, 'Strauchschnitt' = Bush (cuts from plants in the garden)) in combination with the ics file as given by [awr.de](https://www.awr.de/startseite/).

Requires the packages 'screenlets' and 'python-icalendar' to be installed. Screenlets package isn't available yet for Ubuntu 16.04, but you can download the [deb for trusty](http://launchpadlibrarian.net/116382997/screenlets_0.1.6-0ubuntu2_all.deb) and it will work.

If you would like to use it:
- copy the files from this repository into ~/.screenlets/TrashPlanScreenlet
- if you're not using the ics file from awr, you'll probably need to adapt the screenlet. Instructions are inside the .py file, but you can also open an issue here if you need help.
- copy the ics file into the folder with the .py file.
- activate autostart for the screenlet.

Tested on LM18 Xfce.

Licence: GPLv2 or higher

Screenshots:
Need to take garbage to the curb:

![need to take garbage to the curb](https://cloud.githubusercontent.com/assets/3240233/19420619/418ac42c-93ef-11e6-8aa3-bd76f3f6dbc4.png)

Need to fetch the cans:

![need to fetch the cans](https://cloud.githubusercontent.com/assets/3240233/19420618/418ab7ca-93ef-11e6-89a3-41787d6c0a3d.png)

All available icons:

![all available icons](https://cloud.githubusercontent.com/assets/3240233/19420620/418baf2c-93ef-11e6-83d4-6007abb42f1a.png)

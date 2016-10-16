#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This screenlet reminds you of bringing out the garbage cans.
Currently, you need to feed it with an ical file manually,
by editing the settings below. There's a helper function that 
can help you set the correct strings in the settings.
"""

import screenlets
from screenlets.options import IntOption
import cairo
import gobject

import datetime
import os

from icalendar import Calendar, Event, vText

# Settings
# TYPE_OF_GARBAGE = u"string_in_ical_file"

SPERR =   u"erst wieder 2017"
BIO =     u"Bioabfall(14-täglich)"
REST =    u"Restabfall(14-täglich)"
PAPIER =  u"Papiertonne(4-wöchentlich)"
STRAUCH = u"Strauchschnitt"
GELB =    u"Gelber Sack(14-täglich)"

ICALFILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Abfuhrtermine.ics')
print ICALFILE

# dictionary contents: 
# GARBAGESTRING : ('picture_file_basename', <garbage can needs to be retrieved: True/False>)
ICON_FILEBASES = {SPERR:   ('sperr', False),
                  BIO:     ('bio', True),
                  REST:    ('rest', True),
                  PAPIER:  ('papier', True),
                  STRAUCH: ('strauch', False),
                  GELB:    ('gelb', False)}


# run this once a year, or anytime you change the ical file,
# and replace the global values at the top, if needed:

def printEventTypeList(self, filename):
        """
        Do this once a year, so the names of the events can
        be matched with their corresponding icons. 
        """
        calfile = open(filename,'r')

        cal = Calendar.from_ical(calfile.read())
        
        eventTypeList = []
        
        for component in cal.walk('vevent'):
            
            eventType = unicode(component.get('summary'))
            if eventType not in eventTypeList:
                eventTypeList.append(eventType)

        calfile.close()
        for eventType in eventTypeList:
            print eventType

#printEventTypeList(ICALFILE)

class TrashPlanScreenlet(screenlets.Screenlet):
    """Shows you when to bring and fetch the garbage cans."""
    
    # default meta-info for Screenlets
    __name__ = 'TrashPlanScreenlet'
    __version__ = '0.1'
    __author__ = 'Maren Hachmann'
    __desc__ = __doc__

    def __init__(self, **keyword_args):
        screenlets.Screenlet.__init__(self, width=len(ICON_FILEBASES) * 60, height=60, uses_theme=True, **keyword_args) 

        self.theme_name = "Default"
        # add add default menu items
        self.add_default_menuitems()

    def __setattr__(self, name, value):
        screenlets.Screenlet.__setattr__(self, name, value)

    def on_draw(self, ctx):

        ctx.scale(self.scale, self.scale)
        ctx.set_operator(cairo.OPERATOR_OVER)
        
        if self.theme:
            ctx.translate(self.theme.width / 2.0, self.theme.height / 2.0);
            ctx.translate(-self.theme.width / 2.0, -self.theme.height / 2.0);

            for icon in self.getTodaysIcons():
                self.theme[icon].render_cairo(ctx)

            ctx.save()
                
    def on_draw_shape(self,ctx):
        ctx.scale(self.scale, self.scale)
        ctx.set_operator(cairo.OPERATOR_OVER)    
        if self.theme:
            self.on_draw (ctx)
            
    # Helper functions
    # ----------------
    def ical2dict(self):
        """
        Takes a filename of an ics file and
        returns a dictionary with dates as keys
        and and a list of events on that date as value.
        """

        calfile = open(ICALFILE,'r')

        cal = Calendar.from_ical(calfile.read())
        
        caldict = {}
        
        for component in cal.walk('vevent'):
            
            date = component.get('dtstart').dt
            if date not in caldict:
                caldict[date] = []
            
            filebase_and_retrievalinfo = ICON_FILEBASES[unicode(component.get('summary'))]
            caldict[date].append(filebase_and_retrievalinfo)

        calfile.close()
        return caldict

    def getTodaysIcons(self):
        """
        Returns a list of filenames for icons to display today.
        """
        
        eventDict = self.ical2dict()
        
        today = datetime.datetime.today().date()
        tomorrow = today + datetime.timedelta(days=1)
        
        todaysIcons = []
        
        if today in eventDict:
            for filebase, retrieval in eventDict[today]:
                if retrieval:
                    todaysIcons.append(filebase + '_fetch.svg') 
        if tomorrow in eventDict:
            for filebase, retrieval in eventDict[tomorrow]:
                todaysIcons.append(filebase + '_bring.svg')
        
        return todaysIcons
    

# If the program is run directly or passed as an argument to the python
# interpreter then create a Screenlet instance and show it
if __name__ == "__main__":
    import screenlets.session
    screenlets.session.create_session(TrashPlanScreenlet)

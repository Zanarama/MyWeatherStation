# code your activity here
# or replace this file with your python activity file
# import statements

"""
class exampleActivity(activity.Activity):

"""


# Sugar Imports
from sugar3.activity.activity import Activity
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityButton


# Gtk Import
from gi.repository import Gtk
from gettext import gettext as _

# Other imports
import datetime
import os

class Example(Activity):
    def __init__(self, sugar_handle):

        Activity.__init__(self, sugar_handle)

        # Create a Toolbar
        toolbar = Gtk.Toolbar()

        # Add toolbar to Sugar Activity Toolbar Space
        self.set_toolbar_box(toolbar)

        # Add Activity Button
        toolbar.insert(ActivityButton(self), -1)

        # filepath to write to journal
        filepath = os.path.join(self.get_activity_root(), "data")  

        #Load art assets?
        cloudimg = Gtk.Image()
        cloudimg.set_from_file('activity/art/Buttons/Cloudy.png')
        
        sunimg = Gtk.Image()
        sunimg.set_from_file('activity/art/Buttons/Sun.png')

        rainimg = Gtk.Image()
        rainimg.set_from_file('activity/art/Buttons/RainyCloud.png')

        snowimg = Gtk.Image()
        snowimg.set_from_file('activity/art/Buttons/SnowyCloud.png')

        stormimg = Gtk.Image()
        stormimg.set_from_file('activity/art/Buttons/ThunderCloud.png')

        windimg = Gtk.Image()
        stormimg.set_from_file('activity/art/Buttons/WindyCloud.png')

        hotimg = Gtk.Image()
        hotimg.set_from_file('activity/art/Buttons/HotSun.png')

        thermoimg = Gtk.Image()
        thermoimg.set_from_file('activity/art/Buttons/Thermometer.png')

        humidimg = Gtk.Image()
        humidimg.set_from_file('activity/art/Buttons/Humidity.png')

        # Create & Add Separator
        separator = Gtk.SeparatorToolItem(draw=False)
        separator.set_expand(True)
        toolbar.insert(separator, -1)

        # Add Stop Button
        toolbar.insert(StopButton(self), -1)

        # Create Container
        grid = Gtk.Grid()

        # Add grid to Sugar Activity GtkWindow
        self.set_canvas(grid)

        # Create & Add Label
        label = Gtk.Label(label=_("Weather: "))
        grid.attach(label, 0, 0, 1, 1)

        # Add Output Label
        output = Gtk.Label()
        grid.attach(output, 0, 6, 5, 1)

        # Create & Add Text Entry x2
        entry = Gtk.Entry()
        grid.attach(entry, 1, 1, 2, 1)
        entry2 = Gtk.Entry()
        grid.attach(entry2, 1, 2, 2, 1)

        # Empty output on keypress in entry
        entry.connect('key-release-event', self.emptyout, output)
        entry2.connect('key-release-event', self.emptyout, output)

        # Add buttons
        sunnyButton = Gtk.Button(image=_(sunimg))
        grid.attach(sunnyButton, 0, 3, 1, 1)
        
        cloudyButton = Gtk.Button(image=_(cloudimg))
        grid.attach(cloudyButton, 1, 3, 1, 1)

        rainyButton = Gtk.Button(image=_(rainimg))
        grid.attach(rainyButton, 2, 3, 1, 1)

        snowyButton = Gtk.Button(image=_(snowimg))
        grid.attach(snowyButton, 3, 3, 1, 1)

        stormyButton = Gtk.Button(image=_(stormimg))
        grid.attach(stormyButton, 4, 3, 1, 1)

        hotButton = Gtk.Button(image=_(hotimg))
        grid.attach(hotButton, 5, 3, 1, 1)

        windyButton = Gtk.Button(image=_(windimg))
        grid.attach(windyButton, 6, 3, 1, 1)

        tempButton = Gtk.Button(image=_(thermoimg))
        grid.attach(tempButton, 0, 1, 1, 1)

        humidButton = Gtk.Button(image=_(humidimg))
        grid.attach(humidButton, 0, 2, 1, 1)

        # Tell the buttons to run a class method
        sunnyButton.connect('clicked', self.showWeather, "Sunny", entry, entry2, output)
        cloudyButton.connect('clicked', self.showWeather, "Cloudy", entry, entry2, output)
        rainyButton.connect('clicked', self.showWeather, "Rainy", entry, entry2, output)
        snowyButton.connect('clicked', self.showWeather, "Snowy", entry, entry2, output)
        stormyButton.connect('clicked', self.showWeather, "Stormy", entry, entry2, output)
        hotButton.connect('clicked', self.showWeather, "Hot", entry, entry2, output)
        windyButton.connect('clicked', self.showWeather, "Windy", entry, entry2, output)

        # Show all components (otherwise none will be displayed)
        self.show_all()

    def greeter(self, button, entry, entry2, output):
        if len(entry.get_text()) > 0:
            output.set_text("WEATHER TODAY IS: \n" + entry.get_text() + "\n" + entry2.get_text())
        else:
            output.set_text("Enter the weather.")

    def showWeather(self, button, state, entry, entry2, output):
        output.set_text("Weather State is: " + state + ". " + "Temperature is " + entry.get_text() + ". Humidity is " + entry2.get_text())

    def emptyout(self, entry, entry2, event, output):
        output.set_text("")

    def write_files(self, file_path, weather, temperature, humidity):
        logging.debug('Writing Weather Data...')
        date = datetime.datetime.now()

        # save current state
        self.metadata['date'] = date
        self.metadata['weather'] = weather
        self.metadata['temperature'] = temperature
        self.metadata['humidity'] =  humidity

        # write data to journal for posterity
        f = open(file_path, 'w')
        try:
            f.write(date+"|"+weather+"|"+temperature+"|"+humidity+"\n")
        finally:
            f.close()

    """def read_file(self, filepath):
        logging.debug('Reading activity data..')
        data = self.get_data(file_path)

        for entry in data:
            # process data into Weather Objects

    def get_data(self, filepath):
        fd = open(file_path, 'r')
        try:
            data = fd.read()
        finally:
            fd.close()
        return data"""

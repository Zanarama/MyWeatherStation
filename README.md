#MyWeatherStation

This is the documentation for the MyWeatherStation XO Activity Started in 2013 in the RIT HFoss course. Credit for the initial project goes to Suzanne Reed, Chris Cordi, Greg Ekstrom, and Rob Clifford.
The first set of information for the project is the specifics of the MyWeatherStation project, and then the rest will be the README from the Sugar_Activity_QuickStart on which our project is based. 

#Overview

In essence, MyWeatherStation is an XO application designed to allow the user to report the weather and temperature conditions in their area to their XO Journal, in order to improve the state of meteorological information for the international
community, as well as to make it easier for people in remote regions of the world to track and improve their weather reporting in order to better plan for seasonal changes. 

#Functionality
The objective for this project was originally to create something that could easily convert the data taken in by the XO sensor attatchments, into a format that could readibly show the temperature and humidity in the area where the user is pulling the information. The reality has instead become moreso that we are relying a bit more on the user to track much of the weather themselves, while still leaving it open for future developing that would enable the use of the sensors. For now though there are three main states of the activity that are important to mention. 

1. Main Menu
2. Weather Input
3. Calendar View

The function of each of these states is explained below, and is obviously open to changes based on the evolving needs of the user base, as well as the aspirations of new developers, this is just the baseline of what this activity does. 

#Main Menu
The main menu serves the very basic purpose of allowing the user to select between the two other major states of the game, and then go back after viewing them, in order to get to the other. In the first iteration this screen should have the calendar view, as well as the input screen as the two options.

#Weather Input
This is the majority of the activity. The input screen is a place where there will be a number of buttons, each representative of a different weather condition that the user can select as a way to track how the climate in their place of residence is progressing over time. They will then input the temperature and humidity in at the bottom, or in the future they will have the option of allowing the sensor peripheral take in the barometric and temperature data.

#Calendar view
This is the screen on which the user will be viewing the data about how the weather has progressed over time. They should have access here to a visual calendar that they can see the weather they put in on different days, as well as the temperature on those days. It is possible that a good idea for the future would be to put in the functionality of selecting a specific day and either making notes about the weather, or to simply be able to view the data individually for that day directly from the calendar screen.

#To Build
This project was created using the Sugar Activity Quickstart. To build the project run:

    ./setup.py genpot
    ./setup.py build
    ./setup.py dist_xo

You have now created an xo file to run.

#Licencing
This project is licenced under GPL3+.

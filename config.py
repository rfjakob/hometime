# Calendar

CALENDAR = "INSERT YOUR CALENDAR NAME"          # "@group.calendar.google.com" also has to be on the end of the string (see 'get shareable link' on calendar on google 
APIKEY = "INSERT YOUR APIKEY" 
TIMEZONE = "Europe/Zurich"
GOOGLECALBOOL = False                           # Boolean for whether to check google calendar page. If you do not want to use Google Calendar, set to False
REFRESH = 15                                    # Seconds between updates of neopixel
GOOGLE_REFRESH = 40                             # Cycles of updates before Google Calendar gets refreshed
IGNORE_HARDCODED = False                        # Set to True if you want Clock in at the start of first meeting and Clockout at end of last meeting
SCHEDULE = {                                    # This doesn't get used if IGNORE_HARDCODED is True. Othewise, it's the working hours for the week. (9.5 = 09:30 AM; 13 = 01:00 PM)
    "monday":     [{"clockin": "0",   "clockout": "23.9"}],
    "tuesday":    [{"clockin": "0",   "clockout": "23.9"}],
    "wednesday":  [{"clockin": "0",   "clockout": "23.9"}],
    "thursday":   [{"clockin": "0",   "clockout": "23.9"}],
    "friday":     [{"clockin": "0",   "clockout": "23.9"}],
    "saturday":   [{"clockin": "0",   "clockout": "23.9"}],    # I don't roll on shabbos
    "sunday":     [{"clockin": "0",   "clockout": "23.9"}]
}

# Neopixel

PIXELS = 144                                    # The number of pixels on the neopixel strip
GPIOPIN = 15                                    # The pin that the signal wire of the LED strip is connected to
BARCOL = [(0, 10, 10), (0, 0, 100)]             # Color in RGB from 0 to 255
EVENTCOL = [(255, 255, 255), (255, 255, 0)]     # list of tuples used as meeting colors, if you only use one: [(255, 255, 255)]
DISPLAY_EVENTS = True                           # Shows events
FLIP = False                                    # Set to True if you want to flip the bar

# Other

TWOCOL = False                                  # Displays a second bar that shows the progress of an event. While event is active, other events are not displayed anymore.
DELWIFI = False                                 # Deletes wifi credentials if the connection fails

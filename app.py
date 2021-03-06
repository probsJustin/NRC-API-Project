
# Nuclear Information Gathering API Test
# Nuclear Regulatory Commission
# Info A: https://www.nrc.gov/developer.html
# Info A Documentation: https://www.nrc.gov/site-help/developers/wba-api-developer-guide.pdf

# International Atomic Energy Agency
# Info B: https://www.iaea.org/resources/databases/power-reactor-information-system-pris

# Related pypi modules 'nrc_scrape' https://pypi.org/project/nrc-scrape/
# Related pypi modules 'NuclearTools' https://pypi.org/project/NuclearTools/
# Related pypi modules 'pyrk' https://bids.berkeley.edu/resources/videos/pyrk-python-package-nuclear-reactor-kinetics

# I am planning to build this out to have a UI that has a map where you can see all of the nuclear plants on the globe and click on them and get info
# I think this is a good idea to use QT as I have already used TK: https://www.qt.io/qt-for-python
# I am going to start with this example/tutorial and then see if I can help the shapefile a bit to see if I can make it better:
# https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0

# other QT tutorials: https://doc.qt.io/qtforpython/examples/index.html

# Nuclear power plant list from the global energy observatory: http://globalenergyobservatory.org/list.php?db=PowerPlants&type=Nuclear
# Database tools for global energy observatory: http://globalenergyobservatory.org/docs/Overview_of_Structure.php

# it looks like there is a good tool to get this: https://github.com/Open-Power-System-Data/conventional_power_plants/blob/2020-10-01/main.ipynb

# TODO: need to identify a way to make a global clickable map that has pin points on it. I am thinking I might stick with QT
# Here are some examples for the map viewer for QT - perhaps we could do something like this?

# REGEX for stripping html from text: <[^>]*>
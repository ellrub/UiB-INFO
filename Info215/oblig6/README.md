# D3 Program
---
Start by declaring a global variable so that the

# Data
---
`sampleData.csv` contains 24 entries with weather data over a single day.

#### The data
1. Date
    * The task says that different weather data will be tested on the program, so i assumed that the date will stay the same, and so the date is just hardcoded into the grid.
2. Time
    * This was used to determine where to place an icon on the X axis, as well as which icon to display.
    * A string that had to be parsed as an integer.
    * Since it was only whole hours, i decided to convert it to base 10 numbers to just use 0 through 23.
3. Temperature
    * Used to determine where to place an icon on the Y axis.
4. Precipitation
    * Used to determine which icon to display.
    * Since there where some rain throughout the day, i decided to have some clouds on all the icons.
# Welcome.
The University of Maryland Police Department has a website where activity and arrest data live and are updated. However, the data is sequestered and inaccessible: each month of activity is in its own webpage, and fields are not sortable nor filterable by search. Data also are not stored in a pure tabular format; location data are stored as every other row related to the row of data above. Arrests, while they share case numbers with activity logs, are not linked whatsoever to their counterparts. 

This web app seeks to fix all these problems. Police data is scraped every morning and pulled into a simple Flask app with a paginated, searchable datatable, which is frozen daily for quick load times. New data is tweeted out, as well, for reporter alerts. 

## Repository. 
The templates folder holds my index.html file, and my stylesheet and javascript all live in the static folder When frozen, the entirety is knit together into the build folder. All data is updated in the data folder, which holds separate csvs for arrests, activity, and new and updated data separately. Python scripts for running the app locally and for freezing the app locally also live in the repository, as does my twitter bot script and the scraping scripts.

## [Site Link.]( https://rachelll4.github.io/na-gov-upgrade/build/index.html)
The site is very basic: a small introduction and the data table. Click on the More button on an activity item to see arrest activity. Search on any column with the search bar, and click on column headers to sort ascending or descending.

## [Twitter Link.](https://twitter.com/UMPDLogs)
The Twitter bot currently tweets out only new content, and each activity item gets its own tweet. 

## Efforts.
This project began as a government website upgrade. My goal was just to make the existing data more malleable. Originally, I scraped just the most recent data with a Beautiful Soup script, then threw it all clumsily into a table in a frozen Flask app. My goal was to facilitate quick data access, with an all-in-one-page experience that didn’t necessarily need a back-end. I put arrest info in detail pages if only because that was the code example I followed. 

I thought a lot about making a map to go with this app, but the biggest problem was that sometimes, the data came with direct addresses that could be geocoded at latitude and longitude, and sometimes the address was a road or an area, which would be much harder to map. If I could draw my own polygons, I would’ve run with it anyway, but that was deemed outside the scope of this project. 

I had some issues dealing with data types early on, also, and had a rough time with Jinja syntax. I ended up using a lot more pandas DataFrames than I anticipated-- I thought I was staying away from pandas, but now I see it’s just as boring-matrix/array syntax as your average package provides.

The dates in my data gave me a bit of a tough time at first, because the police data was saved as the gross YYYY-MM-DD HH:mm format. It was making it easy to sort by date, but hard for users to understand the timing. I eventually applied datetime to the column on render in my javascript so that what showed in the table was human legible, but what ran the insides and sorted was the computer-legible format.

I also had a heck of a time with duplicates and updated data. When I scrape, I take every month from the last two years in order to solve for updates from Dec. 31 of one year to Jan. 1 of the next. I append all that scraped data to my existing data, then filter out duplicates from the case number column, saving the more recent in cases of duplication. For finding new data, I take all my data, grab just the most recent two months, then remove all duplicates from the previous data-- anything that was just rescraped from the day before. For updates, I check for duplicated case numbers and duplicated full rows and grab only those rows that with present case numbers, but different previous records: case number match but not rescrape match. This logic took me a while to figure out. At one point, I was only de-duplicating my data based on entire rows, which meant that when a case was updated with a different Disposition, it was saved as a new record-- de-duplicating on case number fixed that.

I built out a simple Slack bot to get a handle on webhook processes, which was a lot of fun but ultimately only helpful in setting up an automated GitHub Action to run the script daily.

When the Twitter bot entered the picture, it started absorbing all of my time and throwing it into the abyss. I messed with the authorization levels and Twitter API levels for several weeks, trying to figure out what I was doing wrong with my Essential access. It turns out, it was my local machine holding me back. I was able to use the Client method of accessing the Twitter API with a GitHub Action and saving my environment variables as repository secrets, which was resulting in a 403 forbidden error if I ran it in a Python script-- but not straight in the Python shell. 

## Maintain.
Ultimately, there were many aspects of this project that I didn’t end up working out. I wanted a days-since module, I wanted to color code by type of crime and I wanted to have some sort of map. I also wanted to Tweet in threads and have a separate thread for updates. This website and bot package is still incredibly useful to reporters, but I plan to continue to push patches into the summer to flush out the usability. I’ll check on my Actions every once in a while to see if anything fails.

I also wanted to make the website useful as an alert system-- when there’s more than usual arrests in a week, or when several DUIs are charged in a single night. Weekly stats, which I thought I might Tweet originally, might still be in the cards.

## Outlive.
Once this is running, there shouldn’t be much of a change. My GitHub is linked in my byline at the top of the app, so anyone who uses this has a way to contact me if things break into the future. I’m not expecting to have to sunset this for a while, since even if the links break, it’ll be useful as an archive of previous data. 


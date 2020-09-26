Dear Programmer,

Good day to you!

I am Snehasis Ghosh, a Data Engineer by profession. I would like to share with you a recent project I did on a comparative study on the technologies in demand currently. 

Introduction
============

The intention behind the project was to identify and compare the technologies in demand as well as the respective job openings. The project considers cloud technologies and programming languages as the basis for this study. 
The data is obtained by using the stack exchange query explorer (https://data.stackexchange.com/) to get results from https://stackoverflow.com/. The data for job markets is obtained from https://www.indeed.com/ using beautifulsoup

The project also uses the google map api https://maps.googleapis.com to accurately determine the job locations.

The analysis is published in a Tableau dashboard the snapshots of which you can find in the TableauDashboardSnaps directory


Technology Stack
================
Python3


Pre-requisites
==============

Python 3 installation

Tableau or any other BI tool (optional - if you do not want to visualize the data)

Code Walkthrough
================

The project is comprised of a couple of python scripts, the details of which are provided below-

ScrapeStackovrflwIndeed.py: This is the main script which scrapes the indeed job portal of different countries. The script also pulls stats from stackoverflow.com using the pre-defined query on the stack exchange query explorer

GeoLocator.py: This script calls the google map api to cleanse and accurately determine the geo location of the job openings


Please reach out to me in case you need help or you have suggestions. I am open to feedback.

Regards,

Snehasis Ghosh

LinkedIn: https://linkedin.com/in/snehasis-ghosh-b17b30a3

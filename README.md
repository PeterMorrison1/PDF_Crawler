# PDF_Crawler
This project was a quick script to see if I could replicate the feature on Distiller which allows users to download free articles as PDFs from PubMed. This script successfully identifies free articles with an accuracy rate identical to the Distiller feature.


## Journal PDF Downloader
After completing this script I looked to create a more fully featured and more maintainable script that can identify significantly more free articles. The new project is called Journal PDF Downloader.

This project is currently on hiatus until classes are completed. However, as it currently stands it is significantly more accurate than other free medical journal downloaders available. I have not made this available yet as I intend on increasing the functionality first.


## How to run the project
The only requirement - besides Python and the dependencies - is creating an excel file with data following this format with no headings:
| id | author list | article title | year published |


# Note
This project does not circumvent any payments. This project simply uses Python to automate the process of downloading free journal articles from PubMed. This is an experiment to learn more automation using Python and for fun.
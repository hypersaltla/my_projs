my_projs
========
Author: Ace Yan
Intro: The web data extractor sample fetched all the information of artists and art collections from Getty Center website.

Web data extractor guidelines:

1. The program is developed under Python 3.3 environment along with its "urllib" library to make HTTP requests

2. Install BeautifulSoup 4 on the Python33 Directory
   ---download here "http://www.crummy.com/software/BeautifulSoup/#Download"
   ---then run "setup.py"

3. Run with command "python web_scraper.py" to extract data from website. Note that information are stored seperately by the capitals of artist's lastname.

4. You need to run with command "python merge.py" to merge the datasets to be a single valid json file

5. An error log is output as "err_log.txt" so that you can see the page download abnormally

6. Sample format of datasets (in JSON format):
   for artists:
   [{
            "artist_name": "Domenico Campagnola",
            "nationality": "Italian",
            "birth_data_and_place": "b.  1500 possibly Venice, Italy, d.   1564 Padua, Italy",
            "long_biography": "A German artisan's son, child prodigy Domenico Campagnola probably learned from his adopted father, who instructed him in painting, drawing, engraving, and woodcutting. After his father's death around 1516, Campagnola was Venice's foremost printmaker. He innovated bycuttingwoodblocks himself rather than employing a professional woodcutter. His earliest prints and drawings show the influence of German artist Albrecht D�rer. Campagnola's lush, flowing style and religious subject matter may also indicate access to Titian's workshop.By around 1520 Campagnola moved to Padua, where he became its busiest and most praised painter. Hisfrescoesand easel paintings for churches and palaces betray his Venetian origins with their asymmetrical compositions and rich treatment of fabrics. Nevertheless, he remained most celebrated for hiswoodcutsand landscape drawings, which he sold as finished compositions. He drew raised foregrounds set against poetic vistas of paths, castles, bridges, and ruins, with jagged peaks of distant mountains.",
            "occupation": "Printmaker"
       },
       ...
    ]

    for artwork:
    [
	{"technique": "Pen and brown ink, brown and ocher wash, heightened with white bodycolor", "nationality": "Italian", "access_id": "84.GG.22", "description": "Humans and animals co-exist peacefully in this lush, fantastical setting. In the foreground, graceful nude figures lounge or pose elegantly like statues, while two small boys urinate into a stream that flows into a small pool. In the background, figures dance in a circle; high above in the distance, others sit on a hill and watch wild animals at play.Jacopo Zucchi made this highly finished compositional study, or modello, for the small scale paintingThe Age of Gold, now in the Uffizi Gallery in Florence, Italy. The Golden Age, the first of four ages of the world in classical mythology, followed immediately after the world's creation and was an earthly paradise akin to the Christian Garden of Eden.", "date_made": "1565", "artist_name": "Jacopo Zucchi", "dimensions": "18 7/8 x 14 7/8 in.", "img_url": "www.getty.edu/art/collections/images/l/00006701.jpg", "title": "The Age of Gold"},
	...
    ]

![](https://i.imgur.com/VsUwCLR.png)
- This is a simple platform which you can run locally to test simple web scrapers.
- There's no support for web browsers to run javascript or anything else fancier other than regular HTTP GET requests at this time.

## Setup
Install the required python libraries:
```
pip install -r requirements.txt 
```

## Building a new scraper
- Copy/paste the `argos.py` file in `/scrapers` and rename it
- In `/scrapers/__init__.py` add your new scraper to the top and edit the if-statement to include it

## Testing your scraper
- Empty the `testing/input.csv` file and add your links to it
- Run `python main.py`
- See the results in `testing/output.csv`
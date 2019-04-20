import time

from utils import intput_output
from utils.http import get_page
from utils.validation import get_errors
import scrapers

urls = intput_output.import_urls()
output = []
for url in urls:
    html = get_page(url)
    result = scrapers.scrape(url, html)    
    errors = get_errors(result)
    output.append({'url': url,'errors': errors,'result': result})
    print('Scraped {} with {} errors'.format(url, len(errors)))
    time.sleep(1) #  to avoid spamming

intput_output.export_results(output)
print('Scrape complete! See: ' + intput_output.OUTPUT_FILE)
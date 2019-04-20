import csv, json

INPUT_FILE = 'testing/input.csv'
OUTPUT_FILE = 'testing/output.csv'

def import_urls():
    urls = []
    with open(INPUT_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            urls.append(row[0])
    assert urls, 'No urls found in ' + INPUT_FILE
    return urls

def export_results(output):
    with open(OUTPUT_FILE, mode='w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['errors', 'url', 'result'])
        for row in output:
            writer.writerow([
                json.dumps(row['errors']),
                row['url'],
                json.dumps(row['result']),
            ])
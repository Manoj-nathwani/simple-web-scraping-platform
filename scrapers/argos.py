def parse(html):

    # get price
    price_divs = html.find_all('li', class_ = 'product-price-primary')
    price = price_divs[0]['content']

    # get image
    images = html.find_all('img', class_='ac-media-gallery__main-image')
    image = 'https:' + images[0]['src'].split('?')[0]

    # get description
    descriptions = html.find_all('span', class_='product-title')
    description = descriptions[0].text

    return {
        'price': float(price),
        'image': str(image),
        'description': str(description)
    }
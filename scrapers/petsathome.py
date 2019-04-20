def parse(html):

    # get price
    price = html.find('span', 'pdp-price__price').text

    # get image
    image = html.find('img', class_='pdp-image-viewer__img')['src']

    # get description
    description = html.find('h1', class_='pdp-heading-ratings__title').text.strip()

    return {
        'price': float(price),
        'image': str(image),
        'description': str(description)
    }
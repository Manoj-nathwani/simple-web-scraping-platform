def get_errors(parsed_page):
    errors = []

    # validate type
    type_validations = [
        {'key': 'price', 'type': float},
        {'key': 'image', 'type': str},
        {'key': 'description', 'type': str}
    ]
    for x in type_validations:
        if not type(parsed_page[x['key']]) == x['type']:
            errors.append(
                '{} not formatted as {}'.format(x['key'], x['type'])
            )            

    # validate data
    if not parsed_page['price'] > 0:
        errors.append('price must be > 0')
    if not len(parsed_page['image']):
        errors.append('image length must be > 0')
    if not len(parsed_page['description']):
        errors.append('description length must be > 0')

    return errors
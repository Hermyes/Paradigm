
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]

def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            field_name = args[0]
            if field_name in item and item[field_name] is not None:
                yield item[field_name]
        else:
            filtered_item = {}
            for field in args:
                if field in item and item[field] is not None:
                    filtered_item[field] = item[field]
            if filtered_item:
                yield filtered_item

for title in field(goods, 'title', 'price'):
    print(title)
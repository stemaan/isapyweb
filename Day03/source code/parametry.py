# przypomnienie jak działają *args i **kwargs

def funkcja(a, b, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print('args', args)
    print('kwargs', kwargs)


funkcja(99.99, 10, 20, 30, vat=100, cit=43)





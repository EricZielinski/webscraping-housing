from parsers.bs import BS


def html_parser_factory(parser, page):
    parsers = {"BeautifulSoup": BS}
    if parser in parsers:
        if parser == "BeautifulSoup":
            return BS(page)
    else:
        raise ValueError("Unknown parser")



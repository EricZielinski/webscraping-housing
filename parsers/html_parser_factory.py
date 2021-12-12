from parsers.bs import BS

#refactor
def html_parser_factory(parser, page):

    parsers = {"BeautifulSoup": BS}
    if parser in parsers:
        if parser == "BeautifulSoup":
            return BS(page, "html.parser")
    else:
        raise ValueError("Unknown parser")



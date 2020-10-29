# importing headerz module
# install it with pip

from headerz import headerz

# calling headerz function
hd = headerz()

#header parser function
def parser(header_string):
    raw_parser_result = hd.header_parser(header_string)
    # result of header_parser() attribute is json
    return raw_parser_result

if __name__=='__main__':
    header_string = hd.header_input()
    # the header_input() is headerz attribute to get header input from user
    parsed_header = parser(header_string)
    print(parsed_header)

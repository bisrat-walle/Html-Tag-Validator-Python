"""
Title: HTML tag checker
Created by: Bisrat Walle
Email: bisratwalle3@gmail.com
"""

tag_pairs = {
    '<html>': "</html>",
    '<head>': "</head>",
    '<title>': "</title>",
    '<body>': "</body>",
    '<div>': "</div>",
    '<span>': "</span>",
    '<table>': "</table>",
    '<thead>': "</thead>",
    '<tbody>': "</tbody>",
    '<tr>': "</tr>",
    '<td>': "</td>",
    '<script>': "</script>",
    '<img>': "</img>",
    '<ul>': "</ul>",
    '<li>': "</li>",
    '<strong>': "</strong>",
    '<p>': "</p>",
    '<hr>': "</hr>",
    '<br>': "</br>",
    '<a>': "</a>",
    '<col>': "</col>",
    '<embed>': "</embed>",
    '<meta>': '</meta>',
    '<link>': '</link>',
    '<!DOCTYPE>': ""
}

self_closing_tags = ['<link>', '<hr>', '<meta>', '<br>', '<col>', '<img>', '<embed>',
                     '<!DOCTYPE>'.lower()]  # doctype declaration is case-insensitive
optional_closing_tags = ['</link>', '</hr>', '</meta>', '</br>', '</col>', '</img>', '</embed>']


def tag_search(html_document):
    """
    This function searches all the tags in the html document
    :param html_document:
    :return All the tags as a list:
    """
    tags = []  # tag container
    index = 0
    while index < len(html_document):   # traverse through all the document
        tag = ''
        if html_document[index] == '<' and html_document[index + 1] != '!':  # if it gets tag opening angle bracket
            # and if It is not an html comment(<!)
            while html_document[index] != '>':  # It goes all the way up to '>'
                tag += html_document[index]
                index += 1
            tag += html_document[index]   # append the closing angle bracket
            tags.append(tag)
        else:
            index += 1  # if It can't get an opening angle bracket, It skips it
    return tags


def tag_attribute_remover(tags):
    """
    This function modifies the tags by removing their attributes
    :param tags:
    :return None:
    """
    for i in range(len(tags)):
        if ' ' in tags[i]:  # if there is white space
            split_tag = tags[i].split()
            tags[i] = split_tag[0] + '>'  # append the closing angle bracket


def check_closing_existence(tags, opening, closing):
    """
    This function checks if the passed opening tag has corresponding closing tag
    And It removes the closing tag if it matches
    :param tags:
    :param opening:
    :param closing:
    :return True if it gets a match, false otherwise:
    """

    if opening.lower() in self_closing_tags:  # self closing tag
        return True

    opening_index = tags.index(opening)
    for index in reversed(range(opening_index, len(tags))):  # traverse from the end
        if tags[index] == closing:
            tags.remove(tags[index])
            return True
    return False


def html_tag_checker(html_file):
    """
    This function open and read the html file then checks for a tag validity
    :param html_file:
    :return:
    """
    html_file = open(html_file, 'r')
    html_document = html_file.read()

    tags = tag_search(html_document)   # calling the tag searcher function
    tag_attribute_remover(tags)     # calling the attribute remover function

    openings = []
    for tag in tags:
        if tag in tag_pairs.keys():
            openings.append(tag)

    tag_size = len(openings)


    for counter in range(tag_size):
        current_tag = openings.pop()
        if check_closing_existence(tags, current_tag, tag_pairs[current_tag]):   # if match exist 
            continue
        else:
            return "Sorry, your html document iS INVALID"
    extra_closing_tag = False
    for tag in tags:
        if tag in tag_pairs.values() and tag not in optional_closing_tags:
            extra_closing_tag = True

    if not extra_closing_tag:
        return "Congrats, your html document iS VALID"
    return "Sorry, your html document iS INVALID"


# print(html_tag_checker('Please type your file name here and uncomment it'))

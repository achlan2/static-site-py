from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []
    for old_node in old_nodes:
        t_start = 0;
        text = old_node.text
        delimiter_count = text.count(delimiter)
        if delimiter_count%2 != 0:
            raise Exception('there is no closing delimiter!')
        s_text = text.split(delimiter)
        starting_mark = 1
        for i in range(0, len(s_text)):
            if s_text[i] != '':
                if i == starting_mark:
                    res.append(TextNode(s_text[i], text_type))
                    starting_mark+=2;
                else:
                    res.append(TextNode(s_text[i], old_node.text_type))
    return res


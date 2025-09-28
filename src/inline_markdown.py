import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []
    for old_node in old_nodes:
        t_start = 0;
        text = old_node.text
        delimiter_count = text.count(delimiter)
        if delimiter_count > 0 and delimiter_count%2 != 0:
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

image_regex = r"!\[([^\]]*)\]\((https?:\/\/[^\s)]+)\)"
link_regex = r"\[([^\]]*)\]\((https?:\/\/[^\s)]+)\)"

def split_nodes_image(old_nodes):
    res = []
    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        if not matches:
            res.append(old_node)
        else:
            o = old_node.text
            i = 0
            for e in matches:
                search = f"![{e[0]}]({e[1]})"
                splitted = o.split(search)
                if splitted[0] != '':
                    res.append(TextNode(splitted[0], old_node.text_type))
                res.append(TextNode(e[0], TextType.IMAGE, e[1]))
                o = splitted[-1]
            if o:
                res.append(TextNode(o, old_node.text_type))
    return res

def split_nodes_link(old_nodes):
    res = []
    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)
        if not matches:
            res.append(old_node)
        else:
            o = old_node.text

            for e in matches:
                search = f"[{e[0]}]({e[1]})"
                splitted = o.split(search)
                if splitted[0] != '':
                    res.append(TextNode(splitted[0], old_node.text_type))
                res.append(TextNode(e[0], TextType.LINK, e[1]))
                o = splitted[-1]
            if o:
                res.append(TextNode(o, old_node.text_type))
    return res


def extract_markdown_images(text):
    return re.findall(image_regex, text)

def extract_markdown_links(text):
    return re.findall(link_regex, text)


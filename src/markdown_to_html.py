from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root_childs = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.CODE:

            wrapper = ParentNode('code', [text_node_to_html_node(TextNode(block.strip("```").lstrip('\n'), TextType.TEXT))])
            root_childs.append(ParentNode('pre', [wrapper]))
        else:
            childrens = text_to_children(block)
            root_childs.append(ParentNode('p', childrens))
    root = ParentNode('div', root_childs)
    return root


def text_to_children(text):
    text_nodes = text_to_textnodes(text.replace('\n',' '))
    childrens = []
    for node in text_nodes:
        childrens.append(text_node_to_html_node(node))
    return childrens


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag;
        self.value = value;
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()))

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('value is empty!')
        if not self.tag:
            return self.value;
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('tag is empty!')
        if not self.children:
            raise ValueError('Should have at least 1 children!')
        res = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            res+= child.to_html()
        res+=f"</{self.tag}>"
        return res


from textnode import TextNode, TextType

def main():
    t = TextNode('this is test', TextType.LINK, 'google.com')

    print(t)


if __name__ == '__main__':
    main()

def extract_title(markdown):
    if not markdown or not markdown.strip('\n').startswith('# '):
        raise Exception('Should Have A Header!!!')
    return markdown.split('\n\n')[0].strip('\n').lstrip('# ')

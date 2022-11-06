from bs4 import BeautifulSoup

with open('bleak.html', 'r', encoding='UTF-8') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('td')
    words = []
    with open('randomfile.txt', 'w') as o:
        for links in tags:
            text = links.text
            new_text = text.strip()
            if new_text not in words:
                words.append(new_text)
                o.write(new_text)
                o.write("\n")

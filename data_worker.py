from collections import Counter
import json
import xml.etree.ElementTree as ET


def get_json_file_content():
    with open('newsafr.json', encoding='utf-8') as json_file:
        return json.load(json_file)


def get_xml_root_content():
    with open('newsafr.xml', encoding='utf-8') as xml_file:
        parser = ET.XMLParser(encoding='utf-8')
        return ET.parse(xml_file, parser).getroot()


def print_top_words_from_json_news():
    content = get_json_file_content()
    all_words_longer_six = []
    for item in content['rss']['channel']['items']:
        for word_in_desc in item['description'].split():
            if len(word_in_desc) > 6:
                all_words_longer_six.append(word_in_desc.lower())
        for word_in_title in item['title'].split():
            if len(word_in_title) > 6:
                all_words_longer_six.append(word_in_title.lower())
    most_popular = Counter(all_words_longer_six).most_common(10)
    print('\nНаиболее часто встречающиеся слова в описании новостей (from json):')
    for pair in most_popular:
        print(f'Слово - "{pair[0]}", раз встречается - {pair[1]}')


def print_top_words_from_xml_news():
    root = get_xml_root_content()
    all_words_longer_six = []
    for item in root.findall('channel/item'):
        for word_in_desc in item.find('description').text.split():
            if len(word_in_desc) > 6:
                all_words_longer_six.append(word_in_desc.lower())
        for word_in_title in item.find('title').text.split():
            if len(word_in_title) > 6:
                all_words_longer_six.append(word_in_title.lower())
    most_popular = Counter(all_words_longer_six).most_common(10)
    print('\nНаиболее часто встречающиеся слова в описании новостей (from xml):')
    for pair in most_popular:
        print(f'Слово - "{pair[0]}", раз встречается - {pair[1]}')


if __name__ == '__main__':
    print_top_words_from_json_news()
    print_top_words_from_xml_news()

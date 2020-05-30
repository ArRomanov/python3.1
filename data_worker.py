from collections import Counter
import json


def get_json_file_content():
    with open('newsafr.json', encoding='utf-8') as json_file:
        return json.load(json_file)


def print_top_words_longer_six_chars():
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
    print(most_popular)
    print(type(most_popular))
    for pair in most_popular:
        print(f'Слово - "{pair[0]}", раз встречается - {pair[1]}')


if __name__ == '__main__':
    print_top_words_longer_six_chars()

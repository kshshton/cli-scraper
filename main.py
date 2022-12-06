from os import system

from scraper import Scraper


if __name__ == "__main__":
    robot: object = Scraper()


    system('clear')
    print("""
    Press to run:
    1. Add url of page
    2. List out urls
    3. Expand HTML of url
    4. Search HTML Tag on page
    5. Search regex on page
    """)


    while True:
        answer: str = input()

        system('clear')
        print("""
    Press to run:
    1. Add url of page
    2. List out urls
    3. Expand HTML of url
    4. Search HTML Tag on page
    5. Search regex on page
    """)

        if answer == '1':
            url: str = input('Enter url: ')
            robot.add_page_by_url(url)

        if answer == '2':
            robot.list_of_pages()

        if answer == '3':
            robot.list_of_pages()
            key: int = int(input('Enter url key: '))
            robot.expand_html_of_page(key)

        if answer == '4':
            robot.list_of_pages()
            key: int = int(input('Enter url key: '))
            tag: str = input('Enter HTML Tag: ')
            robot.search_tag_on_page(tag, key)

        if answer == '5':
            robot.list_of_pages()
            key: int = int(input('Enter url key: '))
            regex: str = input('Enter regex: ')
            robot.find_regex_on_page(regex, key)
        

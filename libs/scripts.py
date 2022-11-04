import time

from libs.config import Scrapper


class WebPageStructure:
    URLS = list()

    def create_web_page_structure(self):
        scrapper = Scrapper()
        pages = scrapper.validate_pages()

        for page in pages:
            scrapper_subpages = Scrapper(page.url)
            subpages = scrapper_subpages.validate_pages()
            for subpage in subpages:
                if subpage not in pages:
                    pages.append(subpage)

    def save_to_file(self, filename, content):
        with open(filename, "w+") as f:
            f.write(content)


start = time.time()
a = WebPageStructure()
print(a.create_web_page_structure())
end = time.time()
print(end - start)

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if hasattr(self, '_title') and self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
    
    @property
    def magazine(self, value):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
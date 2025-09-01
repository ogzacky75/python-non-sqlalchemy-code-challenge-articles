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
        if not isinstance(name, str) or name.strip() == 0:
            raise Exception("Name must be a non-empty string")
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value
    

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(set(mag.category for mag in self.magazines())))

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value,str) and (2 <= len(value) <= 16):
            self._name = value

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value.strip())>0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
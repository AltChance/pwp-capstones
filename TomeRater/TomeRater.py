class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(self.name + '\'s email has been updated!')

    def __repr__(self):
        return 'User: {user}, email: {email}, books read: {num}'.format(user = self.name,email=self.email,num=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user and self.email == other_user:
            return True
        else:
            return False

    def read_book(self,book,rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        count = 0
        total = 0
        for book in self.books.keys():
            count += 1
            if self.books[book] is not None:
                total += self.books[book]
        averager = total / len(self.books)
        return averager
    #def	__hash__(self):
        #return	hash((self.name,self.email,self.books))

class Book:
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,new):
        self.isbn = new
        print(self.title + '\'s ISBN has been updated!')

    def add_rating(self,rating):
        if rating >= 0 and rating < 5:
            self.ratings.append(rating)
        else:
            print('Invalid Rating!')

    def __eq__(self, other_book):
        if self.title == other and self.isbn == other:
            return True
        else:
            return False

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        if len(self.ratings) == 0 or total == 0:
            averager = 0
        else:
            averager = total / len(self.ratings)
        return averager

    def	__hash__(self):
        return	hash((self.title,self.isbn))

    def __repr__(self):
        return '{title} is ISBN:{isbn}'.format(title=self.title,isbn=self.isbn)

class Fiction(Book):
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '{title} by {author}'.format(title=self.title,author=self.author)

class NonFiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return '{title}, a {level} manual on {subject}'.format(title=self.title,level=self.level,subject=self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self,title,isbn):
        newBook = Book(title,isbn)
        return newBook

    def create_novel(self,title,author,isbn):
        newNovel = Fiction(title,author,isbn)
        return newNovel

    def create_non_fiction(self,title,subject,level,isbn):
        newNonFiction = NonFiction(title,subject,level,isbn)
        return newNonFiction

    def add_book_to_user(self,book,email,rating=None):
        if email in self.users:
            self.users[email].read_book(book,rating)
            if rating != None:
                Book.add_rating(book,rating)
            if book not in self.books:
                self.books[book] = 1
            if book in self.books:
                value = self.books[book]
                self.books[book] = value + 1
        else:
            print('No user with email {email}!'.format(email=email))
    def add_user(self,name,email,user_books=None):
        user = User(name,email)
        self.users[email] = user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book,email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        highestName = ''
        timesRead = 0
        for book in self.books.keys():
            if self.book[book].get() > timesRead:
                highestName = book.title
                timesRead = self.book[book].get()
        print('Most read book is {book}. It has been read {number} times!'.format(book=highestName,number=timesRead))

    def highest_rated_book(self):
        highestName = ''
        avgRating = 0
        for book in self.books.keys():
            if book.get_average_rating() > avgRating:
                highestName = book.title
                avgRating = book.get_average_rating()
        print('Highest Rated Book is {book} with a Average Rating of {number}'.format(book=highestName,number=avgRating))

    def most_positive_user(self):
        highestName = ''
        avgRating = 0
        for user in self.users.values():
            avg = user.get_average_rating()
            if avg > avgRating:
                highestName = user.name
                avgRating = avg
        print('Most Positive User is {user} with an Average Rating of {number}'.format(user=highestName,number=avgRating))

    def get_most_read_book(self):
        timeRead = 0
        highestName = ''
        for book in self.books.keys():
            if self.books[book] > timeRead:
                timeRead = self.books[book]
                highestName = book.title

        print("Book with Highest Read Count is {name} with {number}".format(name=highestName,number=timeRead))

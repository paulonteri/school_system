from django.db import models
from django.urls import reverse

import uuid

from students.models import Student
from academics.models import Subject


class BookType(models.Model):
    name = models.CharField(max_length=200, help_text="Eg: story book, dictionary, course text book")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name},{self.first_name}'


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='Unique ID for this particular book '
                                                                            'across whole library')
    title = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    author = models.ManyToManyField(Author)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    type = models.ManyToManyField(BookType, help_text='Select a book type')
    subject = models.ManyToManyField(Subject, help_text='Select Subject')
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the Book", blank=True,
                               null=True)
    ISBN = models.CharField('ISBN', max_length=13, blank=True, null=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')

    def __str__(self):
        return f'{self.title}'
        # include author

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    def display_subject(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(subject.name for subject in self.subject.all()[:1])

    display_subject.short_description = 'Subject'


class BorrowBookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    student = models.name = models.OneToOneField(Student, on_delete=models.CASCADE)
    date_due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('l', 'On loan'),
        ('a', 'Available'),
    )

    # tuple containing tuples of key-value pairs then pass it to the choices argument

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='l', help_text="Book Availability")

    def __str__(self):
        return f'{self.book.title}{self.student.student_id}: {self.student.first_name} {self.student.first_name} '

        # String for representing the Model Object

        # The model __str__() represents the BookInstance object
        # using a combination of its unique id and the associated Book's title.

        # f-strings
        # f'{self.id} ({self.book.title})'

    class Meta:
        ordering = ["date_due_back"]

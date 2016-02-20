# -*- coding: utf-8 -*-
from django import forms
from bookmanager.models import Book, Author

class Form_Book_new(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('Title','AuthorID','Publisher',
            'PublishDate', 'Price')
        error_messages = {
            'Title': {'required' : '请填写书名'},
            'AuthorID' : {'required' : '请填写作者ID'},
            'Publisher' : {'required' : '请填写出版社'},
            'Price' : {'required' : '请填写价格'},
        }

    def __init__(self, *args, **kwargs):
        super(Form_Book_new, self).__init__(*args, **kwargs)
        self.fields['PublishDate'].widget = forms.TextInput(attrs={
            'placeholder': "格式举例：1995-05-28"})
            
class Form_Book_update(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('AuthorID','Publisher',
            'PublishDate', 'Price')
        error_messages = {
            'AuthorID' : {'required' : '请填写作者ID'},
            'Publisher' : {'required' : '请填写出版社'},
            'Price' : {'required' : '请填写价格'},
        }

    def __init__(self, *args, **kwargs):
        super(Form_Book_update, self).__init__(*args, **kwargs)
        self.fields['PublishDate'].widget = forms.TextInput(attrs={
            'placeholder': "格式举例：1995-05-28"})
        

class Form_Author(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('Name','Age','Country',)
        error_messages = {
            'Name': {'required' : '请填写作者姓名',},
            'Country' : {'required' : '请填写作者国别',},
        }
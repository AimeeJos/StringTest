from django import forms

class myform(forms.Form):
    master= forms.CharField(label="Master String")
    string1 = forms.CharField(label="String1: ")
    string2 = forms.CharField(label="String2: ")
    string3 = forms.CharField(label="String3: ")
    string4 = forms.CharField(label="String4: ")


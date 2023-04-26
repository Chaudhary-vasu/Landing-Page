from django import forms

class userform(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()

class Calculator(forms.Form):
    input1 = forms.NumberInput()
    input2 = forms.NumberInput()
    # Operator_Choices ={
    # "1": "+",
    # "2": "-",
    # "3": "*",
    # "4": "/",
    # }
    # operator = forms.ChoiceField(choices=Operator_Choices)
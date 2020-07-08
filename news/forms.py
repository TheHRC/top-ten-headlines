from django import forms

# iterable
Country_Code = (
    ("au", "Australia"),
    ("ca", "Canada"),
    ("cn", "China"),
    ("eg", "Egypt"),
    ("in", "India"),
    ("jp", "Japan"),
    ("ma", "Morocco"),
    ("nz", "New Zealand"),
    ("sa", "Saudi Arabia"),
    ("sg", "Singapore"),
    ("gb", "United Kingdom"),
    ("us", "United States"),
)


# creating a form
class HeadlinesForm(forms.Form):
    country_field = forms.ChoiceField(choices=Country_Code)
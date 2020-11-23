from django import forms

from accounts.models import Contact, Agents, Quote


class ContactForm(forms.ModelForm):
    name = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    inquiry = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            # 'name': "Name",
            # 'email': "Email",
            # 'inquiry': "Message",
            # 'phone': 'Phone Number'
        }


class AgentForm(forms.ModelForm):
    name = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    agency = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Agency Name'}))
    resume = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Resume'}))
    contact = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
    message = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Message'}))


    class Meta:
        model = Agents
        fields = '__all__'
        labels = {
            'name': "Name",
            'email': "Email",
            'message': "Message",
            'phone': 'Phone Number',
            'agency': "Agency Name",
            'resume': 'Resume'
        }


class QuoteForm(forms.ModelForm):
    contact_person = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    operations = forms.CharField(label=' ',
                                 widget=forms.Textarea(attrs={'placeholder': 'Brief Description of Operations'}))
    num_employee = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': '# of Employees'}))
    payroll = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Estimated Annual Payroll'}))

    class Meta:
        model = Quote
        fields = '__all__'
        labels = {
            'contact_person': "Contact Person:*",
            'email': "Email:*",
            'operations': 'Brief Description of Operations:*',
            'phone': 'Phone Number:*',
            'num_employee': "# of Employees:*",
            'payroll': 'Estimated Annual Payroll:*'
        }

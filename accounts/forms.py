from django import forms

from accounts.models import Contact, Agents, Quote


class ContactForm(forms.Form):
    name = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    inquiry = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    # class Meta:
    #     model = Contact
    #     labels = {
    #         # 'name': "Name",
    #         # 'email': "Email",
    #         # 'inquiry': "Message",
    #         # 'phone': 'Phone Number'
    #     }
    #     fields = ('__all__')


class AgentForm(forms.ModelForm):
    agency = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Agency Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    contact = forms.CharField(label=' ', required=False, widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
    phone = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    message = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    resume = forms.Field(label=' ', widget=forms.FileInput(attrs={'placeholder': 'Resume'}), required=True)

    class Meta:
        model = Agents
        labels = {
            # 'name': "Name",
            # 'email': "Email",
            # 'message': "Message",
            # 'phone': 'Phone Number',
            # 'agency': "Agency Name",
            # 'resume': 'Resume'
        }
        fields = ('__all__')


class QuoteForm(forms.ModelForm):
    contact_person = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Contact Person'}), required=True)
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=True)
    operations = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Brief Description of Operations:'}), required=True)
    phone = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}), required=True)
    num_employee = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': '# of Employees:'}), required=True)
    payroll = forms.Field(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Estimated Annual Payroll'}), required=True)
    company_name=  forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Company Name'}), required=True)

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

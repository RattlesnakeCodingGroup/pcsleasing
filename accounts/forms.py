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
            'name': "Name",
            'email': "Email",
            'inquiry': "Message",
            'phone': 'Phone Number'
        }


class AgentForm(forms.ModelForm):
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
    class Meta:
        model= Quote
        fields = '__all__'
        labels = {
            'contact_person': "Contact Person:*",
            'email': "Email:*",
            'operations': 'Brief Description of Operations:*',
            'phone': 'Phone Number:*',
            'num_employee': "# of Employees:*",
            'payroll': 'Estimated Annual Payroll:*'
        }


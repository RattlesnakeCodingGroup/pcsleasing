from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.template import RequestContext
from django.urls import reverse
from django.views import View
from django.core.mail import EmailMessage

from accounts.forms import ContactForm, AgentForm, QuoteForm


class Index(View):
    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['inquiry']
            email = form.cleaned_data['email']

            email = EmailMessage(
                subject='Inquiry from ' + str(email),
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'
                ,
                from_email='pcsleasing@gmail.com',
                to=['pcsleasing@gmail.com']

            )
            email.send()

            return redirect(reverse('accounts:index'))


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Services(View):
    def get(self, request):
        return render(request, 'services.html')


class WhyPeo(View):
    def get(self, request):
        return render(request, 'whypeo.html')


# class Agents(View):
#     def get(self, request):
#         form = AgentForm()
#         context = {'form': form}
#         return render(request, 'agents.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = AgentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message= form.cleaned_data['message']
#             resume = request.FILES['resume']  # file is the name value which you have provided in form for file field
#             phone = form.cleaned_data['phone']
#             contact = form.cleaned_data['contact']
#             agency = form.cleaned_data['agency']
#             email = form.cleaned_data['email']
#
#             email= EmailMessage(
#                 subject= 'Agent application from '+ str(email) ,
#                 body= 'Agency Name: '+ str(agency)+ '\n'
#                         + 'message: '+str(message)+ '\n'
#                         + 'contact: '+ str(contact)+ '\n'
#                         + 'phonenumber: '+ str(phone)+ '\n'
#                 ,
#                 from_email= 'pcsleasing@gmail.com',
#                 to=['pcsleasing@gmail.com']
#
#
#             )
#             if request.FILES:
#                 uploaded_file = request.FILES['resume']  # file is the name value which you have provided in form for file field
#                 email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
#             email.send()
#         return redirect(reverse('accounts:index'))


def agents(request):
    if request.method == 'POST':
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.cleaned_data['message']
            #             resume = request.FILES['resume']  # file is the name value which you have provided in form for file field
            phone = form.cleaned_data['phone']
            contact = form.cleaned_data['contact']
            agency = form.cleaned_data['agency']
            email = form.cleaned_data['email']
            uploaded_file = request.FILES['resume']  # file is the name value which you have provided in form for file field
            email = EmailMessage(
                subject='Agent application from ' + str(email),
                body='Agency Name: ' + str(agency) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'contact: ' + str(contact) + '\n'
                     + 'phone number: ' + str(phone) + '\n'
                ,
                from_email='pcsleasing@gmail.com',
                to=['pcsleasing@gmail.com']

            )

            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            email.send()
            messages.success(request, "Inquiry Sent")
            return redirect('accounts:index')
    else:
        form = AgentForm()
    context = {'form': form}
    return render(request, 'agents.html', context)


class Quote(View):
    def get(self, request):
        form = QuoteForm()
        context = {'form': form}
        return render(request, 'quote.html', context)

    def post(self, request, args, kwargs):
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            contactperson = form.cleaned_data['contact_person']
            phone = form.cleaned_data['phone']
            company_name = form.cleaned_data['company_name']
            num_employee = form.cleaned_data['num_employee']
            email = form.cleaned_data['email']
            operations = form.cleaned_data['operations']
            payroll = form.cleaned_data['payroll']

            email = EmailMessage(
                subject='requested quote from ' + str(email),
                body='Company Name: ' + str(company_name) + '\n'
                     + 'Brief Description of Operations: ' + str(operations) + '\n'
                     + 'Estimated Annual Payroll: ' + str(payroll) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'
                     + 'Number of Employees: ' + str(num_employee) + '\n'
                     + 'Contact Person: ' + str(contactperson) + '\n'
                ,
                from_email='pcsleasing@gmail.com',
                to=['pcsleasing@gmail.com']

            )
            email.send()
            return redirect(reverse('accounts:quote'))


class Contact(View):
    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'Contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['inquiry']
            email = form.cleaned_data['email']

            email = EmailMessage(
                subject='Inquiry from ' + str(email),
                body='Name: ' + str(name) + '\n'
                     + 'message: ' + str(message) + '\n'
                     + 'email: ' + str(email) + '\n'
                     + 'phonenumber: ' + str(phone) + '\n'
                ,
                from_email='pcsleasing@gmail.com',
                to=['pcsleasing@gmail.com']

            )
            email.send()

            return redirect(reverse('accounts:index'))

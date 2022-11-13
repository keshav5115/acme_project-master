
from django.contrib.auth.models import User
from authe import serializers
from rest_framework import generics
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from authe.form import Departmentform,  Ticket_modelform, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.generic import UpdateView, ListView, DeleteView
from authe.models import User, Department, Ticket_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions
# Create your views here.


@login_required(login_url='/login')
def Departmentview(request):
    form = Departmentform()
    if request.method == 'POST':
        form = Departmentform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            form.save()
            return redirect('/homepage/')
    return render(request,  'crud_depart.html', {'form': form})


class deptupdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'authe.change_Department'
    model = Department
    fields = '__all__'
    template_name = 'crud_depart.html'


class deptdelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'authe.delete_Department'
    model = Department
    fields = '__all__'
    template_name = 'deptconfirm.html'
    context_object_name = 'data'
    success_url = "/homepage"


class deptlist(PermissionRequiredMixin, ListView):
    permission_required = 'authe.view_Department'
    model = Department
    fields = '__all__'
    template_name = 'deptlist.html'
    context_object_name = 'data'


def Userview(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.password = make_password(form.cleaned_data['password'])
            form.save()
            return redirect('/homepage')
    return render(request,  'crud_depart.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login_page.html", context={"form": form})


def Ticketview(request):
    form = Ticket_modelform()
    if request.method == 'POST':
        form = Ticket_modelform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is stord')
    return render(request, 'ticket.html', {'form': form})


def homepage(request):
    return render(request, 'homepage.html')


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")


class TicketTemplateHTMLRender(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        data = super().get_template_context(data, renderer_context)
        if not data:
            return {}
        else:
            return data


class TicketList(generics.ListCreateAPIView):
    queryset = Ticket_model.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket_model.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

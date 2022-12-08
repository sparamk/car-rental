from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from employee.views import *
from django.contrib.auth.models import User, Group

from user.views import dashboard


@login_required
def list_users(request):
    users_list = []
    admin = User.objects.filter(is_superuser=True).first()
    users = User.objects.exclude(username=request.user).exclude(username=admin.username).all()

    for doser in users:
        l = list(doser.groups.values_list('name', flat=True))
        user_dictionary = {'username': doser.username, 'first_name': doser.first_name, 'last_name': doser.last_name,
                           'email': doser.email, 'is_staff': l, 'id': doser.id, 'is_active': doser.is_active}
        users_list.append(user_dictionary)

    request.session['users_list'] = users_list
    return render(request, 'list_users.html', {'users': users})


# Create your views here.
def addEmployee(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if len(password) == 0:
            messages.error(request, 'Password field cannot be null!')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists. Please choose a different Username!')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered. Please use a different email!')
            return render(request, 'authentication/signup.html')

        if len(username) > 10:
            messages.error(request, 'Username must be under ten characters')
            return render(request, 'authentication/signup.html')
        
        if password != confirm_password:
            messages.error(request, 'Please enter the same password in both the password fields')
            return render(request, 'authentication/signup.html')
        
        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric')
            return render(request, 'authentication/signup.html')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.email = email
        myuser.is_active= True
        myuser.save()
        # Add user to the employee group
        employee_group = Group.objects.get(name='employee')
        employee_group.user_set.add(myuser)
        messages.success(request, "Employee account has been created successfully!")
        
        return render(request, 'addemployee.html')

    return render(request, 'addemployee.html')


def editEmployee(request):
    if request.method == 'POST':
        
        try:
            user_id = request.POST['id']
            employee = User.objects.filter(id=user_id).first()
            return render(request, 'editemployee1.html',{'employee':employee})
            # employee.save()
        except:
            # Error workflow
            return redirect(editEmployee)
    # employee = User.objects.filter(id=user_id).first()
    employee_list = []
    admin = User.objects.filter(is_superuser=True).first()
    users = User.objects.exclude(username=request.user).exclude(username=admin.username).filter(groups__name='employee')

    for doser in users:
        l = list(doser.groups.values_list('name', flat=True))
        user_dictionary = {'username': doser.username, 'first_name': doser.first_name, 'last_name': doser.last_name,
                           'email': doser.email, 'is_staff': l, 'id': doser.id, 'is_active': doser.is_active}
        employee_list.append(user_dictionary)

    request.session['users_list'] = employee_list
    return render(request, 'editemployee.html', {'users': users})
    


def deleteEmployee(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        try:
            User.objects.get(id=user_id).delete()
            return redirect(list_users)
        except:
            return dashboard()




def deletebooking(request):
    booking= Book_Car.objects.all
    if request.method == 'POST':
        booking_id = request.POST['id']
        booking = Book_Car.objects.filter(id=booking_id)
        booking.delete()
        return redirect(bookings)
    return redirect(booking)


def bookings(request):
    bookings = Book_Car.objects.filter(is_paid=False)
    # booked_cars = Book.objects.all()
    return render(request, 'deletebooking.html',{'bookings':bookings})


@login_required
def blockUser(request):
    if request.method == 'POST':
        doser = User.objects.filter(id=request.POST['id']).first()
        if request.POST['ban']:
            mygroup = Group.objects.get(name='block')
            mygroup.user_set.add(doser)
            mygroup = Group.objects.get(name='employee')
            mygroup.user_set.remove(doser)
            mygroup = Group.objects.get(name='manager')
            mygroup.user_set.remove(doser)
            mygroup = Group.objects.get(name='customer')
            mygroup.user_set.remove(doser)

    return redirect(list_users)


@login_required
def employee(request):
    if request.method == 'POST':
        doser = User.objects.filter(id=request.POST['id']).first()
        l = list(doser.groups.values_list('name', flat = True))
        if 'employee' in l:
            mygroup = Group.objects.get(name='employee')
            mygroup.user_set.remove(doser)
        elif request.POST['employee']:
            mygroup = Group.objects.get(name='employee')
            mygroup.user_set.add(doser)
            mygroup = Group.objects.get(name='ban')
            mygroup.user_set.remove(doser)

    return redirect(list_users)

@login_required
def customer(request):
    if request.method == 'POST':
        doser = User.objects.filter(id=request.POST['id']).first()
        # l = list(doser.groups.values_list('name', flat = True))
        # if 'customer' in l:
        #     mygroup = Group.objects.get(name='customer')
        #     mygroup.user_set.remove(doser)
        if request.POST['customer']:
            mygroup = Group.objects.get(name='customer')
            mygroup.user_set.add(doser)
            mygroup = Group.objects.get(name='ban')
            mygroup.user_set.remove(doser)

    return redirect(list_users)


@login_required
def manager(request):
    if request.method == 'POST':
        doser = User.objects.filter(id=request.POST['id']).first()
        l = list(doser.groups.values_list('name', flat = True))
        if 'manager' in l:
            mygroup = Group.objects.get(name='manager')
            mygroup.user_set.remove(doser)
        elif request.POST['manager']:
            mygroup = Group.objects.get(name='manager')
            mygroup.user_set.add(doser)
            mygroup = Group.objects.get(name='ban')
            mygroup.user_set.remove(doser)

    return redirect(list_users)

# Create your views here.
def updateEmployee(request):
    if request.method == 'POST':
        id = request.POST['id']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if len(password) == 0:
            messages.error(request, 'Password field cannot be null!')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists. Please choose a different Username!')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered. Please use a different email!')
            return render(request, 'authentication/signup.html')

        if len(username) > 10:
            messages.error(request, 'Username must be under ten characters')
            return render(request, 'authentication/signup.html')
        
        if password != confirm_password:
            messages.error(request, 'Please enter the same password in both the password fields')
            return render(request, 'authentication/signup.html')
        
        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric')
            return render(request, 'authentication/signup.html')

        myuser = User.objects.filter(id=id).update(username, email, first_name, last_name, password)
        # Add user to the employee group
        employee_group = Group.objects.get(name='employee')
        employee_group.user_set.add(myuser)
        messages.success(request, "Employee account has been updated successfully!")
        
        return redirect('manager/editemployee')

    return redirect('manager/editemployee')

from django.shortcuts import redirect, render
from manager.views import *
from .models import *
from django.contrib.auth.models import User
from user.views import *

# Create your views here.


def addCar(request):
    if request.method == 'POST':
        car = Cars()
        car.car_name = request.POST['car_name']
        car.color = request.POST['color']
        car.capacity = request.POST['capacity']
        car.description = request.POST['description']
        car.car_condition = request.POST['car_condition']
        car.subscription = request.POST['subscription']
        car.save()
        success = "The car has been added to the inventory successfully"
        return render(request, 'addcar.html', {'success': success})
    return render(request, 'addcar.html')


def editCar(request):
    if request.method == 'POST':
        car_id = request.POST['id']
        car = Cars.objects.get(id=car_id)
        return render(request, 'editcar.html',
                      {'car_id': car.id, 'car_name': car.car_name, 'color': car.color, 'description': car.description,
                       'car_condition': car.car_condition, 'capacity': car.capacity, 'subscription': car.subscription,})
    return render(request, 'editcar.html')


def updateCar(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        color = request.POST['color']
        capacity = request.POST['capacity']
        description = request.POST['description']
        car_condition = request.POST['car_condition']
        car_subcription = request.POST['subscription']
        car = Cars.objects.get(id=car_id)
        car.car_name=car_name
        car.color=color
        car.capacity=capacity  
        car.description=description 
        car.car_condition=car_condition
        car.subscription=car_subcription
        car.save()
        success = "The car has been updated successfully"
        car = Cars.objects.filter(id=car_id).first()
        return render(request, 'editcar.html',
                      {'car_id': car.id, 'car_name': car.car_name, 'color': car.color, 'description': car.description,
                       'capacity': car.capacity, 'success': success,'subscription': car.subscription})


def listCars(request):
    cars = Cars.objects.all()
    return render(request, 'listcars.html', {'cars': cars})


def deleteCar(request):
    if request.method == 'POST':
        car_id = request.POST['id']
        car = Cars.objects.filter(id=car_id).first()
        car.delete()
        success = "Car deleted successfully"
        return redirect(listCars)


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


def blockUser(request):
    if request.method == 'POST':
        try:
            user_id = request.POST['id']
            user = User.objects.get(id=user_id)

            # Remove user from all groups
            groups = list(user.groups.values_list('name', flat=True))
            for group in groups:
                group.user_set.remove(user)

            # Add user to the blocked group
            block_group = Group.objects.get(name='block')
            block_group.user_set.add(user)

            return redirect(list_users)
        except:
            return dashboard()


def coupons(request):
    coupons = Coupons.objects.all()
    return render(request, 'coupons.html', {'coupons': coupons})


def addCoupon(request):
    if request.method == 'POST':
        coupon = Coupons()
        coupon.coupon_code = request.POST['coupon_code']
        coupon.discount = request.POST['discount']
        coupon.save()
        success = "The coupon has been listed successfully"
        return render(request, 'addcoupon.html', {'success': success})
    return render(request, 'addcoupon.html')


def editCoupon(request):
    if request.method == 'POST':
        coupon_id = request.POST['id']
        coupon = Coupons.objects.filter(id=coupon_id).first()
        return render(request, 'editcoupon.html',
                      {'coupon_id': coupon.id, 'coupon_code': coupon.coupon_code, 'discount': coupon.discount, })
    return render(request, 'editcar.html')


def updateCoupon(request):
    if request.method == 'POST':
        coupon_id = request.POST['coupon_id']
        coupon_code = request.POST['coupon_code']
        discount = request.POST['discount']

        coupon = Coupons.objects.filter(id=coupon_id).update(coupon_code=coupon_code, discount=discount, )
        success = "The coupon has been updated successfully"
        coupon = Coupons.objects.filter(id=coupon_id).first()
        return render(request, 'editcoupon.html',
                      {'coupon_id': coupon.id, 'coupon_code': coupon.coupon_code, 'discount': coupon.discount,
                       'success': success})


def deleteCoupon(request):
    if request.method == 'POST':
        coupon_id = request.POST['id']
        coupon = Coupons.objects.filter(id=coupon_id).first()
        coupon.delete()
        success = "Coupon deleted successfully"
        return redirect(coupons)

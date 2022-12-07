from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def sendFeedback(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']

    return render(request, 'sendfeedback.html')
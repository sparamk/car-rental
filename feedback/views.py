from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def sendFeedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.user_id = request.user.id
        feedback.feedback_text = request.POST['feedback']
        # feedback.feedback_response_text = ''
        feedback.save()
        success = 'feedback sent successfully'
        return render(request, 'sendfeedback.html',{'success':success})

    return render(request, 'sendfeedback.html')
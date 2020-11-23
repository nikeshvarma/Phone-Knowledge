from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from HOME.models import Mobile
from .forms import UpdateProfileForm, ReviewForm, QuestionForm
from .models import Profile


@login_required
def profile(request):
    args = {
        'user': request.user,
        'profile': request.user.profile
    }

    return render(request, 'User/Profile.html', args)


@login_required
def updateprofile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user_id=request.user.id))
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('updateprofile')
    else:
        form = UpdateProfileForm(instance=Profile.objects.get(user_id=request.user.id))
        return render(request, 'User/UpdateProfile.html', {'form': form})


@login_required
def review(request, pk):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('loginuser')
        else:
            form = ReviewForm(request.GET)
            if form.is_valid():
                re = form.save(commit=False)
                re.user = request.user
                re.mobile = Mobile.objects.get(id=pk)
                re.save()
                return redirect('details_page', pk)
            else:
                return redirect('False')
    else:
        return HttpResponse('Wrong Method')


@login_required
def question_answer(request, pk):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('loginuser')
        else:
            form = QuestionForm(request.POST)
            if form.is_valid():
                re = form.save(commit=False)
                re.user = request.user
                re.phone_id = Mobile.objects.get(id=pk)
                re.save()
                return redirect('details_page', pk)
            else:
                return HttpResponse('false')
    else:
        return HttpResponse('Wrong Method')

from django.shortcuts import render
from django.http import JsonResponse
from myapp.network import three_paths
from .models import Feedback
from .forms import FeedbackForm


def gentext(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        generated_text = three_paths(input_text)
        return JsonResponse({
            'generated_text_1': generated_text[0],
            'generated_text_2': generated_text[1],
            'generated_text_3': generated_text[2]})
    return JsonResponse({'error': 'Invalid request method'})


def addfeedbacktodb(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = FeedbackForm()
        return render(request, 'index.html', {'form': form})


def index(request):
    form = FeedbackForm()
    db = Feedback.objects.all()
    data = {
        'form': form,
        'db': db
    }
    return render(request, 'main/index.html', data)


def FAQs(request):
    return render(request, 'main/FAQs.html')

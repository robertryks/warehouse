from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'main_view.html')

def grade_list(request):
    return render(request, 'grade/grade_list.html')

def grade_add(request):
    return render(request, 'grade/grade_add.html')
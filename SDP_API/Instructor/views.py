from django.shortcuts import render
from forms import CreateCourse
from django.shortcuts import redirect


def create_course(request):
    if request.method == "POST":
        form = CreateCourse(request.POST)
        # if form.is_valid():
        #     course = form.save(commit=False)
        #     course.author = request.user
        #     course.is_opened = timezone.now()
        #     course.save()
        #     return redirect('post_detail', pk=post.pk)
    else:
        form = CreateCourse()
    return render(request, 'site/sample.html',{'form': form})


from django.shortcuts import render, redirect
from .forms import CourseFeedbackForm, InstructorFeedbackForm, CampusFeedbackForm

def course_feedback(request):
    if request.method == 'POST':
        form = CourseFeedbackForm(request.POST)
        if form.is_valid():
            # Save the form data to the database (if desired) and redirect to the next form
            # You can save the form data to the database using form.save()
            return redirect('instructor_feedback')
    else:
        form = CourseFeedbackForm()
    return render(request, 'course_feedback.html', {'form': form})

def instructor_feedback(request):
    if request.method == 'POST':
        form = InstructorFeedbackForm(request.POST)
        if form.is_valid():
            # Save the form data to the database (if desired) and redirect to the next form
            # You can save the form data to the database using form.save()
            return redirect('campus_feedback')
    else:
        form = InstructorFeedbackForm()
    return render(request, 'instructor_feedback.html', {'form': form})

def campus_feedback(request):
    if request.method == 'POST':
        form = CampusFeedbackForm(request.POST)
        if form.is_valid():
            # Save the form data to the database and display a thank you page
            # You can save the form data to the database using form.save()
            return render(request, 'thank_you.html')
    else:
        form = CampusFeedbackForm()
    return render(request, 'campus_feedback.html', {'form': form})

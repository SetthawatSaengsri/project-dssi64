# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import qrcode
import base64
from io import BytesIO
from django.utils import timezone
from datetime import timedelta


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registration successful.')
            return redirect('success_page')
    else:
        form = StudentRegistrationForm()
    return render(request, 'app/register_student.html', {'form': form})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher registration successful.')
            return redirect('index_view')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'app/register_teacher.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # ตรวจสอบประเภทของผู้ใช้และเปลี่ยนเส้นทางไปยังหน้าที่เหมาะสม
            if user.is_student:
                return redirect('dashboard_student')  # ตั้งชื่อ URL สำหรับหน้า dashboard ของนักเรียน
            elif user.is_teacher:
                return redirect('dashboard_teacher')  # ตั้งชื่อ URL สำหรับหน้า dashboard ของครู
            else:
                # ถ้าไม่ใช่ student หรือ teacher, กลับไปที่หน้าหลักหรือหน้าอื่น
                return redirect('index_view')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'app/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('index_view')


def index_view(request):
    return render(request, 'app/index.html')

def success_page(request):
    return render(request, 'app/success_page.html')


@login_required
def dashboard_teacher(request):
    user = request.user
    return render(request, 'app/teacher/dashboard_teacher.html', {'user': user})

@login_required
def add_exam_subject(request):
    if request.method == 'POST':
        form = ExamSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_subject_list')
    else:
        form = ExamSubjectForm()
    return render(request, 'app/teacher/add_exam_subject.html', {'form': form})

@login_required
# View to display the form for editing an exam subject
def edit_exam_subject(request, subject_id):
    subject = get_object_or_404(ExamSubject, id=subject_id)
    if request.method == 'POST':
        form = ExamSubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('exam_subject_list')
    else:
        form = ExamSubjectForm(instance=subject)
    return render(request, 'app/teacher/edit_subject.html', {'form': form})

@login_required
# View to update the exam subject details
def update_exam_subject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(ExamSubject, id=subject_id)
        form = ExamSubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
    return redirect('exam_subject_list')

@login_required
def delete_exam_subject(request, subject_id):
    if request.method == 'POST':
        subject = get_object_or_404(ExamSubject, id=subject_id)
        subject.delete()
        messages.success(request, 'Exam subject deleted successfully.')
        return redirect('exam_subject_list')
    else:
        # Redirect to the exam_subject_list page if the request method is not POST
        return redirect('exam_subject_list')

@login_required
def exam_subject_list(request):
    subjects = ExamSubject.objects.all()
    return render(request, 'app/teacher/exam_subject_list.html', {'subjects': subjects})

@login_required
def class_students_list(request, class_slug):
    class_mapping = {
        '11': '1/1',
        '12': '1/2',
        '21': '2/1',
        '22': '2/2',
        '31': '3/1',
        '32': '3/2',
        '41': '4/1',
        '42': '4/2',
        '51': '5/1',
        '52': '5/2',
        '61': '6/1',    
        '62': '6/2',
    }

    
    class_identifier = class_mapping.get(class_slug, class_slug) 

    students = StudentProfile.objects.filter(student_class=class_identifier)
    return render(request, 'app/teacher/class_students_list.html', {
        'students': students,
        'class_slug': class_identifier  
    })

# @login_required
# def generate_qr_for_student(request, student_id):
#     student = get_object_or_404(StudentProfile, id=student_id)
#     exams = ExamSubject.objects.filter(student_class__student_class=student.student_class)

#     qr_codes = []
#     for exam in exams:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr_data = f"Student ID: {student.student_id}, Name: {student.user.get_full_name()}, Class: {student.student_class}, Exam: {exam.subject_name}"
#         qr.add_data(qr_data)
#         qr.make(fit=True)

#         img = qr.make_image(fill_color="black", back_color="white")
#         buffered = BytesIO()
#         img.save(buffered, format="PNG")
#         img_str = base64.b64encode(buffered.getvalue()).decode()
#         qr_codes.append((f"data:image/png;base64,{img_str}", exam.subject_name))
    
#     return render(request, 'app/student/qr_code.html', {'qr_codes': qr_codes})

@login_required
def generate_qr_for_student(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    # Example: Set QR token to expire in 1 day. Adjust as necessary.
    expiry_time = timezone.now() + timedelta(days=1)
    # Create or update the QR token for the student
    qr_token, created = QRToken.objects.update_or_create(
        student=student,
        defaults={'expiry_time': expiry_time}
    )
    
    # Generate QR code with token
    qr_data = f"Token: {qr_token.token}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    qr_code = f"data:image/png;base64,{img_str}"
    
    return render(request, 'app/student/qr_code.html', {'qr_code': qr_code, 'student': student})



@login_required
def dashboard_student(request):
    try:
        student_profile = request.user.studentprofile
        student_id = student_profile.id
    except StudentProfile.DoesNotExist:
        student_id = None  # หรือจัดการกรณีนี้ตามที่ต้องการ
    return render(request, 'app/student/dashboard_student.html', {'user': request.user, 'student_id': student_id})

def edit_student(request):
    user = request.user
    return render(request, 'app/student/edit_profilestudent.html', {'user': user})

def Examination_history(request):
    user = request.user
    return render(request, 'app/student/Examination_history.html', {'user': user})

def dashboard_unknown(request):
    user = request.user
    return HttpResponse(f"Welcome, {user.first_name} {user.last_name} (Unknown User) - {user.username}")


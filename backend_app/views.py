from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from backend_app.models import Signup_data, Jobs, Proposal, Place_orders, Student_db, Supervisor_db, Client_db
from django.http import HttpResponse
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests


def check_backend(request):
	return HttpResponse('This is a wnc backend.')


@csrf_exempt
def receive_signup_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            sign_up_data = Signup_data(
                joinas=data['joinas'], 
                fname=data['fname'], 
                lname=data['lname'], 
                email=data['email'], 
                pwd=data['pwd'],
            )
            sign_up_data.save()
            return JsonResponse({'status': 'success', 'data_received': sign_up_data.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def receive_student_data(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            elif request.content_type.startswith('multipart/form-data'):
                data = request.POST
                profile = request.FILES.get('profile')
            else:
                return JsonResponse({'status': 'error', 'message': 'Unsupported content type'}, status=400)
            student_data = Student_db(
                email=data['email'], 
                username=data['username'],
                cnic=data['cnic'],
                profile=profile,
                phone=data['phone'],
                skills=data['skills'],
                description=data['description'],
                institute=data['institute'],
                university_email=data['university_email'],
                degree=data['degree'],
                major=data['major'],
                semester=data['semester'],
            )
            student_data.save()
            return JsonResponse({'status': 'success', 'data_received': student_data.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def receive_supervisor_data(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            elif request.content_type.startswith('multipart/form-data'):
                data = request.POST
                profile = request.FILES.get('profile')
            else:
                return JsonResponse({'status': 'error', 'message': 'Unsupported content type'}, status=400)
            supervisor_data = Supervisor_db(
                email=data['email'], 
                username=data['username'],
                profile=profile,
                cnic=data['cnic'],
                phone=data['phone'],
                skills=data['skills'],
                description=data['description'],
                institute=data['institute'],
                university_email=data['university_email'],
                designation=data['designation'],
                department=data['department']
            )
            supervisor_data.save()
            return JsonResponse({'status': 'success', 'data_received': supervisor_data.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def receive_company_data(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
            elif request.content_type.startswith('multipart/form-data'):
                data = request.POST
                profile = request.FILES.get('profile')
            else:
                return JsonResponse({'status': 'error', 'message': 'Unsupported content type'}, status=400)
            company_data = Client_db(
                email=data['email'],
                username=data['username'],
                cnic=data['cnic'],
                phone=data['phone'],
                joiningType=data['joiningType'],
                description=data['description'],
                profile=profile,
                organizationName=data['organizationName'],
                organizationEmail=data['organizationEmail'],
            )
            company_data.save()
            return JsonResponse({'status': 'success', 'data_received': company_data.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def get_signup_data(request):
    if request.method == 'GET':
        persons = Signup_data.objects.all()
        persons_data = [
            {"fname": person.fname, "lname": person.lname, "email": person.email, "password": person.pwd, "title": person.joinas}
            for person in persons
        ]
        return JsonResponse({'status': 'success', 'data': persons_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


def get_student_data(request):
    if request.method == 'GET':
        persons = Student_db.objects.all()
        persons_data = [
            {"username": person.username, "cnic": person.cnic, "phone": person.phone, "description": person.description, "profile": person.profile.name, "degree": person.degree, "major": person.major, "semester": person.semester, "institute": person.institute, "email": person.email, "university_email": person.university_email, "skills": person.skills}
            for person in persons
        ]
        return JsonResponse({'status': 'success', 'data': persons_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


def get_supervisor_data(request):
    if request.method == 'GET':
        persons = Supervisor_db.objects.all()
        persons_data = [
            {"username": person.username, "cnic": person.cnic, "phone": person.phone, "description": person.description, "profile": person.profile.name, "designation": person.designation, "department": person.department, "email": person.email, "institute": person.institute, "university_email": person.university_email, "skills": person.skills}
            for person in persons
        ]
        return JsonResponse({'status': 'success', 'data': persons_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


def get_company_data(request):
    if request.method == 'GET':
        persons = Client_db.objects.all()
        persons_data = [
            {"username": person.username, "cnic": person.cnic, "phone": person.phone, "description": person.description, "profile": person.profile.name, "joiningType": person.joiningType, "email": person.email, "organizationName": person.organizationName, "organizationEmail": person.organizationEmail}
            for person in persons
        ]
        return JsonResponse({'status': 'success', 'data': persons_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


@csrf_exempt
def receive_verify_email(request):
    if request.method == 'POST':
        ver_email = json.loads(request.body)
        print(ver_email)
        letters_and_digits = string.ascii_letters + string.digits
        code = ''.join(random.choice(letters_and_digits) for i in range(6))
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('worknconnect.wnc@gmail.com', 'ukll kamb blzl bbfd')
            subject = 'Verification Code'
            body = f'Hello, \nThank you for registering with us! \n\nTo complete your registration, please use the following verification code: {code}\nIf you did not request this verification code, please disregard this email.\n\n\nBest regards,\nWorknConnect'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail('worknconnect.wnc@gmail.com', ver_email, msg)
    return JsonResponse({'status': 'success', 'code': code})


@csrf_exempt
def recieve_sup_profile(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            s_email = data.get('email')
            existing_record = Signup_data.objects.filter(email=s_email).first()
            if existing_record:
                existing_record.profile = data.get('profile', existing_record.profile)
                existing_record.username = data.get('username', existing_record.username)
                existing_record.cnic = data.get('cnic', existing_record.cnic)
                existing_record.phone = data.get('phone', existing_record.phone)
                existing_record.skills = data.get('skills', existing_record.skills)
                existing_record.description = data.get('description', existing_record.description)
                existing_record.save()
                return JsonResponse({'status': 'success', 'message': 'Profile updated', 'data_received': existing_record.id})
            else:
                sup_profile_data = Signup_data(
                    profile=data['profile'], 
                    username=data['username'], 
                    cnic=data['cnic'], 
                    phone=data['phone'], 
                    skills=data['skills'],
                    description=data['description'],
                )
                sup_profile_data.save()
                return JsonResponse({'status': 'success', 'message': 'Profile created', 'data_received': sup_profile_data.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
def quiz_data(request):
    if request.method == 'GET':
        machine_learning = [
            {
                'question':'In machine learning, which type of learning is associated with models that receive feedback on the correctness of predictions only after a sequence of actions?',
                'answers':['Supervised learning', 'Reinforcement learning', 'Unsupervised learning', 'Semi-supervised learning'],
                'correct':1
            },
            {
                'question':'What is the purpose of using Principal Component Analysis (PCA) in machine learning?',
                'answers':['To increase dimensionality', 'To reduce overfitting', 'To reduce dimensionality', 'To handle missing data'],
                'correct':2
            },
            {
                'question':'Which of the following is a method to handle class imbalance in a dataset?',
                'answers':['Random Initialization', 'Oversampling', 'Stochastic Gradient Descent', 'Dropout'],
                'correct':1
            },
            {
                'question':'Which machine learning algorithm is most suitable for predicting continuous numerical values?',
                'answers':['Logistic Regression', 'K-Means Clustering', 'Decision Trees', 'Linear Regression'],
                'correct':3
            },
            {
                'question':'In which scenario is the F1 score preferred over accuracy as a metric?',
                'answers':['When the dataset is balanced', 'When precision and recall are equally important', 'When the dataset contains continuous variables', 'When false positives are more important than false negatives'],
                'correct':1
            },
            {
                'question':'Which of the following is a characteristic of a support vector machine (SVM)?',
                'answers':['It is only used for regression tasks', 'It relies on the concept of margin maximization', 'It requires very large datasets to perform well', 'It is prone to overfitting'],
                'correct':1
            },
            {
                'question':'In machine learning, what is the "Curse of Dimensionality"?',
                'answers':['The difficulty of processing high-dimensional data', 'The overfitting that happens with too many features', 'The inability to converge during training', 'The low performance of models on unseen data'],
                'correct':0
            },
            {
                'question':'Which of the following techniques is used to handle overfitting in decision trees?',
                'answers':['Pruning', 'Feature scaling', 'Data augmentation', 'Early stopping'],
                'correct':0
            },
            {
                'question':'Which of the following is a characteristic of K-Means clustering?',
                'answers':['It is a supervised learning algorithm', 'It requires specifying the number of clusters in advance', 'It uses gradient descent for optimization', 'It is used for hierarchical clustering'],
                'correct':1
            },
            {
                'question':'In Gradient Boosting, how are new trees created?',
                'answers':['By independently training each tree', 'By combining results from random subsets of features', 'By training on the residuals of the previous trees', 'By randomly splitting the data'],
                'correct':2
            },
            {
                'question':'What is the purpose of using regularization in machine learning models?',
                'answers':['To improve convergence speed', 'To penalize large model coefficients and prevent overfitting', 'To handle imbalanced datasets', 'To reduce training time'],
                'correct':1
            },
            {
                'question':'Which of the following optimizers is widely used to avoid the vanishing gradient problem?',
                'answers':['SGD', 'Momentum', 'Adam', 'AdaBoost'],
                'correct':2
            },
            {
                'question':'What does \"bias-variance tradeoff\" refer to in machine learning?',
                'answers':['The balance between training time and accuracy', 'The balance between a model complexity and its generalization ability', 'The tradeoff between precision and recall', 'The tradeoff between using labeled and unlabeled data'],
                'correct':1
            },
            {
                'question':'What is a common problem encountered when using too many features in a machine learning model?',
                'answers':['Feature scaling', 'Gradient vanishing', 'Dimensionality reduction', 'Multicollinearity'],
                'correct':3
            },
            {
                'question':'Which of the following methods does not belong to ensemble learning?',
                'answers':['Random Forest', 'Gradient Boosting', 'K-Nearest Neighbors', 'Bagging'],
                'correct':2
            },
            {
                'question':'In time-series forecasting, what does autocorrelation measure?',
                'answers':['The correlation between the time-series data and its lagged version', 'The variance of the time series', 'The rate of change in the time series', 'The linearity of the time series'],
                'correct':0
            },
            {
                'question':'In unsupervised learning, which of the following metrics is commonly used to evaluate clustering algorithms?',
                'answers':['AUC-ROC', 'F1 Score', 'Silhouette Score', 'Precision-Recall'],
                'correct':2
            },
            {
                'question':'Which of the following algorithms is typically used for anomaly detection?',
                'answers':['Naive Bayes', 'K-Means', 'Isolation Forest', 'Support Vector Machine'],
                'correct':2
            },
            {
                'question':'In stochastic gradient descent, what does the term \'stochastic\' refer to?',
                'answers':['The use of small random batches of data for updates', 'The use of different activation functions', 'Random initialization of weights', 'The gradual increase of learning rates during training'],
                'correct':0
            },
            {
                'question':'What is the main advantage of using the k-Nearest Neighbors (k-NN) algorithm?',
                'answers':['It is computationally efficient for large datasets', 'It does not require any assumptions about the data distribution', 'It is resistant to noisy data', 'It automatically handles feature selection'],
                'correct':1
            },
        ]
        app_development = [
            {
                'question':'Which architecture pattern is most commonly used in modern mobile app development?',
                'answers':['MVC (Model-View-Controller)', 'MVVM (Model-View-ViewModel)', 'MVP (Model-View-Presenter)', 'All of the above'],
                'correct':3
            },
            {
                'question':'Which of the following is a benefit of using the Flutter framework for mobile app development?',
                'answers':['Directly compiles to native machine code', 'Uses WebAssembly for performance', 'Supports Kotlin and Swift natively', 'Relies on Java for compilation'],
                'correct':0
            },
            {
                'question':'Which lifecycle method is invoked when an activity in Android is no longer visible to the user?',
                'answers':['onCreate()', 'onResume()', 'onPause()', 'onStop()'],
                'correct':3
            },
            {
                'question':'In iOS development, which pattern is commonly used to handle data passing between views?',
                'answers':['Delegate Pattern', 'Adapter Pattern', 'Factory Pattern', 'Observer Pattern'],
                'correct':0
            },
            {
                'question':'In React Native, what is the correct way to handle asynchronous operations?',
                'answers':['Using Promises', 'Using async/await', 'Using callbacks', 'All of the above'],
                'correct':3
            },
            {
                'question':'Which database is often used for offline data storage in mobile app development?',
                'answers':['MySQL', 'SQLite', 'PostgreSQL', 'MongoDB'],
                'correct':1
            },
            {
                'question':'In Android development, what is the primary purpose of the Intent class?',
                'answers':['To pass data between activities and components', 'To render UI components', 'To manage threading', 'To store activity states'],
                'correct':0
            },
            {
                'question':'Which of the following is a security feature implemented in mobile apps to prevent reverse engineering?',
                'answers':['Code obfuscation', 'Memory leaks', 'API versioning', 'Load balancing'],
                'correct':0
            },
            {
                'question':'Which iOS development tool is used to manage project dependencies?',
                'answers':['npm', 'CocoaPods', 'Gradle', 'Maven'],
                'correct':1
            },
            {
                'question':'In mobile app development, which of the following methods is used to optimize performance?',
                'answers':['Threading', 'Lazy loading', 'Image caching', 'All of the above'],
                'correct':3
            },
            {
                'question':'Which of the following tools would you use to debug an iOS app memory usage?',
                'answers':['Android Profiler', 'Xcode Instruments', 'Firebase Analytics', 'Appium'],
                'correct':1
            },
            {
                'question':'What does \"hot reload\" mean in the context of Flutter development?',
                'answers':['Reloading the entire app state from scratch', 'Applying code changes without restarting the app', 'Caching user inputs', 'Reducing app size on compilation'],
                'correct':1
            },
            {
                'question':'In mobile app development, what is the main advantage of using GraphQL over REST?',
                'answers':['Strong type-checking of queries', 'Version control for APIs', 'Decreased number of HTTP requests', 'Both A and C'],
                'correct':3
            },
            {
                'question':'In Android, which of the following components is NOT part of the Jetpack suite?',
                'answers':['Navigation Component', 'LiveData', 'Retrofit', 'ViewModel'],
                'correct':2
            },
            {
                'question':'In SwiftUI, what is the purpose of the @State property wrapper?',
                'answers':['To modify the UI\'s layout', 'To store a value that the view can mutate', 'To manage view navigation', 'To handle network requests'],
                'correct':1
            },
            {
                'question':'Which of the following languages can be used for iOS native app development?',
                'answers':['Java', 'Kotlin', 'Swift', 'Dart'],
                'correct':2
            },
            {
                'question':'Which cross-platform mobile development framework allows developers to write applications in Dart?',
                'answers':['Xamarin', 'Flutter', 'React Native', 'PhoneGap'],
                'correct':1
            },
            {
                'question':'In Android, which tool is typically used for managing build configurations and dependencies?',
                'answers':['Maven', 'Gradle', 'npm', 'CocoaPods'],
                'correct':1
            },
            {
                'question':'What is the primary purpose of using Redux in React Native?',
                'answers':['Managing the UI state', 'Managing global application state', 'Handling navigation between screens', 'Managing app animations'],
                'correct':1
            },
            {
                'question':'In mobile app testing, what does UI Automation test primarily focus on?',
                'answers':['Network performance', 'User interactions with the app', 'Backend logic', 'Database integrity'],
                'correct':1
            },
        ]
        return JsonResponse({'status': 'success', 'data': {'machine_learning':machine_learning, 'app_development':app_development}})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


@csrf_exempt
def receive_post_job(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_skills = json.loads(data.get('required_skills', '[]'))
            print('yes')
            job_id = Jobs.objects.count()+1
            jobs = Jobs(
                job_id=str(job_id),
                company_username=data['company_username'],
                job_title=data['job_title'],
                job_description=data['job_description'],
                job_type=data['job_type'],
                job_EndDate=data['job_EndDate'],
                job_budget=data['job_budget'],
                job_duration=data['job_duration'],
                required_skills=required_skills,
            )
            jobs.save()
            return JsonResponse({'status': 'success', 'data_received': jobs.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def get_jobs(request):
    if request.method == 'GET':
        jobs = Jobs.objects.all()
        jobs_posting_data = [
            {
             "job_id": j.job_id, 
             "company_username": j.company_username,
             "job_title": j.job_title,
             "job_description": j.job_description,
             "job_type": j.job_type,
             "job_EndDate": j.job_EndDate,
             "job_budget": j.job_budget, 
             "job_duration": j.job_duration,
             "required_skills": j.required_skills
            }
            for j in jobs
        ]
        return JsonResponse({'status': 'success', 'data': jobs_posting_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


@csrf_exempt
def receive_proposal(request):
    if request.method == 'POST':
        try:
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
            job_id = data.get('job_id')
            if not job_id:
                return JsonResponse({'status': 'error', 'message': 'Missing job_id in request'}, status=400)
            try:
                job_instance = Jobs.objects.get(id=job_id)
            except Jobs.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': f'Job with ID {job_id} not found'}, status=404)
            proposal = Proposal(
                job_id_id=job_instance,
                user_name=data.get('user_name', ''),
                proposal_message=data.get('proposal_message', '')
            )
            proposal.save()
            return JsonResponse({'status': 'success', 'data_received': proposal.id})
        except Exception as e:
            print(f"Unhandled Error: {e}")
            return JsonResponse({'status': 'error', 'message': 'Internal server error'}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def get_proposal(request):
    if request.method == 'GET':
        proposal = Proposal.objects.all()
        proposal_posting_data = [
            {
                "job_id": p.job_id_id_id,
                "user_name": p.user_name,
                "proposal_message": p.proposal_message
            }
            for p in proposal
        ]
        return JsonResponse({'status': 'success', 'data': proposal_posting_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})


@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            orders = Place_orders(
                job_id_id_id=str(data['job_id_id_id']),
                user_name=data['user_name'],
                budget=data['budget'],
                end_date=data['end_date']
            )
            orders.save()
            return JsonResponse({'status': 'success', 'data_received': orders.id})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def get_orders(request):
    if request.method == 'GET':
        orders = Place_orders.objects.all()
        orders_data = [
            {
                "job_id": o.job_id_id_id,
                "user_name": o.user_name,
                "order_time": o.order_time,
                "budget": o.budget,
                "end_date": o.end_date
            }
            for o in orders
        ]
        return JsonResponse({'status': 'success', 'data': orders_data})
    return JsonResponse({'status': 'error', 'message': 'Only GET method is allowed'})

from django.shortcuts import redirect, render
from django.contrib import messages
from floodapp.models import Camps, Users
import numpy as np
import joblib

# Create your views here.
def index(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        return render(request,"index.html",{'current_user':current_user,'user':user})
    return render(request,"index.html")
def userregister(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        phone=request.POST['phone']
        emailexists=Users.objects.filter(EmailID=email)
        if emailexists:
            messages.error(request,"Email id already exists")
        elif passw!=cpass:
            messages.error(request,"Password doesnt match")
        else:
            Users.objects.create(Name=name,EmailID=email,Password=passw,PhoneNo=phone)
            return redirect('/')
    return render(request,"register.html")
def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        passw=request.POST['password']
        user=Users.objects.filter(EmailID=email,Password=passw)
        if user:
            request.session['EmailID']=email
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials")
    return render(request,"login.html")
def userlogout(request):
    del request.session['EmailID']
    return redirect('/')
def prediction(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        # Preprocess the dataset
        
        if request.method=='POST':
            try:
                year = float(request.POST['year'])
                jan = float(request.POST['jan'])
                feb = float(request.POST['feb'])
                mar = float(request.POST['mar'])
                apr = float(request.POST['apr'])
                may = float(request.POST['may'])
                jun = float(request.POST['jun'])
                jul = float(request.POST['jul'])
                aug = float(request.POST['aug'])
                sep = float(request.POST['sep'])
                oct = float(request.POST['oct'])
                nov = float(request.POST['nov'])
                dec = float(request.POST['dec'])
                annual = float(request.POST['annual'])

                # Create input array
                input_data = np.array([year, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, annual]).reshape(1, -1)

                # Load the trained model and scaler
                loaded_model = joblib.load('static/assets/h5/decision_tree_model.h5')
                loaded_scaler = joblib.load('static/assets/h5/standard_scaler.h5')

                # Scale the input data
                input_data_scaled = loaded_scaler.transform(input_data)

                # Make prediction
                prediction = loaded_model.predict(input_data_scaled)

                # Display prediction result
                if prediction[0] == 1:
                    messages.error(request,"Predicted Output: YES (Flood)")
                    return render(request,"prediction.html",{'current_user':current_user,'user':user,'result':prediction})
                else:
                    messages.error(request,"Predicted Output: NO (No Flood)")
                    return render(request,"prediction.html",{'current_user':current_user,'user':user,'result':prediction})
            except Exception as e:
                    messages.error(request, f"An error occurred: {str(e)}")
        return render(request,"prediction.html",{'current_user':current_user,'user':user})
    else:
        return render(request,"prediction.html")
def profile(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        return render(request,"profile.html",{'current_user':current_user,'user':user})
def updateprofile(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        if request.method=='POST':
            name=request.POST['name']
            passw=request.POST['password']
            cpass=request.POST['cpassword']
            phone=request.POST['phone']
            if passw!=cpass:
                messages.error(request,"Password doesnt match")
            else:
                user.Name=name
                user.Password=passw
                user.PhoneNo=phone
                user.save()
                return redirect('profile')
        return render(request,"updateprofile.html",{'current_user':current_user,'user':user})
def floods(request):
    return render(request,"floods.html")
def reliefcamps(request):
    camp=Camps.objects.all()
    return render(request,"reliefcamps.html",{'camp':camp})
def prevention(request):
    return render(request,"prevention.html")
def presentprediction(request):
    if 'EmailID' in request.session:
        current_user=request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        if request.method=='POST':
            rain=float(request.POST['rainfall'])
            if rain >= 100:
                messages.error(request,"Predicted Output: YES (Flood)")
                return render(request,"presentprediction.html",{'current_user':current_user,'user':user,'result':rain})
            else:
                messages.error(request,"Predicted Output: NO (No Flood)")
                return render(request,"presentprediction.html",{'current_user':current_user,'user':user,'result':rain})
        return render(request,"presentprediction.html",{'current_user':current_user,'user':user})
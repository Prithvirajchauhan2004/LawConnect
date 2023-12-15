from django.shortcuts import render, redirect
from .models import ServiceProvider, Client
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        tel = request.POST.get("tel")
        register_as = request.POST.get("register_as")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if (
                ServiceProvider.objects.filter(username=username).exists()
                or Client.objects.filter(username=username).exists()
            ):
                messages.info(request, "Username Taken!")
                return redirect("register")
            elif (
                ServiceProvider.objects.filter(email=email).exists()
                or Client.objects.filter(email=email).exists()
            ):
                messages.info(request, "Email Taken!")
                return redirect("register")
            else:
                if register_as == "service-provider":
                    """service_provider = ServiceProvider(username=username,
                    email=email,
                    ph_number=tel,

                    password=password1,
                    )"""
                    auth_user = User(
                        username=username,
                        email=email,
                        password=password1,
                    )

                    auth_user.save()
                    """service_provider.save()"""

                    return redirect('personal-detials')
                else:
                    client = Client(
                        username=username,
                        email=email,
                        tel=tel,
                        password=password1,
                    )
                    auth_user = User(
                        username=username,
                        email=email,
                        password=password1,
                    )

                    auth_user.save()
                    client.save()

                    return redirect("law-home")

        else:
            messages.info(request, "Passswords Not Matching!")
            return redirect("register")
    else:
        return render(request, "users/sign.html")


def PersonalDetials(request):
    if request.method == "POST":
        
        first_name = request.POST.get("Name_First")
        last_name = request.POST.get("Name_Last")
        D_O_B = request.POST.get("Date")
        gender = request.POST.get("Radio")
        work_as = request.POST.get("Dropdown")
        f_first_name = request.POST.get("Name1_First")
        f_last_name = request.POST.get("Name1_Last")
        interest = request.POST.get("Radio2")
        ph_number = request.POST.get("PhoneNumber_countrycode")
        a_number = request.POST.get("PhoneNumber_countrycode1")
        email = request.POST.get("Email")
        add = request.POST.get("Name_Firstadd")
        city = request.POST.get("Name_Lastadd")
        state = request.POST.get("Name_FirstS")
        P_code = request.POST.get("Name_LastPC")
        country = request.POST.get("Name_LastC")
        college = request.POST.get("MultiLine")
        cou_desc = request.POST.get("MultiLine1")
        comp = request.POST.get("MultiLineC")
        com_desc = request.POST.get("MultiLine1C")
        adhar = request.POST.get("FileUpload")
        cert = request.POST.get("ImageUpload")

        service_provider = ServiceProvider(
            first_name=first_name,
            last_name=last_name,
            DOB=D_O_B,
            Gender=gender,
            work_as=work_as,
            father_first_name=f_first_name,
            father_last_name=f_last_name,
            interest=interest,
            ph_number=ph_number,
            alt_number=a_number,
            email=email,
            add=add,
            city=city,
            state=state,
            pin_code=P_code,
            country=country,
            college=college,
            course_desc=cou_desc,
            company=comp,
            work_desc=com_desc,
            adhar=adhar,
            bar_certificate=cert,
        )

        service_provider.save()

        return redirect("law-home")

    else:
        return render(request, "users/personal.html")

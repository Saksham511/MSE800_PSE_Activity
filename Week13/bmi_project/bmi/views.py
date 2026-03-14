from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height")) / 100

        bmi = round(weight / (height ** 2), 2)

        if bmi < 20:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        else:
            category = "Overweight"

    return render(request, "index.html", {"bmi": bmi, "category": category})

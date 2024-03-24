import urllib

from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .models import diameter_at_time
from .forms import inputForm
from django.shortcuts import redirect, render
from io import StringIO
import io, base64
from django.contrib import messages


def index(request):
    return HttpResponse("Hello! Welcome to the AirSafe App!")


def interpolateBspline(x, y, xi):
    yi = []
    A = y
    for i in xi:
        #if x[0] <= i <= x[1]:
        index = 0
        while x[index] < i:
            index += 1
        if x[index] == i:
            yi.append(y[index])
        else:
            yi.append(y[index - 1] + (i - x[index - 1]) * (y[index] - y[index - 1]) / (x[index] - x[index - 1]))
        # else:
        #     yi.append(None)
    return yi, A


def interpolatePoly(x, y, xi):
    aVal = len(x)
    if aVal != len(y):
        raise ValueError("Error: x and y must have the same number of elements")

    A = np.zeros((len(x), aVal))

    for i in range(aVal):
        A[:, i] = np.array(x)**i

    co = np.linalg.solve(A, y)

    yi = np.polyval(co[::-1], xi)

    return yi, co

def plot(request):
        fig = plt.figure(num=1, clear=True)
        timeArray = []
        diameterArray = []
        items = diameter_at_time.objects.all().order_by('time')
        for item in items:
            timeArray.append(float(item.time))
            diameterArray.append(float(item.diameter))

        if len(timeArray) == 0 and len(diameterArray) == 0:
            return render(request, 'app/plot.html', {"text": "Error: Graphs couldn't be generated because no data was entered!"})  # Render a template indicating no data


        f, axes = plt.subplots(3, 1)
        f.suptitle("Interpolated Graphs of Time vs Volume")

        axes[0].plot(timeArray, diameterArray, '.-')
        axes[0].set_ylabel('Diameter')
        axes[0].set_xlabel('Time')
        axes[0].set_title('Original Data')


        # calculates times at which to interpolate
        tInterpolated = np.linspace(np.min(timeArray), np.max(timeArray), 100)
        yiP, aP = interpolatePoly(timeArray, diameterArray, tInterpolated)
        axes[1].plot(tInterpolated, yiP, '.-')
        axes[1].set_ylabel('Diameter')
        axes[1].set_xlabel('Time')
        axes[1].set_title('Polynomial Interpolation')


        yiB, aB = interpolateBspline(timeArray, diameterArray, tInterpolated)
        axes[2].plot(tInterpolated, yiB, '.-')
        axes[2].set_ylabel('Diameter')
        axes[2].set_xlabel('Time')
        axes[2].set_title('B-Spline Interpolation')

        plt.tight_layout()


        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format = 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        context = {}
        context['data'] = uri
        return render(request, 'app/plot.html', context)


def home(request):
    form = inputForm(request.POST)
    #display data
    dataset = diameter_at_time.objects.all().order_by('time')

    if request.method == 'POST':
        # form.is_valid() make the form to submit only
        # when it contains CSRF Token
        if form.is_valid():
            # form.cleaned_data returns a dictionary of validated form input fields
            time = form.cleaned_data['time']
            diameter = form.cleaned_data['diameter']
            if diameter_at_time.objects.filter(time=time).exists():
                messages.error(request, 'Time already exists in the database.')
                return redirect('home')
            queryset = diameter_at_time(time = time, diameter = diameter)
            queryset.save()
            return redirect('home')
        else:
            pass
    context = {
        'form': form,
        'dataset': dataset,
        #'graph': plot()
    }
    return render(request, 'app/home.html', context)

def delete(request, id):
    entry = diameter_at_time.objects.get(id = id)
    entry.delete()
    return redirect('home')

def ecgData(request):
    fig = plt.figure(num=1, clear=True)
    df = pd.read_csv("airsafeapp/echocardiogram.csv", low_memory=False) #https://www.kaggle.com/code/loganalive/echocardiogram-dataset-uci/input

    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['lvdd'] = pd.to_numeric(df['lvdd'], errors='coerce')

    df = df.dropna(subset=['age', 'lvdd'])


    plt.scatter(df['age'], df['lvdd'], color='black')

    # Calculate line of best fit
    slope, intercept = np.polyfit(df['age'], df['lvdd'], 1)
    x = np.array([min(df['age']), max(df['age'])])
    y = slope * x + intercept

    # Plot the line of best fit
    plt.plot(x, y, color='red')

    # Calculate correlation coefficient (r value)
    r_value = np.corrcoef(df['age'], df['lvdd'])[0, 1]
    print("Correlation coefficient (r value):", r_value)

    # Add labels and title
    plt.xlabel('Age')
    plt.ylabel('LVDD')
    plt.title('Scatter Plot with Line of Best Fit for Age vs LVDD')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    context = {}
    context['data'] = uri
    return render(request, 'app/plot.html', context)





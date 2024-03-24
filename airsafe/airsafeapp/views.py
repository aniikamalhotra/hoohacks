import urllib

from django.http import HttpResponse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .models import volume_at_time
from .forms import inputForm
from django.shortcuts import redirect, render
from io import StringIO
import io, base64


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
        timeArray = []
        volumeArray = []
        items = volume_at_time.objects.all().order_by('time')
        for item in items:
            timeArray.append(float(item.time))
            volumeArray.append(float(item.volume))

        if len(timeArray) == 0 and len(volumeArray) == 0:
            return render(request, 'app/plot.html', {"text": "Error: Graphs couldn't be generated because no data was entered!"})  # Render a template indicating no data


        f, axes = plt.subplots(3, 1)
        f.suptitle("Interpolated Graphs of Time vs Volume")

        axes[0].plot(timeArray, volumeArray, '.-')
        axes[0].set_ylabel('Volume')
        axes[0].set_xlabel('Time')
        axes[0].set_title('Original Data')


        # calculates times at which to interpolate
        tInterpolated = np.linspace(np.min(timeArray), np.max(timeArray), 100)
        yiP, aP = interpolatePoly(timeArray, volumeArray, tInterpolated)
        axes[1].plot(tInterpolated, yiP, '.-')
        axes[1].set_ylabel('Volume')
        axes[1].set_xlabel('Time')
        axes[1].set_title('Polynomial Interpolation')


        yiB, aB = interpolateBspline(timeArray, volumeArray, tInterpolated)
        axes[2].plot(tInterpolated, yiB, '.-')
        axes[2].set_ylabel('Volume')
        axes[2].set_xlabel('Time')
        axes[2].set_title('B-Spline Interpolation')

        plt.tight_layout()


        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format = 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        return render(request, 'app/plot.html', {'data': uri})


def home(request):
    form = inputForm(request.POST)
    #display data
    dataset = volume_at_time.objects.all()

    if request.method == 'POST':
        # form.is_valid() make the form to submit only
        # when it contains CSRF Token
        if form.is_valid():
            # form.cleaned_data returns a dictionary of validated form input fields
            time = form.cleaned_data['time']
            volume = form.cleaned_data['volume']
            queryset = volume_at_time(time = time, volume = volume)
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
    entry = volume_at_time.objects.get(id = id)
    entry.delete()
    return redirect('home')


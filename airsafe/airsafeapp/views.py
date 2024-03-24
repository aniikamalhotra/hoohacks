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

def plot():
        timeArray = []
        volumeArray = []
        items = volume_at_time.objects.all()
        for item in items:
            timeArray.append(float(item.time))
            volumeArray.append(float(item.volume))
        print(timeArray)
        print(volumeArray)
        f, axes = plt.subplots(3, 1)
        axes[0].plot(timeArray, volumeArray, '.-')
        axes[0].set_ylabel('Volume')

        # calculates times at which to interpolate
        tInterpolated = np.linspace(np.min(timeArray), np.max(timeArray), 100)
        yiP, aP = interpolatePoly(timeArray, volumeArray, tInterpolated)
        axes[1].plot(tInterpolated, yiP, '.-')
        axes[1].set_ylabel('Volume')

        yiB, aB = interpolateBspline(timeArray, volumeArray, tInterpolated)
        axes[2].plot(tInterpolated, yiB, '.-')
        axes[2].set_ylabel('Volume')


        plt.show(block=True)
        plt.interactive(False)
        fig = plt.show()
        # plt.show(block=True)
        #
        # imgdata = StringIO()
        # fig.savefig(imgdata, format='svg')
        # imgdata.seek(0)
        #
        # data = imgdata.getvalue()
        # context = []
        # flike = io.BytesIO()
        # fig.savefig(flike)
        # b64 = base64.b64encode(flike.getvalue()).decode()
        # context['chart'] = b64
        # return context


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
            timeArray = []
            volumeArray = []
            items = volume_at_time.objects.all()
            for item in items:
                timeArray.append(float(item.time))
                volumeArray.append(float(item.volume))
            print(timeArray)
            print(volumeArray)
            f, axes = plt.subplots(3, 1)
            axes[0].plot(timeArray, volumeArray, '.-')
            axes[0].set_ylabel('Volume')

            # calculates times at which to interpolate
            tInterpolated = np.linspace(np.min(timeArray), np.max(timeArray), 100)
            yiP, aP = interpolatePoly(timeArray, volumeArray, tInterpolated)
            axes[1].plot(tInterpolated, yiP, '.-')
            axes[1].set_ylabel('Volume')

            yiB, aB = interpolateBspline(timeArray, volumeArray, tInterpolated)
            axes[2].plot(tInterpolated, yiB, '.-')
            axes[2].set_ylabel('Volume')

            plt.show(block=True)
            plt.interactive(False)

            plt.savefig('plot.png')
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


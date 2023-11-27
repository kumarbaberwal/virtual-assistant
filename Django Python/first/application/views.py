from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from application.models import Contact
from django.contrib import messages
from application.models import Audio
from application.models import Additional_information

from gtts.tts import gTTS
from io import BytesIO
from pygame import mixer
import pygame
import time
from base64 import b64encode
from django.http import JsonResponse

import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit
import string
import os

def home(request):
    # return HttpResponse("This is Home Page")
    return render(request,"header.html")


def about(request):
    return render(request,"about.html")

def services(request):
    if request.method=="POST":
        start=request.POST.get("start")
        audio=Audio(audio=start)
        audio.save()

    return render(request,"services.html")


def additional_information(request):
    if request.method=="POST":
        Command=request.POST.get("Command")
        addition_information=Additional_information(Command=Command)
        addition_information.save()
        messages.success(request, "Your Command has been sent.")
        a=Command2=Additional_information.objects.last()
        
        context={"Command2":Command2,}
        return render(request,"additional_information.html",{"Command2":Command2,})
    
    return render(request,"additional_information.html")

def contact(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        Feedback=request.POST.get("Feedback")
        contact=Contact(Name=Name,Email=Email,Feedback=Feedback)
        contact.save()
        messages.success(request, "Your Feedback has been sent.")
    return render(request,"contact.html")

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text')

        # Generate speech using gTTS
        tts = gTTS(text)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        # Encode the audio data as base64
        audio_base64 = b64encode(audio_buffer.getvalue()).decode('utf-8')

        return JsonResponse({'audio_data': audio_base64})

    return render(request, 'additional_information.html')
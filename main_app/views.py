from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Power, Suit, Photo
from .forms import TrainingForm

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'superpowercollector'

# Create your views here.
class PowersCreate(CreateView):
    model = Power
    fields = '__all__'
    success_url = '/powers/'

class PowersUpdate(UpdateView):
    model = Power
    fields = ['description', 'level', 'weakness']

class PowersDelete(DeleteView):
    model = Power
    success_url = '/powers/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def powers_index(request):
    powers = Power.objects.all() 
    return render(request, 'powers/index.html', {'powers': powers})

def powers_details(request, power_id):
    power = Power.objects.get(id=power_id)
    suits_power_doesnt_have = Suit.objects.exclude(id__in = power.suits.all().values_list('id'))
    training_form = TrainingForm()
    return render(request, 'powers/details.html', {
        'training_form': training_form, 'power': power, 'suits': suits_power_doesnt_have
    })

def add_practice(request, power_id):
  # create the ModelForm using the data in request.POST
  form = TrainingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_training = form.save(commit=False)
    
    new_training.power_id = power_id
    new_training.save()
  return redirect('details', power_id=power_id)

def add_photo(request, power_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to power_id or power (if you have a power object)
            photo = Photo(url=url, power_id=power_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', power_id=power_id)

def assoc_suit(request, power_id, suit_id):
    Power.objects.get(id=power_id).suits.add(suit_id)
    return redirect('details', power_id=power_id)
    
class SuitList(ListView):
  model = Suit

class SuitDetail(DetailView):
  model = Suit

class SuitCreate(CreateView):
  model = Suit
  fields = '__all__'

class SuitUpdate(UpdateView):
  model = Suit
  fields = ['name', 'color']

class SuitDelete(DeleteView):
  model = Suit
  success_url = '/suits/'

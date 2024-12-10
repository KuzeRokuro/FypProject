from django.shortcuts import render
from Records.models import Player  # Replace 'YourModelName' with the name of your model

def record_list(request):
    records = Player.objects.all()  # Fetch all records from the database
    return render(request, 'record_list.html', {'records': records})

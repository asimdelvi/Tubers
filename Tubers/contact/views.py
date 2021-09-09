from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hiretuber
from .forms import ContactAdminForm

# Create your views here.
def hiretuber(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    city = request.POST['city']
    state = request.POST['state']
    phone_number = request.POST['phone_number']
    message = request.POST['message']
    user_id = request.POST['user_id']
    tuber_id = request.POST['tuber_id']
    tuber_name = request.POST['tuber_name']

    hiretuber = Hiretuber(first_name = first_name,
                    last_name = last_name,
                    email = email,
                    city = city,
                    state = state,
                    phone_number = phone_number,
                    message = message,
                    user_id = user_id,
                    tuber_id = tuber_id,
                    tuber_name = tuber_name)
    hiretuber.save()

  messages.success(request, 'Thanks for reaching out!')
  return redirect(f'../youtubers/{tuber_id}', tuber_id)

def contact_admin(request):
  if request.method == 'POST':
    form = ContactAdminForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contact')
  else:
    form = ContactAdminForm()

  data = {
    'form' : form
  }
  return render(request, 'webpages/contact.html', data)

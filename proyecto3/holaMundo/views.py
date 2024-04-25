from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def hola(request):
#     return HttpResponse("""
#     <h1>Hola Mundo!!!</h1>
#     <a>LINK</a>
#     <p>Esta es mi primera aplicación con Django mostrando HTML</p>
#     """)
def Home(request):
    return HttpResponse("""
    <h1>Lorem ipsum</h1>
    """)

def about(request):
    return HttpResponse("""
    <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita aspernatur quasi earum vel consequatur itaque debitis laudantium architecto nesciunt delectus deserunt aliquam ex eius praesentium, quisquam dolorum tempora quaerat. Eaque!
    </p>
    """)

def contact(request):
    return HttpResponse("""
    <form action="/my-handling-form-page" method="post">
    <ul>
      <li>
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="user_name" />
      </li>
      <li>
        <label for="mail">Correo electrónico:</label>
        <input type="email" id="mail" name="user_mail" />
      </li>
      <li>
        <label for="msg">Mensaje:</label>
        <textarea id="msg" name="user_message"></textarea>
      </li>
    </ul>
  </form>
  
    """)



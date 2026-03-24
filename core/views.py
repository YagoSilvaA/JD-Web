from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
def home(request):
    return HttpResponse("Hello from the candidate’s site!")
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def proposals(request):
    return render(request, "core/proposals.html")

def contact(request):
    return render(request, "core/contact.html")

def publicaciones(request):
    publicaciones = [
    {'titulo': 'La Historia del Perú en la Revista de la Universidad Católica', 'caratula': 'core/img/pub1.jpeg', 'url': 'https://repositorio.pucp.edu.pe/items/5775f3f9-fdf1-4979-b930-ceae02586fb4'},
    {'titulo': 'Conde de Superunda', 'caratula': 'core/img/pub2.jpeg', 'url': 'https://link2.com'},
    {'titulo': 'Hipólito Unanue o el Cambio en la Continuidad', 'caratula': 'core/img/pub3.jpeg', 'url': 'https://link3.com'},
    {'titulo': 'El Virrey Amat y su tiempo', 'caratula': 'core/img/pub4.jpeg', 'url': 'https://link4.com'},
    {'titulo': 'Una aproximación a la historiografía del siglo XIX', 'caratula': 'core/img/pub5.jpeg', 'url': 'https://link5.com'},
]

    pdfs = [
        {
            'titulo': 'Historiografía y nación en el Perú del siglo XIX',
            'archivo': 'core/pdfs/histopub1.pdf'
        },
        {
            'titulo': 'La visión de los historiadores. Desde los orígenes republicanos hasta su proyección actual',
            'archivo': 'core/pdfs/visionpub2.pdf'
        }
    ]

    return render(request, 'core/publicaciones.html', {
        'publicaciones': publicaciones,
        'pdfs': pdfs
    })
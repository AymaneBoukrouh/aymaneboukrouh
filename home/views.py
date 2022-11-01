from django.shortcuts import render
from home.models import Service, Project, Image

data = {
  "name": "Aymane Boukrouh",
  "profession": "Software Developer",
  "about": "I'm a software developer with 2+ years of professional experience as a fully-remote freelancer. I'm mostly in exprienced in web development (full-stack), but I've worked on various projects in different domains (e.g. web automation, etc.). I started learning programming back in 2018 as a hobby, and I've been pursuing it with passion ever since.",
  "about_technologies": "I'm most familiar with the following technologies:",
  "technologies": [
    {
      "title": "Back-End",
      "elements": ["FastAPI", "Flask", "Django"]
    },
    {
      "title": "Front-End",
      "elements": ["VueJS", "Bootstrap", "Webpack"]
    },
    {
      "title": "DevOps",
      "elements": ["Git", "CI/CD", "Docker"]
    },
    {
      "title": "Other",
      "elements": ["MySQL", "Cypress", "Selenium"]
    }
  ],
  "social_medias": [
    {
      "url": "https://www.github.com/AymaneBoukrouh",
      "icon": "bi-github"
    },
    {
      "url": "https://paypal.me/boukrouhaymane?country.x=MA&locale.x=en_US",
      "icon": "bi-paypal"
    },
    {
      "url": "https://www.linkedin.com/in/aymane-boukrouh-713473165/",
      "icon": "bi-linkedin"
    },
    {
      "url": "https://discordapp/users/aymaneboukrouh#0401",
      "icon": "bi-discord"
    },
    {
      "url": "https://wa.me/+212670100451",
      "icon": "bi-whatsapp"
    }
  ],
  "sections": [
    {
      "title": "Profile",
      "icon": "bi-person"
    },
    {
      "title": "About",
      "icon": "bi-info-circle"
    },
    {
      "title": "Services",
      "icon": "bi-laptop"
    },
    {
      "title": "Projects",
      "icon": "bi-card-list"
    },
    {
      "title": "Contact Me",
      "icon": "bi-envelope"
    }
  ]
}

def home(request):
    try:
        bg_home_src = Image.objects.get(name='bg-home').image.url
    except Image.DoesNotExist:
        bg_home_src = None

    return render(request, 'home.html', {
        'data': data,
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'bg_home_src': bg_home_src
    })

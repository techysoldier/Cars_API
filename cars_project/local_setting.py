# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0q4l_s35m@q+)@s-6%g1uy%$vma997xl$-@ielo-cv6de-=w7k'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'pass'
    }
}
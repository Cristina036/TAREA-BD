import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taylor-mi-patrona.settings')
import django
django.setup()


from App_tarea.models import Eras
from faker import Faker

faker_generator = Faker()



def populate(N=5):
    for entry in range(N):
        #Crear datos falsos
        fake_first_name = faker_generator.first_name()
        fake_last_name = faker_generator.last_name()
        fake_email = faker_generator.email()
        fake_phone_number = faker_generator.phone_number()

        #Crear registro falso
        mosqueteros = Eras.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, 
                                                 email=fake_email, phone_number=fake_phone_number)[0]
        

if __name__ == '__main__':
    print("Comienzo a poblar")
    populate(30)
    print("Ya quedó")
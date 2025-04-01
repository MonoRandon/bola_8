#Brandon Morales
#31/03/2025

import random

input("Hazme una pregunta: ")
bola8 = random.randint(0, 8)

if bola8 == 0:
    print("La bola mágica dice: Sí, definitivamente.")
elif bola8 == 1:
    print("La bola mágica dice: Con toda certeza, que si.")
elif bola8 == 2:
    print("La bola mágica dice: Sin lugar a dudas.")
elif bola8 == 3:
    print("La bola mágica dice: Pregunta confusa, intentalo de nuevo.")
elif bola8 == 4:
    print("La bola mágica dice: Pregúntalo nuevamente más tarde.")
elif bola8 == 5:
    print("La bola mágica dice: Mejor no decirte ahora.")
elif bola8 == 6:
    print("La bola mágica dice: Mis fuentes dicen que no.")
elif bola8 == 7:
    print("La bola mágica dice: Mi respuesta no es muy favorable.")
else:
    print("La bola mágica dice: Muy dudoso.")


import cv2
import os

chemin_origine='f:/tt1'
chemin_destination='f:/tt2/'
extension_image='jpg'
valeur_maximum=640

def larghaut(valeur_maximum,la_hauteur,la_largeur):
    nouvelle_largeur= valeur_maximum
    nouvelle_hauteur=int(((nouvelle_largeur)*la_hauteur)/la_largeur)
    nouvelle_taille=(nouvelle_largeur,nouvelle_hauteur)
    return nouvelle_taille

def hautlarg(valeur_maximum,la_hauteur,la_largeur):
    nouvelle_hauteur= valeur_maximum
    nouvelle_largeur=int(((nouvelle_hauteur)*la_largeur)/la_hauteur)       
    nouvelle_taille=(nouvelle_largeur,nouvelle_hauteur)
    return nouvelle_taille

def write(ELT,nouvelle_taille,nom_image):
    nouveau_element=cv2.resize(ELT,nouvelle_taille,interpolation = cv2.INTER_AREA)
    nouveau_nom_list=(chemin_destination,nom_image)
    nouveau_nom = ''.join(nouveau_nom_list)
    print (nom_image,'  : ',la_largeur,' x ',la_hauteur,'---------->',nouveau_nom,'  : ',nouvelle_taille[0],' x ',nouvelle_taille[1])
    cv2.imwrite(nouveau_nom,nouveau_element)

def move(nom_image,la_largeur,la_hauteur,chemin_destination,ELT):
    print(nom_image,'  : ',la_largeur,' x ',la_hauteur,'----------> move to',chemin_destination)
    nouveau_nom_list=(chemin_destination,nom_image)
    nouveau_nom = ''.join(nouveau_nom_list)
    cv2.imwrite(nouveau_nom,ELT)

CD = os.getcwd()
os.chdir(chemin_origine)
list_image= os.listdir()

list_imagesclean = [nom_image for nom_image in list_image if((len(nom_image.split('.')) > 1) 
        and (nom_image.split('.')[1].lower() in extension_image))]

for nom_image in list_imagesclean:
    ELT = cv2.imread(nom_image)
    la_hauteur, la_largeur, le_chanel = ELT.shape

    if la_largeur < valeur_maximum and la_hauteur <valeur_maximum:
        move(nom_image,la_largeur,la_hauteur,chemin_destination,ELT)

    elif la_largeur > la_hauteur:
        nouvelle_taille = larghaut(valeur_maximum,la_hauteur,la_largeur)
        write (ELT,nouvelle_taille,nom_image)
    elif la_hauteur > la_largeur:
        nouvelle_taille = hautlarg(valeur_maximum,la_hauteur,la_largeur)
        write (ELT,nouvelle_taille,nom_image)


           
           

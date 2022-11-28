import os



os.system('title Chemik')

imie = input("Jesteś graczem, który znalazł się w grze, która nazywa się " + 
             "chemik. \nPodaj swoje imię: ")
pytanie1 = input(f"{imie}, ile atomów w sobie ma tlen?\n" + 
                "p - 6, l - 8: ")

if pytanie1 == 'l':
    wybor = input("z czego jest zbudowany atom ?\n" + "z neutronu, jądra atomowego, protonu, elektronu - l, tlenu, wodoru, jądra atomowego, potasu ,selenu - a :")
    if wybor == 'l':
        print(f"{imie}!Gratulacje wygrałeś !")



    elif wybor == 'a,q,e,w,r,t,y,u,i,o,a,s,d,f,g,h,j,k,z,x,':
        print("Szkoda...")
    else:
        print("Nie ma takiej opcji.")
elif pytanie1 == 'a':
    wybor = input("co oznacza P ?\n" +
                   "w - potas , u - fosfor : ")
    if wybor == 'w':
        print(f"{imie}! przykro mi to zła odpowieć. " + 
              "sprubuj nastepnym razem!")
    elif wybor == 'u':
        wybor = input("grafit jest odmianą węgla pirwiastkowego ?\n" +
                     "t - tak , n - nie: ")
        if wybor == 't':
            print("Gratulacje wygrałeś !")
        elif wybor == 'b':
            imie_psa = input("dostajesz psa chemicznego w gratisie " + 
                               "Jak dałeś mu na imię?\n")
            print(f"Psa {imie_psa} rósł w Twoim domu, towarzysząc Ci w codziennym życiu.\n" +
                 "Jednak pewnego dnia, kiedy zapomniałeś go nakarmić, ugryzł cię " +
                 "i pobiedł do miasta. \n" +
                 "Morał: nie zabieraj ze sobą dzikich zwierząt.")
        elif wybor == 'n':
            print("Mądry wybór, choć może coś Cię ominęło?")
        else:
            print("Nie ma takiej opcji.")
    else:
        print("Nie ma takiej opcji. Niestety, nie udało ci się przejść gry" + 
              "przegrałeś.")
else:
    print("może uda ci się za innym razem.")
print("Koniec przygody.")

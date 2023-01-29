#DICTIONAR
#Description: reads the list of books
#Returns: a list of dictionary items that represents the books {titlu, autor, limba, nrpagini}
keys=("titlu","autor","limba","nrpagini")
KEY_TITLE = keys[0]
KEY_AUTHOR = keys[1]
KEY_LANG = keys[2]
KEY_PAGES = keys[3]
FRENCH = "FR"

def ReadListofBooks():

    list_carti = []

    while True:
        carte=input("Date carte: ").split(",")
        if carte==['']:
            break
        dict_carte=dict()
        for i in range(4):
            dict_carte[keys[i]] = carte[i].strip()
        list_carti.append(dict_carte)
    return list_carti

def NrBooksDonations(list_carti):
    nr_books = 0
    for carte in list_carti:
        if int(carte[KEY_PAGES]) > 200 and carte[KEY_LANG] != FRENCH:
            nr_books +=1
    return nr_books

def BooksForBrother(list_carti):
    list_authors = []
    for carte in list_carti:
        if carte[KEY_LANG] == FRENCH and int(carte[KEY_PAGES]) <= 200:
            list_authors.append(carte[KEY_AUTHOR])
    return list_authors

def GetBooksForDonations(list_carti):
    list_titles_donation = []
    for carte in list_carti:
        if int(carte[KEY_PAGES]) > 200 and carte[KEY_LANG] != FRENCH:
            list_titles_donation.append(carte[KEY_TITLE])
    return list_titles_donation
       
list_carti = ReadListofBooks()

print("")
print("Carti donate: ",NrBooksDonations(list_carti))
print("")
print("Fratele lui Ion primeste cartile scrise de: ",BooksForBrother(list_carti))
print("")
print("Carti care se vor dona: ",GetBooksForDonations(list_carti))
print("")

from art import logo
import os
print(logo)

print("Benevenuto sul sito delle aste nascoste")
asta_finita=False
offerte={}

def vincitoreAsta(user_offer):
    user_best_offer=0
    user_best_name=""
    for offerta in user_offer:
        offert_amount=offerte[offerta]    
        if offert_amount>user_best_offer:
            user_best_offer=offert_amount
            user_best_name=offerta
    print(f"La migliore offerta è di {user_best_name} che ha offerto {user_best_offer}$.")        
                
while not asta_finita:
    name=input("Inserisci il tuo nome: ").lower()
    offerta=int(input("Inserisci la tua offerta: $. "))
    offerte[name]=offerta
    request_to_user=input("C'è un altro offerente ? - Scrivi: 'si' oppure 'no' ")
    if request_to_user=="no" or request_to_user=='n':
        asta_finita=True
        vincitoreAsta(offerte)
    elif request_to_user=="yes" or request_to_user=="y":
        os.system('cls')        
    
     
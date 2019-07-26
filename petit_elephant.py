# coding: utf8

"""- Client pour Mastodon - auteur:cagliostro <atfield2501@gmail.com> -"""

from mastodon import Mastodon
from secretsElephant import *
import time
import sys


print('< Petit Elephant     ')
print('  client mastodon >  ')
print(' --------------------')
print('  \     /\  ___  /\  ')
print('   \   // \/   \/  \ ')
print('      ((    O O    ))')
print('       \  /     \ // ')
print('        \/  | |  \/  ')
print('         |  | |  |   ')
print('         |  | |  |   ')
print('         |   o   |   ')
print('         | |   | |   ')
print('         |m|   |m|   ')


aleph = False

def prompt_aide():
    """ Affiche un prompt d'aide """
    print('    * client mastodon *') 
    print('usage      : petit_elephant [commande]') 
    print('Commandes  :')
    print('               -h    : Prompt aide')
    print('             toot    : Envois un simple toot sur le réseau')
    print('             status  : Affiche le status du compte')
    print('             abb+    : Affiche la liste des abbonnements')
    print('             abb-    : Affiche la liste des abbonné.es')



class Petit_Elephant():
    """ Classe Principale """

    mastodon = Mastodon(access_token = 'pytooter_usercred.secret',
                         api_base_url = 'https://mastodon.social')
    
 #   mastodon.log_in(babar , babar_mdp,
 #                     to_file = 'pytooter_usercred.secret')

    Me_ID = mastodon._Mastodon__get_logged_in_id()
    
    def Ecriture(self,*args):
        """ classe pour l'ecriture simple de toots sur MAstodon """
        toot = args[0]
        Petit_Elephant.mastodon.toot(toot)

    def Conversation(self):
        """ Renvois le total de teet privés du l'utilisateur """
        flux = Petit_Elephant.mastodon.conversations()
        for i,e in enumerate(flux):
            print(str(i),str(e['last_status'])+"\n")
    
    def Liste_Emoji(self):
        """ Renvois une liste d'émoji """
        flux = Petit_Elephant.mastodon.custom_emojis()
        print("\n*  Liste Emoji   *\n")
        for e in flux:
            print(e['shortcode'])
            print(e['url'])        
            print(e['static_url'])        
    
    
    
    
    def Info_Instance(self):
        """ Affiche des info sur l'instance"""
        flux = Petit_Elephant.mastodon.instance() 
        print("\n*   Infos sur Instance   *\n")
        print(flux['description'])
        print(flux['short_description'])
        print(flux['email'])
        print(flux['title'])
        print(flux['uri'])
        print(flux['version'])
        print(flux['urls'])
        print(flux['stats'])
        print(flux['contact_account'])
        print(flux['languages'])
        print(flux['registrations'])
        print(flux['approval_required'])

    def Lecture_Instance(self):
        """ Affiche le nombres d'instances et leurs noms"""
        flux = Petit_Elephant.mastodon.instance_peers()
        for i,e in enumerate(flux):
            print(i+1,e)

    def Abbonnes(self):
        """ Renvois le nombre et le nom des abonné.es de l'utilisateur.trice """
        
        flux = Petit_Elephant.mastodon.account_followers(Petit_Elephant.Me_ID)
        for i,e in enumerate(flux):
            print(i+1,e['display_name'])

    def Abbonnements(self):
        """ Renvois le nombre et le nom des abonnements de l'utilisateur.trice """
        flux = Petit_Elephant.mastodon.account_following(Petit_Elephant.Me_ID,limit=None)
        for i,e in enumerate(flux):
            print(i+1,e['display_name'])
        

    def Recherche(self,*args):
        """ Recherche dans mastodon """
        flux = Petit_Elephant.mastodon.search(args[0])
        print('compte   : '+str(flux['accounts']))
        print('hashtags : '+str(flux['hashtags']))
        print('statues : '+str(flux['statuses']))

    def Favoris(self):
        """ """
        flux = Petit_Elephant.mastodon.favourites()
        for i,e in enumerate(flux):
            print(i+1,e['url'])
#            print(str(e['display_name'])+"\n")

    def Test1(self):
        """ """
        flux = Petit_Elephant.mastodon.endorsements()
        for i,e in enumerate(flux):
            print(i+1,e)
    
    def Notifications(self):
        """ """
        flux = Petit_Elephant.mastodon.notifications()[0]
        print("\n*   NOTIFICATION   *\n")
        print(flux['id'])
        print(flux['type'])
        auteur=flux['account']
        print(auteur['username'])


    def bidule(self):
        """ """
        while 1:
            flux = Petit_Elephant.mastodon.status_context(Petit_Elephant.Me_ID)
            print(flux['ancestors'])
            print(flux['descendants'])





    def Status(self):
        """ Affiche les informations relativent au compte mastodon """
        flux = Petit_Elephant.mastodon.account(Petit_Elephant.Me_ID)
        print("\n         *   STATUS   *\n")
        print("id                  : "+str(flux['id']))
        print("username            : "+str(flux['username']))
        print("acct                : "+str(flux['acct']))
        print("displayname         : "+str(flux['display_name']))
        print("locked              : "+str(flux['locked']))
        print("Création            : "+str(flux['created_at']))
        print("Abonnements         : "+str(flux['following_count']))
        print("Abonné.es           : "+str(flux['followers_count']))
        print("Status              : "+str(flux['statuses_count']))
        print("Note                : "+str(flux['note']))
        print("url                 : "+str(flux['url']))
        print("avatar              : "+str(flux['avatar']))
        print("header              : "+str(flux['header']))
        print("avatar_static       : "+str(flux['avatar_static']))
        print("header_static       : "+str(flux['header_static']))
        print("bot                 : "+str(flux['bot']))
        flux = Petit_Elephant.mastodon.account_verify_credentials()["source"]
        print("Mode privé          : "+str(flux['privacy']))
        print("Mode sensitive      : "+str(flux['sensitive']))
        print("Note                : "+str(flux['note']))
        flux = Petit_Elephant.mastodon.mutes(Petit_Elephant.Me_ID)
        print('             liste des comptes mutés   : '+str(flux))
        flux = Petit_Elephant.mastodon.blocks(Petit_Elephant.Me_ID)
        print('             Liste des comptes blockés : ')
        a = flux[0]
        print(a['username'])
        print(a['display_name'])
        print(a['note'])
        flux = Petit_Elephant.mastodon.domain_blocks()
        print(flux)

    def Flux_debug(self):
        """ """
        while 1:
            flux = Petit_Elephant.mastodon.account_statuses(Petit_Elephant.Me_ID)
    
    
    
    def flux_acceuil(self):
        while 1:
            flux = Petit_Elephant.mastodon.timeline_home()
            a ,b = flux[0], flux[1]
            print("")
            s = a['account']
            print(s['display_name'])
            print(b['content'])
            time.sleep(0.6)

    def flux_local(self):
        while 1:
            flux = Petit_Elephant.mastodon.timeline_local()
            print(flux)

    def flux_public(self):
        while 1:
            flux = Petit_Elephant.mastodon.timeline_public()
            a ,b = flux[0], flux[1]
            print("")
            s = a['account']
            print(s['display_name'])
            print(b['content'])
#            time.sleep(0.6)



if __name__ == "__main__":
    ## Jolie Instance de la classe Petit_Elephant
    tlaloc = Petit_Elephant()
    # Lecture des arguments
    if len(sys.argv) < 2:
        print("- Veuillez spécifier un argument -")
        prompt_aide()
    if len(sys.argv) > 1:
        action = sys.argv[1]
        aleph = True
    if len(sys.argv) == 3:
        indice = sys.argv[2]
        aleph = True

    #print(sys.argv[1])
    if aleph == True:
        if action == '-h':
            prompt_aide()
        if action == 'toot':
            sujet = input("Toot : \n")
            tlaloc.Ecriture(sujet)
        if action == 'status':
            tlaloc.Status()
        if action == 'abb+':
            tlaloc.Abbonnements()
        if action == 'abb-':
            tlaloc.Abbonnes()




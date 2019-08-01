#! /usr/bin/python3
# coding: utf8

"""- Client pour Mastodon - auteur:cagliostro <atfield2501@gmail.com> -"""

from mastodon import Mastodon
from secretsElephant import *
import time
import random
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
    print('             help     : Prompt aide')
    print('             toot     : Envois un simple toot sur le réseau')
    print('             status   : Affiche le status du compte')
    print('             abb+     : Affiche la liste des abbonnements')
    print('             abb-     : Affiche la liste des abbonné.es')
    print('             flux1    : Affiche le flux acceuil')
    print('             flux2    : Affiche le flux de l instance')
    print('             flux3    : Affiche le flux global')
    print('             search   : Effectue une recherche par mot clée')
    print('             favoris  : Affiche la liste des bookmarks')
    print('             info     : Affiche info sur instance')
    print('             info_all : Affiche info sur instance')
    print('             notif    : Affiche les notifications')
    print('             direct   : Affiche les conversations privées')
    print('             cron     : Enclenche la repetition des toots de medias de  compte') 
    print('             truc1    : bof 1')
    print('             truc 2   : bof 2')

class Petit_Elephant():
    """ Classe Principale """

    mastodon = Mastodon(access_token = 'pytooter_usercred.secret',
                         api_base_url = 'https://mastodon.social')
    
 #   mastodon.log_in(babar , babar_mdp,
 #                     to_file = 'pytooter_usercred.secret')

    Me_ID = mastodon._Mastodon__get_logged_in_id()
    
    def Cron(self):
        """ Enclenche la repetition des toots de media """
        while 1:
            flux = Petit_Elephant.mastodon.account_statuses(Petit_Elephant.Me_ID, only_media=True)
            media_list = []
            for i,e in enumerate(flux):
                media_list.append(e['id'])
            cible = random.choice(media_list)
            print(media_list)
            Petit_Elephant.mastodon.status_reblog(cible)
            print('Toot!!!')
            time.sleep(900) 
       
       
    
    
    def Ecriture(self,*args):
        """ classe pour l'ecriture simple de toots sur MAstodon """
        toot = args[0]
        Petit_Elephant.mastodon.toot(toot)

    def Conversation(self):
        """ Renvois le total de teet privés du l'utilisateur """
        flux = Petit_Elephant.mastodon.conversations()
        print("\n *    Conversations    *\n")
        print(flux)
        for i,e in enumerate(flux):
            print(str(i+1),str(e['last_status'])+"\n")
    
    def Liste_Emoji(self):
        """ Renvois une liste d'émoji """
        flux = Petit_Elephant.mastodon.custom_emojis()
        print(flux)
        print("\n*  Liste Emoji   *\n")
        for e in flux:
            print(e['shortcode'])
            print(e['url'])        
            print(e['static_url'])        
    
    
    
    
    def Info_Instance(self):

        """ Affiche des info sur l'instance"""
        flux = Petit_Elephant.mastodon.instance() 
        print("\n*   Infos sur Instance   *\n")
        print('description : '+str(flux['description']))
#        print('courte description : '+str(flux['short_description']))
        print('email : '+str(flux['email']))
        print('titre : '+str(flux['title']))
        print('uri : '+str(flux['uri']))
        print('version : '+str(flux['version']))
        stupeur = flux['urls'] 
        print('urls : '+str(stupeur['streaming_api']))
        tremblement = flux['stats']
        print('stats compte : '+str(tremblement['status_count']))
        print('stats domaine : '+str(tremblement['domain_count']))
        print('stats user : '+str(tremblement['user_count']))
        print('contact : '+str(flux['contact_account']))
        print('langue : '+str(flux['languages']))
        print('registration : '+str(flux['registrations']))
        print('approuvement requiré : '+str(flux['approval_required']))

    def Lecture_Instance(self):
        """ Affiche le nombres d'instances et leurs noms"""
        flux = Petit_Elephant.mastodon.instance_peers()
        for i,e in enumerate(flux):
            print(i+1,e)

    def Abbonnes(self):
        """ Renvois le nombre et le nom des abonné.es de l'utilisateur.trice """ 
        flux = Petit_Elephant.mastodon.account_followers(Petit_Elephant.Me_ID,limit=None)
#        print(flux)
        for i,e in enumerate(flux):
            print(str(i+1),str(e['display_name'])+' . ',str(e['username']))

    def Abbonnements(self):
        """ Renvois le nombre et le nom des abonnements de l'utilisateur.trice """
        flux = Petit_Elephant.mastodon.account_following(Petit_Elephant.Me_ID,limit=None)
#        print(flux)
        for i,e in enumerate(flux):
            print(str(i+1),str(e['display_name'])+' . ',str(e['username']))
                      

    def Recherche(self,*args):
        """ Recherche dans mastodon """
        flux = Petit_Elephant.mastodon.search(args[0])
        a = flux['accounts']
        print("\n *      Compte.s      *\n")
        try:
            count = a[0]
            print('id            : '+str(count['id']))
            print('username      : '+str(count['username']))
            print('url           : '+str(count['url']))
            print('emoji         : '+str(count['emojis']))
            print('acct          : '+str(count['acct']))
            print('note          : '+str(count['note']))
            print('created_at    : '+str(count['created_at']))
            print('header        : '+str(count['header']))
            print('header_static : '+str(count['header_static']))
            print('avatar        : '+str(count['avatar']))
            print('avatar_static : '+str(count['avatar_static']))
            print('abonné.e.s    : '+str(count['followers_count']))
            print('abonnement.s  : '+str(count['following_count']))
        except IndexError:
            print(' * Aucun compte trouvé *')
        try:
            b = flux['hashtags']
            print("\n *      HashTag       *\n")
            hashT = b[0]
            print('url           : '+str(hashT['url']))
            print('name          : '+str(hashT['name']))
            hist = hashT['datetime']
            print('datetime      : '+str(hist['datetime']))
        except IndexError:    
             print(' * Aucun HashTag trouvé *')
        
        try: 
            c = flux['statuses']
            print("\n *     Statues     * \n")
            print('statues : '+str(c[0]))
        except IndexError:    
            print(' * Aucun Status trouvé *')
        
    def Favoris(self):
        """ """
        flux = Petit_Elephant.mastodon.favourites()
        print("\n *    BookMarks    *\n")
        print(flux)
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
        print(flux)
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
        print("Domaine bloqué.S : \n"+str(flux))
        print("\n *    Attachements    *\n")
        flux = Petit_Elephant.mastodon.account_statuses(Petit_Elephant.Me_ID, only_media=True)
        print("\n * * * * * * * * * * \n")
        print(flux)
#        a = flux[0]
#        b = a['media_attachments']
#        print("***********")
#        print(b)
#        c = b[0]
#        print(c['url'])
        for i,e in enumerate(flux):
            print(i+1)
            print(e['id'])
            r = e['media_attachments']
            c = r[0]
            print(c['url'])
    
    
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
        print("\n - Veuillez spécifier un argument - \n")
        prompt_aide()
    if len(sys.argv) > 1:
        action = sys.argv[1]
        aleph = True
    if len(sys.argv) == 3:
        indice = sys.argv[2]
        aleph = True

    #print(sys.argv[1])
    if aleph == True:
        if action == 'help':
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
        if action == 'flux1':
            tlaloc.flux_acceuil()
        if action == 'flux2':
            tlaloc.flux_local()
        if action == 'flux3': 
            tlaloc.flux_public()
        if action == 'search':
            uni = input('Entrez votre indice de recherche : ')
            tlaloc.Recherche(uni)
        if action == 'favoris': 
            tlaloc.Favoris()
        if action == 'info': 
            tlaloc.Info_Instance()
        if action == 'info_all': 
            tlaloc.Lecture_Instance()
        if action == 'notif': 
            tlaloc.Notifications()
        if action == 'direct': 
            tlaloc.Conversation() 
        if action == 'cron': 
            tlaloc.Cron() 
        if action == 'truc1': 
            tlaloc.Test1()
        if action == 'truc2': 
            tlaloc.bidule()
 
#        else:
#            print('oops.. je ne reconnais pas cette commande')




import discord
from ygcards import require

class Node :
    def __init__(self,question,keyword_list):
        self.question = question
        self.keyword_list = keyword_list
        self.list_child_node = []
    
    def insert_node(self,Node,quest):
        if self.question == quest:
            self.list_child_node.append(Node)
        elif len(self.list_child_node)>0:
            for N in self.list_child_node:
                N.insert_node(Node,quest)


tree =Node("Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc",["help"])
# Quel langage ? Pour sql, shell, graphisme et design, on saute cette étape
tree.insert_node(Node("Quel language de front vous pose problème ?", ["front","html","css","js"]), "Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc")
tree.insert_node(Node("Quel language de back vous pose problème ?", ["back","python","php"]),"Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc")
# Quel type d'aide voulu ?
tree.insert_node(Node("De quoi avez-vous besoin, en html ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["html"]),"Quel language de front vous pose problème ?")
tree.insert_node(Node("De quoi avez-vous besoin, en css ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["css"]),"Quel language de front vous pose problème ?")
tree.insert_node(Node("De quoi avez-vous besoin, en js ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["js"]),"Quel language de front vous pose problème ?")
tree.insert_node(Node("De quoi avez-vous besoin, en python ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["python"]),"Quel language de back vous pose problème ?")
tree.insert_node(Node("De quoi avez-vous besoin, en php ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["php"]),"Quel language de back vous pose problème ?")
tree.insert_node(Node("De quoi avez-vous besoin, pour les bases de données ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["mysql","bdd","base de données","sql"]),"Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc")
tree.insert_node(Node("De quoi avez-vous besoin, pour le shell ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["shell","unix","bash","ubuntu"]),"Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc")
tree.insert_node(Node("De quoi avez-vous besoin, en design ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["design","figma"]),"Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc")
tree.insert_node(Node("De quoi avez-vous besoin, en graphisme ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?", ["graphisme","adobe"]),"Dans quel domaine puis-je vous aider ? \nFront, back, bdd, etc")
# Bout de la branche : ressources demandées
# sql
tree.insert_node(Node("Voilà un lien utile : https://dev.mysql.com/doc/", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, pour les bases de données ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=7S_tz1z_5bA", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, pour les bases de données ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Renaud Berthier.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, pour les bases de données ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#shell
tree.insert_node(Node("Voilà un lien utile : https://doc.ubuntu-fr.org/commande_shell", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, pour le shell ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=GtovwKDemnI", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, pour le shell ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Adrien Quimbre.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, pour le shell ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#html
tree.insert_node(Node("Voilà un lien utile : https://developer.mozilla.org/fr/docs/Web/HTML", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en html ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=pQN-pnXPaVg", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en html ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Damien Boulay.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en html ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#css
tree.insert_node(Node("Voilà un lien utile : https://developer.mozilla.org/en-US/docs/Web/CSS", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en css ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=HDobHQfbRbo", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en css ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Damien Boulay.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en css ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#js
tree.insert_node(Node("Voilà un lien utile : https://developer.mozilla.org/fr/docs/Learn/JavaScript", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en js ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=QB1DTl7HFnc", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en js ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Damien Boulay ou à Valentine.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en js ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#php
tree.insert_node(Node("Voilà un lien utile : https://www.php.net/docs.php", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en php ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=OK_JCtrrv-c", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en php ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Renaud Berthier ou à Adrien Quimbre.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en php ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#python
tree.insert_node(Node("Voilà un lien utile : https://docs.python.org/3/", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en python ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=rfscVS0vtbw", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en python ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Loïc Janin ou à Valentine.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en python ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#design
tree.insert_node(Node("Voilà un lien utile : https://www.webdesign.org/", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en design ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=4Cpv0pAtS7w", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en design ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Grégoire Charassin.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en design ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
#graphisme
tree.insert_node(Node("Voilà un lien utile : https://helpx.adobe.com/fr/photoshop/how-to/photoshop-for-beginners.html", ["écrit","écrite","texte","site","lire"]),"De quoi avez-vous besoin, en graphisme ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Allez voir cette vidéo : https://www.youtube.com/watch?v=fnEZTPiqDxQ", ["vidéo","youtube","tuto","regarder","oral","orale","audio"]),"De quoi avez-vous besoin, en graphisme ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")
tree.insert_node(Node("Vous pouvez demander à Manuel Barbosa.", ["quelqu'un","personne","prof","parler","qqun"]),"De quoi avez-vous besoin, en graphisme ? \nUne explication écrite, une vidéo, quelqu'un à qui parler ?")




# Fun tree
pkmn_tree =Node("Dans quelle région habites-tu ?","i choose you !")
# Quelle région ?
pkmn_tree.insert_node(Node("Quel starter de 1ère génération choisis-tu ?", "kanto"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 2ème génération choisis-tu ?", "johto"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 3ème génération choisis-tu ?", "hoenn"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 4ème génération choisis-tu ?", "sinnoh"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 5ème génération choisis-tu ?", "unys"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 6ème génération choisis-tu ?", "kalos"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 7ème génération choisis-tu ?", "alola"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Quel starter de 8ème génération choisis-tu ?", "galar"), "Dans quelle région habites-tu ?")
pkmn_tree.insert_node(Node("Pff. Vantard ! (J'ai pas encore Légendes Arceus T_T)", "hisui"), "Dans quelle région habites-tu ?")
# Quel starter ?
pkmn_tree.insert_node(Node("En avant, Bulbizarre !", "bulbizarre"), "Quel starter de 1ère génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Salamèche !", "salamèche"), "Quel starter de 1ère génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Carapuce !", "carapuce"), "Quel starter de 1ère génération choisis-tu ?")
pkmn_tree.insert_node(Node("Pikachu, attaque Tonnerre ! - PiiiikaaaaCHUUUUUUU !!!! https://tenor.com/view/thunderbolt-pikachu-pokemon-anime-attack-gif-17278549", "pikachu"), "Quel starter de 1ère génération choisis-tu ?")
pkmn_tree.insert_node(Node("Quel type voulez-vous pour Évoli ?", "évoli"), "Quel starter de 1ère génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Germignon !", "germignon"), "Quel starter de 2ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Héricendre !", "héricendre"), "Quel starter de 2ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Kaïminus !", "kaïminus"), "Quel starter de 2ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Arcko !", "arcko"), "Quel starter de 3ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Poussifeu !", "poussifeu"), "Quel starter de 3ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Gobou !", "gobou"), "Quel starter de 3ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Tortipouss !", "tortipouss"), "Quel starter de 4ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Ouisticram !", "ouisticram"), "Quel starter de 4ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Tiplouf !", "tiplouf"), "Quel starter de 4ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Vipélierre !", "vipélierre"), "Quel starter de 5ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Gruikui !", "gruikui"), "Quel starter de 5ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Moustillon !", "moustillon"), "Quel starter de 5ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Marisson !", "marisson"), "Quel starter de 6ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Feunec !", "feunec"), "Quel starter de 6ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Grenousse !", "grenousse"), "Quel starter de 6ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Brindibou !", "brindibou"), "Quel starter de 7ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Flamiaou !", "flamiaou"), "Quel starter de 7ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Otaquin !", "otaquin"), "Quel starter de 7ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("En avant, Ouistempo !", "ouistempo"), "Quel starter de 8ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("Go, Flambino !", "flambino"), "Quel starter de 8ème génération choisis-tu ?")
pkmn_tree.insert_node(Node("À toi, Larméléon !", "larméléon"), "Quel starter de 8ème génération choisis-tu ?")
# Évolutions d'évoli
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Aquali, Go !", "eau"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Voltali, Go !", "électrik"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Pyroli, Go !", "feu"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Mentali, Go !", "psy"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Noctali, Go !", "ténèbres"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Phyllali, Go !", "plante"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Givrali, Go !", "glace"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("https://tenor.com/view/eevee-starts-to-evolve-eevee-at-night-umbreon-pokemon-eevee-pokemon-umbreon-gif-23726445 Nymphali, Go !", "fée"), "Quel type voulez-vous pour Évoli ?")
pkmn_tree.insert_node(Node("Évoli, Go ! https://tenor.com/view/blazedpx-pokemon-eevee-gif-23902862 Euh... Évoli ?", "normal"), "Quel type voulez-vous pour Évoli ?")


client = discord.Client()

root = tree
node_list = []
node_list.append(root)

pkmn_root = pkmn_tree
pkmn_node_list = []
pkmn_node_list.append(pkmn_root)

@client.event
async def on_message(message):
	message.content = message.content.lower()
	if message.author == client.user:
		return
	# Help function
	help_channel = client.get_channel(978295223660724264)
	#how does the bot work ?
	if (message.channel == help_channel and "bot" in message.content) or message.content == "$bot" :
		embed = discord.Embed (
			title = "**Fonctionnement du bot**",
			color = 0x4434CA,
			description = "*Commandes spécifiques au salon d'aide* \n- messages contenant 'bot' : fonctionnement du bot \n- messages contenant 'help' : assistant d'aide aux études \n---> messages contenant 'reset' ou 'début' : retour au début de l'assistant \n---> messages contenant 'return', 'retour' ou 'annuler' : retour à la question précédente de l'assistant \n\n*Commandes spécifiques au salon général* \n- '$bot' : fonctionnement du bot \n- messages commençant par $salut : le bot vous dit bonjour \n- messages contenant 'i choose you !' : choix d'un starter pokémon \n ---> messages contenant 'reset' ou 'début' : retour au début \n---> messages contenant 'return', 'retour' ou 'annuler' : retour à la question précédente \n - '!ygcard nom_d_une_carte' : afficher une carte yu-gi-oh \n\n*Commandes générales* \n- '$bot' : fonctionnement du bot \n- '$del' : supprime les 5 derniers messages du salon, y compris ceux du bot \n Le bot contient également un easter-egg pour Victorien, buveur de café invétéré."
			)
		await message.channel.send(embed = embed)

	# tree to find help
	if message.channel == help_channel :	
		global root
		global node_list

		for keyword in root.keyword_list :
			if keyword in message.content and root == tree: # we only need this send at the beginning
				await help_channel.send(root.question)
				return
			for child in root.list_child_node:
				for keywd in child.keyword_list :
					if keywd in message.content:
						root = child
						node_list.append(root)
						await help_channel.send(child.question)
						if len(root.list_child_node) < 1: #end of branch : we reset everything.
							root = tree
							node_list=[]
							node_list.append(root)
							return
			if "reset" in message.content or "début" in message.content :
				root = tree
				node_list=[]
				node_list.append(root)
			elif message.content in ["return","retour","annuler"]:
				node_list.pop()
				root = node_list[-1]
				await help_channel.send(root.question)

	if message.content == "$del" :
		await message.channel.purge(limit=5) # deletes the 5 last messages, including those from the bot
	
	# calling for a moderator
	if message.content.startswith('$mod'):
    	# msg = '@Moderator, (some message after this)'.format(message)
		author_tag = "<@" + str(message.author.id) + ">"
		mod_tag = "<@&" + str(981576133290115093) + ">" #981568451455909898 : id of the moderator role
		tag = mod_tag + ", " + author_tag + " a besoin de vous." 
		await message.channel.send(tag)

	# Now, time for fun !
	general_channel = client.get_channel(978294958077411340)


	if message.channel == general_channel :
		
		if "café" in message.content :
			await message.channel.send("Allez, café !") # For victorien !
		
		if message.content.startswith('$salut') :
			answer = "Bonjour " + str(message.author.name) #message.author gats the discord id of the message's author. name gets the message's author's name.
			await general_channel.send(answer)

		#pokemon tree
		global pkmn_root
		global pkmn_node_list

		if message.content.startswith(pkmn_root.keyword_list) and pkmn_root == pkmn_tree: # we only need this send at the beginning
			await general_channel.send(pkmn_root.question)
		if message.content in ["reset", "début"]:
			pkmn_root = pkmn_tree
			pkmn_node_list=[]
			pkmn_node_list.append(pkmn_root)
		elif message.content in ["return","retour","annuler"]:
			pkmn_node_list.pop()
			pkmn_root = pkmn_node_list[-1]
			await general_channel.send(pkmn_root.question)
		else :
			for pokechild in pkmn_root.list_child_node:
				if len(pkmn_root.list_child_node) < 1: #end of branch : we reset everything.
					pkmn_root = pkmn_tree
					pkmn_node_list=[]
					pkmn_node_list.append(pkmn_root)
					return
				if pokechild.keyword_list in message.content:
					pkmn_root = pokechild
					pkmn_node_list.append(pkmn_root)
					await general_channel.send(pokechild.question)

		#Commande pour le listing de cartes Yugioh
		if message.content.startswith("!ygcard"):
			card = message.content.split(" ")
			card.remove("!ygcard")
			card_name = ""
			#Je récupère le message, et retire la commande pour envoyer le nom de la carte que je recherche
			for i in range(len(card)):
				card_name = card_name + card[i]
				if i + 1 < len(card):
					card_name = card_name + " "
			#Je fais appel à ma génération d'embed avec les informations de ma carte
			embed = require(card_name)
			if embed == None:
				await general_channel.send("Not found")
			await general_channel.send(embed=embed)
						




client.run()

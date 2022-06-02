import json
import os
import discord

cardlist = {}
idlist = os.listdir('data/en')
#Les cartes Yugioh ayant une couleur différente en fonction de leur type, je modifie la couleur de l'embed en accordance
colors ={
    'Effect': 0xFF8B53,
    'Fusion': 0xA086B7,
    'Xyz': 0x111111,
    'Synchro': 0xFEFEFE,
    'Ritual': 0x9DB5CC,
    'Link': 0x00008B,
    'Normal': 0xFDE68A,
    'spell': 0x1D9E74,
    'trap': 0xBC5A84,
    'none': 0x000000
    }
#Les cartes "Lien" ont des flèches propres à leur type, je dois donc les récupérer pour les afficher
arrows ={
    '1' : '↖️',
    '2' : '⬆️',
    '3' : '↗️',
    '4' : '➡️',
    '5' : '↘️',
    '6' : '⬇️',
    '7' : '↙️',
    '8' : '⬅️'
    }
#Chaque carte a un attribut, je vais vouloir l'afficher en tant qu'icon_url
attributes ={
    'dark' : 'https://media.discordapp.net/attachments/978193711773151232/979348893395451934/unknown.png',
    'divine' : 'https://media.discordapp.net/attachments/978193711773151232/979349099516141628/unknown.png',
    'earth' : 'https://media.discordapp.net/attachments/978193711773151232/979349127399874570/unknown.png',
    'fire' : 'https://media.discordapp.net/attachments/978193711773151232/979349151542296576/unknown.png',
    'light' : 'https://media.discordapp.net/attachments/978193711773151232/979349179115659314/unknown.png',
    'water' : 'https://media.discordapp.net/attachments/978193711773151232/979349198250074192/unknown.png',
    'wind' : 'https://media.discordapp.net/attachments/978193711773151232/979349221234843658/unknown.png',
    'trap' : 'https://media.discordapp.net/attachments/978193711773151232/979350672409493555/unknown.png',
    'spell' : 'https://media.discordapp.net/attachments/978193711773151232/979350717007532032/unknown.png'
}
#Je récupère la liste des cartes dans un dictionnaire
for id in idlist:
        with open('data/en/'+ id) as f:
            data = json.load(f)
            cardlist[data['name'].lower()] = data

#Je génre l'embed en fonction du nom que m'envoie l'utilisateur     
def require(card):

    try:
        #Par soucis de simplicité lors de la recherche, les noms de cartes ayant des majuscules à chaque mot, je met tout en minuscule
        for key in cardlist.keys():
            if card == key:
                data = cardlist[key]
        #Ici je donne l'attribut de ma carte à une valeur
        for a in attributes.keys():
            if a in data["englishAttribute"]:
                    attribute = attributes[a]
        #Les cartes pièges et magies étant similaires, je leur donne un affichage commun
        if data["type"] == "trap" or data["type"] == "spell":
            for c in colors.keys():
        #Je dois gérer les couleurs séparéments car je ne peux pas me baser sur la même donnée etre les cartes monstres et magies/pièges
                if data["type"] in c:
                    color = colors[c]
            embed = discord.Embed(
            description = data["effectText"],
            colour = color
            )
        #Cette partie s'occupe de toutes les cartes monstres(normal, effet, fusion, rituel, synchro, xyz, pendule, lien)
        else:
            for c in colors.keys():
        #Je récupère la couleur de mon embed pour mon monstre
                if c in data["properties"]:
                    color = colors[c]
            embed = discord.Embed(
            colour = color
            )
        #Je regarde s'il s'agit d'un monstre Synchro, Lien ou Xyz pour l'affichage
            for t in data.keys():
                if "linkRating" in t:
                    levelOrLinkOrRank = "Link"
                elif "level" in t:
                    levelOrLinkOrRank = "Level"
                elif "rank" in t:
                    levelOrLinkOrRank = "Rank"
        #S'il s'agit d'un monstre Normal, Effet, Fusion, Rituel ou Synchro, j'utilise cet affichage
            if levelOrLinkOrRank=="Level":
                embed.add_field(name="Level:", value=data["level"], inline=False)
        #S'il s'agit d'un monstre lien, j'ai besoin de + de précision, et passe donc par celui-là
            elif levelOrLinkOrRank=="Link":
                LArrows = []
                embed.add_field(name="Link:", value=data["linkRating"], inline=True)
                for a in arrows.keys():
                    if a in data["linkArrows"]:
                        LArrows.append(arrows[a])
                LArrows = ', '.join(LArrows)
                embed.add_field(name="Link Arrows:", value=LArrows, inline=False)
        #S'il s'agit d'un monstre Xyz, je m'en occupe ici
            elif levelOrLinkOrRank=="Rank":
                embed.add_field(name="Rank:", value=data["rank"], inline=False)
        #Je vérifie s'il s'agit d'une carte pendule pour afficher son échelle pendule
            for pDs in data.keys():
                if pDs == "pendScale":
                    embed.add_field(name="Pendulum Scale:", value=data["pendScale"], inline=False)
        #Tous les monstres ayant une stat d'attaque, je la sors de mes conditions
            embed.add_field(name="ATK:", value=data["atk"], inline=True)
        #Les monstres liens n'ont pas de stat de défense, je vérifie donc de quel type de monstre il s'agit avant d'afficher la défense
            if levelOrLinkOrRank=="Level" or levelOrLinkOrRank=="Rank":
                embed.add_field(name="DEF:", value=data["def"], inline=True)
        #J'affiche ici les propriétés de la carte monstre ainsi que leur effet
            properties = ""
            for p in range(len(data["properties"])):
                properties = properties + data["properties"][p]
                if p + 1 < len(data["properties"]):
                    properties = properties + "/"
            embed.add_field(name="Properties", value="["+properties+"]", inline=False)
            embed.add_field(name="Effect:", value=data["effectText"], inline=False)
        #Je sors de mes conditions car toutes mes cartes fonctionnent sous le même principe pour l'author, l'icon url et l'image
        embed.set_author(name=data["name"], icon_url=attribute)
        embed.set_image(url="https://artworks.ygorganization.com/en/neuron_high/"+str(data["id"])+"_1.png")
        return(embed)
    except KeyError:
        return(None)



#!/bin/env python
#----------------------------------------------------------------------------
# Name:         Main.py
# Purpose:      Create systetic data for testing machine learning machines
#
# Author:       Marco Visibelli
#
# Created:      A long time ago, in a galaxy far, far away...
# Copyright:    (c) 2018 by Marco Visibelli
# Licence:      MIT license
#----------------------------------------------------------------------------

# FIXME List:
# * Problems with flickering related to ...


# TODO List:
# * creation

'''

for each employee(schema) as employeey.csv
	generate reimburse(TYPE=[HOTEL,RESTURANT],FREQUENCY=1,2 every MONTH)
	generate invoice(TYPE=[payment],FREQUENCY=1,2 every MONTH)

'''

import sys, os
import pandas as pd 
import numpy as np
import random
import datetime


def letters(input):
    valids = []
    for character in input:
        if character.isalpha():
            valids.append(character)
    return ''.join(valids)

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def email(df,context):
    return letters(str(df["name"]).lower()) + "." + letters(str(df["surname"]).lower()) +"@"+ letters(str(context["company"]).lower())+".com"

prog_id_entity = {"selectors":[],"values":0}

email_entity = email

Amount_reimbourse_entity =  {"selectors":["Type"], "type":"choice_range", "values_all":[
         {"Type":"Restaurant","values":(100,200)}
        ,{"Type":"Hotels","values":(200,400)}
        ,{"Type":"Taxi","values":(10,40)}
        ,{"Type":"Honorarium","values":(100,300)}
        ,{"Type":"Others","values":(10,300)}
        ]}  


name_entity = {"selectors":["country","gender"],
        "values_all":[
         {"country":"it","gender":"M","values":["Francesco","Alessandro","Lorenzo","Andrea","Leonardo","Mattia","Matteo","Gabriele","Riccardo","Tommaso","Davide","Giuseppe","Antonio","Federico","Edoardo","Marco","Samuele","Diego","Giovanni","Luca","Christian","Pietro","Simone","Nicolo'","Filippo","Alessio","Gabriel","Michele","Emanuele","Jacopo","Daniele","Cristian","Giacomo","Vincenzo","Salvatore","Manuel","Gioele","Thomas","Stefano","Giulio","Samuel","Nicola","Giorgio","Luigi","Daniel","Elia","Angelo","Domenico","Paolo","Raffaele"]}
        ,{"country":"it","gender":"F","values":["Sofia","Giulia","Aurora","Giorgia","Martina","Emma","Greta","Chiara","Sara","Alice","Gaia","Anna","Francesca","Ginevra","Noemi","Alessia","Matilde","Vittoria","Viola","Beatrice","Nicole","Giada","Elisa","Rebecca","Elena","Arianna","Mia","Camilla","Ludovica","Maria","Marta","Melissa","Bianca","Gioia","Asia","Adele","Eleonora","Miriam","Serena","Benedetta","Irene","Angelica","Ilaria","Carlotta","Caterina","Margherita","Alessandra","Valentina","Emily","Laura"]}
        ,{"country":"uk","gender":"M","values":["Oliver","George","Harry","Jack","Jacob","Noah","Charlie","Muhammad","Thomas","Oscar","William","James","Henry","Leo","Alfie","Joshua","Freddie","Archie","Ethan","Isaac","Alexander","Joseph","Edward","Samuel","Max","Daniel","Arthur","Lucas","Mohammed","Logan","Theo","Harrison","Benjamin","Mason","Sebastian","Finley","Adam","Dylan","Zachary","Riley","Teddy","Theodore","David","Toby","Jake","Louie","Elijah","Reuben","Arlo","Hugo","Luca","Jaxon","Matthew","Harvey","Reggie","Michael","Harley","Jude","Albert","Tommy","Luke","Stanley","Jenson","Frankie","Jayden","Gabriel","Elliot","Mohammad","Ronnie","Charles","Louis","Elliott","Frederick","Nathan","Lewis","Blake","Rory","Ollie","Ryan","Tyler","Jackson","Dexter","Alex","Austin","Kai","Albie","Caleb","Carter","Bobby","Ezra","Ellis","Leon","Roman","Ibrahim","Aaron","Liam","Jesse","Jasper","Felix","Jamie"]   }
        ,{"country":"uk","gender":"F","values":["Emily","Sophie","Olivia","Isla","Jessica","Ava","Amelia","Ella","Lucy","Lily","Grace","Chloe","Freya","Ellie","Millie","Emma","Anna","Eva","Sophia","Mia","Charlotte","Eilidh","Ruby","Hannah","Aria","Evie","Georgia","Poppy","Erin","Katie","Holly","Orla","Layla","Skye","Rosie","Harper","Maisie","Leah","Zoe","Daisy","Amber","Amy","Hollie","Isabella","Niamh","Molly","Robyn","Alice","Sofia","Lilly","Maya","Lacey","Rebecca","Scarlett","Lexi","Willow","Abigail","Brooke","Esme","Lola","Paige","Gracie","Emilia","Mila","Zara","Megan","Abbie","Kayla","Sienna","Ivy","Summer","Cara","Thea","Imogen","Sarah","Rose","Ayla","Bella","Mya","Elizabeth","Rachel","Iona","Julia","Elsie","Amelie","Darcy","Lauren","Mollie","Arianna","Eve","Matilda","Caitlin","Beth","Maria","Phoebe","Heidi","Hope","Ariana","Georgie","Sadie"]} 
        ,{"country":"de","gender":"M","values":["Ben","Jonas","Leon","Elias","Finn","Noah","Paul","Luis","Lukas","Luca","Felix","Maximilian","Henry","Max","Emil","Moritz","Jakob","Niklas","Tim","Julian","Oskar","Anton","Philipp","David","Liam","Alexander","Theo","Tom","Mats","Jan","Matteo","Samuel","Erik","Fabian","Milan","Leo","Jonathan","Rafael","Simon","Vincent","Lennard","Carl","Linus","Hannes","Jona","Mika","Jannik","Nico","Till","Johannes","Marlon","Leonard","Benjamin","Johann","Mattis","Adrian","Julius","Florian","Constantin","Daniel","Aaron","Maxim","Nick","Lenny","Valentin","Ole","Luke","Levi","Nils","Jannis","Sebastian","Tobias","Marvin","Joshua","Mohammed","Timo","Phil","Joel","Benedikt","John","Robin","Toni","Dominic","Damian","Artur","Pepe","Lasse","Malte","Sam","Bruno","Gabriel","Lennox","Justus","Kilian","Theodor","Oliver","Jamie","Levin","Lian","Noel" ]} 
        ,{"country":"de","gender":"F","values":["Mia","Emma","Hannah","Sofia","Anna","Emilia","Lina","Marie","Lena","Mila","Emily","Lea","Léonie","Amelie","Sophie","Johanna","Luisa","Clara","Lilly","Laura","Nele","Lara","Charlotte","Leni","Maja","Frieda","Mathilda","Ida","Ella","Pia","Sarah","Lia","Lotta","Greta","Melina","Julia","Paula","Lisa","Marlene","Zoe","Alina","Victoria","Mira","Elisa","Isabella","Helena","Josephine","Mara","Isabell","Nora","Antonia","Lucy","Emely","Jana","Pauline","Amy","Anni","Merle","Finja","Katharina","Luise","Elena","Theresa","Annika","Luna","Romy","Maria","Stella","Fiona","Jasmin","Magdalena","Jule","Milena","Mina","Carla","Eva","Martha","Nina","Annabell","Melissa","Elina","Carlotta","Paulina","Maila","Elif","Elisabeth","Ronja","Zoey","Chiara","Tilda","Miriam","Franziska","Valentina","Juna","Linda","Thea","Elli","Rosalie","Selina","Fabienne"]} 
        ,{"country":"fr","gender":"M","values":["Gabriel","Adam","Raphael","Paul","Louis","Arthur","Alexandre","Victor","Jules","Mohamed","Lucas","Joseph","Antoine","Gaspard","Maxime","Augustin","Oscar","Ethan","Leo","Leon","Martin","Hugo","Thomas","Sacha","Noe","Noah","Clement","Liam","Rayan","Samuel","Simon","Yanis","Nathan","Timothée","Adrien","Axel","Enzo","Isaac","Camille","Ismael","Naël","Basile","Côme","Charles","David","Mathis","Nolan","Leonard","Aaron","Maël","Maxence","Eliott","Ibrahim","Valentin","Theo","Alexis","Baptiste","Ulysse","Benjamin","Marius","Youssef","Elias","Jean","Lucien","Robin","Felix","William","Gustave","Hector","Auguste","Theodore","Gabin","Edgar","Amir","Noam","Tom","Pierre","Ayoub","Kaïs","Ali","Ruben","Abel","Henri","Achille","Ilyes","Milo","Vadim","Evan","Hadrien","Amine","Daniel","Marceau","Nicolas","Eden","Moussa","Antonin","Rafael","Solal","Joshua","Mehdi" ]}    
        ,{"country":"fr","gender":"F","values":["Louise","Alice","Chloe","Emma","Ines","Sarah","Jeanne","Anna","Adele","Juliette","Camille","Lea","Lina","Eva","Sofia","Charlotte","Victoria","Rose","Mila","Josephine","Manon","Zoe","Nina","Jade","Olivia","Margaux","Lou","Anaïs","Julia","Lucie","Gabrielle","Romane","Heloise","Valentine","Clémence","Apolline","Mathilde","Victoire","Alix","Ava","Agathe","Marie","Nour","Suzanne","Margot","Clara","Elsa","Romy","Iris","Léonie","Mia","Pauline","Yasmine","Constance","Lena","Madeleine","Ambre","Garance","Alma","Alicia","Diane","Laura","Sophia","Maya","Capucine","Aya","Sara","Fatoumata","Giulia","Noémie","Elena","Mariam","Celeste","Inaya","Lisa","Lola","Elise","Sophie","Anouk","Elisa","Aïcha","Lise","Salome","Assia","Maryam","Hanna","Ella","Roxane","Lila","Myriam","Lily","Eleonore","Raphaëlle","Maëlys","Ines","Luna","Berenice","Sasha","Maria","Eleonore" ]}
        ,{"country":"gr","gender":"M","values":["Achilles ","Adonis ","Adrian ","Alesandro ","Basil ","Belen ","Bemus","Caesar ","Calix ","Christophe ","Cicero ","Claus ","Cole ","Constantine ","Corban","Cy ","Damen ","Darius ","Deacon ","Demitrius ","Dennis ","Deo","Dru ","Egan ","Eros ","Estevan ","Eugene ","Evan ","Ezio","Faustus ","Felipe ","Flavian ","George ","Giles ","Gregory ","Griffin ","Hercules ","Homer ","Icarus ","Isidore ","Jace ","Jerry ","Jorges","Julian ","Kal ","Karan ","Keelan ","Kosmos","Kristo","Kyril","Lander ","Layland","Leo ","Magus","Mateo ","Maximus ","Miles ","Moe","Neo","Nicholas ","Nicos","Niles ","Nyke","Obelius","Odell ","Odysseus ","Orien","Orrin ","Othello ","Otis ","Owen ","Pancras","Pearce ","Philip ","Phoenix","Proteus ","Quinn ","Rastus","Sander ","Santos ","Sirius","Spiro","Stavros ","Tadd","Tassos ","Theo ","Timon ","Titan","Tomaso","Tyrone ","Ulysses ","Urion","Vasilios","Vitalis","Xander"]}    
        ,{"country":"gr","gender":"F","values":["Acacia","Acantha","Adelpha","Agapi","Agatha","Agathe","Agnes","Aimilios","Alcie","Alcina","Alethea","Alex","Alexa","Alexandra","Alexandria","Alexandrina","Alexina","Alexis","Alike","Aliz","Alizka","Alpha","Alsie","Althea","Amara","Amarantha","Amaryllis","Ambrosia","Aminta","Anastacia","Anastasha","Anastasia","Anatola","Andromeda","Anemone","Ange","Angela","Angele","Angeliki","Angelina","Aniceta","Annis","Annys","Anthea","Antigone","Antimony","Antinea","Aphrodite","Apollonia","Arcadia","Arcangela","Arete","Aretha","Ariadne","Arianna","Arista","Arkadina","Artemis","Artemisia","Asta","Aster","Asteria","Astraea","Astraia","Atalanta","Athena","Basilia","Beranice","Beraniece","Berenice","Berenike","Bernice","Beryl","Beta","Bronte","Brontë","Bryonia","Calandra","Calantha","Calista","Calixta","Calla","Callie","Calliope","Callista","Calypso","Carissa","Cassandra","Cassia","Cassiane","Cassiopeia","Cat","Cate","Catherine","Celena","Chara","Charis","Charmian","Chloe","Chloris","Christina","Cinda","Cipriana","Circe","Clematis","Cleopatra","Cleora","Cliantha","Clio","Collins","Cora","Corinna","Corisande","Cosima","Cressida","Crisanta","Cyane","Cybele","Cynara","Cynthia","Cytherea","Damara","Damaris","Damia","Damiana","Danaë","Daphne","Daria","Darian","Delia","Delta","Demeter","Demetria","Demi","Desdemona","Despina","Diamanta","Diandra","Diantha","Dido","Dina","Dione","Dionne","Dora","Dorcas","Dorian","Dorinda","Doris","Dorothea","Dorothy","Dree","Echo","Effie","Effy","Eirene","Eirini","Elara","Electa","Electra","Elektra","Elena","Eleni","Eleusine","Elexis","Eliana","Eliane","Elidi","Eloisia","Eos","Epiphany","Ereni","Eudora","Eugenia","Eugenie","Eulala","Eulalia","Eunice","Euphemia","Eurydice","Eustacia","Evadne","Evangeline","Evanthe","Evathia","Fantasia","Fedora","Filomena","Gaia","Galatea","Galen","Halcyon","Hali","Harmonia","Harmony","Hebe","Hecuba","Helen","Helena","Helia","Hera","Hermia","Hermione","Hero","Hestia","Hilary","Hillary","Hyacinth","Hyacinthe","Hyacynthe","Ianthe","Ilena","Ilene","Iliana","Indigo","Ino","Io","Ioanna","Iola","Iolanda","Iolande","Iolanthe","Ione","Ionia","Ionna","Iphigenia","Irene","Irina","Iris","Isadora","Isaura","Ismene","Jocasta","Jolán","Junia","Justina","Kacia","Kalliope","Kallista","Karissa","Kasiani","Kassandra","Kassia","Kassiani","Katerina","Katharine","Katherine","Katie","Khloe","Kosma","Kosta","Kostantina","Kristiana","Kynthia","Lalage","Lamia","Larisa","Larissa","Leda","Lenore","Leora","Letha","Lethe","Lex","Lexia","Lexis","Lexus","Libra","Lici","Liliah","Lilika","Lilis","Lois","Lotus","Lydia","Lyra","Lyric","Magdalen","Magdalena","Mago","Mahail","Mahaila","Mahalia","Maia","Makis","Malina","Malva","Margalo","Margaret","Maryam","Maya","Medea","Medora","Meg","Melania","Melanie","Melantha","Melany","Melia","Melina","Melissa","Melita","Melody","Melora","Muse","Mya","Myra","Myrtle","Nani","Narcissa","Narda","Natasa","Nemea","Neola","Neoma","Neri","Nerida","Nerine","Nerissa","Nickelle","Nicola","Nicole","Nicolina","Nicoline","Nidia","Nike","Niki","Nikola","Nikoleta","Nikolia","Niobe","Nitsa","Nyssa","Nyx","Obelia","Oceana","Olympia","Omega","Ophelia","Orion","Orphea","Pallas","Pandora","Panthea","Parmenia","Parthenia","Pasha","Peg","Peggy","Pelagia","Penelope","Penthia","Peri","Perrine","Persephone","Persis","Pesha","Peta","Petal","Petra","Petrina","Petrini","Petronella","Petronelle","Phaedra","Phedora","Pheobe","Phila","Philadelphia","Philippa","Philomela","Philomena","Phoebe","Phoenix","Phyllida","Phyllis","Pinelopi","Pipitsa","Popi","Praxis","Psyche","Raemonia","Rena","Reta","Reveka","Rhea","Rheta","Rheya","Rhoda","Roxane","Rue","Sapphira","Sappho","Selene","Selia","Sibley","Sibyl","Sirena","Sofi","Sofia","Sophia","Sophie","Sophoon","Sophronia","Stasia","Stavra","Stefania","Stephanie","Sybella","Sybil","Tana","Tancy","Tansy","Tasia","Tasoula","Tassia","Tempe","Tessa","Thais","Thalassa","Thalia","Thaïs","Thea","Theia","Thekla","Themis","Theo","Theodosia","Theone","Theora","Theresa","Thesally","Thetis","Thisbe","Tiffany","Timothea","Tina","Titania","Topaz","Toula","Typhaine","Téa","Urania","Ursa","Varya","Vasilia","Vasiliki","Venedicta","Vernada","Vernamina","Veronike","Veronique","Violante","Xanthe","Xanthipe","Xantho","Xena","Xenia","Xenobia","Yalena","Yannia","Yolanda","Zelena","Zelenia","Zena","Zenaida","Zenobia","Zephyr","Zephyra","Zephyrine","Zeta","Zita","Zoe","Zoei","Zoey","Zoie","Zoila","Zooey","Zosma"]}    
        ]
       }

surname_entity = {"selectors":["country"],"values_all":[
         {"country":"gr","values":["Nagy","Horváth","Kovács","Szabó","Tóth","Varga","Kiss","Molnár","Németh","Farkas","Balogh","Papp","Takács","Juhász","Lakatos","Mészáros","Oláh","Simon","Rácz","Fekete"]}
        ,{"country":"it","values":["Rossi","Russo","Ferrari","Esposito","Bianchi","Romano","Colombo","Bruno","Ricci","Greco","Marino","Gallo","De Luca","Conti","Costa","Mancini","Giordano","Rizzo","Lombardi","Barbieri","Moretti","Fontana","Caruso","Mariani","Ferrara","Santoro","Rinaldi","Leone","D'Angelo","Longo","Galli","Martini","Martinelli","Serra","Conte","V","e","De Santis","Marchetti","Messina","Gentile","Villa","Marini","Lombardo","Coppola","Ferri","Parisi","De Angelis","Bianco","Amato","Fabbri","Gatti","Sala","Morelli","Grasso","Pellegrini","Ferraro","Monti","Palumbo","Grassi","Testa","Valentini","Carbone","Benedetti","Silvestri","Farina","D'Amico","Martino","Bernardi","Caputo","Mazza","Sanna","Fiore","De Rosa","Pellegrino","Giuliani","Rizzi","Di Stefano","Cattaneo","Rossetti","Orlando","Basile","Neri","Barone","Palmieri","Riva","Romeo","Franco","Sorrentino","Pagano","D'Agostino","Piras","Ruggiero","Montanari","Battaglia","Bellini","Castelli","Guerra","Poli","Valente","Ferretti"]}
        ,{"country":"uk","values":["Smith","Jones","Williams","Taylor","Brown","Davies","Evans","Wilson","Thomas","Johnson","Roberts","Robinson","Thompson","Wright","Walker","White","Edwards","Hughes","Green","Hall","Lewis","Harris","Clarke","Patel","Jackson","Wood","Turner","Martin","Cooper","Hill","Ward","Morris","Moore","Clark","Lee","King","Baker","Harrison","Morgan","Allen","James","Scott","Phillips","Watson","Davis","Parker","Price","Bennett","Young","Griffiths","Mitchell","Kelly","Cook","Carter","Richardson","Bailey","Collins","Bell","Shaw","Murphy","Miller","Cox","Richards","Khan","Marshall","Anderson","Simpson","Ellis","Adams","Singh","Begum","Wilkinson","Foster","Chapman","Powell","Webb","Rogers","Gray","Mason","Ali","Hunt","Hussain","Campbell","Matthews","Owen","Palmer","Holmes","Mills","Barnes","Knight","Lloyd","Butler","Russell","Barker","Fisher","Stevens","Jenkins","Murray","Dixon","Harvey","Graham","Pearson","Ahmed","Fletcher","Walsh","Kaur","Gibson","Howard","Andrews","Stewart","Elliott","Reynolds","Saunders","Payne","Fox","Ford","Pearce","Day","Brooks","West","Lawrence","Cole","Atkinson","Bradley","Spencer","Gill","Dawson","Ball","Burton","O'brien","Watts","Rose","Booth","Perry","Ryan","Grant","Wells","Armstrong","Francis","Rees","Hayes","Hart","Hudson","Newman","Barrett","Webster","Hunter","Gregory","Carr","Lowe","Page","Marsh","Riley","Dunn","Woods","Parsons","Berry","Stone","Reid","Holland","Hawkins","Harding","Porter","Robertson","Newton","Oliver","Reed","Kennedy","Williamson","Bird","Gardner","Shah","Dean","Lane","Cooke","Bates","Henderson","Parry","Burgess","Bishop","Walton","Burns","Nicholson","Shepherd","Ross","Cross","Long","Freeman","Warren","Nicholls","Hamilton","Byrne","Sutton","Mcdonald","Yates","Hodgson","Robson","Curtis","Hopkins","O'connor","Harper","Coleman","Watkins","Moss","Mccarthy","Chambers","O'neill","Griffin","Sharp","Hardy","Wheeler","Potter","Osborne","Johnston","Gordon","Doyle","Wallace","George","Jordan","Hutchinson","Rowe","Burke","May","Pritchard","Gilbert","Willis","Higgins","Read","Miles","Stevenson","Stephenson","Hammond","Arnold","Buckley","Walters","Hewitt","Barber","Nelson","Slater","Austin","Sullivan","Whitehead","Mann","Frost","Lambert","Stephens","Blake","Akhtar","Lynch","Goodwin","Barton","Woodward","Thomson","Cunningham","Quinn","Barnett","Baxter","Bibi","Clayton","Nash","Greenwood","Jennings","Holt","Kemp","Poole","Gallagher","Bond","Stokes","Tucker","Davidson","Fowler","Heath","Norman","Middleton","Lawson","Banks","French","Stanley","Jarvis","Gibbs","Ferguson","Hayward","Carroll","Douglas","Dickinson","Todd","Barlow","Peters","Lucas","Knowles","Hartley","Miah","Simmons","Morton","Alexander","Field","Morrison","Norris","Townsend","Preston","Hancock","Thornton","Baldwin","Burrows","Briggs","Parkinson","Reeves","Macdonald","Lamb","Black","Abbott","Sanders","Thorpe","Holden","Tomlinson","Perkins","Ashton","Rhodes","Fuller","Howe","Bryant","Vaughan","Dale","Davey","Weston","Bartlett","Whittaker","Davison","Kent","Skinner","Birch","Morley","Daniels","Glover","Howell","Cartwright","Pugh","Humphreys","Goddard","Brennan","Wall","Kirby","Bowen","Savage","Bull","Wong","Dobson","Smart","Wilkins","Kirk","Fraser","Duffy","Hicks","Patterson","Bradshaw","Little","Archer","Warner","Waters","O'sullivan","Farrell","Brookes","Atkins","Kay","Dodd","Bentley","Flynn","John","Schofield","Short","Haynes","Wade","Butcher","Henry","Sanderson","Crawford","Sheppard","Bolton","Coates","Giles","Gould","Houghton","Gibbons","Pratt","Manning","Law","Hooper","Noble","Dyer","Rahman","Clements","Moran","Sykes","Chan","Doherty","Connolly","Joyce","Franklin","Hobbs","Coles","Herbert","Steele","Kerr","Leach","Winter","Owens","Duncan","Naylor","Fleming","Horton","Finch","Fitzgerald","Randall","Carpenter","Marsden","Browne","Garner","Pickering","Hale","Dennis","Vincent","Chadwick","Chandler","Sharpe","Nolan","Lyons","Hurst","Collier","Peacock","Howarth","Faulkner","Rice","Pollard","Welch","Norton","Gough","Sinclair","Blackburn","Bryan","Conway","Power","Cameron","Daly","Allan","Hanson","Gardiner","Boyle","Myers","Turnbull","Wallis","Mahmood","Sims","Swift","Iqbal","Pope","Brady","Chamberlain","Rowley","Tyler","Farmer","Metcalfe","Hilton","Godfrey","Holloway","Parkin","Bray","Talbot","Donnelly","Nixon","Charlton","Benson","Whitehouse","Barry","Hope","Lord","North","Storey","Connor","Potts","Bevan","Hargreaves","Mclean","Mistry","Bruce","Howells","Hyde","Parkes","Wyatt","Fry","Lees","O'donnell","Craig","Forster","Mckenzie","Humphries","Mellor","Carey","Ingram","Summers","Leonard"]}
        ,{"country":"fr","values":["Bernard","Dubois","Thomas","Robert","Richard","Small","Durand","Leroy","Moreau","Simon","Laurent","Lefebvre","Michel","Garcia","David","Bertrand","Red","Vincent","Fournier","Morel","Girard","Andre","Lefevre","haberdasher","Dupont","Lambert","Cap","Francois","Martinez","Great","Garnier","Faure","Rousseau","White","Guerin","Muller","Henry","Roussel","Nicolas","Perrin","Morin","Mathieu","Clement","Gauthier","Dumont","Lopez","Fountain","Knight","Robin","Masson","Sanchez","Gerard","Nguyen","Boyer","Denis","The mayor","Duval","Joly","Gautier","Roger","rock","Roy","Christmas","Meyer","Lucas","Miller","Jeans","Perez","Trader","From the oven","Blanchard","Married","Barbier","Brown","Dumas","Brunet","Schmitt","Red","hake","Fernandez","Pierre","Fox","Arnaud","Rolland","Because we","Aubert","Giraud","Leclerc","Vidal","Bourgeois","Renaud","The monk","Picard","forecastle","Philippe","Leclercq","The cross","Fabre","Dupuis","Olivier","Rodriguez","Da Silva","Hubert","Louis","Charles","Guillot","River","The Gall","Guillaume","Adam","Rey","Mill","Gonzalez","Shepherd","The count","Menard","Fleury","The fields","Carpentier","Julian","Benoit","Paris","Maillard","Marchal","Aubry","Vasseur","Red","Renault","Backgammon","Collar","Prevost","pear tree","Carpenter","Royer","Huet","Baron","Dupuy","Pons","Paul","Wool","Square","breton","Remy","Schneider","Perrot","Guyot","Closed off","Marty","Cousin","The Goff","Butcher","Bailly","Baker","Collin","Herve","Evrard","Foal","Etienne","The brown","Daniel","Pereira","Pasquier","Tailpiece","Humbert","Gillet","cowherd","Leveque","Albert","Ferreira","Jacob","Germain","Klein","Millet","Weber","Gomez","Marechal","Gay","Chevallier","Mallet","The wise man","Bertin","The White","Alexander","Gonçalves","Perrier","Hamon","Dos Santos","Rodrigues","Pelletier","Bouchet","Monnier","Lightweight","Marine","The master","Reynaud","Pichon","Lamy","Antoine","snub","Georges","Perret","Coulon","Large","Devaux","Langlois","Gilbert","Tessier","Chauvinist","Ollivier","Levy","Marion","Dupond","Joubert","Jacques","Rossi","Besson","The big","Guichard","Fernandes","Carlier","Delattre","Maury","Cohen","Hernandez","Guillon","Coste","greenfinch","Wild","The young","Martins","Ferrand","Blanchet","Ruiz","Bousquet","Didier","Tanguy","brands","Michaud","Gregoire","Barthelemy","Charrier","Briand","Guillou","Mauritius","Navarro","The Duke","Pascal","Delorme","Delaunay","Thibault","Bodin","Valentine","Gaudin","Allard","Mahe","Chauvet","Mass","Tran","Valley","Beard","Bush","Breton","Benard","Blondel","The door","Hebert","Courteous","Riou","Legendre","Fischer","Delannoy","Valiant","The strong","Regnier","Guillet","dressmaker","Raynaud","Bazin","Bigot","Peltier","bumblebee","Allain","Some camps","Duhamel","Dupre","Bruneau","Besnard","Black","Lacombe","The rock","Launay","Loiseau","Morvan","Jacquot","Raymond","Nightingale","Auger","Brunel","Thierry","Jourdan","Neighbour","Godard","Blin","Baudry","Pages","Martel","Martineau","Faivre","Berthelot","Pineau","Texier","Girault","Norman","Small Jean","Seguin","blot","Delmas","Fouquet","Guilbert","Colas","Blackbird","Pruvost","skua","Imbert","Toussaint","Mallet","Bonneau","Tournier","Salaun","Vallet","Favre","Delage","Wagner","Hardy","Gervais","Christian","Grandjean","relative","Gomes","Peron","Guyon","Lombard","Claude","cleric","Chartier","The blond","Da Costa","The guard","Guibert","Mace","Chauveau","The tale","Hamel","Provost","Horned","Hare","Flament","poleaxe","Vial","Boulay","Mary","Parmentier","Valletta","Chapuis","Rooster","Sheep","Geoffroy","Alves","Ribeiro","Lopes","The borders","Besse","Mark","Picot","Boutin","Lacoste","Salmon","Prigent","Gilles","Fish","Pujol","Gallet","Gueguen","Thiery","Lemonnier","Costa","Greenhouse","Bouvet","Foucher","Pottier","Mas","Attic","Leonard","During","Doucet","Potter","Torres","Corre","Brault","Coal","Bouchard","fat","Bayle","Delahaye","ferry","Berthier","Maurin","Fellow","Battle","Bouquet","Dubreuil","Along","Rault","Prost","Path","Jordan","great","Moreno","Bocquet","Good","Jacquemin","Nephew","Becker","Husson","Combes","Marquet","Benoist","Guy","Mayor","From the mill","Huguet","Bernier","Lafon","Sabatier","Rock","Arnould","drag","Lecocq","Morand","Ferre","County","Monier","The Roy","Thiebaut","Bourdin","Guillemin","Leleu","Millot","Forest","Mangin","Fort","Ricard","Billiards","Guen","Rousset","Jamet","Roques","Chambon","Jung","Of the garden","Turpin","Diaz","Prat","Jolivet","Favier","Andrieux","Castel","Bonnin","shoe","Grosjean","Maurel","Dias","Munoz","Chatelain","Pink","Blondeau","Guignard","Tellier","Cros","The","Tardy","Combe","Cochet","Schmidt","Magnier","saddler","Bar","Monnet","Guiraud","Zimmermann","Granger","Leon","Godin","Andrieu","Walter","Granier","Gosselin","Drouet","Villain","Lavergne","Savary","Barn","mow","strong","Lafont","barn","Letellier","Veron","Good","The courtyard","cowherd","Lecuyer","Guillemot","The page","Guegan","Levasseur","Armand","Bonnefoy","Keller","Derrien","The Bihan","Samson","Geffroy","Mignot","One eyed","Prior","Door","Poncet","Belin","The Gal","Kieffer","Bonnard","Gil","Blaise","Mounier","Vernet","Baudouin","Bob","Laval","Duclos","Hoffmann","The franc","Godfrey","Payet","Lalanne","Corre","Rigaud","Caillaud","The arm","Jane","Berard","Morice","Cartier","Weaver","Saunier","Weiss","Apple tree","Welsh","Stephan","Bauer","Ramos","Villette","Vine","Casanova","Beck","Guitton","George","Ledoux","Dupin","Horn","Brossard","Office","Master","Woodland","basket-maker","Sergeant","Papin","Constant","Lallemand","Claudel","Marcel","swift","Merchant","Pinto","Jouan","Simonnet","Barret","Demange","Pierron","Soler","Shirt","Bastien","Mathis","Vigneron","Quere","Poirot","Berthet","Terrier","Bellanger","Sicard","Leray","Gicquel","Roland","Jarry","Lang","Tavernier","Jullien","Le Berre","Capelle","Thebault","Wood","From Sousa","Joseph","Vivier","Fuller","Janin","Goatherd","Nicolle","De Oliveira","Aubin","Payen","Ragot","Esnault","Louvet","Hamelin","Jan","Binet","Champion","Galland","Oak","Forest","Pinel","Caillet","Stud","Fayolle","Thery","Tower","Sarrazin","Proust","Froment","The beautiful","Viard","Porter","Deshayes","Alix","Gibert","Langlais","Hammer","Dubus","Brochard","Courtin","Gimenez","Lefeuvre","Ly","Felix","The French","The Archer","Mora","picket","Baudin","Alvarez","Of yours","Lasserre","Mendes","Roman","Chollet","Swamp","Foucault","Bucket","Durieux","Castle","Duprat","Charlie","Jegou","Esteve","Jolly","The Floch","Collignon","Bossard","Beaufils","Duchene","Ticket","Pasquet","German","Teixeira","Villeneuve","Tissier","ugly","brand","Roth","Bailleul","Parisot","Fourcade","Serra","Briere","Stuffy","Monk","Lienard","Magne","Solomon","Romero","Leclere","Stone","Rio","Simonin","Cariou","Jouve","Basset","Blandin","Lallement","Garreau","Guilbaud","Chabert","gee up","Gobert","Darras","Beaumont","Rivet","Duchesne","Raynal","Provost","bertha","Guillard","Boudet","glass-blower","Pollet","From the street","Career","Teyssier","Charlet"]}
        ,{"country":"de","values":["Müller ","Schmidt","Schneider","Fischer","Weber","Schäfer","Meyer","Wagner","Becker","Bauer","Hoffmann","Schulz","Koch","Richter","Klein","Wolf","Schröder","Neumann","Braun","Werner","Schwarz ","Hofmann","Zimmermann","Schmitt","Hartmann","Schmid","Weiß","Schmitz ","Krüger","Lange","Meier","Walter","Köhler","Maier","Beck","König","Krause ","Schulze","Huber","Mayer","Frank","Lehmann","Kaiser","Fuchs","Herrmann","Lang","Thomas","Peters","Stein","Jung","Möller","Berger ","Martin ","Friedrich ","Scholz","Keller","Groß","Hahn","Roth ","Günther  ","Vogel","Schubert ","Winkler ","Schuster","Lorenz","Ludwig ","Baumann - ","Heinrich ","Otto ","Simon ","Graf","Kraus","Krämer ","Böhm","Schulte ","Albrecht ","Franke","Winter","Schumacher ","Vogt","Haas ","Sommer","Schreiber","Engel ","Ziegler","Dietrich ","Brandt","Seidel","Kuhn","Busch","Horn","Arnold ","Kühn","Bergmann","Pohl","Pfeiffer","Wolff","Voigt","Sauer"]}
        ,{"country":"es","values":["Garcia"," Fernandez"," Lopez"," Martinez"," Gonzalez"," Rodriguez"," Sanchez"," Perez"," Martin"," Gomez"," Ruiz"," Diaz"," Hernandez"," Alvarez"," Jimenez"," Moreno"," Munoz"," Alonso"," Romero"," Navarro"," Gutierrez"," Torres"," Dominguez"," Gil"," Vazquez"," Blanco"," Serrano"," Ramos"," Castro"," Suarez"," Sanz"," Rubio"," Ortega"," Molina"," Delgado"," Ortiz"," Morales"," Ramirez"," Marin"," Iglesias"," Santos"," Castillo"," Garrido"," Calvo"," Pena"," Cruz"," Cano"," Nunez"," Prieto"," Diez"," Lozano"," Vidal"," Pascual"," Ferrer"," Medina"," Vega"," Leon"," Herrero"," Vicente"," Mendez"," Guerrero"," Fuentes"," Campos"," Nieto"," Cortes"," Caballero"," Ibanez"," Lorenzo"," Pastor"," Gimenez"," Saez"," Soler"," Marquez"," Carrasco"," Herrera"," Montero"," Arias"," Crespo"," Flores"," Andres"," Aguilar"," Hidalgo"," Cabrera"," Mora"," Duran"," Velasco"," Rey"," Pardo"," Roman"," Vila"," Bravo"," Merino"," Moya"," Soto"," Izquierdo"," Reyes"," Redondo"," Marcos"," Carmona"," Menendez"]}
        ]}


currency_entity =  {"selectors":["country"], "type":"choice", "values_all":[
         {"country":"gr","values": ["EUR"]}
        ,{"country":"it","values": ["EUR"]}
        ,{"country":"uk","values": ["GBP"]}
        ,{"country":"fr","values": ["EUR"]}
        ,{"country":"de","values": ["EUR"]}
        ,{"country":"es","values": ["EUR"]}
        ]}  

city_entity =  {"selectors":["country"], "type":"choice", "values_all":[
         {"country":"gr","values":['Athens', 'Thessaloniki', 'Patras', 'Heraklion', 'Larissa', 'Volos', 'Rhodes', 'Ioannina', 'Chania', 'Agrinio']}
        ,{"country":"it","values":['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania']}
        ,{"country":"uk","values":['London', 'Birmingham', 'Leeds', 'Glasgow', 'Sheffield', 'Bradford', 'Manchester', 'Edinburgh', 'Liverpool', 'Bristol']}
        ,{"country":"fr","values":['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille']}
        ,{"country":"de","values":['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt am Main', 'Stuttgart', 'Düsseldorf', 'Dortmund', 'Essen', 'Leipzig']}
        ,{"country":"es","values":['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza', 'Málaga', 'Las Palmas de Gran Canaria', 'Bilbao', 'Murcia', 'Valladolid']}
        ]}  

def statistical_select(elements):
    results = []
    resoltion = 1000
    for ele in elements:
        for conte in range(0,int(resoltion*ele[1])):
            results.append(ele[0])
    return random.choice(results)
        

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def apply_context(selectors,element,context,current_row):
    
    #print(element," vs ",current_row)
    # applica i selettore generico
    if selectors != []:
        lista_selectors = [ a for a in selectors if a in context.keys()]

        # per tutte le combinazioni usando il context
        ritorno = []
        # se rispetta tutti i check

        for ele_sele in lista_selectors:
            if element[ele_sele] == context[ele_sele]:
                ritorno.append(element["values"])

        lista_selectors_2 = [ a for a in selectors if a in current_row.keys()]
        # per tutte le combinazioni usando l'ultima riga 
        
        # se rispetta tutti i check
        for ele_sele in lista_selectors_2:
            if element[ele_sele] == current_row[ele_sele]:
                ritorno.append(element["values"])

        return ritorno
    else:
        return element["values"]


def builder(table_element,context):
    # this rappresent one row

    data_rows = []
    
    prog_id_entity["values"] = context["index_start"]

    for ele in range(0,context["number"]):

        data_row ={}

        for entity in  table_element["structure"]:
            
            value = 0
            
            lista_selected = []

            #print("Processing: ",entity)
            if entity["type"] == "choice":
                
                entity_values = globals()[entity["enity"] +"_entity"]
                
                list_of_values = entity_values["values_all"]

                lista_selected = []
                
                for ele in list_of_values:
                    # search in the context or IN THE CURRENT row
                    rit = apply_context(entity_values["selectors"],ele,context,data_row) 
                    if rit:
                        lista_selected +=rit
                
                x_list = sum(lista_selected, [])
                                
                value = random.choice(x_list)

                # this add the feature to the row
            #print("Processing: ",entity)
            if entity["type"] == "choice_range":
                
                entity_values = globals()[entity["enity"] +"_entity"]
                
                list_of_values = entity_values["values_all"]

                lista_selected = []
                
                for ele in list_of_values:
                    # search in the context or IN THE CURRENT row
                    rit = apply_context(entity_values["selectors"],ele,context,data_row) 
                    if rit:
                        lista_selected +=rit
                                                                
                value = round(random.uniform(lista_selected[0][0],lista_selected[0][1]),2)

                # this add the feature to the row                
                
            elif entity["type"] == "progressive":
                
                entity_values = globals()[entity["enity"] +"_entity"]

                last_value = entity_values["values"]

                value = last_value + 1

                entity_values["values"] = value

            elif entity["type"] == "choice_fix":

                value = random.choice(entity["range"])            
      
            elif entity["type"] == "choice_stat":

                value = statistical_select(entity["range"])        

            elif entity["type"] == "random_range":

                value = random.randint(entity["range"][0], entity["range"][1])

            elif entity["type"] == "fix_value":   

                value = entity["value"]
                
            elif entity["type"] == "rand_date":   
                
                value = random_date(entity["range"][0], entity["range"][1])
                
            elif entity["type"] == "context":   
                
                # data could be i the context or in the current directory
                if entity["enity"] in context.keys():
                    value = context[entity["enity"]]

                elif entity["enity"] in data_row.keys():
                    value = data_row[entity["enity"]]

            elif entity["type"] == "function":   
                
                entity_function = globals()[entity["enity"] +"_entity"]

                value = entity_function(data_row,context)
            
            data_row[entity["name"]] = value    
        # append row to dataframe
        data_rows.append(data_row)

    df = pd.DataFrame(data_rows)
    
    prog_id_entity["values"] = 0
    
    return df

def process_df(df,context_2,structure_table_2):
    df_final_return = None 

    counter = 0
    for index, row in df.iterrows():
        context_final = merge_two_dicts(context_2,row.to_dict())

        if counter == 0:
            df_final_return = builder(structure_table_2,context_final)
            
        else:
            df2 = builder(structure_table_2,context_final)
            df_final_return = df_final_return.append(df2)

        context_2["index_start"] = df_final_return['id'].max()

        counter +=1

    return df_final_return
        
def process_numb(number,context,structure_table):
    df_final = None 

    for index in range(0,number):

        if index == 0:
           #print(data_row)
            df_final = builder(structure_table,context)
            
        else:
            df2 = builder(structure_table,context)
            df_final = df_final.append(df2)

        context["index_start"] = df_final['id'].max()

        
    return df_final
        


def main():
    print(" --- syntetic data creator --- ")

    context = {
    "language": "en",
    "country": statistical_select([("es",0.20),("uk",0.20),("fr",0.20),("it",0.20),("gr",0.20)]),
    "company": "happycompany",
    "index_start":1500,
    "number" : 1
    }

    structure_table ={
    "name": "employee_table",
    "structure":[
     {"enity":"country","type":"context","name":"country"},
    {"enity":"name","type":"choice","name":"name"},
    {"enity":"surname","type":"choice","name":"surname"},  
    {"enity":"email","type":"function","name":"email"},  
    {"enity":"prog_id", "type":"progressive" ,"name":"id"},  
    {"type":"random_range","name":"seniority", "range":(1,10)}, 
    {"type":"random_range","name":"Age", "range":(26,55)}, 
    {"type":"fix_value","name":"Role", "value":"Sales rep"}, ]
    }

    df = process_numb(1000,context,structure_table)

    df.to_csv("data/"+str(structure_table["name"])+".csv")

    print(df)

    structure_table_2 ={
    "name": "reimbourse",
    "structure":[
    {"enity":"name","type":"context","name":"name"},
    {"enity":"surname","type":"context","name":"surname"},  
    {"enity":"id","type":"context","name":"Emploeyy_id"}, 
    {"enity":"prog_id","type":"progressive","name":"id"},  
    {"enity":"rand_date","type":"rand_date","name":"Date", "range":(datetime.date(2017,1, 1),datetime.date(2017, 12, 31))}, 
    {"type":"choice_stat","name":"Type","range":[("Restaurant",0.3),("Hotels",0.3),("Taxi",0.3),("Honorarium",0.03),("Others",0.07)]}, 
    {"enity":"Amount_reimbourse","type":"choice_range","name":"Amount"},
    {"enity":"currency","type":"choice","name":"currency"},
    {"enity":"city","type":"choice","name":"City"},
    {"type":"fix_value","name":"Role", "value":"Sales rep"}, ]
    }


    context_2 = {
    "language": "en",
    "country": statistical_select([("uk",0.20),("fr",0.40),("it",0.40)]),
    "number" :150,
    "index_start":25000
    }


    df_final = process_df(df,context_2,structure_table_2)
    df_final.to_csv("data/"+str(structure_table_2["name"])+".csv")

    print(df_final)

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

if __name__ == '__main__':
    __name__ = 'Main'
    main()

#----------------------------------------------------------------------------








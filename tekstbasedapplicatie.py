from time import sleep
import os
clear = lambda: os.system('cls')
angel = 'miranda'
keuzejalist = ['ja','zeker','duh','tuurlijk','Ja','Zeker','Duh','Tuurlijk','JA','ZEKER','DUH','TUURLIJK']
keuzeneelist = ['nee','nope','zeker niet','ik dacht het niet','Nee','Nope','Zeker niet','Ik dacht het niet','NEE','NOPE','ZEKER NIET','IK DACHT HET NIET',]
skilllist = ['great sage', 'skill tame', 'power absoberen']
mannenstem = ['Onbekende mannen stem']
sage = ['Great sage']
oude_zwaard = 0
coins = 0
def keuze6():
                        keuze6 = input('')
                        if keuze6 == 'klusjes doen':
                            print(naam,': kan ik iets voor u doen als klusje')
                            sleep(2.6)
                            print('Groenteman: je kan die 8 dozen naar achter brengen voor 20 geld stukken')
                            sleep(2.6)
                            print('Je draagt de laatste doos naar achter en komt een versleten oude zwaard tegen ')
                            coins+= 20
                            

                            #keuze 8 vraag je of je hem mag houden
                            keuze8 = input('')
                            if keuze8 in keuzejalist:
                                oude_zwaard+= 1
                                print('')
                            elif keuze8 in keuzeneelist:
                                oude_zwaard = 0
                                print('')

                        elif keuze6 == 'bodyguard':
                            print()
                        elif keuze6 == 'adventurer':
                            print()
    

while 1:
    print('midas')
    sleep(2)
    print('een game gemaakt door  jamy de waal')
    sleep(2)
    print('veel plezier en duik in het verhaal')
    print("loading . . .")
    sleep(2)
    print('loading . . . .')
    sleep(2)
    print('loading complete')
    sleep(2)
    clear()
    sleep(2)
    # hier begint start 
    print('Je zit in je kamer het is donker en je gordijn is dicht.')
    sleep(2)
    print('Je  start je computer op en gaat aan je bureau zitten.')
    sleep(2)
    print('Je start midas op een mmorpg rpg.')
    sleep(2)
    print('Midas opstartscherm: wat is jouw naam ')
    #naam is de naam van de speler 
    naam = input('')
    sleep(2)
    print('Na 10 uur begin je een beetje hoofd pijn te krijgen en langzaam word alles…')
    sleep(2)
    print('zwart')
    sleep(2)
    print('Je ligt in completen duisternis')
    sleep(2)
    print('In de verte hoor je een stem zachtjes luider worden ')
    sleep(2)
    print('Onbekende stem: Hallo? ….hallo?')
    sleep(2)
    while 1:

        print('Onbekende stem: kun je me horen?')
        keuze1 = input()
        if keuze1 in keuzejalist:
            print('Onbekende stem: geweldig ik ben Miranda ik ben hier om jouw een hergeboorte')
            sleep(2.6)
            print('te geven in een andere wereld. één waar zwaard vechten en magie de norm zijn.')
            sleep(2.6)
            print(naam,':dit is een grap')
            sleep(2.6)
            print(angel,': als ik jou was zou ik dit serieus gaan nemen want je krijgt geen tweede kans',naam)
            sleep(2.6)
            print(naam,':hoe weet je mijn naam?')
            sleep(2.6)
            print(angel,': ik heb hier geen tijd voor je kunt 3 skills kiezen voor je nieuwe leven kies wijs')
            sleep(2.6)
            print(skilllist)
            keuze2 = input('')
            if keuze2 == 'great sage':
                print(angel,': dat is een solid keuze ')
                sleep(2)
                print(angel,'de skill : great sage')
                sleep(2)
                print(angel,': je kunt nu spreken met de great sage door heb een vraag in je hoofd testellen')
                sleep(2)
                print(angel,':alleen kun je het niet al te vaak gebruiken vanwege … bijwerkingen anyway..')
                sleep(2)
                print(angel,': good luck met je avontuur ik zorg dat je wakker word naast een dorp waar je kan beginnen')
                sleep(2)
                clear()
                print('kling, kling')
                sleep(2)
                print(mannenstem,': ben je nog levend?')
                sleep(2)
                print(mannenstem,': hallo?')
                sleep(2)
                print('Water word over je heen gegooid')
                sleep(2)
                print('je zit gelijk overeind')
                sleep(2.6)
                print(naam,': wat is jouw probleem?')
                sleep(2.6)
                print(mannenstem,': mijn probleem?')
                sleep(2.6)
                print(mannenstem,': ik ben niet degene die bewusteloos ligt buiten de muren van het dorp ')
                sleep(2.6)
                print(mannenstem,': wil je dood ofzo?')
                sleep(2.6)
                print(naam,': dorp? Waar heb je het over?')
                sleep(2.6)
                print(naam,': o wacht dat is wat de god tegen me zei')
                sleep(2.6)
                print(mannenstem,': god?')
                sleep(2.6)
                print('ga je nu vertellen wat er is gebeurd?')
                sleep(2.6)
                keuze3 = input('')
                if keuze3 in keuzejalist:
                    print('Je verteld hem over wat je is overkomen')
                    sleep(2.6)
                    print(mannenstem,': een onderdaan van god ')
                    sleep(2.6)
                    print('Onbekende man word enthousiast')
                    sleep(2.6)
                    print(mannenstem,':  we zijn gered eindelijk ')
                    sleep(2.6)
                    print(naam,': gered?')
                    sleep(2.6)
                    print(mannenstem,': jij komt ons redden van de demonen')
                    sleep(2.6)
                    print(naam,': ja dat denk ik toch niet ')
                    sleep(2.6)
                    print('Onbekende man zegt het tegen de ridders en vertelt dat je geen intensie hebt de demonen te bevechten.')
                    sleep(2.6)
                    print('Je word publiekelijk geëxecuteerd ')
                    sleep(2.6)
                    print('wil je opnieuw')
                    sleep(2.6)
                    restart = input()
                    if restart in keuzejalist:
                        break
                    elif restart in keuzeneelist:
                        quit
                if keuze3 in keuzeneelist:
                    print('Je houd het voor je.')
                    sleep(2.6)
                    print('En de man brengt je in de stad.')
                    sleep(2.6)
                    print('Je loop door een gigantische poort die lijkt alsof het uit een fantasie wereld komt.')
                    sleep(2.6)
                    print('De man blijkt een bewaker van de gate te zijn waar hij jouw vond.')
                    sleep(2.6)
                    print('Hij geeft je een pasje met toestemming om in de stad te blijven.')
                    sleep(2.6)
                    print('Je gaat opzoek naar een plaats om te slapen maar je beseft dat je geen geld hebt.')
                    sleep(2.6)
                    print('Je raakt in paniek en vraagt je zelf af wat je kan doen en dan herinnerde je wat')
                    sleep(2.6)
                    print('Miranda zei je hebt nu de skill great sage en je kon het alles vragen wat je wou en hij zou een antwoord hebben.')
                    sleep(2.6)
                    print('ga je great sage gebruiken')
                    sleep(2.6)
                    keuze4 = input('')
                    if keuze4 in keuzejalist:
                        print(sage,': er is een dungeon 4 km van de west gate vandaan je kunt daar makelijk schatten vinden.')
                        print('ga je naar de dungeon of ga je verder door de stad zoeken')
                        print('dungeon of verder kijken')
                        keuze5 = input('')
                        if keuze5 == 'dungeon':
                            print()
                        elif keuze5 == 'verder kijken':
                                print('Je besluit om rond te kijken en je vind een markt.')
                                sleep(2.6)
                                print('Groenteman: he knul wil je wat fruit het is het verste uit de hele stad')
                                sleep(2.6)
                                print(naam,': ik heb geen geld, weet u een manier om makelijk geld teverdienen.')
                                sleep(2.6)
                                print('Groenteman: hmm…')
                                sleep(2.6)
                                print('Groenteman: je zou klusjes kunnen doen, je zou een bodyguard kunnen zijn en aan sluiten bij de adventurer guild.')
                                sleep(2.6)
                        else:
                            print('dat is geen optie')
                            clear()
                    elif keuze4 in keuzeneelist:
                        print('Je besluit om rond te kijken en je vind een markt.')
                        sleep(2.6)
                        print('Groenteman: he knul wil je wat fruit het is het verste uit de hele stad')
                        sleep(2.6)
                        print(naam,': ik heb geen geld, weet u een manier om makelijk geld teverdienen.')
                        sleep(2.6)
                        print('Groenteman: hmm…')
                        sleep(2.6)
                        print('Groenteman: je zou klusjes kunnen doen, je zou een bodyguard kunnen zijn en aan sluiten bij de adventurer guild.')
                        sleep(2.6)
                        keuze6 = input('')
                        if keuze6 == 'klusjes doen':
                            print(naam,': kan ik iets voor u doen als klusje')
                            sleep(2.6)
                            print('Groenteman: je kan die 8 dozen naar achter brengen voor 20 geld stukken')
                            sleep(2.6)
                            print('Je draagt de laatste doos naar achter en komt een versleten oude zwaard tegen ')
                            coins+= 20
                            

                            #keuze 8 vraag je of je hem mag houden
                            keuze8 = input('')
                            if keuze8 in keuzejalist:
                                oude_zwaard+= 1
                                print('')
                            elif keuze8 in keuzeneelist:
                                oude_zwaard = 0
                                print('')

                        elif keuze6 == 'bodyguard':
                            print()
                        elif keuze6 == 'adventurer':
                            print()

            elif keuze2 == 'skill tame':
                print()
            elif keuze2 == 'power absoberen':
                print()
            else:
                print('geen optie probeer nog een keer')


        elif keuze1 in keuzeneelist:
            print('Onbekende stem: ha ha ha heel grappig ')
            print(naam,': weet ik ')
            sleep(2)
            print('angel : mijn naam is miranda.')
            sleep(2)
            print(angel,': ik had een speech klaar staan maar daar heb ik geen zin meer in.')
            sleep(2)
            while 1:
                print(angel,': kort samengevat je gaat naar een nieuwe wereld je hebt keuze tussen 3 skills')
                sleep(2)
                print(angel,': kies wijs of niet. het boeit mij niet meer')
                sleep(2)
                print(naam,': wacht wat?')
                sleep(2)
                print(skilllist)
                keuze2 = input('')
                if keuze2 == 'great sage':
                        print(angel,': dat is een solid keuze ')
                        sleep(2)
                        print(angel,'de skill : great sage')
                        sleep(2)
                        print(angel,': je kunt nu spreken met de great sage door heb een vraag in je hoofd testellen')
                        sleep(2)
                        print(angel,':alleen kun je het niet al te vaak gebruiken vanwege … bijwerkingen anyway..')
                        sleep(2)
                        print(angel,': good luck met je avontuur ik zorg dat je wakker word naast een dorp waar je kan beginnen')
                        sleep(2)
                        clear()
                        print('kling, kling')
                        sleep(2)
                        print(mannenstem,': ben je nog levend?')
                        sleep(2)
                        print(mannenstem,': hallo?')
                        sleep(2)
                        print('Water word over je heen gegooid')
                        sleep(2)
                        print('je zit gelijk overeind')
                        sleep(2.6)
                        print(naam,': wat is jouw probleem?')
                        sleep(2.6)
                        print(mannenstem,': mijn probleem?')
                        sleep(2.6)
                        print(mannenstem,': ik ben niet degene die bewusteloos ligt buiten de muren van het dorp ')
                        sleep(2.6)
                        print(mannenstem,': wil je dood ofzo?')
                        sleep(2.6)
                        print(naam,': dorp? Waar heb je het over?')
                        sleep(2.6)
                        print(naam,': o wacht dat is wat de god tegen me zei')
                        sleep(2.6)
                        print(mannenstem,': god?')
                        sleep(2.6)
                        print('ga je nu vertellen wat er is gebeurd?')
                        sleep(2.6)
                        keuze3 = input('')
                        if keuze3 in keuzejalist:
                            print('Je verteld hem over wat je is overkomen')
                            sleep(2.6)
                            print(mannenstem,': een onderdaan van god ')
                            sleep(2.6)
                            print('Onbekende man word enthousiast')
                            sleep(2.6)
                            print(mannenstem,':  we zijn gered eindelijk ')
                            sleep(2.6)
                            print(naam,': gered?')
                            sleep(2.6)
                            print(mannenstem,': jij komt ons redden van de demonen')
                            sleep(2.6)
                            print(naam,': ja dat denk ik toch niet ')
                            sleep(2.6)
                            print('Onbekende man zegt het tegen de ridders en vertelt dat je geen intensie hebt de demonen te bevechten.')
                            sleep(2.6)
                            print('Je word publiekelijk geëxecuteerd ')
                            sleep(2.6)
                            print('wil je opnieuw')
                            sleep(2.6)
                            restart = input()
                            if restart in keuzejalist:
                                break
                            elif restart in keuzeneelist:
                                quit
                elif keuze2 == 'skil tame':
                    print()
                elif keuze2 == 'power absoberen':
                    print()
                else:
                    print('geen optie probeer nog een keer')
        else:
            print('geen optie probeer nog een keer')
from time import sleep
import os
clear = lambda: os.system('cls')
angel = 'miranda'
keuzejalist = ['ja','zeker','duh','tuurlijk']
keuzeneelist = ['nee','nope','zeker niet',]
skilllist = ['great sage', 'skill tame', 'power absoberen']
mannenstem = ['Onbekende mannen stem']


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
            print('te geven in een andere wereld. één waar zwaard vechten en magie de norm zijn.')
            print(naam,':dit is een grap')
            print(angel,': als ik jou was zou ik dit serieus gaan nemen want je krijgt geen tweede kans',naam)
            print(naam,':hoe weet je mijn naam?')
            print(angel,': ik heb hier geen tijd voor je kunt 3 skills kiezen voor je nieuwe leven kies wijs')
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
                print(naam,': wat is jouw probleem?')
                print(mannenstem,': mijn probleem?')
                print(mannenstem,': ik ben niet degene die bewusteloos ligt buiten de muren van het dorp ')
                print(mannenstem,': wil je dood ofzo?')
                print(naam,': dorp? Waar heb je het over?')
                print(naam,': o wacht dat is wat de god tegen me zei')
                print(mannenstem,': god?')
                print('ga je nu vertellen wat er is gebeurd?')
                keuze3 = input('')
                if keuze3 in keuzejalist:
                    print('Je verteld hem over wat je is overkomen')
                    print(mannenstem,': een onderdaan van god ')
                    print('Onbekende man word enthousiast')
                    print(mannenstem,':  we zijn gered eindelijk ')
                    print(naam,': gered?')
                    print(mannenstem,': jij komt ons redden van de demonen')
                    print(naam,': ja dat denk ik toch niet ')
                    print('Onbekende man zegt het tegen de ridders en vertelt dat je geen intensie hebt de demonen te bevechten.')
                    print('Je word publiekelijk geëxecuteerd ')
                    print('wil je opnieuw')
                    restart = input()
                    if restart in keuzejalist:
                        break
                    elif restart in keuzeneelist:
                        quit
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
                    print()
                elif keuze2 == 'skil tame':
                    print()
                elif keuze2 == 'power absoberen':
                    print()
                else:
                    print('geen optie probeer nog een keer')
        else:
            print('geen optie probeer nog een keer')
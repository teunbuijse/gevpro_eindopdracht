Spelling Bee

Eindopdracht gevorderd programmeren 
13-04-2020
Ties Leneman, Teun Buijse, Tycho Klein Gunnewiek, Timo Lankamp

Dit spel is een python programma gebasseerd op het 'spelling bee' spel van de New York Times.
Het is de bedoeling er woorden gemaakt worden met de  7 letters die op de knoppen staan. Elk woord moet uit minimaal 4 letters bestaan, en de middelste letter in de gele knop moet in elk woord voorkomen. Als er een woord is gemaakt, wordt er op de submit knop gedrukt om te controleren of het inderdaad een bestaand Nederlands woord is, waarna er vervolgens al dan niet punten worden toegekend voor het woord. De puntenverdeling voor de woorden is als volgt:

4-letterwoord: 1 punt
5-letterwoord: 2 punten
6-letterwoord: 3 punten
7-letterwoord: 4 punten
8-letterwoord: 5 punten
9-letterwoord: 6 punten
10-letterwoord: 7 punten
pangram (alle 7 letters 1 keer gebruiken): 7 punten

Hiernaast is er ook nog een clear knop om de huidige geselecteerde letters te wissen, en nog een hint knop waarbij je een hint krijgt, het programma zegt dan een aantal letters van een woord voor. Bij het gebruiken van een hint wordt 1 punt in mindering gebracht.

Bij het aanroepen van het programma zijn er ook verschillende keuzes in moeilijkheidsgraden. De moeilijkheidsgraden waaruit gekozen kan worden zijn: makkelijk, gemiddeld, moeilijk en extreem_moeilijk. Er kan ook nog gekozen worden om de solver te printen. Als deze wordt aangeroepen, print het programma alle mogelijke woordcombinaties in de terminal.

Het aanroepen van het programma gaat als volgt:

timolankamp@Timos-MacBook-Pro gevpro_eindopdracht % python3 *moeilijkheidsgraad* *Bool*

hierbij moet moeilijkheidsgraad vervangen worden door makkelijk, gemiddeld, moeilijk of extreem_moeilijk. Dit ligt er natuurlijk aan welke moeilijkheidsgraad gespeeld wil worden.

Bool moet vervangen worden door True of False. True als de solver in de terminal geprint dient te worden, en False als dit niet hoeft. Een voorbeeld van het aanroepen in de terminal is dus:

timolankamp@Timos-MacBook-Pro gevpro_eindopdracht % python3 gui.py gemiddeld True

Hierbij wordt het spel gestart met een gemiddelde moeilijkheidsgraad, en de solver wordt geprint in de terminal.









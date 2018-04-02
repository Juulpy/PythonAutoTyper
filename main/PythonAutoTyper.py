#--import section--
import pyautogui as typer
import time

#Starting lines
print('Vocabtyper v0.1 by Petit, made in Goutum')
print('==================================' )
print('')
print('Werkt momenteel alleen voor Engels omdat Python Franse tekens niet herkent in de textfiles.')
print('')
print("Zorg dat je de file van je vocab in goede volgorde hebt, en dat het txt-bestandje 'vocab' heet")
print("Als het hele textbestand is getypt, start dit programma opnieuw op. (Wordt later automatisch)")
time.sleep(1)

#Ask for interval
interval = input('Interval tussen letters (seconden): ')
print('In 5 seconden start de typer')

#import file
text_file = open('vocab.txt', "r")
text_file.close()

#Count number of lines as num_lines
num_lines = sum(1 for line in open('vocab.txt'))
print('Aantal lines: ',num_lines)

#Read text file
text_file = open('vocab.txt', "r")
a = (text_file.read())
print(text_file.readline(1))

#Delay before typing time.sleep([secs])
time.sleep(5)

#Auto-typer ('Text', delay=[var]')
typer.typewrite((a), interval=(interval))




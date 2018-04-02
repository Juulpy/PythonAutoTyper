#--import section--
import pyautogui as typer
import time

#Starting lines
print('Vocabtyper v0.11 by me, made in Goutum')
print('==================================' )
print('')

#Ask and print interval
interval = input('Interval tussen karakters (seconden): ')
print(interval)
print('')
#Ask and print delay
delay = input('Aantal seconden na de eerstvolgende entertoets dat de autotyper gaat typen: ')
print('Na',(delay),'seconden start de typer')

#import file
#text_file = open('vocab.txt', "r")
#text_file.close()

#Count number of lines as num_lines
num_lines = sum(1 for line in open('vocab.txt'))
print('Aantal lines: ',num_lines * 2)

#Read text file
text_file = open('vocab.txt', "r")
a = (text_file.read())
print(text_file.readline(1))

#Delay before typing time.sleep([secs])
time.sleep(5)

#Auto-typer ('Text', delay=[var]')
typer.typewrite((a), interval=(interval))
typer.typewrite((a), interval=(interval))

print('klaar')

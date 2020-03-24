import telegram
import sys
from ValidarCedula import ValidarCedula

bot_token = '1086161801:AAH6HK3Iu0etpUrG05zVItd3zyAYfSeZfm4'
chat_bot = '776623494'
channel = '-1001404899043'

bot = telegram.Bot(bot_token)

print('Buenas tardes, dias y noches. Espero disfrute de su cuarentena XD.')
print('Si quieres tener el privilegio de estar en un chat con Zen, el bot del futuro')
print('Dame la siguiente informacion...')

cedula = input('Tu cedula: ')
print('Hola')

if not ValidarCedula(cedula):
    print('Desaprovechaste una buena oportunidad')
    print('Hola')
    sys.exit()

partido = input('Partido al que apoyas: ')
frase = input('Tu frase favorita: ')

# bot.send_message(channel, f'''
# Hola soy Zen. Es un privilegio estar contigo.
# Gracias por no decir mentiras y poner tu cedula correcta "{cedula}", se aprecia mucho.
# Veo que apoyas al {partido} espero hagan un buen trabajo en su gobierno.
# A mi tambien me encanta la frase {frase}, somos almas gemelas!
# ''')

bot.send_message(channel, cedula + ' del ' + partido + ' dice: ' + frase)

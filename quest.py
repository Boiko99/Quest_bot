import telebot
import os, sys
bot = telebot.TeleBot("1197986049:AAH4JP5CQt-92Uyp_O1yStC9Md74pz1ljsU")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''Хей, друзі, вітаємо вас на квесті «Месники». \n Неймовірна небезпека, яка виникла буквально з нізвідки загрожує знищити все людство. Ніхто толком не може зрозуміти, хто ж цей таємничий ворог. Було створене управління під назвою Щ.И.Т., покликане підтримувати мир на Землі, яке взялось за оборону всієї планети. Але навіть їм не під силу вберегти планету від зла. Відтак, у них було викрадено секретну зброю – тессеракт.
З цією метою було створено загін, що вперше обєднав всіх супергероїв відомих коміксів. Захисники всіх пригноблених, люті борці за правду, такі як Галк, Залізна людина, Капітан Америка, Тор і інші герої тепер разом виступлять на стороні добра і справедливості. 
Не зважаючи на їхню силу, вони не справляться самі, без вашої допомоги. Тому одягайте свої костюми, відкривайте свої потаємні сили і допоможіть їм врятувати нашу планету.
Успіхів вам! \n Щоб познайомитись з правилами і почати гру пиши /rules ''')
@bot.message_handler(commands=['rules'])
def send_rules(message):
        bot.send_message(message.chat.id, '''1.	Розв’язуйте завдання та вписуйте свої варіанти відповідей (кількість спроб необмежена).
2.	Тільки коли ви введете  правильну відповідь, зможете перейти до виконання наступного завдання. 
3.	Перевіряйте правопис написання слів (при неправильному правописі ви не зможете перейти до виконання наступних завдань).
4.	Якщо ви не можете самостійно виконати завдання протягом 5 хвилин, тоді ви можете написати нам і ми вам дамо підказку (кількість підказок необмежена).
5.	Протягом квесту ви можете набрати 14 балів (по 1 балу за кожне завдання). Кожна підказка – це мінус 1 бал до вашого оцінювання.
6.	Можете використовувати всі доступні ресурси.
7.	Будьте уважними, думайте та аналізуйте.
8.	Коли ви закінчите гру, то заскріньте останнє повідомлення так, щоб було видно годину і надішліть нам
9. Для початку гри напиши /game
''' )

@bot.message_handler(commands=['game'])
def start_game(message):
    bot.send_message(message.chat.id, 'Ти хто?')
    

@bot.message_handler(content_types=['text'])

def quest_send(message):
        names = ['халк', 'тор', 'галк', 'залізна людина', 'соколине око', 'капітан америка', 'чорна вдова' ]
        x = message.text.lower()
        for i in names:
            if i == x:
                bot.send_message(message.chat.id, "Знайдіть місце схову тессеракту. У цьому вам допоможе загадка.")
                bot.send_message(message.chat.id, '''Назва округу у якому розташовані найвищі хмарочоси США, зокрема, Рокфеллерський центр. ''')
                break  
        if message.text.lower() == 'мангеттен':  
            bot.send_message(message.chat.id, 'Зберіть команду для пошуку тессеракту')
            bot.send_message(message.chat.id, 'https://fex.net/uk/s/dmeynss')
        elif message.text.lower() == 'манхеттен':
            bot.send_message(message.chat.id, 'Зберіть команду для пошуку тессеракту')
            bot.send_message(message.chat.id, 'https://fex.net/uk/s/dmeynss')
        elif message.text.lower().replace(",", "").replace(".", "") ==  'галк залізна людина капітан америка соколине око чорна вдова': 
            bot.send_message(message.chat.id, 'Так, тепер треба знайти Локі. Перевірте камери і вкажіть на якій є Локі.')
            bot.send_message(message.chat.id, 'https://drive.google.com/drive/folders/13vVGwhDjxNq-RaIEpeqoDIvXFZ-UGYul')
        elif message.text.lower() == '1':
            bot.send_message(message.chat.id, 'О, ви його знайшли. А вулицю і будинок запам’ятали?')
            bot.send_message(message.chat.id, 'Ні? Тепер потрібно шукати Локі по геолокації. \n Будьте дуже уважними.')
            bot.send_message(message.chat.id, '''Ну що ж, гайда за мною! Починаємо наш шлях із точки - 9GW7+8J Київ. Знайди її на карті. А далі. Йди
вулицею прямо, поки не побачиш білу автівку, а може жовту...фарби змішались. Там поверни наліво.
Йди до кінця вулиці. Біля синього смарт-авто поверни направо та продовжуй йти до середини вулиці
поки не побачиш |101|, там ти повернеш наліво, де згодом побачиш кота. Йди до нього, погладь
малюка та продовжуй свій шлях вулицею, яку він переходить. Біля будинку із бузком поверни наліво і
ти вже близько. Зупинись біля букви |W|; на червоному фоні та вкажи номер і назву вулиці кінцевої
точки.''')
        elif message.text.lower().replace(",", "").replace(".", "") == 'уральський провулок 11':
            bot.send_message(message.chat.id, 'Збій системи, Локі у Німеччині. Негайно вилітаємо.')
            bot.send_message(message.chat.id, 'Непросте завдання. Відчуваю, ми самотужки не впораємось. О! Нове повідомлення із штабу.')
            bot.send_message(message.chat.id, '''"У вас є можливість запросити ще 1 людину приєднатися до Щ.И.Та. Хто це ви дізнаєтесь, розгадавши
стереограму"''')
            bot.send_message(message.chat.id, 'P.s. якщо введете відповідь не англійською мовою, то втратите все і повернетесь на 2 завдання') 
            photo = open('D:/quest/stereogram.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text.lower() == 'tor':
            bot.send_message(message.chat.id, 'Ой, на ваших пристроях низький рівень заряду. Терміново покладіть їх на зарядку.')
            bot.send_message(message.chat.id, 'Скільки пристроїв ви можете поставити на зарядку? Відповідь введіть цифрами.')
            
            photo1 = open('D:/quest/zard.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1)
        elif message.text.lower() == '11':
            bot.send_message(message.chat.id, '''На вашому борту приземлився літак, зараз вам потрібно дізнатися скільки людей у ньому і у якій
частині він приземлився. Напишіть цифрою кількість людей та буквами ту частину, у якій він
приземлився.''')
            bot.send_message(message.chat.id, 'https://drive.google.com/drive/folders/1wcJhHQikj8EP0jqcoyIuZekDoqaOL16a')
        elif message.text.lower().replace(",", "").replace(".", "") == '6 силова установка':
            bot.send_message(message.chat.id, 'Розгіпнутизувати Клінта Бартона може тільки 1 людина. Ребус допоможе дізнатися хто це.')
            photo2 = open('D:/quest/reb.jpg', 'rb')
            bot.send_photo(message.chat.id, photo2)
        elif message.text.lower() == 'наташа романова':
            bot.send_message(message.chat.id, 'Почався бій. Вкажіть будівлю, яка стала епіцентром початку захоплення?')
            photo3 = open('D:/quest/tsufr.jpg', 'rb')
            bot.send_photo(message.chat.id, photo3)
        elif message.text.lower() == 'stark':
            bot.send_message(message.chat.id, '''Починається бій, ви вправно відбиваєте всі атаки. Але чітаврі не здаються, вони загнали всіх людей
у 1 приміщення. Ви повинні їх врятувати. Напишіть назву приміщення.''')
            bot.send_message(message.chat.id, '0:56; 2:23; 1:41; 2:12')
            audio = open('D:/quest/audio.ogg', 'rb')
            bot.send_audio(message.chat.id, audio)
        elif message.text.lower() == 'банк':
            bot.send_message(message.chat.id, 'Визначте траєкторію польоту луку Соколиного Ока.')
            photo4 = open('D:/quest/dzer.jpg', 'rb')
            bot.send_photo(message.chat.id, photo4)
        elif message.text.lower() == 'тридцять градусів':
            bot.send_message(message.chat.id, '''Щоразу прибувають нові чітаврі. Ви не зможете побороти їх всіх, потрібно терміново закрити
Портал. Інакше весь світ буде знищено. Але як це зробити?''')
            bot.send_message(message.chat.id, 'Cт.121 р.23 б.15')
            bot.send_message(message.chat.id, 'Cт.66 р.36 б.59')
            bot.send_message(message.chat.id, 'Cт.20 р.10 б.15')
            bot.send_message(message.chat.id, 'Cт.79 р.40 б.13')
            bot.send_message(message.chat.id, 'Cт.91 р.28 б.21')
            bot.send_message(message.chat.id, 'Cт.109 р.29 б.4')
            bot.send_message(message.chat.id, 'Cт.147 р.16 б.7')
            doc = open('D:/quest/bot2.doc', 'rb')
            bot.send_document(message.chat.id, doc)
        elif message.text.lower() == 'скіпетр':
            bot.send_message(message.chat.id, 'Хто придумав «Месників»?')
            bot.send_message(message.chat.id, '35:10 з 2:22:54')
        elif message.text.lower().replace("'", "").replace(".", "") == 'нік фюрі':
            bot.send_message(message.chat.id, '''Вітаємо вас, сьогодні ви врятували світ. Дякуємо за допомогу.
Тому мерщій робіть скрін цього повідомлення, щоб було видно годину і надсилайте нам. ''' + ' @Zorya_star ' +
'\nПриємного перегляду відео. ' )
            bot.send_message(message.chat.id, 'https://youtu.be/fPzq2xZetWE')
            bot.send_message(message.chat.id, '@Zorya_star')
            
            
            
              
    


bot.polling(none_stop=True)
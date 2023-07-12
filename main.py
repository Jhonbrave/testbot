import telebot
token='6196379875:AAFiPbpal0DVENhHvWtg7YVS7Nm_7LTY_wU'
bot=telebot.TeleBot(token)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"HELLO Sir/Mam\n\nWelcome To----CALC BOT\n\n(iam in developing condition)")
@bot.message_handler(['developer'])
def developer(message):
    bot.reply_to(message,"I am developed by Miss Chaithali")
@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"/start :for greeting\n\n/developer :to know developer's name\n\n/help :to get list of commands\n\n YOU CAN PERFORM ARITHMATIC CALCULATIONS")
@bot.message_handler()
def custom(message):
    try:
     msg=f' Answer is: {eval(message.text.strip())}'
    except Exception as e:
     msg='Sorry....!! This Cant Be Evaluated'
    bot.reply_to(message,msg)
bot.polling()


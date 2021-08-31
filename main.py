import telebot

from config import TOKEN
import keyboard as kb


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        text="<code>Выберите четность недели 👇</code>",
        reply_markup=kb.week_markup,
        parse_mode="html"
    )


@bot.message_handler(content_types=['text'])
def week(message):
    if message.text == "📌 I Нечетная неделя":
        msg = bot.send_message(
            message.chat.id,
            text="<code>Выберите день недели 👇</code>",
            reply_markup=kb.main_markup1,
            parse_mode="html"
        )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📌 II Четная неделя":
        msg = bot.send_message(
            message.chat.id,
            text="<code>Выберите день недели 👇</code>",
            reply_markup=kb.main_markup2,
            parse_mode="html"
        )
        bot.register_next_step_handler(msg, text2)
    else:
        msg = bot.send_message(message.chat.id,
        text = "<b>⚠️ Неправильный ввод, попробуйте снова!</b>",
        reply_markup = kb.week_markup,
        parse_mode="html"
        )
        bot.register_next_step_handler(msg, week)


def text1(message):
    if message.text == "🔥 I Нечетная неделя 🔥":
        msg = bot.send_message(
            message.chat.id,
            text = "<b>✏️ Вы смотрите расписание на Нечетную неделю</b>",
            reply_markup=kb.main_markup1,
            parse_mode="html"
        )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📅 Пн":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>3️⃣ [12:40-14:10] Физ-ра | ПР</code>

<code>4️⃣ [14:20-15:50] Физика | ПР | A-7</code>

<code>5️⃣ [16:20-17:50] История | ПР | A-206</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup1,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📅 Вт":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>💻 Дистанционный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>2️⃣ [10:40-12:10] ЛА и АГ | ЛК</code>

<code>3️⃣ [12:40-14:10] Физика | ЛК</code>

<code>4️⃣ [14:20-15:50] История | ЛК</code>

<code>5️⃣ [16:20-17:50] ВВПД | ЛК</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup1,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📅 Ср":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>5️⃣ [16:20-17:50] Мат. анл. | ПР | A-405</code>

<code>6️⃣ [18:00-19:30] ЛА и АГ | ПР | A-405</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup1,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📅 Чт":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>💻 Дистанционный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>4️⃣ [14:20-15:50] Инфа | ЛК</code>

<code>5️⃣ [16:20-17:50] Мат. анл. | ЛК</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup1,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📅 Пт":
        msg = bot.send_message(
            message.chat.id,
            text = '''
</b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>4️⃣ [14:20-15:50] Ин.яз | ПР | И-307</code>

<code>5️⃣ [16:20-17:50] Прога | ПР | ИВЦ-108</code>

<code>6️⃣ [18:00-19:30] Прога | ПР | ИВЦ-108</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup1,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "📅 Сб":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>3️⃣ [12:40-14:10] Инфа | ПР | A-424-1</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup1,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text1)

    elif message.text == "🔙 Назад":
        msg = bot.send_message(
            message.chat.id,
            text="<code>Выберите четность недели 👇</code>",
            reply_markup=kb.week_markup,
            parse_mode="html"
        )
        bot.register_next_step_handler(msg, week)

    else:
        msg = bot.send_message(message.chat.id,
        text = "<b>⚠️ Неправильный ввод, попробуйте снова!</b>",
        reply_markup = kb.main_markup1,
        parse_mode="html"
        )
        bot.register_next_step_handler(msg, text1)


def text2(message):
    if message.text == "🔥 II Четная неделя 🔥":
        msg = bot.send_message(
            message.chat.id,
            text = "<b>✏️ Вы смотрите расписание на Четную неделю</b>",
            reply_markup=kb.main_markup2,
            parse_mode="html"
        )
        bot.register_next_step_handler(msg, text2)

    elif message.text == "📅 Пн":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>3️⃣ [12:40-14:10] Физ-ра | ПР</code>

<code>4️⃣ [14:20-15:50] Физика | ПР | A-7</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖


<b>‼️ [4, 8, 12, 16] Неделя полугодий</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>5️⃣ [16:20-17:50] Физика | ПР | B-326</code>

<code>6️⃣ [18:00-19:30] Физика | ПР | B-326</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup2,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text2)

    elif message.text == "📅 Вт":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>💻 Дистанционный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>2️⃣ [10:40-12:10] ЛА и АГ | ЛК</code>

<code>3️⃣ [12:40-14:10] Физика | ЛК</code>

<code>4️⃣ [14:20-15:50] Прога | ЛК</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup2,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text2)

    elif message.text == "📅 Ср":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>5️⃣ [16:20-17:50] Мат. анл. | ПР | A-405</code>

<code>6️⃣ [18:00-19:30] ЛА и АГ | ПР | A-405</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup2,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text2)

    elif message.text == "📅 Чт":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>💻 Дистанционный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>4️⃣ [14:20-15:50] Инфа | ЛК</code>

<code>5️⃣ [16:20-17:50] Мат. анл. | ЛК</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup2,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text2)

    elif message.text == "📅 Пт":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>4️⃣ [14:20-15:50] Ин.яз | ПР | И-307</code>

<code>5️⃣ [16:20-17:50] Прога | ПР | ИВЦ-108</code>

<code>6️⃣ [18:00-19:30] Прога | ПР | ИВЦ-108</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup2,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text2)
    elif message.text == "📅 Сб":
        msg = bot.send_message(
            message.chat.id,
            text = '''
<b>🎒 Очный день</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>3️⃣ [12:40-14:10] Инфа | ПР | A-424-1</code>
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
            ''',
            reply_markup=kb.main_markup2,
            parse_mode="html"
            )
        bot.register_next_step_handler(msg, text2)

    elif message.text == "🔙 Назад":
        msg = bot.send_message(
            message.chat.id,
            text="<code>Выберите четность недели 👇</code>",
            reply_markup=kb.week_markup,
            parse_mode="html"
        )
        bot.register_next_step_handler(msg, week)

    else:
        msg = bot.send_message(message.chat.id,
        text = "<b>⚠️ Неправильный ввод, попробуйте снова!</b>",
        reply_markup = kb.main_markup2,
        parse_mode="html"
        )
        bot.register_next_step_handler(msg, text2)


bot.polling(none_stop=True)



















# datetime.today().strftime('%A')

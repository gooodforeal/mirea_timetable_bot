from telebot import types


week_markup = types.ReplyKeyboardMarkup(resize_keyboard=True).row("📌 I Нечетная неделя").row("📌 II Четная неделя")
main_markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True).row("🔥 I Нечетная неделя 🔥").row("📅 Пн","📅 Вт","📅 Ср").row("📅 Чт","📅 Пт","📅 Сб").row("🔙 Назад")
main_markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True).row("🔥 II Четная неделя 🔥").row("📅 Пн","📅 Вт","📅 Ср").row("📅 Чт","📅 Пт","📅 Сб").row("🔙 Назад")
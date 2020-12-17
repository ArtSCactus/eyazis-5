import playsound as playsound
from google.cloud import texttospeech

from Main import syntesis


def test():
    print("Приветствую!\n")
    while True:
        text = input("Введите текст (или 0 чтобы выйти): ")
        if text is None or len(text) == 0:
            print("Текст не был введён. Пожалуйста, попробуйте снова")
            continue
        if text == "0":
            print("До встречи!")
            exit(0)
        lang = None
        while True:
            lang = input("Введите язык:\n1 - RU\n2 - EN\n0 - Отмена\n")
            if lang is None or len(lang) == 0:
                print("Язык не был введён. Пожалуйста, попробуйте снова")
                continue
            elif lang == "0":
                break
            elif lang == "1":
                lang = "ru-RU"
                break
            elif lang == "2":
                lang = "en-EN"
                break
            else:
                print("Язык нераспознан, попробуйте ещё раз.")
                continue
        gender = None
        gender_str = None
        while True:
            gender = input("Выберите пол:\n1 - Мужской\n2 - Женский\n3 - Нейтральный\n0 - Отмена\n")
            if gender is None or len(gender) == 0:
                print("Пол не был введён. Пожалуйста, попробуйте снова")
                continue
            elif gender == "0":
                break
            elif gender == "1":
                gender = texttospeech.SsmlVoiceGender.MALE
                gender_str = "Мужской"
                break
            elif gender == "2":
                gender = texttospeech.SsmlVoiceGender.FEMALE
                gender_str = "Женский"
                break
            elif gender == "3":
                gender = texttospeech.SsmlVoiceGender.NEUTRAL
                gender_str = "Нейтральный"
            else:
                print("Пол не распознан, попробуйте ещё раз.")
                continue
        speech_rate = None
        while True:
            speech_rate = input(
                "Выберите скорость чтения в диапазоне [0.25, 4.0]\n1 - нормальная скорость, будет установлена по умолчанию\n"
                "Введите 0 для отмены: ")
            if speech_rate is None or len(speech_rate) == 0:
                speech_rate = 1
                break
            else:
                try:
                    speech_rate = float(speech_rate)
                    break
                except ValueError:
                    print("Неверный формат числа, попробуйте ещё раз")
                    continue
        while True:
            confirmation = input("Введённые параметры:\n"
                                 "Текст: " + text + "\n"
                                                    "Язык: " + lang + "\n"
                                                                      "Пол: " + gender_str + "\n"
                                                                                             "Скорость чтения: " + str(
                speech_rate) + "\n"
                               "Подтверждаете ввод?\n1 - Да\n2 - Нет, начать занова\n")
            if confirmation == "1":
                syntesis(text, lang, gender, speech_rate)
                break
            elif confirmation == "2":
                break
            else:
                print("Неверный ввод, попробуйте ещё раз.")
                continue
        print("Не пугайтесь, это я воспроивожу результат.")
        playsound.playsound('output.mp3')
        print("Готово, результат сохранён в файле output.mp3")

test()

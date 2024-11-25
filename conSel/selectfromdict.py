import json
import os

# Загружаем файл с пресетами для языков и формируем список имён пресетов
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "langPresets.json")
with open(file_path, "r", encoding="utf-8") as f:
    presets = json.load(f)
havePresets = presets.keys()

wrongInput = "Incorrect input. Try again."
inputCustomValue = "Enter value: "
selectVariant = "Select an option: "
selfInput = "Enter manually"


def setCustomLang(text):
    global wrongInput, inputCustomValue, selectVariant, selfInput
    # example = {"wrongInput": "Неверный ввод. Попробуйте снова.", "inputCusValue": "Введите значение: ","selectVariant": "Выберите вариант: ", "selfInput": "Ввести самому"}
    if str(text).lower() in havePresets:
        wrongInput = presets[text.lower()]["wrongInput"]
        inputCustomValue = presets[text.lower()]["inputCusValue"]
        selectVariant = presets[text.lower()]["selectVariant"]
        selfInput = presets[text.lower()]["selfInput"]
    else:
        try:
            wrongInput = text["wrongInput"]
            inputCustomValue = text["inputCusValue"]
            selectVariant = text["selectVariant"]
            selfInput = text["selfInput"]
        except Exception as e:
            return e


def help():
    print("""
    RU: Идите на страницу https://github.com/Gengelenok/ConsoleSelect и прочитайте файл README.md.
    EN: Go to https://github.com/Gengelenok/ConsoleSelect and read the README.md file.""")


def choose(optionForSelect, allowSelfInput=False):
    print(selectVariant)
    for i, (name, numID) in enumerate(optionForSelect.items(), start=1):  # Выводим элементы словаря с нумерацией
        print(f"{i} - {name}")

    if allowSelfInput:  # Добавляем вариант для ввода вручную, если это разрешено
        print(f"{len(optionForSelect) + 1} - {selfInput}")

    # Получаем выбор пользователя
    choice = input(selectVariant)

    if choice.isdigit():  # Проверяем выбор пользователя
        choice = int(choice)
        if 1 <= choice <= len(optionForSelect):
            # Возвращаем id выбранного элемента
            selected_name = list(optionForSelect.keys())[choice - 1]
            return optionForSelect[selected_name]
        elif allowSelfInput and choice == len(optionForSelect) + 1:
            return input(inputCustomValue)
        else:
            print(wrongInput)
            return None
    else:
        print(wrongInput)
        return None

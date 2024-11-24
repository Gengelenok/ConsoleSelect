wrongInput = "Неверный ввод. Попробуйте снова."
inputCustomValue = "Введите значение: "
selectVariant = "Выберите вариант: "
selfInput = "Ввести самому"


def setCustomLang(text):
    global wrongInput, inputCustomValue, selectVariant, selfInput
    # example = {"wrongInput": "Неверный ввод. Попробуйте снова.", "inputCusValue": "Введите значение: ","selectVariant": "Выберите вариант: ", "selfInput": "Ввести самому"}
    wrongInput = text["wrongInput"]
    inputCustomValue = text["inputCusValue"]
    selectVariant = text["selectVariant"]
    selfInput = text["selfInput"]


def help():
    print("""----- Original text: -----
Библиотека для выбора в консоли (по словарю)
--Функции--:
- setCustomLang(text) - изменить текст при вызове choose_from_dict
вид параметра text = {"wrongInput": "текст при неправильном вводе",
"inputCusValue": "текст при выборе вариант 'ввести самому'",
"selectVariant": "текст сверху типа 'выберите вариант'",    
"selfInput": "текст для варианта "ввести самому""}

- choose(optionForSelect, allowSelfInput) - выбор из словаря optionForSelect.
Если allowSelfInput=True, то в консоли будет добавлен вариант для ввода самому.
По умолчанию False
вид параметра optionForSelect - {"value1": "dataForReturn1", "value2": "dataForReturn2"}

- help() - выводит это текст


----- English text (translated by ChatGPT): -----
A library for console selection (based on a dictionary)  
--Functions--:  
- setCustomLang(text) - changes the text displayed during the choose_from_dict function call.  
  Example parameter text:  
  {"wrongInput": "text displayed on incorrect input",
    "inputCusValue": "text displayed when choosing the 'enter manually' option",
    "selectVariant": "header text like 'select an option'",
    "selfInput": "text for the 'enter manually' option"}
 
- choose(optionForSelect, allowSelfInput) - allows selection from the optionForSelect dictionary.  
  If allowSelfInput=True, an option to manually enter a value will be added to the console.  
  Default is False.  
  Example parameter optionForSelect:  
  
  {"value1": "dataForReturn1", "value2": "dataForReturn2"}

- help() - displays this text.
""")


def choose(optionForSelect, allowSelfInput=False):
    for i, (name, id) in enumerate(optionForSelect.items(), start=1):  # Выводим элементы словаря с нумерацией
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

# if __name__ == "__main__":
#     options = {
#         "Первый вариант": 1,
#         "Второй вариант": 2,
#         "Третий вариант": 3,
#         "Четвертый вариант": 4,
#         "Пятый вариант": 5,
#         "Шестой вариант": 6,
#         "Седьмой вариант": 7,
#         "Восьмой вариант": 8,
#         "Девятый вариант": 9,
#         "Десятый вариант": 10}
#
#     print(choose_from_dict(options, allowSelfInput=True))

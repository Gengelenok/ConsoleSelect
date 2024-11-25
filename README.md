# Installing / Инсталляция

#### Install with pip / Установка через pip

```bash
pip install https://github.com/Gengelenok/ConsoleSelect/releases/latest/download/conSel-1.0-py3-none-any.whl
```

#### Import / Импорт

```python
import conSel as cs
```

---

# Guide

<!-- ## **Russian text:** _(original)_ -->

<details>
<summary><b>Russian text:</b> <i>(original)</i></summary>

### Библиотека для реализации выбора в консоли

#### Основные функции:

-   **`setCustomLang(text)`**  
    Позволяет настроить текстовые сообщения, отображаемые при использовании функции `choose(...)`.

    **Пример настройки параметра `text`:**

    ```json
    {
    	"wrongInput": "Сообщение при некорректном вводе",
    	"inputCusValue": "Сообщение при выборе варианта 'ввести самостоятельно'",
    	"selectVariant": "Сообщение, отображаемое над списком вариантов (например, 'выберите вариант')",
    	"selfInput": "Текст для варианта 'ввести самостоятельно'"
    }
    ```

    Также доступны предустановленные языковые настройки, которые находятся в файле `langPresets.json`. На данный момент поддерживаются только два языка: `ru` (русский) и `en` (английский). Вы можете добавить собственные языковые конфигурации, опираясь на существующие пресеты.  
    Чтобы использовать предустановленный язык, в параметр `text` нужно передать значение `"ru"`, `"en"` или имя созданного вами пресета.

---

-   **`choose(optionForSelect, allowSelfInput=False)`**  
    Отвечает за выбор одного из доступных вариантов из словаря `optionForSelect`.  
    Если параметр `allowSelfInput` установлен в `True`, то в консоли дополнительно появится возможность ввода произвольного значения. По умолчанию этот параметр равен `False`.

    **Пример параметра `optionForSelect`:**

    ```json
    {
    	"text1": "dataForReturn1",
    	"text2": "dataForReturn2"
    }
    ```

</details>

<details>
<summary><b>English text:</b> <i>(translated)</i></summary>

### Library for Console-Based Selection

#### Key Functions:

-   **`setCustomLang(text)`**  
    Allows customization of text messages displayed when using the `choose(...)` function.

    **Example configuration for the `text` parameter:**

    ```json
    {
    	"wrongInput": "Message displayed for invalid input",
    	"inputCusValue": "Message displayed when selecting the 'enter manually' option",
    	"selectVariant": "Message displayed above the list of options (e.g., 'select an option')",
    	"selfInput": "Text for the 'enter manually' option"
    }
    ```

    Predefined language settings are also available in the `langPresets.json` file. Currently, only two languages are supported: `ru` (Russian) and `en` (English). You can add your own language configurations based on the existing presets.  
    To use a predefined language, pass `"ru"`, `"en"`, or the name of your custom preset as the `text` parameter.

---

-   **`choose(optionForSelect, allowSelfInput=False)`**  
    Responsible for selecting one of the available options from the `optionForSelect` dictionary.  
    If the `allowSelfInput` parameter is set to `True`, an additional option to input a custom value will appear in the console. By default, this parameter is set to `False`.

    **Example configuration for the `optionForSelect` parameter:**

    ```json
    {
    	"text1": "dataForReturn1",
    	"text2": "dataForReturn2"
    }
    ```

</details>

<!--
## English text (translated): (NEED FIX!)

Library for creating a selection in the console

#### Functions:

-   `setCustomLang(text)` - changes the text displayed during the `choose(...)` function call. \_Example of text parameter:\*

    ```JSON
    {
    "wrongInput": "text displayed on incorrect input",
    "inputCusValue": "text displayed when choosing the 'enter manually' option'",
    "selectVariant": "header text like 'select an option'",
    "selfInput": "text for the 'enter manually' option"
    }
    ```

    Alternatively, you can use the templates from `langPresets.json`, which include only **ru** and **en**, but you can add your languages based on the already created presets. To use it, you need to pass the string `"ru"`, `"en"`, or one created by you to the `text` parameter.

-   `choose(optionForSelect, allowSelfInput)` - allows selection from the optionForSelect dictionary.
    If allowSelfInput=True, an option to manually enter a value will be added to the console, default is False.
    _Example of optionForSelect parameter:_

    ```JSON
    {
    "value1":"dataForReturn1",
    "value2":"dataForReturn2"
    }
    ``` -->

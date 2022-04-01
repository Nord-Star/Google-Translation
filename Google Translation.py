from tkinter import *
from tkinter import ttk
from googletrans import Translator


# Pop-up for the 'paste' menu
def do_popup(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()
        menu.entryconfigure('Paste',
                            command=lambda: input_lang_txt.event_generate('<<Paste>>'))


# Gets the source & dectination languages,
# changes the long language name to the short one,
# and translates the text.
def translated_txt():
    src = input_lang.get()
    dest = output_lang.get()
    for key, value in langs_dict.items():
        if src == value:
            src = key
        if dest == value:
            dest = key
    translator = Translator()
    a = translator.translate(text = input_lang_txt.get(1.0, END), src=src, dest=dest)
    output_lang_txt.delete(1.0, END)
    output_lang_txt.insert(1.0, a.text)


# Interface
root = Tk()
root.title('Google Translate')
root.iconbitmap('translate.ico')

# 'Paste' menu
menu = Menu(root, tearoff = 0)
menu.add_command(label='Paste')

# Frame with the program name
name_frame = LabelFrame(root, text = 'Google Translate', relief = RIDGE,
                        font = ('bold', 12))
name_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

# List of languages (short name : long name)
langs_dict = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
              'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque',
              'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
              'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
              'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
              'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish',
              'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
              'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
              'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek',
              'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa',
              'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi',
              'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo',
              'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese',
              'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer',
              'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
              'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
              'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy',
              'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori',
              'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)',
              'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto',
              'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
              'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan',
              'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona',
              'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian',
              'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili',
              'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu',
              'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu',
              'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh',
              'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

# Choose a source language
input_lang = ttk.Combobox(name_frame, values=list(langs_dict.values()))
input_lang.grid(row=1, column=0, sticky = E, padx = 5, pady = 5)
input_lang.current(21)

# Choose a destination language
output_lang = ttk.Combobox(name_frame, values=list(langs_dict.values()))
output_lang.grid(row=1, column=2, sticky = W, padx = 5, pady = 5)
output_lang.current(77)

# The area for the text in the source language.
input_lang_txt = Text(name_frame, height=30, width=70, wrap=WORD)
input_lang_txt.grid(row=2, column=0, padx = 5, pady = 5)
input_lang_txt.focus_set()
input_lang_txt.bind('<Button-3>', do_popup)

# Translate button
photo = PhotoImage(file = 'arrow.png')
btn = Button(name_frame, image=photo, command=translated_txt)
btn.grid(row=2, column=1, padx = 5, pady = 5)

# The area for the text in the destination language.
output_lang_txt = Text(name_frame, height=30, width=70, wrap=WORD)
output_lang_txt.grid(row=2, column=2, padx = 5, pady = 5)

root.mainloop()

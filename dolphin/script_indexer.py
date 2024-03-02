KNOWN_CLASS_NAMES = [
    'Toroste', 'Callback', 'TutorialPuzzle',
    'FavoliteWordList', 'MobDefine', 'CharaMenu',
    'FashionShow', 'Talkodekake', 'Talkcommon',
    'KuroController', 'Talksupport', 'DicDefine',
    'PierreTarot', 'Talkfriend', 'Talkpuzzle'
]


def index_script(script_contents):
    indexed_class_names = []

    for class_name in KNOWN_CLASS_NAMES:
        class_define_position = script_contents.find('t.' + class_name + '=')

        if class_define_position == -1:
            continue

        indexed_class_names.append({"class_name": class_name, "class_define_position": class_define_position})

    return {"indexed_class_names": indexed_class_names}

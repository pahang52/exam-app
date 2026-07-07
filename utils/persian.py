import arabic_reshaper
from bidi.algorithm import get_display


def fa(text):
    if text is None:
        return ""

    return get_display(
        arabic_reshaper.reshape(str(text))
    )

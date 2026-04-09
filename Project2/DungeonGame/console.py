def clear_console():
    print('\033c', end='')

text_bank = []
def save_text(text : str, purge : bool = False):
    text_bank.append(text)
    if purge:
        text_bank.clear()
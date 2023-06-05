from .interface import IGPTClient

def limit_num_words_to_context_windows_size(list_p: list, context_windows_size: int = 1000) -> str:
    return_str, word_count = '', 0
    for p in list_p:
        return_str += '\n'
        for word in p.split(' '):
            if word_count < context_windows_size:
                return_str += word + ' '
                word_count += 1
            else:
                break
    return return_str

def resume(gpt: IGPTClient, topic:str) -> str:
    all_search_text = gpt.epub.repo.search_str(str_to_find=topic)
    action = '--- Resume el texto anterior de manera clara en el idioma del texto'
    if all_search_text:
        resized_str = limit_num_words_to_context_windows_size(all_search_text)
        return gpt.send_message(resized_str + action)
    else:
        return gpt.send_message(topic + action)

def explain_text(gpt: IGPTClient,  text:str) -> str:
    all_search_text = gpt.epub.repo.search_str(str_to_find=text)
    action = '--- Explica el texto anterior de manera clara en el idioma del texto'
    if all_search_text:
        resized_str = limit_num_words_to_context_windows_size(all_search_text)
        return gpt.send_message(resized_str + action)
    else:
        return gpt.send_message(text + action)

def describe_own_name(gpt: IGPTClient, noun:str) -> str:
    if len(noun.split(' ')) > 4:
        raise Exception('El sustantivo propio debe tener menos de 4 palabras')
    
    all_search_text = gpt.epub.repo.search_str(str_to_find=noun)
    if all_search_text:
        resized_str = limit_num_words_to_context_windows_size(all_search_text)
        action = '--- Resume en una lista las caracteristicas de ' + noun + ' segun el texto anterior.'
        return gpt.send_message(resized_str + action)

def translate_text(gpt: IGPTClient, text:str, language:str) -> str:
    action = f'--- Traduce el texto anterior solamente, en el idioma {language}. La salida es el texto traducido y nada más.'
    return gpt.send_message(text + action)

def define_word(gpt: IGPTClient, word:str) -> str:
    if len(word.split(' ')) == 1:
        action = '--- Define formalmente la palabra anterior'
        return gpt.send_message(word + action)
    else:
        return 'Lo sentimos, no se puede definir más de una palabra. '
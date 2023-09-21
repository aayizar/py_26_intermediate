string = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt ipsam dolore reiciendis quae hic obcaecati accusamus sapiente maiores incidunt vero itaque numquam delectus eius cupiditate, ducimus praesentium sint omnis quia.'


def align_right(text:str, width:int):
    words = text.split(' ')
    answer = ''
    
    index = 0
    
    # Проходим по всем словам
    while index < len(words):
        # Здесь делим слова на строки по несколько слов до длины 30
        inner_word = []
        inner_len = 0
        while index < len(words):
            if inner_len + len(words[index]) > width:
                break
            inner_word.append(words[index])
            inner_len += len(words[index]) + 1
            index += 1

        # Добавляем пробелы
        word = " ".join(inner_word)
        answer += f"{' ' * (width - len(word))}{word}\n"
    
    print(answer[:-1])
    
  
align_right(string, 30)
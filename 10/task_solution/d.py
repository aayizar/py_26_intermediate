string = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nesciunt ipsam dolore reiciendis quae hic obcaecati accusamus sapiente maiores incidunt vero itaque numquam delectus eius cupiditate, ducimus praesentium sint omnis quia.'
length= 30


def justify(string:str, length:int):
    words = string.split(' ')
    answer = ''
    
    index = 0
    # Проходим по всем словам
    while index < len(words):
        # Здесь делим слова на строки по несколько слов до длины 30
        inner_word = []
        inner_len = 0
        while index < len(words):
            if inner_len + len(words[index]) > length:
                break
            inner_word.append(words[index])
            inner_len += len(words[index]) + 1
            index += 1
        
        # Здесь оканчиваем работу если это последнее слово
        if index == len(words) - 1:
            answer += words[index]
            break
        
        # Дальше идет логика с пробелами
        space_cnt = length - len(''.join(inner_word))
        word_count = len(inner_word) - 1
        
        spaces = [' ' * (space_cnt // word_count) for i in range(word_count)]
        
        for i in range(space_cnt % word_count):
            spaces[i] += ' '
        
        # Здесь объединяем пробелы со словами
        word = ''
        for i in range(len(spaces)):
            word += inner_word[i] + spaces[i]
        word += inner_word[-1] + "\n"
        answer += word
    
    print(answer)

justify('123 45 6', 7)
url = 'http://test.com/dir1/dir2/dir3/page.html'

def first_solution(url):
    slash_count = 0
    directories = []
    word = ''

    for symbol in url:
        if symbol == '/':
            if slash_count < 3:
                slash_count += 1
            else:
                directories.append(word)
                word = ''
                slash_count += 1
        elif slash_count > 2:
            word += symbol

    print(directories)
    
def second_solution(url: str):
    slash_count = 0
    index = 0
    for i, symbol in enumerate(url):
        if slash_count == 3:
            index = i
            break
        if symbol == '/':
            slash_count += 1
    
    print(url[index:].split('/')[:-1])

# second_solution(url)
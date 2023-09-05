

def save(callback):
    def save_function(path):
        try:
            callback(path)
        except Exception as e:
            print(e)
        
    return save_function


def read_text_file(path):
    try:
        f = open(path, 'r', encoding='utf8')
        for line in f.readlines():
            print(line, end='')
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except Exception as e:
        raise e


save(read_text_file('6/text.tx'))
print(1)
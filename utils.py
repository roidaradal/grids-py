import random, msvcrt

# Generate <count> random numbers from [0, limit)
def random_numbers(limit: int, count: int) -> list[int]:
    numbers: set[int] = set()
    while len(numbers) != count:
        numbers.add(random.randrange(limit))
    return list(numbers)

# Center text
def center(text: str, width: int) -> str: 
    extra = width - len(text)
    if extra <= 0: return text 
    right = extra // 2
    left = extra - right 
    return (' ' * left) + text + (' ' * right)

class Color:
    reset = '\033[0m'

    @classmethod 
    def red(cls, text: str) -> str:
        return '\033[31m%s%s' % (text, cls.reset)
    
    @classmethod 
    def redOnWhite(cls, text: str) -> str: 
        return '\033[31;47m%s%s' % (text, cls.reset)

    @classmethod 
    def green(cls, text: str) -> str:
        return '\033[32m%s%s' % (text, cls.reset)

    @classmethod 
    def yellow(cls, text: str) -> str:
        return '\033[33m%s%s' % (text, cls.reset)

    @classmethod 
    def blue(cls, text: str) -> str:
        return '\033[34m%s%s' % (text, cls.reset)

    @classmethod 
    def magenta(cls, text: str) -> str:
        return '\033[35m%s%s' % (text, cls.reset)

    @classmethod 
    def cyan(cls, text: str) -> str:
        return '\033[36m%s%s' % (text, cls.reset)
    
    @classmethod 
    def white(cls, text: str) -> str:
        return '\033[37m%s%s' % (text, cls.reset)
    
class Keyboard:
    @staticmethod
    def get_char() -> str:
        try: 
            return msvcrt.getch().decode('utf-8')
        except:
            return ''
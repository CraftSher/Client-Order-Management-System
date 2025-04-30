import random
import datetime

KARMA_TO_ACHIEVE = 500

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

def one_day():
    karma = random.randint(1, 7)
    if random.random() < 0.1:
        errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        raise random.choice(errors)()
    return karma


def main():
    total_karma = 0
    with open('karma.log', 'a', encoding= 'utf-8') as log_file:
        while True:
            try:
                total_karma += one_day()
                if total_karma >= KARMA_TO_ACHIEVE:
                    print("Достигнуто просветление! Карма:", total_karma)
                    break
            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp} - Произошло исключение: {type(e).__name__}\n")

if __name__ == "__main__":
    main()

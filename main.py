from colorama import Fore, Back, Style
import os
import time


class Main:
    def __init__(self):
        self.bullets = [0, 0]
        self.sorted_bullets = []

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        self.print_bullets()

    def print_logo(self):
        print(r'''
 ____             _        _           _     ____  _     _                
| __ ) _   _  ___| | _____| |__   ___ | |_  |  _ \(_) __| | ___  _ __ ___ 
|  _ \| | | |/ __| |/ / __| '_ \ / _ \| __| | |_) | |/ _` |/ _ \| '__/ __|
| |_) | |_| | (__|   <\__ \ | | | (_) | |_  |  __/| | (_| | (_) | |  \__ \
|____/ \__,_|\___|_|\_\___/_| |_|\___/ \__| |_|   |_|\__,_|\___/|_|  |___/
              ''')

    def print_bullets(self):
        print(f"| Боевых: {Fore.RED}{self.bullets[0]}{Style.RESET_ALL}\tХолостых: {Fore.GREEN}{self.bullets[1]}{Style.RESET_ALL}")
        combat_count = self.sorted_bullets.count(1)
        blank_count = self.sorted_bullets.count(0)
        unknown_count = self.sorted_bullets.count(None)
    
        if self.sorted_bullets and self.sorted_bullets[0] == None:
            combat_left = self.bullets[0] - combat_count
            blank_left = self.bullets[1] - blank_count
            combat_percent = round((combat_left / unknown_count) * 100) if combat_left > 0 else "?"
            blank_percent = round((blank_left / unknown_count) * 100) if blank_left > 0 else "?"
        elif self.sorted_bullets:
            combat_percent = "100" if self.sorted_bullets[0] == 1 else '0'
            blank_percent = "100" if self.sorted_bullets[0] == 0 else '0'
        else:
            combat_percent = "?"
            blank_percent = "?"

        print(f"| {Fore.RED}{combat_percent}%{Style.RESET_ALL}\t\t\t{Fore.GREEN}{blank_percent}%{Style.RESET_ALL}")        
        print(f"| {' '.join(f'{Fore.RED}Б{Style.RESET_ALL}' if x == 1 else f'{Fore.GREEN}Х{Style.RESET_ALL}' if x is not None else f'?' for x in self.sorted_bullets)}")    

    def input_bullets(self):
        self.clear()
        try:
            print('\nВведите число пуль (Б/Х)', end='')
            self.bullets = [int(x) for x in input("> ")]

            if len(self.bullets) != 2:
                self.bullets = [0, 0]
                self.input_bullets()

            self.sorted_bullets = [None] * sum(self.bullets)
            self.process_define_bullet()
        except ValueError:
            self.input_bullets()

    def process_define_bullet(self):
        combat_left = self.bullets[0] - self.sorted_bullets.count(1)
        blank_left = self.bullets[1] - self.sorted_bullets.count(0)
        if combat_left == 0:
            self.sorted_bullets = [0 if x is None else x for x in self.sorted_bullets]
        elif blank_left == 0: 
            self.sorted_bullets = [1 if x is None else x for x in self.sorted_bullets]

    def define_bullet(self):
        self.clear()
        try:
            print('\nВведите пулю (Номер/Пуля)', end='')
            bullet_data = [x for x in input("> ")]

            if not len(bullet_data):
                self.menu()

            if len(bullet_data) != 2:
                self.define_bullet()
            
            if int(bullet_data[0]) > sum(self.bullets):
                self.define_bullet()

            if bullet_data[1].lower() not in ['б', 'х']:
                self.define_bullet()

            self.sorted_bullets[int(bullet_data[0]) - 1] = 1 if bullet_data[1].lower() == 'б' else 0

            self.process_define_bullet()
            self.menu()
        except ValueError:
            self.define_bullet()
        except IndexError:
            self.define_bullet()

    def menu(self):
        self.clear()
        print('\n[1] Сброс\n[2] Определить')
        option = input('> ').lower()
        match option:
            case '1':
                self.__init__()
                self.start()

            case '2':
                self.clear()
                self.define_bullet()

            case _:
                if option not in ['б', 'х']:
                    self.menu()

                if option == 'б':
                    self.bullets[0] -= 1 if self.bullets[0] > 0 else 0
                else:
                    self.bullets[1] -= 1 if self.bullets[1] > 0 else 0
            
                self.sorted_bullets.pop(0)
                self.process_define_bullet()

                if sum(self.bullets) == 0:
                    self.__init__()
                    self.start()
                    
                self.menu()
            
    def start(self):
        self.clear()
        self.input_bullets()
        self.menu()


if __name__ == '__main__':
    main = Main()
    main.start()

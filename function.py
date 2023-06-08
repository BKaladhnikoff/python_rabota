# Калашников Богдан Дмитриевич,группа 44-22-117,Вариант 6

import argparse
import unittest
import math
import sys
import PySimpleGUI as pysimplegui


class TestCalculate(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(round(function(0), 3), 0.000)
        self.assertEqual(round(function(14), 3), 0.470)
        self.assertEqual(round(function(56), 3), 0.503)
        self.assertEqual(round(function(78), 3), 0.506)
        self.assertIsNone(function("STRING"))
        self.assertIsNone(function(None))


def function(number):
    try:
        x = float(number)
        return (
            x * math.sin(x**3)**2
            if x < math.pi / 2
            else math.log(math.atan(x) + 0.1)
        )
    except Exception as e:
        print(f"Невозможно вычислить функцию для входного значения {number}; Ошибка: {e}")
        return None
    

def run_interface():
    layout = [
        [pysimplegui.Text("Перечислите числа через точку с запятой (;)")],
        [pysimplegui.Input(enable_events=True, key="-INPUT-")],
        [pysimplegui.Button("Запуск программы")],
        [pysimplegui.Listbox(values=[], enable_events=True, key="-LISTBOX-", size=(100, 24))]
    ]

    window = pysimplegui.Window("Расчет функций", layout, font=("Arial, 10"))

    while True:
        event, values = window.read()
        if event == "Запуск программы":
            numbers = values['-INPUT-'].strip().split(";")
            results = [function(argument) for argument in numbers]
            for i in range(len(results)):
                if results[i] is None:
                    results[i] = f"Функция не может быть вычислена при входном значении {numbers[i]}"
                else:
                    results[i] = f"Функция от {numbers[i]} = {results[i]:.4f}"
            window["-LISTBOX-"].update(results)
        if event == pysimplegui.WIN_CLOSED:
            break

    window.close()
    sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="*", help="Входные числа")
    parser.add_argument("--mode", "-m", type=str, default="console", help="Режим запуска: console, gui, test")
    arguments = parser.parse_args()

    if not len(arguments.numbers) and arguments.mode == "console":
        print("Для запуска в режиме консоли требуются входные числа")
        sys.exit()

    if arguments.mode == "console":
        for input_number in arguments.numbers:
            print(f"Функция от {input_number} равна {function(input_number)}")
    elif arguments.mode == "test":
        print("Запускаю тесты")
        print(TestCalculate("test_equal").run())
    elif arguments.mode == "gui":
        run_interface()
    else:
        print(f"Некорректный режим запуска: {arguments.mode}; Доступные варианты: console, gui, tests")

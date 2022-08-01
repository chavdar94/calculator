from kivy.app import App
from kivy.uix.widget import Widget
# Uncomment for PC app
# from kivy.core.window import Window
from kivy.lang import Builder
import re

Builder.load_file('calculator.kv')


# Uncomment for PC app
# Window.size = (350, 550)

# Creating the calculator window
class CalculatorWidget(Widget):

    # clearing the result text box ('C' button)
    def clear(self):
        self.ids.input_box.text = "0"

    # Writing out the numbers in the text box
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if '.' not in prev_number:
            res = re.split(r'(\D)', prev_number)
            empty_list = []
            for i in res:
                i = i.lstrip('0')
                empty_list.append(i)
                prev_number = ''.join(empty_list)

        # Checks if user tried to divide by 0
        if "Can't divide by 0" in prev_number:
            prev_number = ""

        # If the first number starts with 0 it is replaced by the next number
        if prev_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # ('/','*','-','+','%') button functions
    def signs(self, sign):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f'{prev_number}{sign}'

    # deletes the last number
    def remove_last_sign(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = f"{prev_number}"

    # Calculating the result with eval() unless '%' is used
    def results(self):
        prev_number = self.ids.input_box.text
        try:
            if '%' in self.ids.input_box.text:
                idx = prev_number.index('%')
                left = prev_number[:idx]
                right = prev_number[idx + 1:]
                result = (float(left) * float(right)) / 100
                self.ids.input_box.text = str(result)
            else:
                result = eval(prev_number)
                self.ids.input_box.text = str(result)
        except ZeroDivisionError:
            self.ids.input_box.text = "Can't divide by 0"

    # Leading '-' if you want the first number to be a negative, else positive
    def positive_negative(self):
        prev_number = self.ids.input_box.text

        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"

    # Using '.' for floating numbers
    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number)

        if ('+' in prev_number
            or '-' in prev_number
            or '*' in prev_number
            or '/' in prev_number
            or '%' in prev_number) \
                and '.' not in num_list[-1]:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass
        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number


# Building the app
class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


# Running the app
if __name__ == "__main__":
    CalculatorApp().run()

from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934

class Convert_to_Miles(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('ConvertertoMiles.kv')
        return self.root

    def calculate_conversion(self):
        value = self.mile_test()
        result = value * CONVERSION
        self.root.ids.output_label.text = str(result)

    def increment(self, change):
        value = self.mile_test() + change
        self.root.ids.input_miles.text = str(value)
        self.calculate_conversion()

    def mile_test(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

Convert_to_Miles().run()


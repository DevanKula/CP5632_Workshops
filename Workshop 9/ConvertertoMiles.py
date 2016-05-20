from kivy.app import App
from kivy.lang import Builder


class ConverttoMiles(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('ConvertertoMiles.kv')
        return self.root

ConverttoMiles().run()


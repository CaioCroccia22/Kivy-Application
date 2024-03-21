from kivy.app import App #Todo aplicativo Kivy precisa da subclasse App e da função build()
from kivy.uix.label import Label

class MainApp(App):
    def build(self): #Nesse caso foi criado um widget do tipo label e passado como parâmetro: text, size_hint e pos_hint
        label= Label(text="Olá mundo",
        size_hint=(0.5, 0.5),
        pos_hint={'center_x': .5, 'center_y': .5})

        return label 
if __name__ == '__main__':
    app = MainApp()
    app.run()
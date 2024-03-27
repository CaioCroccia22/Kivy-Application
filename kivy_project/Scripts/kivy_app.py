from kivy.app import App
from kivy.uix.label import Label
# Perceba que todo aplicativo Kivy 
# precisa da subclasseApp e da 
# função build(). 
# É aqui que você colocará seu código de 
# interface dousuário ou fará chamadas
# para outras funções quedefinem seu 
# código de interface do usuário

class MainApp(App):
    def build(self):
        # Neste caso, crie um widget do
        # tipo label e passe como parâmetro: 
        # text, size_hint, e pos_hint (estes dois últimosargumentos não são obrigatórios).

        label= Label(text="Olá mundo",
        size_hint=(0.5, 0.5),
        # O comando size_hint informa ao Kivy as proporções a
        # serem usadas ao criar o widget
        pos_hint={'center_x': .5, 'center_y': .5})
        # Para isso são necessários dois números:O primeiro número (x): 
        # refere-se à largura do controle.O segundo número (y): 
        # refere-se à altura do controle.
        return label 
if __name__ == '__main__':
    app = MainApp()
    app.run()
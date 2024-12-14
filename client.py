import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests

class ClientApp(App):
    def build(self):
        self.server_url = "http://127.0.0.1:5000/api/messages"
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="Enter your message:")
        self.layout.add_widget(self.label)
        
        self.text_input = TextInput(hint_text='Message', multiline=False)
        self.layout.add_widget(self.text_input)
        
        self.send_button = Button(text="Send Message", on_release=self.send_message)
        self.layout.add_widget(self.send_button)
        
        self.retrieve_button = Button(text="Retrieve Messages", on_release=self.retrieve_messages)
        self.layout.add_widget(self.retrieve_button)
        
        self.message_display = Label(text="")
        self.layout.add_widget(self.message_display)
        
        return self.layout

    def send_message(self, instance):
        message = self.text_input.text
        if message:
            response = requests.post(self.server_url, json={"message": message})
            if response.status_code == 200:
                self.text_input.text = ""
                self.message_display.text = "Message sent successfully!"
            else:
                self.message_display.text = "Failed to send message."

    def retrieve_messages(self, instance):
        response = requests.get(self.server_url)
        if response.status_code == 200:
            messages = response.json()
            self.message_display.text = "Messages:\n" + "\n".join(messages)
        else:
            self.message_display.text = "Failed to retrieve messages."

if __name__ == "__main__":
    ClientApp().run()

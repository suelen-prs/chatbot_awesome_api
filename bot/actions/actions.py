# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "moeda_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        moeda = tracker.get_slot("moeda")
        url = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/1'

        json_data = requests.get(url).json()
        nome_moeda = json_data[0].get('name')
        valor_moeda_real = json_data[0].get('bid')

        nome_oficial = nome_moeda.split('/')

        print(nome_moeda)

        resp_valor = f'1 {nome_oficial[0]} equivale a R$ {valor_moeda_real} {nome_oficial[1]} hoje.'

        dispatcher.utter_message(text=resp_valor)

        return [SlotSet("moeda", url)]

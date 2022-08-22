# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa.event import SlotSet
from rasa_sdk.executor import CollectingDispatcher

# Weather Api
# !pip install pyowm
from pyowm import OWM

key = "a5427ae5b5659c6836283c611b161f96"

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        area = tracker.get_slot("area")
        owm = OWM(key)
        mgr = owm.weather_manager()
        
        observation = mgr.weather_at_place(area)
        w = observation.weather

        msg1 = f"Cuaca di {area} ialah : "
        msg2 = f"Suhu ialah (Celcius) : {w.temperature('celcius')['temp']}"
        msg3 = f"Kelajuan Angin ialah : {w.wind()['speed']} Km/h"
        msg4 = f"kelembapan di {area} ialah : {w.humidity} %"
        msg5 = f"status cuaca keseluruhan ialah :{w.detailed_status}."

        message = msg1 + "/n"+ msg2 + "/n" + msg3 + "/n"+ msg4 + "/n" + msg5 
        dispatcher.utter_message(text = message)

        return []

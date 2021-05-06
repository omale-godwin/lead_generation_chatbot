# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType


class validateRestuarantForm(Action):

    def name(self) -> Text:
        return "lead_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:
            require_slot = ["description", "timeline", "amount", "name", "email", "phone"]

            for slot_name in require_slot:
                if tracker.slots.get(slot_name) is None:
                    return [SlotSet("requested_slot", slot_name)]
                    

            return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    
    def run(
        self,
        dispatcher,
        tracker:Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_feedback_form_data",
        description=tracker.get_slot("description"),
        amount= tracker.get_slot("amount"),
        timeline= tracker.get_slot("timeline"),  name= tracker.get_slot("name"),
        email= tracker.get_slot("email"),  phone= tracker.get_slot("phone"),)


class ActionLogic(Action):
    def name(self) -> Text:
        return "custom_response"
    def run(self, dispatcher, tracker, domain):
        service = tracker.get_slot('service')
        if service == 'web':
            dispatcher.utter_message(text="Great. We have developed more than 20+ web applications till date!")
        elif service == 'mobile':
            dispatcher.utter_message(text="Great. We have developed more than 20+ andriod and ios applications till date!")
        elif service == 'machine':
            dispatcher.utter_message(text="Great. We have developed serveral artificial intelligent and machine learing program for different use case till date!")
        elif service == 'Frontend':
            dispatcher.utter_message(text="Great. We have developed react, vue, and angular frontend applications servicing more than 30+ client till date!")
        elif service == 'devops':
            dispatcher.utter_message(text="Great. We have orcerstrate the organisation scaling and deployment of more than 20+  applications till date!")
        else:
            dispatcher.utter_message(text="Great. We have developed serveral application more than 20+ till date!")
        return []
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import subprocess
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction
class ActionValidateCredentials(Action):
    def name(self) -> str:
        return "action_validate_credentials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global username
        global password
        username = tracker.get_slot("username")
        password = tracker.get_slot("password")
        print(username)
        print(password)
        aws_access_key_id=""
        aws_secret_access_key=""
        try:
            subprocess.run(["C:\\Program Files\\Amazon\\AWSCLIV2\\aws.exe", "configure", "set", aws_access_key_id, username], check=True)
            subprocess.run(["C:\\Program Files\\Amazon\\AWSCLIV2\\aws.exe", "configure", "set", aws_secret_access_key, password], check=True)
            subprocess.run(["C:\\Program Files\\Amazon\\AWSCLIV2\\aws.exe", "configure", "set", "region", "us-east-1"], check=True)
            #subprocess.run(["aws", "configure", "set", "output", "json"], check=True)

            dispatcher.utter_message(text="✅ AWS credentials configured successfully.")
        except Exception as e:
            dispatcher.utter_message(text=f"❌ Failed to configure AWS: {str(e)}")
            print(f"Error in action_aws_login: {e}")

        return []
#**********************************SERVICES***********************************

# def run_aws_cli_command(command: List[str]) -> str:
#     try:
#         result = subprocess.run(command, capture_output=True, text=True, check=True)
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         return f"Failed to execute command: {e}"

# class ActionListS3(Action):

#     def name(self) -> Text:
#         return "action_list_s3"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         output = run_aws_cli_command(["aws", "s3", "ls"])
#         dispatcher.utter_message(text=f"S3 Buckets:\n{output}")
#         return []

# class ActionListRDS(Action):

#     def name(self) -> Text:
#         return "action_list_rds"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         output = run_aws_cli_command(["aws", "rds", "describe-db-instances"])
#         dispatcher.utter_message(text=f"RDS Instances:\n{output}")
#         return []

# class ActionListECS(Action):

#     def name(self) -> Text:
#         return "action_list_ecs"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         output = run_aws_cli_command(["aws", "ecs", "list-clusters"])
#         dispatcher.utter_message(text=f"ECS Clusters:\n{output}")
#         return []

# class ActionListLambda(Action):

#     def name(self) -> Text:
#         return "action_list_lambda"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         output = run_aws_cli_command(["aws", "lambda", "list-functions"])
#         dispatcher.utter_message(text=f"Lambda Functions:\n{output}")
#         return []
#     # from typing import Dict, Text, Any, List

# # from rasa_sdk import Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # from rasa_sdk.forms import FormValidationAction

# # # Dummy user database
# # USER_DB = {
# #     "alice": "password123",
# #     "bob": "secure456"
# # }

# # class ValidateCredentialForm(FormValidationAction):
# #     def name(self) -> Text:
# #         return "validate_credential_form"

# #     def validate_username(
# #         self,
# #         slot_value: Any,
# #         dispatcher: CollectingDispatcher,
# #         tracker: Tracker,
# #         domain: Dict
# #     ) -> Dict[Text, Any]:
# #         if slot_value.lower() in USER_DB:
# #             return {"username": slot_value}
# #         dispatcher.utter_message(text="Username not found.")
# #         return {"username": None}

# #     def validate_password(
# #         self,
# #         slot_value: Any,
# #         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict
#     ) -> Dict[Text, Any]:
#         username = tracker.get_slot("username")
#         if username and USER_DB.get(username.lower()) == slot_value:
#             return {"password": slot_value}
#         dispatcher.utter_message(text="Incorrect password.")
#         return {"password": None}

import urllib2
import json
import dbb

def lambda_handler(event, context):
    if (event["session"]["application"]["applicationId"] !=
            "amzn1.ask.skill.cf2f3d20-045e-4e8a-ac06-cea574333e12"):
        raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def on_session_started(session_started_request, session):
    print "Starting new session."

def on_launch(launch_request, session):
    return get_welcome_response()




def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "GetTitle":
        return get_title(intent)
    elif intent_name == "GetTime":
        return get_time(intent)
    elif intent_name == "GetWho":
        return get_who(intent)
    elif intent_name =="GetSeats":
        return get_seats(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...

def handle_session_end_request():
    card_title = "Thomas - Thanks"
    speech_output = "Thank you for using the Thomas skill.  See you next time!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

def get_welcome_response():
    session_attributes = {}
    card_title = "Thomas Scheduling"
    speech_output = "Welcome to the Alexa Thomas Scheduling skill. " \
                    "You can ask me four questions stated in PA6."
    reprompt_text = "Please ask me only the four questions in PA6."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_title(intent):
    session_attributes = {}
    card_title = "Course Title"
    reprompt_text = ""
    should_end_session = False
    cn=intent["slots"]["coursenum"]["value"]
    speech_output = dbb.accessDatabase(str(cn),4)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_time(intent):
    session_attributes = {}
    card_title = "Course Time"
    reprompt_text = ""
    should_end_session = False

    cn=intent["slots"]["coursenum"]["value"]
    speech_output = dbb.accessDatabase(str(cn),2)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_who(intent):
    session_attributes = {}
    card_title = "Course Instructor"
    reprompt_text = ""
    should_end_session = False
    cn=intent["slots"]["coursenum"]["value"]
    speech_output = dbb.accessDatabase(str(cn),3)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def get_seats(intent):
    session_attributes = {}
    card_title = "Course Time"
    reprompt_text = ""
    should_end_session = False
    cn=intent["slots"]["coursenum"]["value"]
    speech_output = dbb.accessDatabase(str(cn),4)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }

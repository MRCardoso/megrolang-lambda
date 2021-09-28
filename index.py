################### Install specific version
## pip install googletrans==3.1.0a0
## https://wakeupcoders.medium.com/how-to-use-external-libraries-in-lambda-function-df1cee4a7c3a
###################
import json
from googletrans import Translator
from Validator import Validator

def handler(event, context):
    errorList = []
    successList = {}
    
    for item in event["phrases"]:
        validator = Validator({
            "text": "required",
            "origin": "required",
            "trans": "required"
        }, item)
            
        if not(validator.validate()):
            for err in validator.getErrors():
                errorList.append(err)
            continue
        
        translator = Translator(service_urls=['translate.googleapis.com'])
        result = translator.translate(item["text"], src=item["origin"],  dest=item["trans"])
        
        successList[item["text"]] = result.text
     
    state = [200, successList]  
    
    if len(errorList):
        state = [400, errorList]
    
    return {
        "statusCode": state[0],
        "body": state[1]
    }

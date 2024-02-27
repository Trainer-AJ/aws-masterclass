# DISCLAIMER : Fpr Devs ONLY 

# DFINR
# def ask_instance_id():
#     ID = input("Please enter EC2 Instance ID [ONLY one]: ")
#     REGION = input("Pls enter aws region: ")
#     #print(f"Your Input is: {ID} and {REGION} ")
#     return [ID,REGION]

# # Calling
# # print(ask_instance_id())

# # ------------------------------------------------------- LAMBDA -------------------------------

# def lambda_handler(event,context):
#     # DO somwting
#     return some_value

# # The first argument is the event object. An event is a 
# # JSON-formatted document that contains data for a Lambda function to process.
# #  The Lambda runtime converts the event to an object and passes it to your 
# # function code. It is usually of the Python dict type. It can also be list, str, int, float, or the NoneType type.
# # aws service ytype defines event type

event = {
    "year": 2000
}

def lambda_handler(event,context):
    # print(event["year"])
    DOY = event["year"]
    AGE = 2024 - DOY
    print("***********************************************")
    print(f"Your Age is {AGE}")
    print("***********************************************")

lambda_handler(event,context=[])

# returning value = https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html#python-handler-return

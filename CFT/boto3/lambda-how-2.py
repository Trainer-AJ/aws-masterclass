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
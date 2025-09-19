import requests
import msal
import json
import csv
import os
import boto3
import io
from urllib.parse import quote


# Global variables
CLIENT_ID = None
CLIENT_SECRET = None
TENANT_ID = None

def get_azure_credentials():
    global CLIENT_ID, CLIENT_SECRET, TENANT_ID
    
    secret_name = os.environ.get("secret_name")
    region_name = os.environ.get("region_name")

    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        # Retrieve the secret value
        response = client.get_secret_value(SecretId=secret_name)
        secret_string = response["SecretString"]
        secret_dict = json.loads(secret_string)

        # Extract individual values
        CLIENT_ID = secret_dict["CLIENT_ID"]
        CLIENT_SECRET = secret_dict["CLIENT_SECRET"]
        TENANT_ID = secret_dict["TENANT_ID"]

        return CLIENT_ID, CLIENT_SECRET, TENANT_ID

    except Exception as e:
        print(f"Error retrieving secret: {e}")
        return None, None, None
 
 
# The static list of user emails to check
USERS_TO_CHECK = [
    "user1@gmail.com",
    "kalwapalli.vishal@gmail.com"
]
 
# NEW: Define the email addresses of managers where the search should stop.
# This list should now contain values from the 'mail' attribute.
TOP_MANAGERS_EMAILS = [
    "manager3@gmail.com" ,
    "raj@gmail.com"
]

# Get credentials at module import time
CLIENT_ID, CLIENT_SECRET, TENANT_ID = get_azure_credentials()

# Microsoft Graph API endpoint
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"
AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]
 
def get_access_token():
    """Acquires an access token from Microsoft Entra ID."""
    app = msal.ConfidentialClientApplication(
        client_id=CLIENT_ID,
        authority=AUTHORITY_URL,
        client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=SCOPES)
    if "access_token" not in result:
        print("Error acquiring token. Check credentials and permissions.")
        print(result.get("error_description"))
        return None
    return result['access_token']
 
def find_designated_manager(user_email, headers, stop_at_managers):
    """
    Finds a user by email and traverses their management chain, returning
    the displayName and mail of the first manager in the 'stop_at_managers' list.
    """
    encoded_email = quote(user_email)
    search_url = f"{GRAPH_API_ENDPOINT}/users?$filter=mail eq '{encoded_email}'"
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        users = response.json().get('value')
        if not users:
            print(f"Warning: User with email '{user_email}' not found.")
            return None
        user_id = users[0]['id']
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error finding user {user_email}: {e}")
        return None
 
    next_manager_url = f"{GRAPH_API_ENDPOINT}/users/{user_id}/manager"
 
    while next_manager_url:
        try:
            response = requests.get(next_manager_url, headers=headers)
            response.raise_for_status()
            manager_data = response.json()
            manager_email = manager_data.get("mail")
 
            if manager_email in stop_at_managers:
                print(f"Success: Found designated manager '{manager_email}' for {user_email}.")
                return {
                    "displayName": manager_data.get("displayName"),
                    "mail": manager_email
                }
 
            manager_id = manager_data.get("id")
            next_manager_url = f"{GRAPH_API_ENDPOINT}/users/{manager_id}/manager"
 
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Reached top of hierarchy for {user_email} without finding a designated manager.")
            else:
                print(f"HTTP Error during manager lookup for {user_email}: {e}")
            break
 
    return None


def save_to_csv_s3(data):
    """
    Saves the final data to a CSV file and uploads it to an S3 bucket using environment variables.
    """

    if not data:
        print("No data to save to CSV.")
        return

    # Read environment variables
    bucket_name = os.environ.get("S3_BUCKET_NAME")
    object_key = os.environ.get("S3_OBJECT_KEY", "reports/manager.csv")

    if not bucket_name:
        print("S3_BUCKET_NAME environment variable is not set.")
        return

    # Define CSV headers
    headers = ["User Email", "Manager Display Name", "Manager Email", "Count"]

    # Create in-memory CSV
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(headers)

    for user_email, manager_info in data.items():
        writer.writerow([
            user_email,
            manager_info.get("displayName", ""),
            manager_info.get("mail", ""),
            manager_info.get("count", 0)
        ])

    # Upload to S3
    s3_client = boto3.client("s3")
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        print(f"✅ Successfully uploaded report to S3: s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"❌ Error uploading to S3: {e}")

    """
    Saves the final data to a CSV file and uploads it to an S3 bucket using environment variables.
    """
    if not data:
        print("No data to save to CSV.")
        return

    # Read environment variables
    bucket_name = os.environ.get("S3_BUCKET_NAME")
    object_key = os.environ.get("S3_OBJECT_KEY")  # This replaces 'filename'
    filename = object_key

    if not bucket_name or not object_key:
        print("Missing environment variables: S3_BUCKET_NAME or S3_OBJECT_KEY.")
        return

    headers = ["User Email", "Manager Display Name", "Manager Email", "Count"]

    # Create in-memory CSV
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(headers)

    for user_email, manager_info in data.items():
        writer.writerow([
            user_email,
            manager_info.get("displayName"),
            manager_info.get("mail"),
            manager_info.get("count")
        ])

    # Upload to S3
    s3_client = boto3.client("s3")
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        print(f"Successfully uploaded report to S3: s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

    """
    Saves the final data to a CSV file and uploads it to an S3 bucket using environment variables.
    """
    if not data:
        print("No data to save to CSV.")
        return

    # Read environment variables
    bucket_name = os.environ.get("S3_BUCKET_NAME")
    object_key = os.environ.get("S3_OBJECT_KEY", "manager_report.csv")

    if not bucket_name:
        print("S3_BUCKET_NAME environment variable is not set.")
        return

    headers = ["User Email", "Manager Display Name", "Manager Email", "Count"]

    # Create in-memory CSV
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(headers)

    for user_email, manager_info in data.items():
        writer.writerow([
            user_email,
            manager_info.get("displayName"),
            manager_info.get("mail"),
            manager_info.get("count")
        ])

    # Upload to S3
    s3_client = boto3.client("s3")
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        print(f"Successfully uploaded report to S3: s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

    """
    Saves the final data to a CSV file and uploads it to an S3 bucket.

    Args:
        data (dict): The dictionary containing the processed user and manager data.
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key (filename) for the object in S3.
    """
    if not data:
        print("No data to save to CSV.")
        return

    headers = ["User Email", "Manager Display Name", "Manager Email", "Count"]

    # Create in-memory CSV
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(headers)

    for user_email, manager_info in data.items():
        writer.writerow([
            user_email,
            manager_info.get("displayName"),
            manager_info.get("mail"),
            manager_info.get("count")
        ])

    # Upload to S3
    s3_client = boto3.client("s3")
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        print(f"Successfully uploaded report to S3: s3://{bucket_name}/{object_key}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

    """
    Saves the final data to a CSV file.
 
    Args:
        data (dict): The dictionary containing the processed user and manager data.
        filename (str): The name of the output CSV file.
    """
    if not data:
        print("No data to save to CSV.")
        return
 
    # Define the headers for the CSV file
    headers = ["User Email", "Manager Display Name", "Manager Email", "Count"]
 
    try:
        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            
            # Write the data rows
            for user_email, manager_info in data.items():
                writer.writerow([
                    user_email,
                    manager_info.get("displayName"),
                    manager_info.get("mail"),
                    manager_info.get("count")
                ])
        
        # Print a confirmation message with the absolute path to the file
        print(f"\nSuccessfully saved report to: {os.path.abspath(filename)}")
 
    except IOError as e:
        print(f"Error writing to CSV file: {e}")
 
 
def main():
    """Main function to orchestrate the process and save the output."""
    access_token = get_access_token()
    if not access_token:
        return
 
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
 
    all_top_managers = {}
    manager_counts = {}
 
    for email in USERS_TO_CHECK:
        print(f"\nProcessing user with email: {email}")
        top_manager_details = find_designated_manager(email, headers, TOP_MANAGERS_EMAILS)
        
        if top_manager_details:
            all_top_managers[email] = top_manager_details
            manager_email = top_manager_details['mail']
            manager_counts[manager_email] = manager_counts.get(manager_email, 0) + 1
 
    for user_email, manager_info in all_top_managers.items():
        manager_email = manager_info['mail']
        manager_info['count'] = manager_counts.get(manager_email)
 
    print("\n--- Final Results ---")
    # You can still print the JSON to the console if you like
    print(json.dumps(all_top_managers, indent=4))
    
    # MODIFIED: Call the new function to save the results to a CSV file
    save_to_csv_s3(all_top_managers)
 
# if __name__ == "__main__":
#     main()

def lambda_handler(event, context):
    main()
 

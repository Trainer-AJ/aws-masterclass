#################################
# Doc link: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html
####################################

import datetime
import hashlib
import hmac
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning

def create_headers(method, endpoint, service, host, region, access_key, secret_key):
    # Get the current time in UTC using the recommended approach
    t = datetime.datetime.now(datetime.timezone.utc)
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d')

    # Create the canonical request
    canonical_uri = endpoint
    canonical_querystring = ''
    
    # Include both 'x-amz-date' and 'x-amz-content-sha256' in the canonical headers
    canonical_headers = f'host:{host}\n' + f'x-amz-date:{amzdate}\n'
    signed_headers = 'host;x-amz-date'  # include both 'host' and 'x-amz-date' in the signed headers
    
    # For GET requests, use an empty payload (or 'UNSIGNED-PAYLOAD' if needed)
    payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()

    # Construct the canonical request
    canonical_request = (method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n'
                         + canonical_headers + '\n' + signed_headers + '\n' + payload_hash)

    print("Canonical Request:\n", canonical_request)  # Log the canonical request for debugging

    # Create the string to sign
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = f'{datestamp}/{region}/{service}/aws4_request'
    string_to_sign = (algorithm + '\n' + amzdate + '\n' + credential_scope + '\n' +
                      hashlib.sha256(canonical_request.encode('utf-8')).hexdigest())

    print("String to Sign:\n", string_to_sign)  # Log the string to sign for debugging

    # Sign the string
    signing_key = getSignatureKey(secret_key, datestamp, region, service)
    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    print("Signature:\n", signature)  # Log the signature for debugging

    # Add signing information to the request
    authorization_header = (f'{algorithm} Credential={access_key}/{credential_scope}, '
                            f'SignedHeaders={signed_headers}, Signature={signature}')
 
    headers = {
        'Host': host,
        #'x-amz-content-sha256':'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'x-amz-content-sha256': payload_hash, 
        'x-amz-date': amzdate,
        'Authorization': authorization_header
    }
# The x-amz-content-sha256 header is required for Amazon S3 AWS requests.
#    It provides a hash of the request payload.
#    If there is no payload, you must provide the hash of an empty string.

    return headers, amzdate

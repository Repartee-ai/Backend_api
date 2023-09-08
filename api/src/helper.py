from ..models import *
from ..serializers import *
from datetime import timedelta
from django.utils import timezone
import requests
from django.core.exceptions import ObjectDoesNotExist

def get_external_api_token(user):
    try:
        # Define the API endpoint and the payload
        url = "https://edgesphereszsciit.com/v3-public/localProviders/local?action=login"
        payload = {
            "username": user.email, # Assuming username is the email of the user
            "password": user.password, # You should store passwords securely (hashed) and not in plain text
        }
        # Send the POST request
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            # Extract the token from the Set-Cookie header
            cookies = response.headers.get('Set-Cookie')
            if cookies:
                token = cookies.split(';')[0].split('=')[1]
                return token
        else:
            # Handle unsuccessful response (you might want to log this)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def start_instance(user, spec, cluster_id):
    unique_data = {
        'user_id': user,
        'vm_name': spec.get("name"),
        'vm_namespace': spec.get("namespace"),
    }
    try:
        # Find the price from the Pricing table using the cluster_id
        pricing_obj = Pricing.objects.get(cluster_id=cluster_id)
        price = pricing_obj.price
    except ObjectDoesNotExist:
        price=1.0
        print(f"No pricing information found for cluster_id: {cluster_id}, using defualt value 1")
        # return False

    # Default values for creation
    defaults = {
        'status': "started",
        'start_time': timezone.now(),
        'cluster': cluster_id,
        'usage': 0.0,
        'price': price,
        }

    # Merging two dictionaries
    data = {**unique_data, **defaults}

    # Creating an instance with the merged data
    instance = Instance.objects.create(**data)
    
    return True


def update_instance(instance, action):
    instance.status = action
    stop_time = timezone.now()
    instance.usage += (stop_time - instance.start_time).total_seconds() / 60 # Convert seconds to mins
    if action == 'terminated':
        instance.stop_time = stop_time
    instance.save()

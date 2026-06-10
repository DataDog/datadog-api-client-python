"""
Delete a form returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi

# there is a valid "form" in the system
FORM_DATA_ID = environ["FORM_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.delete_form(
        form_id=FORM_DATA_ID,
    )

    print(response)

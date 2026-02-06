"""
Delete a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["delete_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    api_instance.delete_form(
        form_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

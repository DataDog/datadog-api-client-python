"""
Cancel downtimes by scope returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.downtimes_api import DowntimesApi
from datadog_api_client.v1.model.cancel_downtimes_by_scope_request import CancelDowntimesByScopeRequest

# there is a valid "downtime" in the system
DOWNTIME_SCOPE_0 = environ["DOWNTIME_SCOPE_0"]

body = CancelDowntimesByScopeRequest(
    scope=DOWNTIME_SCOPE_0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.cancel_downtimes_by_scope(body=body)

    print(response)

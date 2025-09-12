"""
Delete incident notification rule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "notification_rule" in the system
NOTIFICATION_RULE_DATA_ID = environ["NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_notification_rule(
        id=NOTIFICATION_RULE_DATA_ID,
    )

"""
Create a status page email subscription returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_statuspage_subscription_data_attributes_request import (
    IncidentStatuspageSubscriptionDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_statuspage_subscription_data_request import (
    IncidentStatuspageSubscriptionDataRequest,
)
from datadog_api_client.v2.model.incident_statuspage_subscription_request import IncidentStatuspageSubscriptionRequest
from datadog_api_client.v2.model.incident_statuspage_subscription_type import IncidentStatuspageSubscriptionType

body = IncidentStatuspageSubscriptionRequest(
    data=IncidentStatuspageSubscriptionDataRequest(
        attributes=IncidentStatuspageSubscriptionDataAttributesRequest(
            email="user@example.com",
        ),
        type=IncidentStatuspageSubscriptionType.STATUSPAGE_EMAIL_SUBSCRIPTION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_statuspage_email_subscription"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_statuspage_email_subscription(page_id="page_id", body=body)

    print(response)

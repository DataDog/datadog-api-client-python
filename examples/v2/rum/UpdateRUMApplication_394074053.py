"""
Update a RUM application with Product Scales returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_update import RUMApplicationUpdate
from datadog_api_client.v2.model.rum_application_update_attributes import RUMApplicationUpdateAttributes
from datadog_api_client.v2.model.rum_application_update_request import RUMApplicationUpdateRequest
from datadog_api_client.v2.model.rum_application_update_type import RUMApplicationUpdateType
from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState
from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

body = RUMApplicationUpdateRequest(
    data=RUMApplicationUpdate(
        attributes=RUMApplicationUpdateAttributes(
            name="updated_rum_with_product_scales",
            rum_event_processing_state=RUMEventProcessingState.ALL,
            product_analytics_retention_state=RUMProductAnalyticsRetentionState.MAX,
        ),
        id=RUM_APPLICATION_DATA_ID,
        type=RUMApplicationUpdateType.RUM_APPLICATION_UPDATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.update_rum_application(id=RUM_APPLICATION_DATA_ID, body=body)

    print(response)

"""
Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_server_side_event_item import ProductAnalyticsServerSideEventItem
from datadog_api_client.v2.model.product_analytics_server_side_event_item_account import (
    ProductAnalyticsServerSideEventItemAccount,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_application import (
    ProductAnalyticsServerSideEventItemApplication,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_event import (
    ProductAnalyticsServerSideEventItemEvent,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_session import (
    ProductAnalyticsServerSideEventItemSession,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_type import (
    ProductAnalyticsServerSideEventItemType,
)
from datadog_api_client.v2.model.product_analytics_server_side_event_item_usr import (
    ProductAnalyticsServerSideEventItemUsr,
)

body = ProductAnalyticsServerSideEventItem(
    account=ProductAnalyticsServerSideEventItemAccount(
        id="account-67890",
    ),
    application=ProductAnalyticsServerSideEventItemApplication(
        id="123abcde-123a-123b-1234-123456789abc",
    ),
    event=ProductAnalyticsServerSideEventItemEvent(
        name="payment.processed",
    ),
    session=ProductAnalyticsServerSideEventItemSession(
        id="session-abcdef",
    ),
    type=ProductAnalyticsServerSideEventItemType.SERVER,
    usr=ProductAnalyticsServerSideEventItemUsr(
        id="user-12345",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.submit_product_analytics_event(body=body)

    print(response)

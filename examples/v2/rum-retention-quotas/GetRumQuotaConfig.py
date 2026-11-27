"""
Get a RUM retention quota configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_quotas_api import RUMRetentionQuotasApi
from datadog_api_client.v2.model.rum_retention_quota_scope_type import RumRetentionQuotaScopeType

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionQuotasApi(api_client)
    response = api_instance.get_rum_quota_config(
        scope_type=RumRetentionQuotaScopeType.APPLICATION,
        scope_id=RUM_APPLICATION_DATA_ID,
    )

    print(response)

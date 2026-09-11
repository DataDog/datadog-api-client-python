"""
Get a Snowflake integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.snowflake_integration_api import SnowflakeIntegrationApi

configuration = Configuration()
configuration.unstable_operations["get_snowflake_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = SnowflakeIntegrationApi(api_client)
    response = api_instance.get_snowflake_integration_account(
        account_id="account_id",
    )

    print(response)

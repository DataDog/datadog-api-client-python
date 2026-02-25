"""
Get an AWS cloud authentication persona mapping returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi

configuration = Configuration()
configuration.unstable_operations["get_aws_cloud_auth_persona_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.get_aws_cloud_auth_persona_mapping(
        persona_mapping_id="persona_mapping_id",
    )

    print(response)

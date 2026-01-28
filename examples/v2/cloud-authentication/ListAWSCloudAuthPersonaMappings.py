"""
List AWS cloud authentication persona mappings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi

configuration = Configuration()
configuration.unstable_operations["list_aws_cloud_auth_persona_mappings"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.list_aws_cloud_auth_persona_mappings()

    print(response)

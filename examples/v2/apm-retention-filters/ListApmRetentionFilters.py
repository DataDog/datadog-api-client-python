"""
List all APM retention filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apm_retention_filters_api import APMRetentionFiltersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = APMRetentionFiltersApi(api_client)
    response = api_instance.list_apm_retention_filters()

    print(response)

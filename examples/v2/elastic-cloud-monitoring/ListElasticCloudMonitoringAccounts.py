"""
List Elastic Cloud monitoring accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_monitoring_api import ElasticCloudMonitoringApi

configuration = Configuration()
configuration.unstable_operations["list_elastic_cloud_monitoring_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudMonitoringApi(api_client)
    response = api_instance.list_elastic_cloud_monitoring_accounts()

    print(response)

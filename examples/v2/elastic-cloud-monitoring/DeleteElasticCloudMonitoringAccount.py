"""
Delete an Elastic Cloud monitoring account returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.elastic_cloud_monitoring_api import ElasticCloudMonitoringApi

configuration = Configuration()
configuration.unstable_operations["delete_elastic_cloud_monitoring_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ElasticCloudMonitoringApi(api_client)
    api_instance.delete_elastic_cloud_monitoring_account(
        account_id="account_id",
    )

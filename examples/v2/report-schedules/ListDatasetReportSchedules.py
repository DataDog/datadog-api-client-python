"""
List dataset report schedules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.report_schedules_api import ReportSchedulesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReportSchedulesApi(api_client)
    response = api_instance.list_dataset_report_schedules(
        dataset_id="dataset_id",
    )

    print(response)

"""
Bulk Delete SLO Timeframes returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.slo_bulk_delete import SLOBulkDelete
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe

body = SLOBulkDelete(
    id1=[
        SLOTimeframe("7d"),
        SLOTimeframe("30d"),
    ],
    id2=[
        SLOTimeframe("7d"),
        SLOTimeframe("30d"),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.delete_slo_timeframe_in_bulk(body=body)

    print(response)

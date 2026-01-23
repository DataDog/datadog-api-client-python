"""
Get SLO status returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi

configuration = Configuration()
configuration.unstable_operations["get_slo_status"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_status(
        slo_id="00000000-0000-0000-0000-000000000000",
        from_ts=1690901870,
        to_ts=1706803070,
    )

    print(response)

"""
Create an SLO object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

body = ServiceLevelObjectiveRequest(
    type=SLOType.METRIC,
    description="string",
    groups=[
        "env:test",
        "role:mysql",
    ],
    monitor_ids=[],
    name="Example-Create_an_SLO_object_returns_OK_response",
    query=ServiceLevelObjectiveQuery(
        denominator="sum:httpservice.hits{!code:3xx}.as_count()",
        numerator="sum:httpservice.hits{code:2xx}.as_count()",
    ),
    tags=[
        "env:prod",
        "app:core",
    ],
    thresholds=[
        SLOThreshold(
            target=95.0,
            target_display="95.0",
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=98.0,
            warning_display="98.0",
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=97.0,
    warning_threshold=98.0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo(body=body)

    print(response)

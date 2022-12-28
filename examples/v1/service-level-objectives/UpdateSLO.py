"""
Update an SLO returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective
from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]
SLO_DATA_0_NAME = environ["SLO_DATA_0_NAME"]

body = ServiceLevelObjective(
    type=SLOType.METRIC,
    name=SLO_DATA_0_NAME,
    thresholds=[
        SLOThreshold(
            target=97.0,
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=98.0,
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=97.0,
    warning_threshold=98.0,
    query=ServiceLevelObjectiveQuery(
        numerator="sum:httpservice.hits{code:2xx}.as_count()",
        denominator="sum:httpservice.hits{!code:3xx}.as_count()",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.update_slo(slo_id=SLO_DATA_0_ID, body=body)

    print(response)

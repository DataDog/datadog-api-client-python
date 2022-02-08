import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objectives_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    body = ServiceLevelObjectiveRequest(
        description="description_example",
        groups=["env:prod","role:mysql"],
        monitor_ids=[
            1,
        ],
        name="Custom Metric SLO",
        query=ServiceLevelObjectiveQuery(
            denominator="sum:my.custom.metric{*}.as_count()",
            numerator="sum:my.custom.metric{type:good}.as_count()",
        ),
        tags=["env:prod","app:core"],
        thresholds=[
            SLOThreshold(
                target=99.9,
                target_display="99.9",
                timeframe=SLOTimeframe("30d"),
                warning=90.0,
                warning_display="90.0",
            ),
        ],
        type=SLOType("metric"),
    )  # ServiceLevelObjectiveRequest | Service level objective request object.

    # example passing only required values which don't have defaults set
    try:
        # Create an SLO object
        api_response = api_instance.create_slo(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->create_slo: %s\n" % e)

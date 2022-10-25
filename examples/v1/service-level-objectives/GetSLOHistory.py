"""
Get an SLO's history returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_history(
        slo_id=SLO_DATA_0_ID,
        from_ts=int((datetime.now() + relativedelta(days=-1)).timestamp()),
        to_ts=int(datetime.now().timestamp()),
    )

    print(response)

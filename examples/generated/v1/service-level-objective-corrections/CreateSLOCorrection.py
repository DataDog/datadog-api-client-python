import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["create_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)
    body = SLOCorrectionCreateRequest(
        data=SLOCorrectionCreateData(
            attributes=SLOCorrectionCreateRequestAttributes(
                category=SLOCorrectionCategory("Scheduled Maintenance"),
                description="description_example",
                duration=1600000000,
                end=1600000000,
                rrule="FREQ=DAILY;INTERVAL=10;COUNT=5",
                slo_id="sloId",
                start=1600000000,
                timezone="UTC",
            ),
            type=SLOCorrectionType("correction"),
        ),
    )  # SLOCorrectionCreateRequest | Create an SLO Correction

    # example passing only required values which don't have defaults set
    try:
        # Create an SLO correction
        api_response = api_instance.create_slo_correction(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->create_slo_correction: %s\n" % e)

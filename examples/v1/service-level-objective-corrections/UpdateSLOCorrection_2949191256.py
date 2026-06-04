"""
Update an SLO correction with slo_query returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType
from datadog_api_client.v1.model.slo_correction_update_data import SLOCorrectionUpdateData
from datadog_api_client.v1.model.slo_correction_update_request import SLOCorrectionUpdateRequest
from datadog_api_client.v1.model.slo_correction_update_request_attributes import SLOCorrectionUpdateRequestAttributes

# there is a valid "correction_with_query" in the system
CORRECTION_WITH_QUERY_DATA_ID = environ["CORRECTION_WITH_QUERY_DATA_ID"]

body = SLOCorrectionUpdateRequest(
    data=SLOCorrectionUpdateData(
        attributes=SLOCorrectionUpdateRequestAttributes(
            category=SLOCorrectionCategory.SCHEDULED_MAINTENANCE,
            description="Example-Service-Level-Objective-Correction",
            end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
            slo_query="env:staging service:checkout",
            start=int(datetime.now().timestamp()),
            timezone="UTC",
        ),
        type=SLOCorrectionType.CORRECTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.update_slo_correction(slo_correction_id=CORRECTION_WITH_QUERY_DATA_ID, body=body)

    print(response)

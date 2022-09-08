"""
Create an SLO correction returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_create_data import SLOCorrectionCreateData
from datadog_api_client.v1.model.slo_correction_create_request import SLOCorrectionCreateRequest
from datadog_api_client.v1.model.slo_correction_create_request_attributes import SLOCorrectionCreateRequestAttributes
from datadog_api_client.v1.model.slo_correction_type import SLOCorrectionType

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

body = SLOCorrectionCreateRequest(
    data=SLOCorrectionCreateData(
        attributes=SLOCorrectionCreateRequestAttributes(
            category=SLOCorrectionCategory.SCHEDULED_MAINTENANCE,
            description="Example-Create_an_SLO_correction_returns_OK_response",
            end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
            slo_id=SLO_DATA_0_ID,
            start=int(datetime.now().timestamp()),
            timezone="UTC",
        ),
        type=SLOCorrectionType.CORRECTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.create_slo_correction(body=body)

    print(response)

"""
Create a new SLO report returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v2.model.slo_report_create_request import SloReportCreateRequest
from datadog_api_client.v2.model.slo_report_create_request_attributes import SloReportCreateRequestAttributes
from datadog_api_client.v2.model.slo_report_create_request_data import SloReportCreateRequestData
from datadog_api_client.v2.model.slo_report_interval import SLOReportInterval

body = SloReportCreateRequest(
    data=SloReportCreateRequestData(
        attributes=SloReportCreateRequestAttributes(
            from_ts=int((datetime.now() + relativedelta(days=-40)).timestamp()),
            to_ts=int(datetime.now().timestamp()),
            query='slo_type:metric "SLO Reporting Test"',
            interval=SLOReportInterval.MONTHLY,
            timezone="America/New_York",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_slo_report_job"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo_report_job(body=body)

    print(response)

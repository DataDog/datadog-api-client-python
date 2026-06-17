"""
Create or update an indicator triage state returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.io_c_triage_state import IoCTriageState
from datadog_api_client.v2.model.io_c_triage_write_request import IoCTriageWriteRequest
from datadog_api_client.v2.model.io_c_triage_write_request_attributes import IoCTriageWriteRequestAttributes
from datadog_api_client.v2.model.io_c_triage_write_request_data import IoCTriageWriteRequestData

body = IoCTriageWriteRequest(
    data=IoCTriageWriteRequestData(
        attributes=IoCTriageWriteRequestAttributes(
            indicator="192.0.2.1",
            triage_state=IoCTriageState.REVIEWED,
        ),
        type="ioc_triage_state",
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_io_c_triage_state"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_io_c_triage_state(body=body)

    print(response)

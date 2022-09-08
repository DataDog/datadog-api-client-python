"""
Submit a Service Check returns "Payload accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_checks_api import ServiceChecksApi
from datadog_api_client.v1.model.service_check import ServiceCheck
from datadog_api_client.v1.model.service_check_status import ServiceCheckStatus
from datadog_api_client.v1.model.service_checks import ServiceChecks

body = ServiceChecks(
    [
        ServiceCheck(
            check="app.ok",
            host_name="host",
            status=ServiceCheckStatus.OK,
            tags=[
                "test:ExampleSubmitaServiceCheckreturnsPayloadacceptedresponse",
            ],
        ),
    ]
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceChecksApi(api_client)
    response = api_instance.submit_service_check(body=body)

    print(response)

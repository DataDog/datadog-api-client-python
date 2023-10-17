"""
Save new value for on-demand concurrency cap returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.on_demand_concurrency_cap_attributes import OnDemandConcurrencyCapAttributes

body = OnDemandConcurrencyCapAttributes(
    on_demand_concurrency_cap=20.0,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.set_on_demand_concurrency_cap(body=body)

    print(response)

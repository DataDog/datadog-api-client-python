"""
Fetch uptime for multiple tests returns "OK." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_fetch_uptimes_payload import SyntheticsFetchUptimesPayload

body = SyntheticsFetchUptimesPayload(
    from_ts=1726041488,
    public_ids=[
        "p8m-9gw-nte",
    ],
    to_ts=1726055954,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.fetch_uptimes(body=body)

    print(response)

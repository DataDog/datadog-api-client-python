"""
Post an event returns "OK" response with an int64 ID above 2^53
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest

body = EventCreateRequest(
    title="Example-Event",
    text="An event whose ID exceeds Number.MAX_SAFE_INTEGER.",
    tags=[
        "test:ExampleEvent",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)

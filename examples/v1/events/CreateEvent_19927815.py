"""
Post an event with a long title returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest

body = EventCreateRequest(
    title="Example-Post_an_event_with_a_long_title_returns_OK_response very very very looooooooong looooooooooooong loooooooooooooooooooooong looooooooooooooooooooooooooong title with 100+ characters",
    text="A text message.",
    tags=[
        "test:ExamplePostaneventwithalongtitlereturnsOKresponse",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)

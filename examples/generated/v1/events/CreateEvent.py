import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import events_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    body = EventCreateRequest(
        aggregation_key="aggregation_key_example",
        alert_type=EventAlertType("info"),
        date_happened=1,
        device_name="device_name_example",
        host="host_example",
        priority=EventPriority("normal"),
        related_event_id=1,
        source_type_name="source_type_name_example",
        tags=["environment:test"],
        text="Oh boy!",
        title="Did you hear the news today?",
    )  # EventCreateRequest | Event request object

    # example passing only required values which don't have defaults set
    try:
        # Post an event
        api_response = api_instance.create_event(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->create_event: %s\n" % e)

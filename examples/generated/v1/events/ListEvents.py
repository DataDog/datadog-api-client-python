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
    start = 1  # int | POSIX timestamp.
    end = 1  # int | POSIX timestamp.
    priority = EventPriority("normal")  # EventPriority | Priority of your events, either `low` or `normal`. (optional)
    sources = "sources_example"  # str | A comma separated string of sources. (optional)
    tags = "host:host0"  # str | A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. (optional)
    unaggregated = True  # bool | Set unaggregated to `true` to return all events within the specified [`start`,`end`] timeframe. Otherwise if an event is aggregated to a parent event with a timestamp outside of the timeframe, it won't be available in the output. Aggregated events with `is_aggregate=true` in the response will still be returned unless exclude_aggregate is set to `true.` (optional)
    exclude_aggregate = True  # bool | Set `exclude_aggregate` to `true` to only return unaggregated events where `is_aggregate=false` in the response. If the `exclude_aggregate` parameter is set to `true`, then the unaggregated parameter is ignored and will be `true` by default. (optional)
    page = 1  # int | By default 1000 results are returned per request. Set page to the number of the page to return with `0` being the first page. The page parameter can only be used when either unaggregated or exclude_aggregate is set to `true.` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query the event stream
        api_response = api_instance.list_events(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query the event stream
        api_response = api_instance.list_events(start, end, priority=priority, sources=sources, tags=tags, unaggregated=unaggregated, exclude_aggregate=exclude_aggregate, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)

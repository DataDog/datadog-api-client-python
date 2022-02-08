import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import snapshots_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snapshots_api.SnapshotsApi(api_client)
    start = 1  # int | The POSIX timestamp of the start of the query.
    end = 1  # int | The POSIX timestamp of the end of the query.
    metric_query = "metric_query_example"  # str | The metric query. (optional)
    event_query = "event_query_example"  # str | A query that adds event bands to the graph. (optional)
    graph_def = "graph_def_example"  # str | A JSON document defining the graph. `graph_def` can be used instead of `metric_query`. The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar) and should be formatted to a single line then URL encoded. (optional)
    title = "title_example"  # str | A title for the graph. If no title is specified, the graph does not have a title. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Take graph snapshots
        api_response = api_instance.get_graph_snapshot(start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotsApi->get_graph_snapshot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Take graph snapshots
        api_response = api_instance.get_graph_snapshot(start, end, metric_query=metric_query, event_query=event_query, graph_def=graph_def, title=title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotsApi->get_graph_snapshot: %s\n" % e)

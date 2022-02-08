import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    group_states = "alert"  # str | When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`. (optional)
    name = "name_example"  # str | A string to filter monitors by name. (optional)
    tags = "host:host0"  # str | A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. For example, `host:host0`. (optional)
    monitor_tags = "service:my-app"  # str | A comma separated list indicating what service and/or custom tags, if any, should be used to filter the list of monitors. Tags created in the Datadog UI automatically have the service key prepended. For example, `service:my-app`. (optional)
    with_downtimes = True  # bool | If this argument is set to true, then the returned data includes all current active downtimes for each monitor. (optional)
    id_offset = 1  # int | Use this parameter for paginating through large sets of monitors. Start with a value of zero, make a request, set the value to the last ID of result set, and then repeat until the response is empty. (optional)
    page = 0  # int | The page to start paginating from. If this argument is not specified, the request returns all monitors without pagination. (optional)
    page_size = 20  # int | The number of monitors to return per page. If the page argument is not specified, the default behavior returns all monitors without a `page_size` limit. However, if page is specified and `page_size` is not, the argument defaults to 100. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all monitor details
        api_response = api_instance.list_monitors(group_states=group_states, name=name, tags=tags, monitor_tags=monitor_tags, with_downtimes=with_downtimes, id_offset=id_offset, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->list_monitors: %s\n" % e)

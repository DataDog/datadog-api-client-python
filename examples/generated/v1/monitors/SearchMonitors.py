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
    query = "query_example"  # str | After entering a search query in your [Manage Monitor page][1] use the query parameter value in the URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation][2] page to learn more.  The query can contain any number of space-separated monitor attributes, for instance `query=\"type:metric status:alert\"`.  [1]: https://app.datadoghq.com/monitors/manage [2]: /monitors/manage/#find-the-monitors (optional)
    page = 0  # int | Page to start paginating from. (optional) if omitted the server will use the default value of 0
    per_page = 30  # int | Number of monitors to return per page. (optional) if omitted the server will use the default value of 30
    sort = "sort_example"  # str | String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:  * `name` * `status` * `tags` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Monitors search
        api_response = api_instance.search_monitors(query=query, page=page, per_page=per_page, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->search_monitors: %s\n" % e)

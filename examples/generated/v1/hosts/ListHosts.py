import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import hosts_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hosts_api.HostsApi(api_client)
    filter = "filter_example"  # str | String to filter search results. (optional)
    sort_field = "sort_field_example"  # str | Sort hosts by this field. (optional)
    sort_dir = "sort_dir_example"  # str | Direction of sort. Options include `asc` and `desc`. (optional)
    start = 1  # int | Host result to start search from. (optional)
    count = 1  # int | Number of hosts to return. Max 1000. (optional)
    _from = 1  # int | Number of seconds since UNIX epoch from which you want to search your hosts. (optional)
    include_muted_hosts_data = True  # bool | Include information on the muted status of hosts and when the mute expires. (optional)
    include_hosts_metadata = True  # bool | Include additional metadata about the hosts (agent_version, machine, platform, processor, etc.). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all hosts for your organization
        api_response = api_instance.list_hosts(filter=filter, sort_field=sort_field, sort_dir=sort_dir, start=start, count=count, _from=_from, include_muted_hosts_data=include_muted_hosts_data, include_hosts_metadata=include_hosts_metadata)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->list_hosts: %s\n" % e)

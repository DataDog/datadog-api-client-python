import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import tags_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)
    host_name = "host_name_example"  # str | When specified, filters list of tags to those tags with the specified source.
    source = "source_example"  # str | Source to filter. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get host tags
        api_response = api_instance.get_host_tags(host_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_host_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get host tags
        api_response = api_instance.get_host_tags(host_name, source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->get_host_tags: %s\n" % e)

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
    source = "source_example"  # str | When specified, filters host list to those tags with the specified source. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Tags
        api_response = api_instance.list_host_tags(source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->list_host_tags: %s\n" % e)

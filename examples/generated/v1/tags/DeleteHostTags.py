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
    host_name = "host_name_example"  # str | This endpoint allows you to remove all user-assigned tags for a single host.
    source = "source_example"  # str | The source of the tags (for example chef, puppet). [Complete list of source attribute values](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove host tags
        api_instance.delete_host_tags(host_name)
    except ApiException as e:
        print("Exception when calling TagsApi->delete_host_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove host tags
        api_instance.delete_host_tags(host_name, source=source)
    except ApiException as e:
        print("Exception when calling TagsApi->delete_host_tags: %s\n" % e)

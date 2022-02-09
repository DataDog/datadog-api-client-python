import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    author_handle = "test@datadoghq.com"  # str | Return notebooks created by the given `author_handle`. (optional)
    exclude_author_handle = "test@datadoghq.com"  # str | Return notebooks not created by the given `author_handle`. (optional)
    start = 0  # int | The index of the first notebook you want returned. (optional)
    count = 5  # int | The number of notebooks to be returned. (optional)
    sort_field = "modified"  # str | Sort by field `modified`, `name`, or `created`. (optional) if omitted the server will use the default value of "modified"
    sort_dir = "desc"  # str | Sort by direction `asc` or `desc`. (optional) if omitted the server will use the default value of "desc"
    query = "postmortem"  # str | Return only notebooks with `query` string in notebook name or author handle. (optional)
    include_cells = False  # bool | Value of `false` excludes the `cells` and global `time` for each notebook. (optional) if omitted the server will use the default value of True
    is_template = False  # bool | True value returns only template notebooks. Default is false (returns only non-template notebooks). (optional) if omitted the server will use the default value of False
    type = "investigation"  # str | If type is provided, returns only notebooks with that metadata type. Default does not have type filtering. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all notebooks
        api_response = api_instance.list_notebooks(author_handle=author_handle, exclude_author_handle=exclude_author_handle, start=start, count=count, sort_field=sort_field, sort_dir=sort_dir, query=query, include_cells=include_cells, is_template=is_template, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotebooksApi->list_notebooks: %s\n" % e)

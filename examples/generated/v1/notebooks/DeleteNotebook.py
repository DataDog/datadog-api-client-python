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
    notebook_id = 1  # int | Unique ID, assigned when you create the notebook.

    # example passing only required values which don't have defaults set
    try:
        # Delete a notebook
        api_instance.delete_notebook(notebook_id)
    except ApiException as e:
        print("Exception when calling NotebooksApi->delete_notebook: %s\n" % e)

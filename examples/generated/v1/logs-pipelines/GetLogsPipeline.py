import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_pipelines_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_pipelines_api.LogsPipelinesApi(api_client)
    pipeline_id = "pipeline_id_example"  # str | ID of the pipeline to get.

    # example passing only required values which don't have defaults set
    try:
        # Get a pipeline
        api_response = api_instance.get_logs_pipeline(pipeline_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsPipelinesApi->get_logs_pipeline: %s\n" % e)

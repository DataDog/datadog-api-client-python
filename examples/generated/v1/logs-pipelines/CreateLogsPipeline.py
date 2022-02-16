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
    body = LogsPipeline(
        filter=LogsFilter(
            query="source:python",
        ),
        is_enabled=True,
        name="",
        processors=[
            LogsProcessor(),
        ],
    )  # LogsPipeline | Definition of the new pipeline.

    # example passing only required values which don't have defaults set
    try:
        # Create a pipeline
        api_response = api_instance.create_logs_pipeline(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsPipelinesApi->create_logs_pipeline: %s\n" % e)

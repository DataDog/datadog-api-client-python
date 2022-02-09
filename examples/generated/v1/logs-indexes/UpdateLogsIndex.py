import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_indexes_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_indexes_api.LogsIndexesApi(api_client)
    name = "name_example"  # str | Name of the log index.
    body = LogsIndexUpdateRequest(
        daily_limit=1,
        disable_daily_limit=True,
        exclusion_filters=[
            LogsExclusion(
                filter=LogsExclusionFilter(
                    query="*",
                    sample_rate=1.0,
                ),
                is_enabled=True,
                name="payment",
            ),
        ],
        filter=LogsFilter(
            query="source:python",
        ),
        num_retention_days=1,
    )  # LogsIndexUpdateRequest | Object containing the new `LogsIndexUpdateRequest`.

    # example passing only required values which don't have defaults set
    try:
        # Update an index
        api_response = api_instance.update_logs_index(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsIndexesApi->update_logs_index: %s\n" % e)

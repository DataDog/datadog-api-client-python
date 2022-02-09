import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objectives_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objectives_api.ServiceLevelObjectivesApi(api_client)
    ids = "id1, id2, id3"  # str | A comma separated list of the IDs of the service level objectives objects. (optional)
    query = "monitor"  # str | The query string to filter results based on SLO names. (optional)
    tags_query = "env:prod"  # str | The query string to filter results based on a single SLO tag. (optional)
    metrics_query = "aws.elb.request_count"  # str | The query string to filter results based on SLO numerator and denominator. (optional)
    limit = 1  # int | The number of SLOs to return in the response. (optional)
    offset = 1  # int | The specific offset to use as the beginning of the returned response. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all SLOs
        api_response = api_instance.list_slos(ids=ids, query=query, tags_query=tags_query, metrics_query=metrics_query, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectivesApi->list_slos: %s\n" % e)

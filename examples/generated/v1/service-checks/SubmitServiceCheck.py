import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_checks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_checks_api.ServiceChecksApi(api_client)
    body = ServiceChecks([
        ServiceCheck(
            check="app.ok",
            host_name="app.host1",
            message="app is running",
            status=ServiceCheckStatus(0),
            tags=["environment:test"],
            timestamp=1,
        ),
    ])  # ServiceChecks | Service Check request body.

    # example passing only required values which don't have defaults set
    try:
        # Submit a Service Check
        api_response = api_instance.submit_service_check(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceChecksApi->submit_service_check: %s\n" % e)

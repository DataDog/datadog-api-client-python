import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)
    agent_rule_id = "3b5-v82-ns6"  # str | The ID of the Agent rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Cloud Workload Security Agent rule
        api_instance.delete_cloud_workload_security_agent_rule(agent_rule_id)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->delete_cloud_workload_security_agent_rule: %s\n" % e)

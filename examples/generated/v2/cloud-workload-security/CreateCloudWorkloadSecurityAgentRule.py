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
    body = CloudWorkloadSecurityAgentRuleCreateRequest(
        data=CloudWorkloadSecurityAgentRuleCreateData(
            attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
                description="My Agent rule",
                enabled=True,
                expression="exec.file.name == \"sh\"",
                name="my_agent_rule",
            ),
            type=CloudWorkloadSecurityAgentRuleType("agent_rule"),
        ),
    )  # CloudWorkloadSecurityAgentRuleCreateRequest | The definition of the new Agent rule.

    # example passing only required values which don't have defaults set
    try:
        # Create a Cloud Workload Security Agent rule
        api_response = api_instance.create_cloud_workload_security_agent_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->create_cloud_workload_security_agent_rule: %s\n" % e)

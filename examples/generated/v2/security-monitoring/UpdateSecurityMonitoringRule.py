import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import security_monitoring_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_monitoring_api.SecurityMonitoringApi(api_client)
    rule_id = "rule_id_example"  # str | The ID of the rule.
    body = SecurityMonitoringRuleUpdatePayload(
        cases=[
            SecurityMonitoringRuleCase(
                condition="condition_example",
                name="name_example",
                notifications=[
                    "notifications_example",
                ],
                status=SecurityMonitoringRuleSeverity("critical"),
            ),
        ],
        filters=[
            SecurityMonitoringFilter(
                action=SecurityMonitoringFilterAction("require"),
                query="query_example",
            ),
        ],
        has_extended_title=True,
        is_enabled=True,
        message="message_example",
        name="name_example",
        options=SecurityMonitoringRuleOptions(
            detection_method=SecurityMonitoringRuleDetectionMethod("threshold"),
            evaluation_window=SecurityMonitoringRuleEvaluationWindow(0),
            keep_alive=SecurityMonitoringRuleKeepAlive(0),
            max_signal_duration=SecurityMonitoringRuleMaxSignalDuration(0),
            new_value_options=SecurityMonitoringRuleNewValueOptions(
                forget_after=SecurityMonitoringRuleNewValueOptionsForgetAfter(1),
                learning_duration=SecurityMonitoringRuleNewValueOptionsLearningDuration(0),
            ),
        ),
        queries=[
            SecurityMonitoringRuleQuery(
                aggregation=SecurityMonitoringRuleQueryAggregation("count"),
                distinct_fields=[
                    "distinct_fields_example",
                ],
                group_by_fields=[
                    "group_by_fields_example",
                ],
                metric="metric_example",
                name="name_example",
                query="query_example",
            ),
        ],
        tags=[
            "tags_example",
        ],
        version=1,
    )  # SecurityMonitoringRuleUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update an existing rule
        api_response = api_instance.update_security_monitoring_rule(rule_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityMonitoringApi->update_security_monitoring_rule: %s\n" % e)

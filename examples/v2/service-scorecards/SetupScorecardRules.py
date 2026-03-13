"""
Set up rules for organization returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.setup_rules_request import SetupRulesRequest
from datadog_api_client.v2.model.setup_rules_request_attributes import SetupRulesRequestAttributes
from datadog_api_client.v2.model.setup_rules_request_data import SetupRulesRequestData
from datadog_api_client.v2.model.setup_rules_request_data_type import SetupRulesRequestDataType

body = SetupRulesRequest(
    data=SetupRulesRequestData(
        attributes=SetupRulesRequestAttributes(
            disabled_default_rules=[
                "q8MQxk8TCqrHnWkx",
                "r9NRyl9UDrsIoXly",
            ],
        ),
        type=SetupRulesRequestDataType.SETUP,
    ),
)

configuration = Configuration()
configuration.unstable_operations["setup_scorecard_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.setup_scorecard_rules(body=body)

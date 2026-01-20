"""
List Entity Risk Scores returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.entity_risk_scores_api import EntityRiskScoresApi

configuration = Configuration()
configuration.unstable_operations["list_entity_risk_scores"] = True
with ApiClient(configuration) as api_client:
    api_instance = EntityRiskScoresApi(api_client)
    response = api_instance.list_entity_risk_scores()

    print(response)

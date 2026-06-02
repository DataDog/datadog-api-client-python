"""
Get Entity Risk Score returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.entity_risk_scores_api import EntityRiskScoresApi

configuration = Configuration()
configuration.unstable_operations["get_entity_risk_score"] = True
with ApiClient(configuration) as api_client:
    api_instance = EntityRiskScoresApi(api_client)
    response = api_instance.get_entity_risk_score(
        entity_id="arn:aws:iam::123456789012:user/john.doe",
    )

    print(response)

"""
Update a suppression rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.security_monitoring_suppression_type import SecurityMonitoringSuppressionType
from datadog_api_client.v2.model.security_monitoring_suppression_update_attributes import (
    SecurityMonitoringSuppressionUpdateAttributes,
)
from datadog_api_client.v2.model.security_monitoring_suppression_update_data import (
    SecurityMonitoringSuppressionUpdateData,
)
from datadog_api_client.v2.model.security_monitoring_suppression_update_request import (
    SecurityMonitoringSuppressionUpdateRequest,
)

# there is a valid "suppression" in the system
SUPPRESSION_DATA_ID = environ["SUPPRESSION_DATA_ID"]

body = SecurityMonitoringSuppressionUpdateRequest(
    data=SecurityMonitoringSuppressionUpdateData(
        attributes=SecurityMonitoringSuppressionUpdateAttributes(
            suppression_query="env:staging status:low",
        ),
        type=SecurityMonitoringSuppressionType.SUPPRESSIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_security_monitoring_suppression(suppression_id=SUPPRESSION_DATA_ID, body=body)

    print(response)

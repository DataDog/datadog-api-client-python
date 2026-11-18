"""
Replace a fleet access scope returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fleet_automation_api import FleetAutomationApi
from datadog_api_client.v2.model.fleet_access_scope_attributes import FleetAccessScopeAttributes
from datadog_api_client.v2.model.fleet_access_scope_features import FleetAccessScopeFeatures
from datadog_api_client.v2.model.fleet_access_scope_resource_type import FleetAccessScopeResourceType
from datadog_api_client.v2.model.fleet_access_scope_write import FleetAccessScopeWrite
from datadog_api_client.v2.model.fleet_access_scope_write_request import FleetAccessScopeWriteRequest

# there is a valid "fleet_access_scope" in the system
FLEET_ACCESS_SCOPE_ID = environ["FLEET_ACCESS_SCOPE_ID"]

body = FleetAccessScopeWriteRequest(
    data=FleetAccessScopeWrite(
        type=FleetAccessScopeResourceType.ACCESS_SCOPE,
        attributes=FleetAccessScopeAttributes(
            description="Example-Fleet-Automation updated",
            query="env:staging",
            features=FleetAccessScopeFeatures(
                install=False,
                upgrade=False,
                configure=True,
            ),
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_fleet_access_scope"] = True
with ApiClient(configuration) as api_client:
    api_instance = FleetAutomationApi(api_client)
    response = api_instance.update_fleet_access_scope(access_scope_id=FLEET_ACCESS_SCOPE_ID, body=body)

    print(response)

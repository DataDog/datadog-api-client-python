"""
Grant role to a restriction query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["add_role_to_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.add_role_to_restriction_query(restriction_query_id="restriction_query_id", body=body)

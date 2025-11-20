"""
Revoke role from a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRole
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RelationshipToRole(
    data=RelationshipToRoleData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["remove_role_from_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    api_instance.remove_role_from_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

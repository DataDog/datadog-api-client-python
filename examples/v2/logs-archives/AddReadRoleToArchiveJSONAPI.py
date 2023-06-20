"""
Grant role to an archive returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.relationship_to_role import RelationshipToRoleJSON

body = RelationshipToRoleJSON(
    id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    api_instance.add_read_role_to_archive(archive_id="archive_id", body=body)

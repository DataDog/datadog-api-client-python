import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_archives_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_archives_api.LogsArchivesApi(api_client)
    archive_id = "archive_id_example"  # str | The ID of the archive.
    body = RelationshipToRole(
        data=RelationshipToRoleData(
            id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            type=RolesType("roles"),
        ),
    )  # RelationshipToRole | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke role from an archive
        api_instance.remove_role_from_archive(archive_id, body)
    except ApiException as e:
        print("Exception when calling LogsArchivesApi->remove_role_from_archive: %s\n" % e)

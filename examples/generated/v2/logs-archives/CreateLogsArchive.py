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
    body = LogsArchiveCreateRequest(
        data=LogsArchiveCreateRequestDefinition(
            attributes=LogsArchiveCreateRequestAttributes(
                destination=LogsArchiveCreateRequestDestination(),
                include_tags=False,
                name="Nginx Archive",
                query="source:nginx",
                rehydration_tags=["team:intake","team:app"],
            ),
            type="archives",
        ),
    )  # LogsArchiveCreateRequest | The definition of the new archive.

    # example passing only required values which don't have defaults set
    try:
        # Create an archive
        api_response = api_instance.create_logs_archive(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsArchivesApi->create_logs_archive: %s\n" % e)

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

    # example passing only required values which don't have defaults set
    try:
        # Delete an archive
        api_instance.delete_logs_archive(archive_id)
    except ApiException as e:
        print("Exception when calling LogsArchivesApi->delete_logs_archive: %s\n" % e)

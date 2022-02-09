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
    body = LogsArchiveOrder(
        data=LogsArchiveOrderDefinition(
            attributes=LogsArchiveOrderAttributes(
                archive_ids=["a2zcMylnM4OCHpYusxIi1g","a2zcMylnM4OCHpYusxIi2g","a2zcMylnM4OCHpYusxIi3g"],
            ),
            type=LogsArchiveOrderDefinitionType("archive_order"),
        ),
    )  # LogsArchiveOrder | An object containing the new ordered list of archive IDs.

    # example passing only required values which don't have defaults set
    try:
        # Update archive order
        api_response = api_instance.update_logs_archive_order(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsArchivesApi->update_logs_archive_order: %s\n" % e)

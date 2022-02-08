import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["create_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    body = IncidentCreateRequest(
        data=IncidentCreateData(
            attributes=IncidentCreateAttributes(
                customer_impacted=False,
                fields={
                    "key": IncidentFieldAttributes(),
                },
                initial_cells=[
                    IncidentTimelineCellCreateAttributes(),
                ],
                notification_handles=[
                    IncidentNotificationHandle(
                        display_name="Jane Doe",
                        handle="@test.user@test.com",
                    ),
                ],
                title="A test incident title",
            ),
            relationships=IncidentCreateRelationships(
                commander=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
            ),
            type=IncidentType("incidents"),
        ),
    )  # IncidentCreateRequest | Incident payload.

    # example passing only required values which don't have defaults set
    try:
        # Create an incident
        api_response = api_instance.create_incident(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->create_incident: %s\n" % e)

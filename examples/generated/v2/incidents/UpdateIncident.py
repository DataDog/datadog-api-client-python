import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import incidents_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["update_incident"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    incident_id = "incident_id_example"  # str | The UUID of the incident.
    body = IncidentUpdateRequest(
        data=IncidentUpdateData(
            attributes=IncidentUpdateAttributes(
                customer_impact_end=dateutil_parser('1970-01-01T00:00:00.00Z'),
                customer_impact_scope="Example customer impact scope",
                customer_impact_start=dateutil_parser('1970-01-01T00:00:00.00Z'),
                customer_impacted=False,
                detected=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields={
                    "key": IncidentFieldAttributes(),
                },
                notification_handles=[
                    IncidentNotificationHandle(
                        display_name="Jane Doe",
                        handle="@test.user@test.com",
                    ),
                ],
                resolved=dateutil_parser('1970-01-01T00:00:00.00Z'),
                title="A test incident title",
            ),
            id="00000000-0000-0000-0000-000000000000",
            relationships=IncidentUpdateRelationships(
                commander_user=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                created_by_user=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                integrations=RelationshipToIncidentIntegrationMetadatas(
                    data=[
                        RelationshipToIncidentIntegrationMetadataData(
                            id="00000000-0000-0000-0000-000000000000",
                            type=IncidentIntegrationMetadataType("incident_integrations"),
                        ),
                    ],
                ),
                last_modified_by_user=RelationshipToUser(
                    data=RelationshipToUserData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=UsersType("users"),
                    ),
                ),
                postmortem=RelationshipToIncidentPostmortem(
                    data=RelationshipToIncidentPostmortemData(
                        id="00000000-0000-0000-0000-000000000000",
                        type=IncidentPostmortemType("incident_postmortems"),
                    ),
                ),
            ),
            type=IncidentType("incidents"),
        ),
    )  # IncidentUpdateRequest | Incident Payload.

    # example passing only required values which don't have defaults set
    try:
        # Update an existing incident
        api_response = api_instance.update_incident(incident_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IncidentsApi->update_incident: %s\n" % e)

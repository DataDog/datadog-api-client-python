"""
Create or update service definition returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2 import ServiceDefinitionV2
from datadog_api_client.v2.model.service_definition_v2_doc import ServiceDefinitionV2Doc
from datadog_api_client.v2.model.service_definition_v2_email import ServiceDefinitionV2Email
from datadog_api_client.v2.model.service_definition_v2_email_type import ServiceDefinitionV2EmailType
from datadog_api_client.v2.model.service_definition_v2_integrations import ServiceDefinitionV2Integrations
from datadog_api_client.v2.model.service_definition_v2_link import ServiceDefinitionV2Link
from datadog_api_client.v2.model.service_definition_v2_link_type import ServiceDefinitionV2LinkType
from datadog_api_client.v2.model.service_definition_v2_opsgenie import ServiceDefinitionV2Opsgenie
from datadog_api_client.v2.model.service_definition_v2_opsgenie_region import ServiceDefinitionV2OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_repo import ServiceDefinitionV2Repo
from datadog_api_client.v2.model.service_definition_v2_version import ServiceDefinitionV2Version

body = ServiceDefinitionV2(
    contacts=[
        ServiceDefinitionV2Email(
            contact="contact@datadoghq.com",
            name="Team Email",
            type=ServiceDefinitionV2EmailType.EMAIL,
        ),
    ],
    dd_service="service-Example-Create_or_update_service_definition_returns_CREATED_response",
    dd_team="my-team",
    docs=[
        ServiceDefinitionV2Doc(
            name="Architecture",
            provider="google drive",
            url="https://gdrive/mydoc",
        ),
    ],
    extensions=dict(myorgextension="extensionvalue"),
    integrations=ServiceDefinitionV2Integrations(
        opsgenie=ServiceDefinitionV2Opsgenie(
            region=ServiceDefinitionV2OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty="https://my-org.pagerduty.com/service-directory/PMyService",
    ),
    links=[
        ServiceDefinitionV2Link(
            name="Runbook",
            type=ServiceDefinitionV2LinkType.RUNBOOK,
            url="https://my-runbook",
        ),
    ],
    repos=[
        ServiceDefinitionV2Repo(
            name="Source Code",
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
    ],
    schema_version=ServiceDefinitionV2Version.V2,
    tags=[
        "my:tag",
        "service:tag",
    ],
    team="my-team",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceDefinitionApi(api_client)
    response = api_instance.create_or_update_service_definitions(body=body)

    print(response)

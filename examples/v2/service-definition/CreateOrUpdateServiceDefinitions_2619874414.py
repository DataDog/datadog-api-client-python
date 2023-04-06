"""
Create or update service definition using schema v2-1 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2_dot1 import ServiceDefinitionV2Dot1
from datadog_api_client.v2.model.service_definition_v2_dot1_email import ServiceDefinitionV2Dot1Email
from datadog_api_client.v2.model.service_definition_v2_dot1_email_type import ServiceDefinitionV2Dot1EmailType
from datadog_api_client.v2.model.service_definition_v2_dot1_integrations import ServiceDefinitionV2Dot1Integrations
from datadog_api_client.v2.model.service_definition_v2_dot1_link import ServiceDefinitionV2Dot1Link
from datadog_api_client.v2.model.service_definition_v2_dot1_link_type import ServiceDefinitionV2Dot1LinkType
from datadog_api_client.v2.model.service_definition_v2_dot1_opsgenie import ServiceDefinitionV2Dot1Opsgenie
from datadog_api_client.v2.model.service_definition_v2_dot1_opsgenie_region import ServiceDefinitionV2Dot1OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_dot1_pagerduty import ServiceDefinitionV2Dot1Pagerduty
from datadog_api_client.v2.model.service_definition_v2_dot1_version import ServiceDefinitionV2Dot1Version

body = ServiceDefinitionV2Dot1(
    contacts=[
        ServiceDefinitionV2Dot1Email(
            contact="contact@datadoghq.com",
            name="Team Email",
            type=ServiceDefinitionV2Dot1EmailType.EMAIL,
        ),
    ],
    dd_service="service-exampleservicedefinition",
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Dot1Integrations(
        opsgenie=ServiceDefinitionV2Dot1Opsgenie(
            region=ServiceDefinitionV2Dot1OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty=ServiceDefinitionV2Dot1Pagerduty(
            service_url="https://my-org.pagerduty.com/service-directory/PMyService",
        ),
    ),
    links=[
        ServiceDefinitionV2Dot1Link(
            name="Runbook",
            type=ServiceDefinitionV2Dot1LinkType.RUNBOOK,
            url="https://my-runbook",
        ),
        ServiceDefinitionV2Dot1Link(
            name="Source Code",
            type=ServiceDefinitionV2Dot1LinkType.REPO,
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
        ServiceDefinitionV2Dot1Link(
            name="Architecture",
            type=ServiceDefinitionV2Dot1LinkType.DOC,
            provider="Gigoogle drivetHub",
            url="https://my-runbook",
        ),
    ],
    schema_version=ServiceDefinitionV2Dot1Version.V2_1,
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

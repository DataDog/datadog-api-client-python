"""
Create or update service definition using schema v2-2 returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_definition_api import ServiceDefinitionApi
from datadog_api_client.v2.model.service_definition_v2_dot2 import ServiceDefinitionV2Dot2
from datadog_api_client.v2.model.service_definition_v2_dot2_contact import ServiceDefinitionV2Dot2Contact
from datadog_api_client.v2.model.service_definition_v2_dot2_integrations import ServiceDefinitionV2Dot2Integrations
from datadog_api_client.v2.model.service_definition_v2_dot2_link import ServiceDefinitionV2Dot2Link
from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie import ServiceDefinitionV2Dot2Opsgenie
from datadog_api_client.v2.model.service_definition_v2_dot2_opsgenie_region import ServiceDefinitionV2Dot2OpsgenieRegion
from datadog_api_client.v2.model.service_definition_v2_dot2_pagerduty import ServiceDefinitionV2Dot2Pagerduty
from datadog_api_client.v2.model.service_definition_v2_dot2_version import ServiceDefinitionV2Dot2Version

body = ServiceDefinitionV2Dot2(
    contacts=[
        ServiceDefinitionV2Dot2Contact(
            contact="contact@datadoghq.com",
            name="Team Email",
            type="email",
        ),
    ],
    dd_service="service-exampleservicedefinition",
    extensions=dict([("myorgextension", "extensionvalue")]),
    integrations=ServiceDefinitionV2Dot2Integrations(
        opsgenie=ServiceDefinitionV2Dot2Opsgenie(
            region=ServiceDefinitionV2Dot2OpsgenieRegion.US,
            service_url="https://my-org.opsgenie.com/service/123e4567-e89b-12d3-a456-426614174000",
        ),
        pagerduty=ServiceDefinitionV2Dot2Pagerduty(
            service_url="https://my-org.pagerduty.com/service-directory/PMyService",
        ),
    ),
    links=[
        ServiceDefinitionV2Dot2Link(
            name="Runbook",
            type="runbook",
            url="https://my-runbook",
        ),
        ServiceDefinitionV2Dot2Link(
            name="Source Code",
            type="repo",
            provider="GitHub",
            url="https://github.com/DataDog/schema",
        ),
        ServiceDefinitionV2Dot2Link(
            name="Architecture",
            type="doc",
            provider="Gigoogle drivetHub",
            url="https://my-runbook",
        ),
    ],
    schema_version=ServiceDefinitionV2Dot2Version.V2_2,
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

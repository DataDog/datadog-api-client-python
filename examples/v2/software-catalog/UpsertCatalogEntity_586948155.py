"""
Create or update software catalog entity using schema v3 returns "ACCEPTED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.software_catalog_api import SoftwareCatalogApi
from datadog_api_client.v2.model.entity_v3_api_version import EntityV3APIVersion
from datadog_api_client.v2.model.entity_v3_datadog_code_location_item import EntityV3DatadogCodeLocationItem
from datadog_api_client.v2.model.entity_v3_datadog_event_item import EntityV3DatadogEventItem
from datadog_api_client.v2.model.entity_v3_datadog_integration_opsgenie import EntityV3DatadogIntegrationOpsgenie
from datadog_api_client.v2.model.entity_v3_datadog_integration_pagerduty import EntityV3DatadogIntegrationPagerduty
from datadog_api_client.v2.model.entity_v3_datadog_log_item import EntityV3DatadogLogItem
from datadog_api_client.v2.model.entity_v3_datadog_performance import EntityV3DatadogPerformance
from datadog_api_client.v2.model.entity_v3_datadog_pipelines import EntityV3DatadogPipelines
from datadog_api_client.v2.model.entity_v3_integrations import EntityV3Integrations
from datadog_api_client.v2.model.entity_v3_metadata import EntityV3Metadata
from datadog_api_client.v2.model.entity_v3_metadata_contacts_items import EntityV3MetadataContactsItems
from datadog_api_client.v2.model.entity_v3_metadata_links_items import EntityV3MetadataLinksItems
from datadog_api_client.v2.model.entity_v3_service import EntityV3Service
from datadog_api_client.v2.model.entity_v3_service_datadog import EntityV3ServiceDatadog
from datadog_api_client.v2.model.entity_v3_service_kind import EntityV3ServiceKind
from datadog_api_client.v2.model.entity_v3_service_spec import EntityV3ServiceSpec

body = EntityV3Service(
    api_version=EntityV3APIVersion.V3,
    datadog=EntityV3ServiceDatadog(
        code_locations=[
            EntityV3DatadogCodeLocationItem(
                paths=[],
            ),
        ],
        events=[
            EntityV3DatadogEventItem(),
        ],
        logs=[
            EntityV3DatadogLogItem(),
        ],
        performance_data=EntityV3DatadogPerformance(
            tags=[],
        ),
        pipelines=EntityV3DatadogPipelines(
            fingerprints=[],
        ),
    ),
    integrations=EntityV3Integrations(
        opsgenie=EntityV3DatadogIntegrationOpsgenie(
            service_url="https://www.opsgenie.com/service/shopping-cart",
        ),
        pagerduty=EntityV3DatadogIntegrationPagerduty(
            service_url="https://www.pagerduty.com/service-directory/Pshopping-cart",
        ),
    ),
    kind=EntityV3ServiceKind.SERVICE,
    metadata=EntityV3Metadata(
        additional_owners=[],
        contacts=[
            EntityV3MetadataContactsItems(
                contact="https://slack/",
                type="slack",
            ),
        ],
        id="4b163705-23c0-4573-b2fb-f6cea2163fcb",
        inherit_from="application:default/myapp",
        links=[
            EntityV3MetadataLinksItems(
                name="mylink",
                type="link",
                url="https://mylink",
            ),
        ],
        name="service-examplesoftwarecatalog",
        tags=[
            "this:tag",
            "that:tag",
        ],
    ),
    spec=EntityV3ServiceSpec(
        depends_on=[],
        languages=[],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SoftwareCatalogApi(api_client)
    response = api_instance.upsert_catalog_entity(body=body)

    print(response)

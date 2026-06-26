"""
Import security vulnerabilities returns "Vulnerabilities accepted successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.cyclone_dx_bom import CycloneDXBom
from datadog_api_client.v2.model.cyclone_dx_component import CycloneDXComponent
from datadog_api_client.v2.model.cyclone_dx_component_type import CycloneDXComponentType
from datadog_api_client.v2.model.cyclone_dx_metadata import CycloneDXMetadata
from datadog_api_client.v2.model.cyclone_dx_metadata_component import CycloneDXMetadataComponent
from datadog_api_client.v2.model.cyclone_dx_metadata_tools import CycloneDXMetadataTools
from datadog_api_client.v2.model.cyclone_dx_tool_component import CycloneDXToolComponent
from datadog_api_client.v2.model.cyclone_dx_vulnerability import CycloneDXVulnerability
from datadog_api_client.v2.model.cyclone_dx_vulnerability_advisory import CycloneDXVulnerabilityAdvisory
from datadog_api_client.v2.model.cyclone_dx_vulnerability_affects import CycloneDXVulnerabilityAffects
from datadog_api_client.v2.model.cyclone_dx_vulnerability_analysis import CycloneDXVulnerabilityAnalysis
from datadog_api_client.v2.model.cyclone_dx_vulnerability_rating import CycloneDXVulnerabilityRating
from datadog_api_client.v2.model.cyclone_dx_vulnerability_reference import CycloneDXVulnerabilityReference
from datadog_api_client.v2.model.cyclone_dx_vulnerability_reference_source import CycloneDXVulnerabilityReferenceSource

body = CycloneDXBom(
    bom_format="CycloneDX",
    components=[
        CycloneDXComponent(
            bom_ref="a3390fca-c315-41ae-ae05-af5e7859cdee",
            name="lodash",
            purl="pkg:npm/lodash@4.17.21",
            type=CycloneDXComponentType.LIBRARY,
            version="4.17.21",
        ),
    ],
    metadata=CycloneDXMetadata(
        component=CycloneDXMetadataComponent(
            bom_ref="host-ref-abc123",
            name="i-12345",
            type="operating-system",
        ),
        tools=CycloneDXMetadataTools(
            components=[
                CycloneDXToolComponent(
                    name="my-scanner",
                    type="application",
                ),
            ],
        ),
    ),
    spec_version="1.5",
    version=1,
    vulnerabilities=[
        CycloneDXVulnerability(
            advisories=[
                CycloneDXVulnerabilityAdvisory(
                    url="https://example.com/advisory/CVE-2021-1234",
                ),
            ],
            affects=[
                CycloneDXVulnerabilityAffects(
                    ref="a3390fca-c315-41ae-ae05-af5e7859cdee",
                ),
            ],
            analysis=CycloneDXVulnerabilityAnalysis(
                state="resolved",
            ),
            cwes=[
                123,
                345,
            ],
            description="Sample vulnerability detected in the application.",
            detail="Details about the vulnerability.",
            id="CVE-2021-1234",
            ratings=[
                CycloneDXVulnerabilityRating(
                    score=9.0,
                    severity="high",
                    vector="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N",
                ),
            ],
            references=[
                CycloneDXVulnerabilityReference(
                    id="GHSA-35m5-8cvj-8783",
                    source=CycloneDXVulnerabilityReferenceSource(
                        url="https://example.com",
                    ),
                ),
            ],
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["import_security_vulnerabilities"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.import_security_vulnerabilities(body=body)

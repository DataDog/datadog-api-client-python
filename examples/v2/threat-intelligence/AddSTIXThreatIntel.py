"""
Ingest STIX threat intelligence returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.threat_intelligence_api import ThreatIntelligenceApi
from datadog_api_client.v2.model.stix_bundle_request import STIXBundleRequest
from datadog_api_client.v2.model.stix_bundle_type import STIXBundleType
from datadog_api_client.v2.model.stix_object import STIXObject
from datadog_api_client.v2.model.stix_pattern_type import STIXPatternType
from datadog_api_client.v2.model.stix_spec_version import STIXSpecVersion
from datetime import datetime
from dateutil.tz import tzutc

body = STIXBundleRequest(
    id="bundle--44444444-4444-4444-8444-444444444444",
    objects=[
        STIXObject(
            created=datetime(2026, 7, 22, 12, 0, tzinfo=tzutc()),
            id="indicator--55555555-5555-4555-8555-555555555555",
            modified=datetime(2026, 7, 22, 12, 0, tzinfo=tzutc()),
            pattern="[ipv4-addr:value = '198.51.100.42']",
            pattern_type=STIXPatternType.STIX,
            spec_version="2.1",
            type="indicator",
            valid_from=datetime(2026, 7, 22, 12, 0, tzinfo=tzutc()),
        ),
    ],
    spec_version=STIXSpecVersion.VERSION_2_1,
    type=STIXBundleType.BUNDLE,
)

configuration = Configuration()
configuration.unstable_operations["add_stix_threat_intel"] = True
with ApiClient(configuration) as api_client:
    api_instance = ThreatIntelligenceApi(api_client)
    response = api_instance.add_stix_threat_intel(ti_vendor="Acme-Inc", body=body)

    print(response)

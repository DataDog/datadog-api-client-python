"""
Update a WAF exclusion filter returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.application_security_api import ApplicationSecurityApi
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_on_match import (
    ApplicationSecurityWafExclusionFilterOnMatch,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
    ApplicationSecurityWafExclusionFilterType,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_attributes import (
    ApplicationSecurityWafExclusionFilterUpdateAttributes,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_data import (
    ApplicationSecurityWafExclusionFilterUpdateData,
)
from datadog_api_client.v2.model.application_security_waf_exclusion_filter_update_request import (
    ApplicationSecurityWafExclusionFilterUpdateRequest,
)

# there is a valid "exclusion_filter" in the system
EXCLUSION_FILTER_DATA_ID = environ["EXCLUSION_FILTER_DATA_ID"]

body = ApplicationSecurityWafExclusionFilterUpdateRequest(
    data=ApplicationSecurityWafExclusionFilterUpdateData(
        attributes=ApplicationSecurityWafExclusionFilterUpdateAttributes(
            description="Exclude false positives on a path",
            enabled=False,
            ip_list=[
                "198.51.100.72",
            ],
            on_match=ApplicationSecurityWafExclusionFilterOnMatch.MONITOR,
        ),
        type=ApplicationSecurityWafExclusionFilterType.EXCLUSION_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ApplicationSecurityApi(api_client)
    response = api_instance.update_application_security_waf_exclusion_filter(
        exclusion_filter_id=EXCLUSION_FILTER_DATA_ID, body=body
    )

    print(response)

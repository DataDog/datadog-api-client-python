# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_content_pack_state_details import (
        SecurityMonitoringContentPackStateDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_status import SecurityMonitoringContentPackStatus
    from datadog_api_client.v2.model.security_monitoring_content_pack_logs_details import (
        SecurityMonitoringContentPackLogsDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_threat_intel_details import (
        SecurityMonitoringContentPackThreatIntelDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_entity_details import (
        SecurityMonitoringContentPackEntityDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_audit_details import (
        SecurityMonitoringContentPackAuditDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_app_sec_details import (
        SecurityMonitoringContentPackAppSecDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_vulnerability_details import (
        SecurityMonitoringContentPackVulnerabilityDetails,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_onboarding_details import (
        SecurityMonitoringContentPackOnboardingDetails,
    )


class SecurityMonitoringContentPackStateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_state_details import (
            SecurityMonitoringContentPackStateDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_status import (
            SecurityMonitoringContentPackStatus,
        )

        return {
            "details": (SecurityMonitoringContentPackStateDetails,),
            "status": (SecurityMonitoringContentPackStatus,),
        }

    attribute_map = {
        "details": "details",
        "status": "status",
    }

    def __init__(
        self_,
        details: Union[
            SecurityMonitoringContentPackStateDetails,
            SecurityMonitoringContentPackLogsDetails,
            SecurityMonitoringContentPackThreatIntelDetails,
            SecurityMonitoringContentPackEntityDetails,
            SecurityMonitoringContentPackAuditDetails,
            SecurityMonitoringContentPackAppSecDetails,
            SecurityMonitoringContentPackVulnerabilityDetails,
            SecurityMonitoringContentPackOnboardingDetails,
        ],
        status: SecurityMonitoringContentPackStatus,
        **kwargs,
    ):
        """
        Attributes of a content pack state.

        :param details: Type-specific details for a content pack state. The set of fields present depends
            on the content pack's ``type``. When Cloud SIEM is inactive for the requesting organization, ``onboarding`` is returned instead of the content pack's usual type, such as ``logs`` or ``vulnerability``.`
        :type details: SecurityMonitoringContentPackStateDetails

        :param status: The current operational status of a content pack.
        :type status: SecurityMonitoringContentPackStatus
        """
        super().__init__(kwargs)

        self_.details = details
        self_.status = status

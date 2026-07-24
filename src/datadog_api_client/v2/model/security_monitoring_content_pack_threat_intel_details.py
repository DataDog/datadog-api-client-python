# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_content_pack_activation import (
        SecurityMonitoringContentPackActivation,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_timestamp_bucket import (
        SecurityMonitoringContentPackTimestampBucket,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_integration_status import (
        SecurityMonitoringContentPackIntegrationStatus,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_threat_intel_details_type import (
        SecurityMonitoringContentPackThreatIntelDetailsType,
    )


class SecurityMonitoringContentPackThreatIntelDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_activation import (
            SecurityMonitoringContentPackActivation,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_timestamp_bucket import (
            SecurityMonitoringContentPackTimestampBucket,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_integration_status import (
            SecurityMonitoringContentPackIntegrationStatus,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_threat_intel_details_type import (
            SecurityMonitoringContentPackThreatIntelDetailsType,
        )

        return {
            "cp_activation": (SecurityMonitoringContentPackActivation,),
            "data_last_seen": (SecurityMonitoringContentPackTimestampBucket,),
            "integration_installed_status": (SecurityMonitoringContentPackIntegrationStatus,),
            "type": (SecurityMonitoringContentPackThreatIntelDetailsType,),
        }

    attribute_map = {
        "cp_activation": "cp_activation",
        "data_last_seen": "data_last_seen",
        "integration_installed_status": "integration_installed_status",
        "type": "type",
    }

    def __init__(
        self_,
        cp_activation: SecurityMonitoringContentPackActivation,
        data_last_seen: SecurityMonitoringContentPackTimestampBucket,
        integration_installed_status: SecurityMonitoringContentPackIntegrationStatus,
        type: SecurityMonitoringContentPackThreatIntelDetailsType,
        **kwargs,
    ):
        """
        Details for a threat intelligence content pack.

        :param cp_activation: The activation status of a content pack.
        :type cp_activation: SecurityMonitoringContentPackActivation

        :param data_last_seen: Timestamp bucket indicating when logs were last collected.
        :type data_last_seen: SecurityMonitoringContentPackTimestampBucket

        :param integration_installed_status: The installation status of the related integration.
        :type integration_installed_status: SecurityMonitoringContentPackIntegrationStatus

        :param type: Type for threat intelligence content pack details.
        :type type: SecurityMonitoringContentPackThreatIntelDetailsType
        """
        super().__init__(kwargs)

        self_.cp_activation = cp_activation
        self_.data_last_seen = data_last_seen
        self_.integration_installed_status = integration_installed_status
        self_.type = type

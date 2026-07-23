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
    from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType


class SecurityMonitoringContentPackLogsDetails(ModelNormal):
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
        from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

        return {
            "cp_activation": (SecurityMonitoringContentPackActivation,),
            "data_last_seen": (SecurityMonitoringContentPackTimestampBucket,),
            "filters_configured": (bool,),
            "integration_installed_status": (SecurityMonitoringContentPackIntegrationStatus,),
            "logs_seen_from_any_index": (bool,),
            "siem_index_incorrect": (bool,),
            "type": (SecurityFilterFilteredDataType,),
        }

    attribute_map = {
        "cp_activation": "cp_activation",
        "data_last_seen": "data_last_seen",
        "filters_configured": "filters_configured",
        "integration_installed_status": "integration_installed_status",
        "logs_seen_from_any_index": "logs_seen_from_any_index",
        "siem_index_incorrect": "siem_index_incorrect",
        "type": "type",
    }

    def __init__(
        self_,
        cp_activation: SecurityMonitoringContentPackActivation,
        data_last_seen: SecurityMonitoringContentPackTimestampBucket,
        filters_configured: bool,
        integration_installed_status: SecurityMonitoringContentPackIntegrationStatus,
        logs_seen_from_any_index: bool,
        siem_index_incorrect: bool,
        type: SecurityFilterFilteredDataType,
        **kwargs,
    ):
        """
        Details for a logs-based content pack.

        :param cp_activation: The activation status of a content pack.
        :type cp_activation: SecurityMonitoringContentPackActivation

        :param data_last_seen: Timestamp bucket indicating when logs were last collected.
        :type data_last_seen: SecurityMonitoringContentPackTimestampBucket

        :param filters_configured: Whether filters (Security Filters or Index Query depending on the pricing model) are
            present and correctly configured to route logs into Cloud SIEM.
        :type filters_configured: bool

        :param integration_installed_status: The installation status of the related integration.
        :type integration_installed_status: SecurityMonitoringContentPackIntegrationStatus

        :param logs_seen_from_any_index: Whether logs for this content pack have been seen in any Datadog index in the last 72 hours.
        :type logs_seen_from_any_index: bool

        :param siem_index_incorrect: Whether the Cloud SIEM index configuration is incorrect (only applies to certain pricing models).
        :type siem_index_incorrect: bool

        :param type: The filtered data type.
        :type type: SecurityFilterFilteredDataType
        """
        super().__init__(kwargs)

        self_.cp_activation = cp_activation
        self_.data_last_seen = data_last_seen
        self_.filters_configured = filters_configured
        self_.integration_installed_status = integration_installed_status
        self_.logs_seen_from_any_index = logs_seen_from_any_index
        self_.siem_index_incorrect = siem_index_incorrect
        self_.type = type

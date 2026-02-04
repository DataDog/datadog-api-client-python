# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_content_pack_activation import (
        SecurityMonitoringContentPackActivation,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_integration_status import (
        SecurityMonitoringContentPackIntegrationStatus,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_timestamp_bucket import (
        SecurityMonitoringContentPackTimestampBucket,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_status import SecurityMonitoringContentPackStatus


class SecurityMonitoringContentPackStateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_activation import (
            SecurityMonitoringContentPackActivation,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_integration_status import (
            SecurityMonitoringContentPackIntegrationStatus,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_timestamp_bucket import (
            SecurityMonitoringContentPackTimestampBucket,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_status import (
            SecurityMonitoringContentPackStatus,
        )

        return {
            "cloud_siem_index_incorrect": (bool,),
            "cp_activation": (SecurityMonitoringContentPackActivation,),
            "filters_configured_for_logs": (bool,),
            "integration_installed_status": (SecurityMonitoringContentPackIntegrationStatus,),
            "logs_last_collected": (SecurityMonitoringContentPackTimestampBucket,),
            "logs_seen_from_any_index": (bool,),
            "state": (SecurityMonitoringContentPackStatus,),
        }

    attribute_map = {
        "cloud_siem_index_incorrect": "cloud_siem_index_incorrect",
        "cp_activation": "cp_activation",
        "filters_configured_for_logs": "filters_configured_for_logs",
        "integration_installed_status": "integration_installed_status",
        "logs_last_collected": "logs_last_collected",
        "logs_seen_from_any_index": "logs_seen_from_any_index",
        "state": "state",
    }

    def __init__(
        self_,
        cloud_siem_index_incorrect: bool,
        cp_activation: SecurityMonitoringContentPackActivation,
        filters_configured_for_logs: bool,
        logs_last_collected: SecurityMonitoringContentPackTimestampBucket,
        logs_seen_from_any_index: bool,
        state: SecurityMonitoringContentPackStatus,
        integration_installed_status: Union[SecurityMonitoringContentPackIntegrationStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a content pack state

        :param cloud_siem_index_incorrect: Whether the cloud SIEM index configuration is incorrect (only applies to certain pricing models)
        :type cloud_siem_index_incorrect: bool

        :param cp_activation: The activation status of a content pack
        :type cp_activation: SecurityMonitoringContentPackActivation

        :param filters_configured_for_logs: Whether filters (Security Filters or Index Query depending on the pricing model) are configured for logs
        :type filters_configured_for_logs: bool

        :param integration_installed_status: The installation status of the related integration
        :type integration_installed_status: SecurityMonitoringContentPackIntegrationStatus, optional

        :param logs_last_collected: Timestamp bucket indicating when logs were last collected
        :type logs_last_collected: SecurityMonitoringContentPackTimestampBucket

        :param logs_seen_from_any_index: Whether logs have been seen from any index
        :type logs_seen_from_any_index: bool

        :param state: The current status of a content pack
        :type state: SecurityMonitoringContentPackStatus
        """
        if integration_installed_status is not unset:
            kwargs["integration_installed_status"] = integration_installed_status
        super().__init__(kwargs)

        self_.cloud_siem_index_incorrect = cloud_siem_index_incorrect
        self_.cp_activation = cp_activation
        self_.filters_configured_for_logs = filters_configured_for_logs
        self_.logs_last_collected = logs_last_collected
        self_.logs_seen_from_any_index = logs_seen_from_any_index
        self_.state = state

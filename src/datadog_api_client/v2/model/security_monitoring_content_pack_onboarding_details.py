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
    from datadog_api_client.v2.model.security_monitoring_content_pack_integration_status import (
        SecurityMonitoringContentPackIntegrationStatus,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_onboarding_details_type import (
        SecurityMonitoringContentPackOnboardingDetailsType,
    )


class SecurityMonitoringContentPackOnboardingDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_integration_status import (
            SecurityMonitoringContentPackIntegrationStatus,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_onboarding_details_type import (
            SecurityMonitoringContentPackOnboardingDetailsType,
        )

        return {
            "integration_installed_status": (SecurityMonitoringContentPackIntegrationStatus,),
            "logs_seen_from_any_index": (bool,),
            "type": (SecurityMonitoringContentPackOnboardingDetailsType,),
        }

    attribute_map = {
        "integration_installed_status": "integration_installed_status",
        "logs_seen_from_any_index": "logs_seen_from_any_index",
        "type": "type",
    }

    def __init__(
        self_,
        logs_seen_from_any_index: bool,
        type: SecurityMonitoringContentPackOnboardingDetailsType,
        integration_installed_status: Union[SecurityMonitoringContentPackIntegrationStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Content pack details returned when Cloud SIEM is inactive for the requesting organization.

        :param integration_installed_status: The installation status of the related integration.
        :type integration_installed_status: SecurityMonitoringContentPackIntegrationStatus, optional

        :param logs_seen_from_any_index: Whether logs for this content pack have been seen in any Datadog index in the last 72 hours.
        :type logs_seen_from_any_index: bool

        :param type: Type for onboarding content pack details.
        :type type: SecurityMonitoringContentPackOnboardingDetailsType
        """
        if integration_installed_status is not unset:
            kwargs["integration_installed_status"] = integration_installed_status
        super().__init__(kwargs)

        self_.logs_seen_from_any_index = logs_seen_from_any_index
        self_.type = type

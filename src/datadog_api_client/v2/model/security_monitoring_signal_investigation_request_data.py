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
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_request_attributes import (
        SecurityMonitoringSignalInvestigationRequestAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_type import (
        SecurityMonitoringSignalInvestigationType,
    )


class SecurityMonitoringSignalInvestigationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_request_attributes import (
            SecurityMonitoringSignalInvestigationRequestAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_type import (
            SecurityMonitoringSignalInvestigationType,
        )

        return {
            "attributes": (SecurityMonitoringSignalInvestigationRequestAttributes,),
            "type": (SecurityMonitoringSignalInvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalInvestigationRequestAttributes,
        type: SecurityMonitoringSignalInvestigationType,
        **kwargs,
    ):
        """
        Data for creating a signal investigation.

        :param attributes: Attributes for creating a signal investigation.
        :type attributes: SecurityMonitoringSignalInvestigationRequestAttributes

        :param type: The type of investigation signal.
        :type type: SecurityMonitoringSignalInvestigationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

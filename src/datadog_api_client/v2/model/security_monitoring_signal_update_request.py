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
    from datadog_api_client.v2.model.security_monitoring_signal_update_data import SecurityMonitoringSignalUpdateData


class SecurityMonitoringSignalUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_update_data import (
            SecurityMonitoringSignalUpdateData,
        )

        return {
            "data": (SecurityMonitoringSignalUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityMonitoringSignalUpdateData, **kwargs):
        """
        Request body for updating the triage state or assignee of a security signal.

        :param data: Data containing the triage state or assignee update for a security signal.
        :type data: SecurityMonitoringSignalUpdateData
        """
        super().__init__(kwargs)

        self_.data = data

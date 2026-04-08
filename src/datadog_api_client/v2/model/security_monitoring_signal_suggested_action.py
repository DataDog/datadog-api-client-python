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
    from datadog_api_client.v2.model.security_monitoring_signal_suggested_action_attributes import (
        SecurityMonitoringSignalSuggestedActionAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_suggested_action_type import (
        SecurityMonitoringSignalSuggestedActionType,
    )


class SecurityMonitoringSignalSuggestedAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_suggested_action_attributes import (
            SecurityMonitoringSignalSuggestedActionAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_suggested_action_type import (
            SecurityMonitoringSignalSuggestedActionType,
        )

        return {
            "attributes": (SecurityMonitoringSignalSuggestedActionAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringSignalSuggestedActionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalSuggestedActionAttributes,
        id: str,
        type: SecurityMonitoringSignalSuggestedActionType,
        **kwargs,
    ):
        """
        A suggested action for a security signal.

        :param attributes: Attributes of a suggested action for a security signal. The available fields depend on the action type.
        :type attributes: SecurityMonitoringSignalSuggestedActionAttributes

        :param id: The unique ID of the suggested action.
        :type id: str

        :param type: The type of the suggested action resource.
        :type type: SecurityMonitoringSignalSuggestedActionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type

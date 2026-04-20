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
    from datadog_api_client.v2.model.security_monitoring_signal_update_attributes import (
        SecurityMonitoringSignalUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_type import SecurityMonitoringSignalType


class SecurityMonitoringSignalsBulkUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_update_attributes import (
            SecurityMonitoringSignalUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_type import SecurityMonitoringSignalType

        return {
            "attributes": (SecurityMonitoringSignalUpdateAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringSignalType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalUpdateAttributes,
        id: str,
        type: Union[SecurityMonitoringSignalType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for updating a single security signal in a bulk update operation.

        :param attributes: Attributes for updating the triage state or assignee of a security signal.
        :type attributes: SecurityMonitoringSignalUpdateAttributes

        :param id: The unique ID of the security signal.
        :type id: str

        :param type: The type of event.
        :type type: SecurityMonitoringSignalType, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_signal_state_update_attributes import (
        SecurityMonitoringSignalStateUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import (
        SecurityMonitoringSignalMetadataType,
    )


class SecurityMonitoringSignalStateUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_state_update_attributes import (
            SecurityMonitoringSignalStateUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import (
            SecurityMonitoringSignalMetadataType,
        )

        return {
            "attributes": (SecurityMonitoringSignalStateUpdateAttributes,),
            "id": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "type": (SecurityMonitoringSignalMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalStateUpdateAttributes,
        id: Union[Any, UnsetType] = unset,
        type: Union[SecurityMonitoringSignalMetadataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data containing the patch for changing the state of a signal.

        :param attributes: Attributes describing the change of state of a security signal.
        :type attributes: SecurityMonitoringSignalStateUpdateAttributes

        :param id: The unique ID of the security signal.
        :type id: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param type: The type of event.
        :type type: SecurityMonitoringSignalMetadataType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes

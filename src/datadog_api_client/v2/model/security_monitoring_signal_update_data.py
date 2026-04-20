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
    from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import (
        SecurityMonitoringSignalMetadataType,
    )


class SecurityMonitoringSignalUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_update_attributes import (
            SecurityMonitoringSignalUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import (
            SecurityMonitoringSignalMetadataType,
        )

        return {
            "attributes": (SecurityMonitoringSignalUpdateAttributes,),
            "type": (SecurityMonitoringSignalMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSignalUpdateAttributes,
        type: Union[SecurityMonitoringSignalMetadataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data containing the triage state or assignee update for a security signal.

        :param attributes: Attributes for updating the triage state or assignee of a security signal.
        :type attributes: SecurityMonitoringSignalUpdateAttributes

        :param type: The type of event.
        :type type: SecurityMonitoringSignalMetadataType, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes

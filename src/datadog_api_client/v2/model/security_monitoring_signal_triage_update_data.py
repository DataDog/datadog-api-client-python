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
    from datadog_api_client.v2.model.security_monitoring_signal_triage_attributes import (
        SecurityMonitoringSignalTriageAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import (
        SecurityMonitoringSignalMetadataType,
    )


class SecurityMonitoringSignalTriageUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_triage_attributes import (
            SecurityMonitoringSignalTriageAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_metadata_type import (
            SecurityMonitoringSignalMetadataType,
        )

        return {
            "attributes": (SecurityMonitoringSignalTriageAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringSignalMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SecurityMonitoringSignalTriageAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityMonitoringSignalMetadataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data containing the updated triage attributes of the signal.

        :param attributes: Attributes describing a triage state update operation over a security signal.
        :type attributes: SecurityMonitoringSignalTriageAttributes, optional

        :param id: The unique ID of the security signal.
        :type id: str, optional

        :param type: The type of event.
        :type type: SecurityMonitoringSignalMetadataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

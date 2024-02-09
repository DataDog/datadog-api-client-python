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
    from datadog_api_client.v2.model.security_monitoring_suppression_attributes import (
        SecurityMonitoringSuppressionAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_suppression_type import SecurityMonitoringSuppressionType


class SecurityMonitoringSuppression(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_suppression_attributes import (
            SecurityMonitoringSuppressionAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_suppression_type import SecurityMonitoringSuppressionType

        return {
            "attributes": (SecurityMonitoringSuppressionAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringSuppressionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SecurityMonitoringSuppressionAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityMonitoringSuppressionType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The suppression rule's properties.

        :param attributes: The attributes of the suppression rule.
        :type attributes: SecurityMonitoringSuppressionAttributes, optional

        :param id: The ID of the suppression rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``suppressions``.
        :type type: SecurityMonitoringSuppressionType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

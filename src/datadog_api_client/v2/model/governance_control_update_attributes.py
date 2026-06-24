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
    from datadog_api_client.v2.model.governance_control_parameters_map import GovernanceControlParametersMap


class GovernanceControlUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_parameters_map import GovernanceControlParametersMap

        return {
            "detection_frequency": (str,),
            "detection_parameters": (GovernanceControlParametersMap,),
            "mitigation_parameters": (GovernanceControlParametersMap,),
            "mitigation_type": (str,),
            "name": (str,),
            "notification_frequency": (str,),
            "notification_parameters": (GovernanceControlParametersMap,),
            "notification_type": (str,),
        }

    attribute_map = {
        "detection_frequency": "detection_frequency",
        "detection_parameters": "detection_parameters",
        "mitigation_parameters": "mitigation_parameters",
        "mitigation_type": "mitigation_type",
        "name": "name",
        "notification_frequency": "notification_frequency",
        "notification_parameters": "notification_parameters",
        "notification_type": "notification_type",
    }

    def __init__(
        self_,
        detection_frequency: Union[str, UnsetType] = unset,
        detection_parameters: Union[GovernanceControlParametersMap, UnsetType] = unset,
        mitigation_parameters: Union[GovernanceControlParametersMap, UnsetType] = unset,
        mitigation_type: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        notification_frequency: Union[str, UnsetType] = unset,
        notification_parameters: Union[GovernanceControlParametersMap, UnsetType] = unset,
        notification_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance control that can be updated. Only the attributes present in the request are modified.

        :param detection_frequency: How often detections should be evaluated for the control.
        :type detection_frequency: str, optional

        :param detection_parameters: A free-form map of parameter names to their configured values.
        :type detection_parameters: GovernanceControlParametersMap, optional

        :param mitigation_parameters: A free-form map of parameter names to their configured values.
        :type mitigation_parameters: GovernanceControlParametersMap, optional

        :param mitigation_type: The mitigation type to configure for the control.
        :type mitigation_type: str, optional

        :param name: A new human-readable name for the control.
        :type name: str, optional

        :param notification_frequency: The notification frequency to configure for the control.
        :type notification_frequency: str, optional

        :param notification_parameters: A free-form map of parameter names to their configured values.
        :type notification_parameters: GovernanceControlParametersMap, optional

        :param notification_type: The notification type to configure for the control.
        :type notification_type: str, optional
        """
        if detection_frequency is not unset:
            kwargs["detection_frequency"] = detection_frequency
        if detection_parameters is not unset:
            kwargs["detection_parameters"] = detection_parameters
        if mitigation_parameters is not unset:
            kwargs["mitigation_parameters"] = mitigation_parameters
        if mitigation_type is not unset:
            kwargs["mitigation_type"] = mitigation_type
        if name is not unset:
            kwargs["name"] = name
        if notification_frequency is not unset:
            kwargs["notification_frequency"] = notification_frequency
        if notification_parameters is not unset:
            kwargs["notification_parameters"] = notification_parameters
        if notification_type is not unset:
            kwargs["notification_type"] = notification_type
        super().__init__(kwargs)

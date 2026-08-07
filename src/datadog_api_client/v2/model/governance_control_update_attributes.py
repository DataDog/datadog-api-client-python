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
            "detection_parameters": (GovernanceControlParametersMap,),
            "mitigation_parameters": (GovernanceControlParametersMap,),
            "mitigation_type": (str,),
        }

    attribute_map = {
        "detection_parameters": "detection_parameters",
        "mitigation_parameters": "mitigation_parameters",
        "mitigation_type": "mitigation_type",
    }

    def __init__(
        self_,
        detection_parameters: Union[GovernanceControlParametersMap, UnsetType] = unset,
        mitigation_parameters: Union[GovernanceControlParametersMap, UnsetType] = unset,
        mitigation_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance control that can be updated. Only the attributes present in the request are modified.

        :param detection_parameters: A free-form map of parameter names to their configured values.
        :type detection_parameters: GovernanceControlParametersMap, optional

        :param mitigation_parameters: A free-form map of parameter names to their configured values.
        :type mitigation_parameters: GovernanceControlParametersMap, optional

        :param mitigation_type: The mitigation type to configure for the control.
        :type mitigation_type: str, optional
        """
        if detection_parameters is not unset:
            kwargs["detection_parameters"] = detection_parameters
        if mitigation_parameters is not unset:
            kwargs["mitigation_parameters"] = mitigation_parameters
        if mitigation_type is not unset:
            kwargs["mitigation_type"] = mitigation_type
        super().__init__(kwargs)

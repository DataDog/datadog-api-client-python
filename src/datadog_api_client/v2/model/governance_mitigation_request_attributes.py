# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_control_parameters_map import GovernanceControlParametersMap


class GovernanceMitigationRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_parameters_map import GovernanceControlParametersMap

        return {
            "detection_ids": ([str],),
            "detection_type": (str,),
            "mitigation_parameters": (GovernanceControlParametersMap,),
            "mitigation_type": (str,),
        }

    attribute_map = {
        "detection_ids": "detection_ids",
        "detection_type": "detection_type",
        "mitigation_parameters": "mitigation_parameters",
        "mitigation_type": "mitigation_type",
    }

    def __init__(
        self_,
        detection_ids: Union[List[str], UnsetType] = unset,
        detection_type: Union[str, UnsetType] = unset,
        mitigation_parameters: Union[GovernanceControlParametersMap, UnsetType] = unset,
        mitigation_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a governance mitigation request.

        :param detection_ids: The identifiers of the detections to mitigate in this request.
        :type detection_ids: [str], optional

        :param detection_type: The detection type whose detections should be mitigated.
        :type detection_type: str, optional

        :param mitigation_parameters: A free-form map of parameter names to their configured values.
        :type mitigation_parameters: GovernanceControlParametersMap, optional

        :param mitigation_type: The mitigation to apply to the selected detections. Defaults to the control's configured mitigation when omitted.
        :type mitigation_type: str, optional
        """
        if detection_ids is not unset:
            kwargs["detection_ids"] = detection_ids
        if detection_type is not unset:
            kwargs["detection_type"] = detection_type
        if mitigation_parameters is not unset:
            kwargs["mitigation_parameters"] = mitigation_parameters
        if mitigation_type is not unset:
            kwargs["mitigation_type"] = mitigation_type
        super().__init__(kwargs)

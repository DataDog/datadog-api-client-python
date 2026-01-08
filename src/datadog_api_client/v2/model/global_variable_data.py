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
    from datadog_api_client.v2.model.synthetics_global_variable import SyntheticsGlobalVariable
    from datadog_api_client.v2.model.global_variable_type import GlobalVariableType


class GlobalVariableData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_global_variable import SyntheticsGlobalVariable
        from datadog_api_client.v2.model.global_variable_type import GlobalVariableType

        return {
            "attributes": (SyntheticsGlobalVariable,),
            "id": (str,),
            "type": (GlobalVariableType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SyntheticsGlobalVariable, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GlobalVariableType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Synthetics global variable data. Wrapper around the global variable object.

        :param attributes: Synthetic global variable.
        :type attributes: SyntheticsGlobalVariable, optional

        :param id: Global variable identifier.
        :type id: str, optional

        :param type: Global variable type.
        :type type: GlobalVariableType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

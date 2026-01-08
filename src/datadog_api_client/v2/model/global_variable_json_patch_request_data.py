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
    from datadog_api_client.v2.model.global_variable_json_patch_request_data_attributes import (
        GlobalVariableJsonPatchRequestDataAttributes,
    )
    from datadog_api_client.v2.model.global_variable_json_patch_type import GlobalVariableJsonPatchType


class GlobalVariableJsonPatchRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_variable_json_patch_request_data_attributes import (
            GlobalVariableJsonPatchRequestDataAttributes,
        )
        from datadog_api_client.v2.model.global_variable_json_patch_type import GlobalVariableJsonPatchType

        return {
            "attributes": (GlobalVariableJsonPatchRequestDataAttributes,),
            "type": (GlobalVariableJsonPatchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GlobalVariableJsonPatchRequestDataAttributes, UnsetType] = unset,
        type: Union[GlobalVariableJsonPatchType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: GlobalVariableJsonPatchRequestDataAttributes, optional

        :param type: Global variable JSON Patch type.
        :type type: GlobalVariableJsonPatchType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.global_variable_json_patch_request_data import GlobalVariableJsonPatchRequestData


class GlobalVariableJsonPatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_variable_json_patch_request_data import (
            GlobalVariableJsonPatchRequestData,
        )

        return {
            "data": (GlobalVariableJsonPatchRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GlobalVariableJsonPatchRequestData, **kwargs):
        """
        JSON Patch request for global variable.

        :param data:
        :type data: GlobalVariableJsonPatchRequestData
        """
        super().__init__(kwargs)

        self_.data = data

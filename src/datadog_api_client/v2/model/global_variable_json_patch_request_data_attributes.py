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
    from datadog_api_client.v2.model.json_patch_operation import JsonPatchOperation


class GlobalVariableJsonPatchRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.json_patch_operation import JsonPatchOperation

        return {
            "json_patch": ([JsonPatchOperation],),
        }

    attribute_map = {
        "json_patch": "json_patch",
    }

    def __init__(self_, json_patch: Union[List[JsonPatchOperation], UnsetType] = unset, **kwargs):
        """


        :param json_patch: JSON Patch operations following RFC 6902.
        :type json_patch: [JsonPatchOperation], optional
        """
        if json_patch is not unset:
            kwargs["json_patch"] = json_patch
        super().__init__(kwargs)

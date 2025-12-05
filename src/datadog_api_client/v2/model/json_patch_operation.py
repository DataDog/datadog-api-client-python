# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.json_patch_operation_op import JsonPatchOperationOp


class JsonPatchOperation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.json_patch_operation_op import JsonPatchOperationOp

        return {
            "op": (JsonPatchOperationOp,),
            "path": (str,),
            "value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "op": "op",
        "path": "path",
        "value": "value",
    }

    def __init__(self_, op: JsonPatchOperationOp, path: str, value: Union[Any, UnsetType] = unset, **kwargs):
        """
        A JSON Patch operation as per RFC 6902.

        :param op: The operation to perform.
        :type op: JsonPatchOperationOp

        :param path: A JSON Pointer path (e.g., "/name", "/value/secure").
        :type path: str

        :param value: The value to use for the operation (not applicable for "remove" and "test" operations).
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.op = op
        self_.path = path

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
    from datadog_api_client.v1.model.synthetics_patch_test_operation_name import SyntheticsPatchTestOperationName


class SyntheticsPatchTestOperation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_patch_test_operation_name import SyntheticsPatchTestOperationName

        return {
            "op": (SyntheticsPatchTestOperationName,),
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

    def __init__(
        self_,
        op: Union[SyntheticsPatchTestOperationName, UnsetType] = unset,
        path: Union[str, UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single `JSON Patch <https://jsonpatch.com>`_ operation to perform on the test

        :param op: The operation to perform
        :type op: SyntheticsPatchTestOperationName, optional

        :param path: The path to the value to modify
        :type path: str, optional

        :param value: A value to use in a `JSON Patch <https://jsonpatch.com>`_ operation
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if op is not unset:
            kwargs["op"] = op
        if path is not unset:
            kwargs["path"] = path
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

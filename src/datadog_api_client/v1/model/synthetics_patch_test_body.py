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
    from datadog_api_client.v1.model.synthetics_patch_test_operation import SyntheticsPatchTestOperation


class SyntheticsPatchTestBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_patch_test_operation import SyntheticsPatchTestOperation

        return {
            "data": ([SyntheticsPatchTestOperation],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[SyntheticsPatchTestOperation], UnsetType] = unset, **kwargs):
        """
        Wrapper around an array of `JSON Patch <https://jsonpatch.com>`_ operations to perform on the test

        :param data: Array of `JSON Patch <https://jsonpatch.com>`_ operations to perform on the test
        :type data: [SyntheticsPatchTestOperation], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

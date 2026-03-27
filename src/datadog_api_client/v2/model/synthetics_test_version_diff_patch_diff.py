# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestVersionDiffPatchDiff(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "change_text": (str,),
            "operation": (str,),
        }

    attribute_map = {
        "change_text": "change_text",
        "operation": "operation",
    }

    def __init__(self_, change_text: Union[str, UnsetType] = unset, operation: Union[str, UnsetType] = unset, **kwargs):
        """
        Object describing a single text diff operation.

        :param change_text: The text that was changed.
        :type change_text: str, optional

        :param operation: The diff operation applied.
        :type operation: str, optional
        """
        if change_text is not unset:
            kwargs["change_text"] = change_text
        if operation is not unset:
            kwargs["operation"] = operation
        super().__init__(kwargs)

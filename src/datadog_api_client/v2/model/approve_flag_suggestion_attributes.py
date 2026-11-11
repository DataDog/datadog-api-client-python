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


class ApproveFlagSuggestionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "apply": (bool,),
            "comment": (str,),
        }

    attribute_map = {
        "apply": "apply",
        "comment": "comment",
    }

    def __init__(self_, apply: Union[bool, UnsetType] = unset, comment: Union[str, UnsetType] = unset, **kwargs):
        """
        Approval options for the suggestion.

        :param apply: Whether to apply the change immediately. Set to ``false`` to approve without applying, then
            call ``ApplyFlagSuggestion`` later.
        :type apply: bool, optional

        :param comment: A comment explaining the approval.
        :type comment: str, optional
        """
        if apply is not unset:
            kwargs["apply"] = apply
        if comment is not unset:
            kwargs["comment"] = comment
        super().__init__(kwargs)

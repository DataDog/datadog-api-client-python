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


class SecretRuleDataAttributesMatchValidationInvalidHttpStatusCodeItems(ModelNormal):
    validations = {
        "end": {
            "inclusive_maximum": 1.8446744073709552e19,
            "inclusive_minimum": 0,
        },
        "start": {
            "inclusive_maximum": 1.8446744073709552e19,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "end": (int,),
            "start": (int,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(self_, end: Union[int, UnsetType] = unset, start: Union[int, UnsetType] = unset, **kwargs):
        """


        :param end:
        :type end: int, optional

        :param start:
        :type start: int, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)

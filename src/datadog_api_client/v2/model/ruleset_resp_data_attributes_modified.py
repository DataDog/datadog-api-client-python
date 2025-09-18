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


class RulesetRespDataAttributesModified(ModelNormal):
    validations = {
        "nanos": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "nanos": (int,),
            "seconds": (int,),
        }

    attribute_map = {
        "nanos": "nanos",
        "seconds": "seconds",
    }

    def __init__(self_, nanos: Union[int, UnsetType] = unset, seconds: Union[int, UnsetType] = unset, **kwargs):
        """
        The definition of ``RulesetRespDataAttributesModified`` object.

        :param nanos: The ``modified`` ``nanos``.
        :type nanos: int, optional

        :param seconds: The ``modified`` ``seconds``.
        :type seconds: int, optional
        """
        if nanos is not unset:
            kwargs["nanos"] = nanos
        if seconds is not unset:
            kwargs["seconds"] = seconds
        super().__init__(kwargs)

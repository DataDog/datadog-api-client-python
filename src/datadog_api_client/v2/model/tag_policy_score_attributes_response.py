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


class TagPolicyScoreAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "score": (float,),
            "ts_end": (int,),
            "ts_start": (int,),
            "version": (int,),
        }

    attribute_map = {
        "score": "score",
        "ts_end": "ts_end",
        "ts_start": "ts_start",
        "version": "version",
    }

    def __init__(self_, score: float, ts_end: int, ts_start: int, version: Union[int, UnsetType] = unset, **kwargs):
        """
        Attributes of a tag policy score.

        :param score: The compliance score for the tag policy.
        :type score: float

        :param ts_end: End timestamp for the score calculation period.
        :type ts_end: int

        :param ts_start: Start timestamp for the score calculation period.
        :type ts_start: int

        :param version: The version of the score.
        :type version: int, optional
        """
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.score = score
        self_.ts_end = ts_end
        self_.ts_start = ts_start

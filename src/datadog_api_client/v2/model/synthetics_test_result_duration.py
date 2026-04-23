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


class SyntheticsTestResultDuration(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_duration": (bool,),
            "value": (int,),
        }

    attribute_map = {
        "has_duration": "has_duration",
        "value": "value",
    }

    def __init__(self_, has_duration: Union[bool, UnsetType] = unset, value: Union[int, UnsetType] = unset, **kwargs):
        """
        Total duration of a Synthetic test execution.

        :param has_duration: Whether a duration was recorded for this execution.
        :type has_duration: bool, optional

        :param value: Duration value in milliseconds.
        :type value: int, optional
        """
        if has_duration is not unset:
            kwargs["has_duration"] = has_duration
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

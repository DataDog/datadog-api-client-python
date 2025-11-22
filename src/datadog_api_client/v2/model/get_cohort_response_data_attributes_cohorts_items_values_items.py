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


class GetCohortResponseDataAttributesCohortsItemsValuesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "absolute_value": (int,),
            "end_time": (int,),
            "relative_value": (float,),
            "start_time": (int,),
            "window": (int,),
        }

    attribute_map = {
        "absolute_value": "absolute_value",
        "end_time": "end_time",
        "relative_value": "relative_value",
        "start_time": "start_time",
        "window": "window",
    }

    def __init__(
        self_,
        absolute_value: Union[int, UnsetType] = unset,
        end_time: Union[int, UnsetType] = unset,
        relative_value: Union[float, UnsetType] = unset,
        start_time: Union[int, UnsetType] = unset,
        window: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param absolute_value:
        :type absolute_value: int, optional

        :param end_time:
        :type end_time: int, optional

        :param relative_value:
        :type relative_value: float, optional

        :param start_time:
        :type start_time: int, optional

        :param window:
        :type window: int, optional
        """
        if absolute_value is not unset:
            kwargs["absolute_value"] = absolute_value
        if end_time is not unset:
            kwargs["end_time"] = end_time
        if relative_value is not unset:
            kwargs["relative_value"] = relative_value
        if start_time is not unset:
            kwargs["start_time"] = start_time
        if window is not unset:
            kwargs["window"] = window
        super().__init__(kwargs)

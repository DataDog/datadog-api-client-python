# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestOptionsSchedulingTimeframe(ModelNormal):
    validations = {
        "day": {
            "inclusive_maximum": 7,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "day": (int,),
            "_from": (str,),
            "to": (str,),
        }

    attribute_map = {
        "day": "day",
        "_from": "from",
        "to": "to",
    }

    def __init__(self_, day: int, _from: str, to: str, **kwargs):
        """
        Object describing a timeframe.

        :param day: Number representing the day of the week.
        :type day: int

        :param _from: The hour of the day on which scheduling starts.
        :type _from: str

        :param to: The hour of the day on which scheduling ends.
        :type to: str
        """
        super().__init__(kwargs)

        self_.day = day
        self_._from = _from
        self_.to = to

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsBanditObservationCountsV2(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "invalid": (int,),
            "total": (int,),
            "valid_immature": (int,),
            "valid_mature": (int,),
        }

    attribute_map = {
        "invalid": "invalid",
        "total": "total",
        "valid_immature": "valid_immature",
        "valid_mature": "valid_mature",
    }

    def __init__(self_, invalid: int, total: int, valid_immature: int, valid_mature: int, **kwargs):
        """
        How many observations the latest saved refresh saw, whatever the range. Null when its counts can't be read.

        :param invalid: Observations the refresh couldn't use.
        :type invalid: int

        :param total: Every observation. The sum of the other three.
        :type total: int

        :param valid_immature: Valid observations whose aggregation window is still open.
        :type valid_immature: int

        :param valid_mature: Valid observations whose aggregation window has closed. The estimates use these.
        :type valid_mature: int
        """
        super().__init__(kwargs)

        self_.invalid = invalid
        self_.total = total
        self_.valid_immature = valid_immature
        self_.valid_mature = valid_mature

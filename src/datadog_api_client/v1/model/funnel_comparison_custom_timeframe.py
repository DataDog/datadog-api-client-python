# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FunnelComparisonCustomTimeframe(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "_from": (float,),
            "to": (float,),
        }

    attribute_map = {
        "_from": "from",
        "to": "to",
    }

    def __init__(self_, _from: float, to: float, **kwargs):
        """
        Custom timeframe for funnel comparison.

        :param _from: Start of the custom timeframe.
        :type _from: float

        :param to: End of the custom timeframe.
        :type to: float
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.to = to

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProductAnalyticsSankeyTime(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (int,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "to": "to",
    }

    def __init__(self_, _from: int, to: int, **kwargs):
        """
        The time window a Sankey query covers.

        :param _from: Start of the query window, in epoch milliseconds.
        :type _from: int

        :param to: End of the query window, in epoch milliseconds.
        :type to: int
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.to = to

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.arbitrary_rule_response_data import ArbitraryRuleResponseData
    from datadog_api_client.v2.model.arbitrary_rule_response_array_meta import ArbitraryRuleResponseArrayMeta


class ArbitraryRuleResponseArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_response_data import ArbitraryRuleResponseData
        from datadog_api_client.v2.model.arbitrary_rule_response_array_meta import ArbitraryRuleResponseArrayMeta

        return {
            "data": ([ArbitraryRuleResponseData],),
            "meta": (ArbitraryRuleResponseArrayMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ArbitraryRuleResponseData],
        meta: Union[ArbitraryRuleResponseArrayMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryRuleResponseArray`` object.

        :param data: The ``ArbitraryRuleResponseArray`` ``data``.
        :type data: [ArbitraryRuleResponseData]

        :param meta: The ``ArbitraryRuleResponseArray`` ``meta``.
        :type meta: ArbitraryRuleResponseArrayMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

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
    from datadog_api_client.v2.model.monthly_cost_attribution_body import MonthlyCostAttributionBody
    from datadog_api_client.v2.model.monthly_cost_attribution_meta import MonthlyCostAttributionMeta


class MonthlyCostAttributionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monthly_cost_attribution_body import MonthlyCostAttributionBody
        from datadog_api_client.v2.model.monthly_cost_attribution_meta import MonthlyCostAttributionMeta

        return {
            "data": ([MonthlyCostAttributionBody],),
            "meta": (MonthlyCostAttributionMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[MonthlyCostAttributionBody], UnsetType] = unset,
        meta: Union[MonthlyCostAttributionMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing the monthly cost attribution by tag(s).

        :param data: Response containing cost attribution.
        :type data: [MonthlyCostAttributionBody], optional

        :param meta: The object containing document metadata.
        :type meta: MonthlyCostAttributionMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

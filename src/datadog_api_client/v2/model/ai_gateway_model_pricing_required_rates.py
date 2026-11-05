# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AiGatewayModelPricingRequiredRates(ModelNormal):
    validations = {
        "cache_read_cost_per_mtok": {
            "inclusive_minimum": 0,
        },
        "cache_write_cost_per_mtok": {
            "inclusive_minimum": 0,
        },
        "non_cached_input_cost_per_mtok": {
            "inclusive_minimum": 0,
        },
        "output_cost_per_mtok": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "cache_read_cost_per_mtok": (float,),
            "cache_write_cost_per_mtok": (float,),
            "non_cached_input_cost_per_mtok": (float,),
            "output_cost_per_mtok": (float,),
        }

    attribute_map = {
        "cache_read_cost_per_mtok": "cache_read_cost_per_mtok",
        "cache_write_cost_per_mtok": "cache_write_cost_per_mtok",
        "non_cached_input_cost_per_mtok": "non_cached_input_cost_per_mtok",
        "output_cost_per_mtok": "output_cost_per_mtok",
    }

    def __init__(
        self_,
        cache_read_cost_per_mtok: float,
        cache_write_cost_per_mtok: float,
        non_cached_input_cost_per_mtok: float,
        output_cost_per_mtok: float,
        **kwargs,
    ):
        """
        Complete set of rates required for custom pricing.

        :param cache_read_cost_per_mtok: Cost per million tokens for cache reads.
        :type cache_read_cost_per_mtok: float

        :param cache_write_cost_per_mtok: Cost per million tokens for cache writes.
        :type cache_write_cost_per_mtok: float

        :param non_cached_input_cost_per_mtok: Cost per million tokens for non-cached input.
        :type non_cached_input_cost_per_mtok: float

        :param output_cost_per_mtok: Cost per million tokens for output.
        :type output_cost_per_mtok: float
        """
        super().__init__(kwargs)

        self_.cache_read_cost_per_mtok = cache_read_cost_per_mtok
        self_.cache_write_cost_per_mtok = cache_write_cost_per_mtok
        self_.non_cached_input_cost_per_mtok = non_cached_input_cost_per_mtok
        self_.output_cost_per_mtok = output_cost_per_mtok

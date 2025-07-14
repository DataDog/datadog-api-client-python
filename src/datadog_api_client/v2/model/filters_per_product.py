# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FiltersPerProduct(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "filters": ([str],),
            "product": (str,),
        }

    attribute_map = {
        "filters": "filters",
        "product": "product",
    }

    def __init__(self_, filters: List[str], product: str, **kwargs):
        """
        Product-specific filters for the dataset.

        :param filters: Defines the list of tag-based filters used to restrict access to telemetry data for a specific product.
            These filters act as access control rules. Each filter must follow the tag query syntax used by
            Datadog (such as ``@tag.key:value`` ), and only one tag or attribute may be used to define the access strategy
            per telemetry type.
        :type filters: [str]

        :param product: Name of the product the dataset is for. Possible values are 'apm', 'rum', 'synthetics',
            'metrics', 'logs', 'sd_repoinfo', 'error_tracking', 'cloud_cost', and 'ml_obs'.
        :type product: str
        """
        super().__init__(kwargs)

        self_.filters = filters
        self_.product = product

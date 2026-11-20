# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class MetricMetadataOrigin(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "product": (str, none_type),
            "product_detail": (str, none_type),
            "sub_product": (str, none_type),
        }

    attribute_map = {
        "product": "product",
        "product_detail": "product_detail",
        "sub_product": "sub_product",
    }

    def __init__(
        self_,
        product: Union[str, none_type],
        product_detail: Union[str, none_type],
        sub_product: Union[str, none_type],
        **kwargs,
    ):
        """
        Where the metric comes from. Each value is the display label shown on the Metrics Summary page. The set of labels can grow as Datadog adds products. Each field is ``null`` when it isn't known.

        :param product: Product that reports the metric, such as ``Agent``.
        :type product: str, none_type

        :param product_detail: Finer-grained origin within the sub-product, such as ``Cpu``.
        :type product_detail: str, none_type

        :param sub_product: Part of the product that reports the metric, such as ``Integration``.
        :type sub_product: str, none_type
        """
        super().__init__(kwargs)

        self_.product = product
        self_.product_detail = product_detail
        self_.sub_product = sub_product

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct


class SensitiveDataScannerSamplings(ModelNormal):
    validations = {
        "rate": {
            "inclusive_maximum": 100.0,
            "inclusive_minimum": 0.0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct

        return {
            "product": (SensitiveDataScannerProduct,),
            "rate": (float,),
        }

    attribute_map = {
        "product": "product",
        "rate": "rate",
    }

    def __init__(
        self_,
        product: Union[SensitiveDataScannerProduct, UnsetType] = unset,
        rate: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sampling configurations for the Scanning Group.

        :param product: Datadog product onto which Sensitive Data Scanner can be activated.
        :type product: SensitiveDataScannerProduct, optional

        :param rate: Rate at which data in product type will be scanned, as a percentage.
        :type rate: float, optional
        """
        if product is not unset:
            kwargs["product"] = product
        if rate is not unset:
            kwargs["rate"] = rate
        super().__init__(kwargs)

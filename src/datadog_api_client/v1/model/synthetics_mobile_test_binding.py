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
    from datadog_api_client.v1.model.synthetics_mobile_test_binding_items import SyntheticsMobileTestBindingItems


class SyntheticsMobileTestBinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_test_binding_items import SyntheticsMobileTestBindingItems

        return {
            "items": (SyntheticsMobileTestBindingItems,),
        }

    attribute_map = {
        "items": "items",
    }

    def __init__(self_, items: Union[SyntheticsMobileTestBindingItems, UnsetType] = unset, **kwargs):
        """
        Objects describing the binding used for a mobile test.

        :param items: Object describing the binding used for a mobile test.
        :type items: SyntheticsMobileTestBindingItems, optional
        """
        if items is not unset:
            kwargs["items"] = items
        super().__init__(kwargs)

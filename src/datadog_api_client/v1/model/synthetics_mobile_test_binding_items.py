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
    from datadog_api_client.v1.model.synthetics_mobile_test_binding_items_role import (
        SyntheticsMobileTestBindingItemsRole,
    )


class SyntheticsMobileTestBindingItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_test_binding_items_role import (
            SyntheticsMobileTestBindingItemsRole,
        )

        return {
            "principals": ([str],),
            "role": (SyntheticsMobileTestBindingItemsRole,),
        }

    attribute_map = {
        "principals": "principals",
        "role": "role",
    }

    def __init__(
        self_,
        principals: Union[List[str], UnsetType] = unset,
        role: Union[SyntheticsMobileTestBindingItemsRole, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the binding used for a mobile test.

        :param principals: List of principals for a mobile test binding.
        :type principals: [str], optional

        :param role: The definition of ``SyntheticsMobileTestBindingItemsRole`` object.
        :type role: SyntheticsMobileTestBindingItemsRole, optional
        """
        if principals is not unset:
            kwargs["principals"] = principals
        if role is not unset:
            kwargs["role"] = role
        super().__init__(kwargs)

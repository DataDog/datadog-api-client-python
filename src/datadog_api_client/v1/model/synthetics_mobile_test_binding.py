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
    from datadog_api_client.v1.model.synthetics_mobile_test_binding_relation import SyntheticsMobileTestBindingRelation


class SyntheticsMobileTestBinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_test_binding_relation import (
            SyntheticsMobileTestBindingRelation,
        )

        return {
            "principals": ([str],),
            "relation": (SyntheticsMobileTestBindingRelation,),
        }

    attribute_map = {
        "principals": "principals",
        "relation": "relation",
    }

    def __init__(
        self_,
        principals: Union[List[str], UnsetType] = unset,
        relation: Union[SyntheticsMobileTestBindingRelation, UnsetType] = unset,
        **kwargs,
    ):
        """
        Objects describing the binding used for a mobile test.

        :param principals: List of principals for a mobile test binding.
        :type principals: [str], optional

        :param relation: The definition of ``SyntheticsMobileTestBindingRelation`` object.
        :type relation: SyntheticsMobileTestBindingRelation, optional
        """
        if principals is not unset:
            kwargs["principals"] = principals
        if relation is not unset:
            kwargs["relation"] = relation
        super().__init__(kwargs)

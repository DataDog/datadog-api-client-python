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
    from datadog_api_client.v1.model.synthetics_test_restriction_policy_binding_relation import (
        SyntheticsTestRestrictionPolicyBindingRelation,
    )


class SyntheticsTestRestrictionPolicyBinding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_restriction_policy_binding_relation import (
            SyntheticsTestRestrictionPolicyBindingRelation,
        )

        return {
            "principals": ([str],),
            "relation": (SyntheticsTestRestrictionPolicyBindingRelation,),
        }

    attribute_map = {
        "principals": "principals",
        "relation": "relation",
    }

    def __init__(
        self_,
        principals: Union[List[str], UnsetType] = unset,
        relation: Union[SyntheticsTestRestrictionPolicyBindingRelation, UnsetType] = unset,
        **kwargs,
    ):
        """
        Objects describing the binding used for a mobile test.

        :param principals: List of principals for a mobile test binding.
        :type principals: [str], optional

        :param relation: The type of relation for the binding.
        :type relation: SyntheticsTestRestrictionPolicyBindingRelation, optional
        """
        if principals is not unset:
            kwargs["principals"] = principals
        if relation is not unset:
            kwargs["relation"] = relation
        super().__init__(kwargs)

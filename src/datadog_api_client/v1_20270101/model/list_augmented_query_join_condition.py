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
    from datadog_api_client.v1_20270101.model.list_augmented_query_join_condition_augment_attribute_normalization import (
        ListAugmentedQueryJoinConditionAugmentAttributeNormalization,
    )
    from datadog_api_client.v1_20270101.model.join_type import JoinType


class ListAugmentedQueryJoinCondition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.list_augmented_query_join_condition_augment_attribute_normalization import (
            ListAugmentedQueryJoinConditionAugmentAttributeNormalization,
        )
        from datadog_api_client.v1_20270101.model.join_type import JoinType

        return {
            "augment_attribute": (str,),
            "augment_attribute_normalization": (ListAugmentedQueryJoinConditionAugmentAttributeNormalization,),
            "base_attribute": (str,),
            "is_negated": (bool,),
            "join_type": (JoinType,),
        }

    attribute_map = {
        "augment_attribute": "augment_attribute",
        "augment_attribute_normalization": "augment_attribute_normalization",
        "base_attribute": "base_attribute",
        "is_negated": "is_negated",
        "join_type": "join_type",
    }

    def __init__(
        self_,
        augment_attribute: str,
        base_attribute: str,
        join_type: JoinType,
        augment_attribute_normalization: Union[
            ListAugmentedQueryJoinConditionAugmentAttributeNormalization, UnsetType
        ] = unset,
        is_negated: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param augment_attribute: Test-only generated schema for the dashboard versioning proof of concept.
        :type augment_attribute: str

        :param augment_attribute_normalization: Test-only generated schema for the dashboard versioning proof of concept.
        :type augment_attribute_normalization: ListAugmentedQueryJoinConditionAugmentAttributeNormalization, optional

        :param base_attribute: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_attribute: str

        :param is_negated: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_negated: bool, optional

        :param join_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_type: JoinType
        """
        if augment_attribute_normalization is not unset:
            kwargs["augment_attribute_normalization"] = augment_attribute_normalization
        if is_negated is not unset:
            kwargs["is_negated"] = is_negated
        super().__init__(kwargs)

        self_.augment_attribute = augment_attribute
        self_.base_attribute = base_attribute
        self_.join_type = join_type

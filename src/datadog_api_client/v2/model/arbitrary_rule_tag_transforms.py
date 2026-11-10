# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.arbitrary_rule_tag_value_transform import ArbitraryRuleTagValueTransform


class ArbitraryRuleTagTransforms(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_tag_value_transform import ArbitraryRuleTagValueTransform

        return {
            "tag_key_rename": ({str: (str,)},),
            "tag_value_transforms": ({str: (ArbitraryRuleTagValueTransform,)},),
        }

    attribute_map = {
        "tag_key_rename": "tag_key_rename",
        "tag_value_transforms": "tag_value_transforms",
    }

    def __init__(
        self_,
        tag_key_rename: Union[Dict[str, str], UnsetType] = unset,
        tag_value_transforms: Union[Dict[str, ArbitraryRuleTagValueTransform], UnsetType] = unset,
        **kwargs,
    ):
        """
        Only supported for ``proportional_timeseries`` and ``even_timeseries`` rules. Applies tag key renames and tag value transforms to timeseries input rows after ``mapping_transform``.

        :param tag_key_rename: Map of source tag key to renamed tag key.
        :type tag_key_rename: {str: (str,)}, optional

        :param tag_value_transforms: Map of tag key to the transform applied to its values.
        :type tag_value_transforms: {str: (ArbitraryRuleTagValueTransform,)}, optional
        """
        if tag_key_rename is not unset:
            kwargs["tag_key_rename"] = tag_key_rename
        if tag_value_transforms is not unset:
            kwargs["tag_value_transforms"] = tag_value_transforms
        super().__init__(kwargs)

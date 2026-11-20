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
    from datadog_api_client.v1_20270101.model.text_match import TextMatch
    from datadog_api_client.v1_20270101.model.text_replacement_rule20270101_replace import (
        TextReplacementRule20270101Replace,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of import TextMatch20270101OneOf
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462865408 import (
        TextMatch20270101OneOf4462865408,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462866048 import (
        TextMatch20270101OneOf4462866048,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462866688 import (
        TextMatch20270101OneOf4462866688,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462867328 import (
        TextMatch20270101OneOf4462867328,
    )
    from datadog_api_client.v1_20270101.model.text_match20270101_one_of4462867968 import (
        TextMatch20270101OneOf4462867968,
    )
    from datadog_api_client.v1_20270101.model.text_replacement_rule20270101_replace_one_of import (
        TextReplacementRule20270101ReplaceOneOf,
    )
    from datadog_api_client.v1_20270101.model.text_replacement_rule20270101_replace_one_of4462870048 import (
        TextReplacementRule20270101ReplaceOneOf4462870048,
    )


class TextReplacementRule(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.text_match import TextMatch
        from datadog_api_client.v1_20270101.model.text_replacement_rule20270101_replace import (
            TextReplacementRule20270101Replace,
        )

        return {
            "match": (TextMatch,),
            "replace": (TextReplacementRule20270101Replace,),
        }

    attribute_map = {
        "match": "match",
        "replace": "replace",
    }

    def __init__(
        self_,
        match: Union[
            TextMatch,
            TextMatch20270101OneOf,
            TextMatch20270101OneOf4462865408,
            TextMatch20270101OneOf4462866048,
            TextMatch20270101OneOf4462866688,
            TextMatch20270101OneOf4462867328,
            TextMatch20270101OneOf4462867968,
        ],
        replace: Union[
            TextReplacementRule20270101Replace,
            TextReplacementRule20270101ReplaceOneOf,
            TextReplacementRule20270101ReplaceOneOf4462870048,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param match: Test-only generated schema for the dashboard versioning proof of concept.
        :type match: TextMatch

        :param replace: Test-only generated schema for the dashboard versioning proof of concept.
        :type replace: TextReplacementRule20270101Replace, optional
        """
        if replace is not unset:
            kwargs["replace"] = replace
        super().__init__(kwargs)

        self_.match = match

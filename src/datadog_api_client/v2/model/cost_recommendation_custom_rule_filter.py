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
    from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter_type import (
        CostRecommendationCustomRuleFilterType,
    )


class CostRecommendationCustomRuleFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_custom_rule_filter_type import (
            CostRecommendationCustomRuleFilterType,
        )

        return {
            "filter_type": (CostRecommendationCustomRuleFilterType,),
            "tag": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "filter_type": "filter_type",
        "tag": "tag",
        "values": "values",
    }

    def __init__(
        self_,
        filter_type: CostRecommendationCustomRuleFilterType,
        tag: str,
        values: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A tag filter. A rule applies to a resource only when every filter of the rule matches.

        :param filter_type: How the filter compares the tag. ``is`` , ``is_not`` , ``contains`` , ``does_not_contain`` , ``like`` (glob), and ``not_like``
            compare the tag values with ``values``. ``all`` matches resources that have the tag and ``untagged`` matches resources
            that do not, so both ignore ``values``.
        :type filter_type: CostRecommendationCustomRuleFilterType

        :param tag: The tag key the filter compares.
        :type tag: str

        :param values: Tag values the filter compares. Required unless ``filter_type`` is ``all`` or ``untagged``.
        :type values: [str], optional
        """
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)

        self_.filter_type = filter_type
        self_.tag = tag

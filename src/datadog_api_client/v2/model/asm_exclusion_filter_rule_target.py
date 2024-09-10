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
    from datadog_api_client.v2.model.asm_exclusion_filter_rule_target_tags import ASMExclusionFilterRuleTargetTags


class ASMExclusionFilterRuleTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asm_exclusion_filter_rule_target_tags import ASMExclusionFilterRuleTargetTags

        return {
            "tags": (ASMExclusionFilterRuleTargetTags,),
        }

    attribute_map = {
        "tags": "tags",
    }

    def __init__(self_, tags: Union[ASMExclusionFilterRuleTargetTags, UnsetType] = unset, **kwargs):
        """
        A rule targeted by the exclusion filter.

        :param tags: Tags identifying the category and type of the targeted rule.
        :type tags: ASMExclusionFilterRuleTargetTags, optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

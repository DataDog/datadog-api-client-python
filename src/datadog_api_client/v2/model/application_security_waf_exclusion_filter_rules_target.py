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
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target_tags import (
        ApplicationSecurityWafExclusionFilterRulesTargetTags,
    )


class ApplicationSecurityWafExclusionFilterRulesTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target_tags import (
            ApplicationSecurityWafExclusionFilterRulesTargetTags,
        )

        return {
            "rule_id": (str,),
            "tags": (ApplicationSecurityWafExclusionFilterRulesTargetTags,),
        }

    attribute_map = {
        "rule_id": "rule_id",
        "tags": "tags",
    }

    def __init__(
        self_,
        rule_id: Union[str, UnsetType] = unset,
        tags: Union[ApplicationSecurityWafExclusionFilterRulesTargetTags, UnsetType] = unset,
        **kwargs,
    ):
        """
        Target WAF rules based either on an identifier or tags.

        :param rule_id: Target a single WAF rule based on its identifier.
        :type rule_id: str, optional

        :param tags: Target multiple WAF rules based on their tags.
        :type tags: ApplicationSecurityWafExclusionFilterRulesTargetTags, optional
        """
        if rule_id is not unset:
            kwargs["rule_id"] = rule_id
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

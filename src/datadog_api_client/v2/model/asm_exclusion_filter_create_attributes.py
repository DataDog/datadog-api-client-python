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
    from datadog_api_client.v2.model.asm_exclusion_filter_rule_target import ASMExclusionFilterRuleTarget
    from datadog_api_client.v2.model.asm_exclusion_filter_scope import ASMExclusionFilterScope


class ASMExclusionFilterCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asm_exclusion_filter_rule_target import ASMExclusionFilterRuleTarget
        from datadog_api_client.v2.model.asm_exclusion_filter_scope import ASMExclusionFilterScope

        return {
            "description": (str,),
            "enabled": (bool,),
            "ip_list": ([str],),
            "path_glob": (str,),
            "rules_target": ([ASMExclusionFilterRuleTarget],),
            "scope": ([ASMExclusionFilterScope],),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "ip_list": "ip_list",
        "path_glob": "path_glob",
        "rules_target": "rules_target",
        "scope": "scope",
    }

    def __init__(
        self_,
        description: str,
        enabled: bool,
        ip_list: Union[List[str], UnsetType] = unset,
        path_glob: Union[str, UnsetType] = unset,
        rules_target: Union[List[ASMExclusionFilterRuleTarget], UnsetType] = unset,
        scope: Union[List[ASMExclusionFilterScope], UnsetType] = unset,
        **kwargs,
    ):
        """
        Create a new ASM WAF exclusion filter.

        :param description: A description for the exclusion filter.
        :type description: str

        :param enabled: Indicates whether the exclusion filter is enabled.
        :type enabled: bool

        :param ip_list: The IPs list for the exclusion filter.
        :type ip_list: [str], optional

        :param path_glob: The path glob for the exclusion filter.
        :type path_glob: str, optional

        :param rules_target: A list of rules targeted by the exclusion filter.
        :type rules_target: [ASMExclusionFilterRuleTarget], optional

        :param scope: The scope of the exclusion filter.
        :type scope: [ASMExclusionFilterScope], optional
        """
        if ip_list is not unset:
            kwargs["ip_list"] = ip_list
        if path_glob is not unset:
            kwargs["path_glob"] = path_glob
        if rules_target is not unset:
            kwargs["rules_target"] = rules_target
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.description = description
        self_.enabled = enabled

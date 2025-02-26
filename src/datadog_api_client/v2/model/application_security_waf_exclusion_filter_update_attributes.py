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
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_on_match import (
        ApplicationSecurityWafExclusionFilterOnMatch,
    )
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target import (
        ApplicationSecurityWafExclusionFilterRulesTarget,
    )
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_scope import (
        ApplicationSecurityWafExclusionFilterScope,
    )


class ApplicationSecurityWafExclusionFilterUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_on_match import (
            ApplicationSecurityWafExclusionFilterOnMatch,
        )
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_rules_target import (
            ApplicationSecurityWafExclusionFilterRulesTarget,
        )
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_scope import (
            ApplicationSecurityWafExclusionFilterScope,
        )

        return {
            "description": (str,),
            "enabled": (bool,),
            "ip_list": ([str],),
            "on_match": (ApplicationSecurityWafExclusionFilterOnMatch,),
            "parameters": ([str],),
            "path_glob": (str,),
            "rules_target": ([ApplicationSecurityWafExclusionFilterRulesTarget],),
            "scope": ([ApplicationSecurityWafExclusionFilterScope],),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "ip_list": "ip_list",
        "on_match": "on_match",
        "parameters": "parameters",
        "path_glob": "path_glob",
        "rules_target": "rules_target",
        "scope": "scope",
    }

    def __init__(
        self_,
        description: str,
        enabled: bool,
        ip_list: Union[List[str], UnsetType] = unset,
        on_match: Union[ApplicationSecurityWafExclusionFilterOnMatch, UnsetType] = unset,
        parameters: Union[List[str], UnsetType] = unset,
        path_glob: Union[str, UnsetType] = unset,
        rules_target: Union[List[ApplicationSecurityWafExclusionFilterRulesTarget], UnsetType] = unset,
        scope: Union[List[ApplicationSecurityWafExclusionFilterScope], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a WAF exclusion filter.

        :param description: A description for the exclusion filter.
        :type description: str

        :param enabled: Indicates whether the exclusion filter is enabled.
        :type enabled: bool

        :param ip_list: The client IP addresses matched by the exclusion filter (CIDR notation is supported).
        :type ip_list: [str], optional

        :param on_match: The action taken when the exclusion filter matches. When set to ``monitor`` , security traces are emitted but the requests are not blocked. By default, security traces are not emitted and the requests are not blocked.
        :type on_match: ApplicationSecurityWafExclusionFilterOnMatch, optional

        :param parameters: A list of parameters matched by the exclusion filter in the HTTP query string and HTTP request body. Nested parameters can be matched by joining fields with a dot character.
        :type parameters: [str], optional

        :param path_glob: The HTTP path glob expression matched by the exclusion filter.
        :type path_glob: str, optional

        :param rules_target: The WAF rules targeted by the exclusion filter.
        :type rules_target: [ApplicationSecurityWafExclusionFilterRulesTarget], optional

        :param scope: The services where the exclusion filter is deployed.
        :type scope: [ApplicationSecurityWafExclusionFilterScope], optional
        """
        if ip_list is not unset:
            kwargs["ip_list"] = ip_list
        if on_match is not unset:
            kwargs["on_match"] = on_match
        if parameters is not unset:
            kwargs["parameters"] = parameters
        if path_glob is not unset:
            kwargs["path_glob"] = path_glob
        if rules_target is not unset:
            kwargs["rules_target"] = rules_target
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.description = description
        self_.enabled = enabled

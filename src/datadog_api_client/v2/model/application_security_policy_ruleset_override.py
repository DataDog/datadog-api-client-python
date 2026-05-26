# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationSecurityPolicyRulesetOverride(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "blocking": (bool,),
            "enabled": (bool,),
            "id": (str,),
        }

    attribute_map = {
        "blocking": "blocking",
        "enabled": "enabled",
        "id": "id",
    }

    def __init__(self_, blocking: bool, enabled: bool, id: str, **kwargs):
        """
        Deprecated: Override WAF ruleset parameters. Use ``protectionPresets`` instead.

        :param blocking: When blocking is enabled, the ruleset will block the traffic it matches.
        :type blocking: bool

        :param enabled: When false, this ruleset will not match any traffic.
        :type enabled: bool

        :param id: The identifier of the ruleset to override.
        :type id: str
        """
        super().__init__(kwargs)

        self_.blocking = blocking
        self_.enabled = enabled
        self_.id = id

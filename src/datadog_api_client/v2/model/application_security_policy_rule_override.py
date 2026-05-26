# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ApplicationSecurityPolicyRuleOverride(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "blocking": (bool,),
            "enabled": (bool,),
            "extended_data_collection": (bool,),
            "id": (str,),
        }

    attribute_map = {
        "blocking": "blocking",
        "enabled": "enabled",
        "extended_data_collection": "extended_data_collection",
        "id": "id",
    }

    def __init__(
        self_,
        blocking: bool,
        enabled: bool,
        id: str,
        extended_data_collection: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Override WAF rule parameters for services in a policy.

        :param blocking: When blocking is enabled, the rule will block the traffic matched by this rule.
        :type blocking: bool

        :param enabled: When false, this rule will not match any traffic.
        :type enabled: bool

        :param extended_data_collection: When true, collects additional data from the WAF for this rule.
        :type extended_data_collection: bool, optional

        :param id: Override the parameters for this WAF rule identifier.
        :type id: str
        """
        if extended_data_collection is not unset:
            kwargs["extended_data_collection"] = extended_data_collection
        super().__init__(kwargs)

        self_.blocking = blocking
        self_.enabled = enabled
        self_.id = id

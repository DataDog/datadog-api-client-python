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
    from datadog_api_client.v2.model.application_security_waf_custom_rule_attributes import (
        ApplicationSecurityWafCustomRuleAttributes,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_type import (
        ApplicationSecurityWafCustomRuleType,
    )


class ApplicationSecurityWafCustomRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_attributes import (
            ApplicationSecurityWafCustomRuleAttributes,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_type import (
            ApplicationSecurityWafCustomRuleType,
        )

        return {
            "attributes": (ApplicationSecurityWafCustomRuleAttributes,),
            "id": (str,),
            "type": (ApplicationSecurityWafCustomRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        attributes: Union[ApplicationSecurityWafCustomRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ApplicationSecurityWafCustomRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single WAF custom rule.

        :param attributes: A WAF custom rule.
        :type attributes: ApplicationSecurityWafCustomRuleAttributes, optional

        :param id: The ID of the custom rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``custom_rule``.
        :type type: ApplicationSecurityWafCustomRuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

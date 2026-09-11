# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.default_inbox_rule_attributes_response import DefaultInboxRuleAttributesResponse
    from datadog_api_client.v2.model.default_inbox_rule_type import DefaultInboxRuleType


class DefaultInboxRuleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.default_inbox_rule_attributes_response import (
            DefaultInboxRuleAttributesResponse,
        )
        from datadog_api_client.v2.model.default_inbox_rule_type import DefaultInboxRuleType

        return {
            "attributes": (DefaultInboxRuleAttributesResponse,),
            "id": (str,),
            "type": (DefaultInboxRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DefaultInboxRuleAttributesResponse, id: str, type: DefaultInboxRuleType, **kwargs):
        """
        The data object for a default inbox rule returned by the API.

        :param attributes: Attributes of a default inbox rule returned by the API.
        :type attributes: DefaultInboxRuleAttributesResponse

        :param id: The ID of the default inbox rule.
            Known default rule IDs include: ``identity_risk_default_rule`` ,
            ``secret_default_rule`` , ``library_vulnerability_default_rule`` ,
            ``attack_path_default_rule`` , ``host_and_container_vulnerability_default_rule`` ,
            ``runtime_code_vulnerability_default_rule`` , ``iac_misconfiguration_default_rule`` ,
            and ``misconfiguration_default_rule``. Datadog can add new default rules
            over time.
        :type id: str

        :param type: The JSON:API type for default inbox rules.
        :type type: DefaultInboxRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type

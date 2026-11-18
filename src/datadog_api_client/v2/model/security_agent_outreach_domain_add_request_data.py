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
    from datadog_api_client.v2.model.security_agent_outreach_domain_add_request_data_attributes import (
        SecurityAgentOutreachDomainAddRequestDataAttributes,
    )
    from datadog_api_client.v2.model.security_agent_outreach_domain_add_type import SecurityAgentOutreachDomainAddType


class SecurityAgentOutreachDomainAddRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_domain_add_request_data_attributes import (
            SecurityAgentOutreachDomainAddRequestDataAttributes,
        )
        from datadog_api_client.v2.model.security_agent_outreach_domain_add_type import (
            SecurityAgentOutreachDomainAddType,
        )

        return {
            "attributes": (SecurityAgentOutreachDomainAddRequestDataAttributes,),
            "type": (SecurityAgentOutreachDomainAddType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityAgentOutreachDomainAddRequestDataAttributes,
        type: SecurityAgentOutreachDomainAddType,
        **kwargs,
    ):
        """
        The email domain to allow.

        :param attributes: The email domain to allow.
        :type attributes: SecurityAgentOutreachDomainAddRequestDataAttributes

        :param type: Type of an allowed outreach domain add request.
        :type type: SecurityAgentOutreachDomainAddType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

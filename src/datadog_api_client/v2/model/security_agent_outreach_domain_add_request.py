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
    from datadog_api_client.v2.model.security_agent_outreach_domain_add_request_data import (
        SecurityAgentOutreachDomainAddRequestData,
    )


class SecurityAgentOutreachDomainAddRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_domain_add_request_data import (
            SecurityAgentOutreachDomainAddRequestData,
        )

        return {
            "data": (SecurityAgentOutreachDomainAddRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityAgentOutreachDomainAddRequestData, **kwargs):
        """
        Request to add one allowed email domain.

        :param data: The email domain to allow.
        :type data: SecurityAgentOutreachDomainAddRequestData
        """
        super().__init__(kwargs)

        self_.data = data

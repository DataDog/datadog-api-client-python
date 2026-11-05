# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_agent_investigation_list_item import SecurityAgentInvestigationListItem
    from datadog_api_client.v2.model.security_agent_investigations_list_meta import SecurityAgentInvestigationsListMeta


class SecurityAgentInvestigationsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_list_item import (
            SecurityAgentInvestigationListItem,
        )
        from datadog_api_client.v2.model.security_agent_investigations_list_meta import (
            SecurityAgentInvestigationsListMeta,
        )

        return {
            "data": ([SecurityAgentInvestigationListItem],),
            "meta": (SecurityAgentInvestigationsListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[SecurityAgentInvestigationListItem], meta: SecurityAgentInvestigationsListMeta, **kwargs
    ):
        """
        A page of investigations.

        :param data: The investigations on this page.
        :type data: [SecurityAgentInvestigationListItem]

        :param meta: Metadata of a page of investigations.
        :type meta: SecurityAgentInvestigationsListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta

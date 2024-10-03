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
    from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_info_response_data import (
        MicrosoftTeamsTenantBasedHandleInfoResponseData,
    )


class MicrosoftTeamsTenantBasedHandlesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_info_response_data import (
            MicrosoftTeamsTenantBasedHandleInfoResponseData,
        )

        return {
            "data": ([MicrosoftTeamsTenantBasedHandleInfoResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[MicrosoftTeamsTenantBasedHandleInfoResponseData], **kwargs):
        """
        Response with a list of tenant-based handles.

        :param data: An array of tenant-based handles.
        :type data: [MicrosoftTeamsTenantBasedHandleInfoResponseData]
        """
        super().__init__(kwargs)

        self_.data = data

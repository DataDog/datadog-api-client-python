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
    from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_attributes import (
        MicrosoftTeamsTenantBasedHandleAttributes,
    )
    from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType


class MicrosoftTeamsUpdateTenantBasedHandleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_attributes import (
            MicrosoftTeamsTenantBasedHandleAttributes,
        )
        from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import (
            MicrosoftTeamsTenantBasedHandleType,
        )

        return {
            "attributes": (MicrosoftTeamsTenantBasedHandleAttributes,),
            "type": (MicrosoftTeamsTenantBasedHandleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: MicrosoftTeamsTenantBasedHandleAttributes,
        type: MicrosoftTeamsTenantBasedHandleType,
        **kwargs,
    ):
        """
        Tenant-based handle data from a response.

        :param attributes: Tenant-based handle attributes.
        :type attributes: MicrosoftTeamsTenantBasedHandleAttributes

        :param type: Specifies the tenant-based handle resource type.
        :type type: MicrosoftTeamsTenantBasedHandleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

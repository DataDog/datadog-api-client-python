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
    from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_attributes import (
        MicrosoftTeamsTenantBasedHandleAttributes,
    )
    from datadog_api_client.v2.model.microsoft_teams_tenant_based_handle_type import MicrosoftTeamsTenantBasedHandleType


class MicrosoftTeamsTenantBasedHandleResponseData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

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
            "id": (str,),
            "type": (MicrosoftTeamsTenantBasedHandleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MicrosoftTeamsTenantBasedHandleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MicrosoftTeamsTenantBasedHandleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Tenant-based handle data from a response.

        :param attributes: Tenant-based handle attributes.
        :type attributes: MicrosoftTeamsTenantBasedHandleAttributes, optional

        :param id: The ID of the tenant-based handle.
        :type id: str, optional

        :param type: Specifies the tenant-based handle resource type.
        :type type: MicrosoftTeamsTenantBasedHandleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_team_role import UserTeamRole


class UserTeamAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team_role import UserTeamRole

        return {
            "provisioned_by": (str, none_type),
            "provisioned_by_id": (str, none_type),
            "role": (UserTeamRole,),
        }

    attribute_map = {
        "provisioned_by": "provisioned_by",
        "provisioned_by_id": "provisioned_by_id",
        "role": "role",
    }
    read_only_vars = {
        "provisioned_by",
        "provisioned_by_id",
    }

    def __init__(
        self_,
        provisioned_by: Union[str, none_type, UnsetType] = unset,
        provisioned_by_id: Union[str, none_type, UnsetType] = unset,
        role: Union[UserTeamRole, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team membership attributes

        :param provisioned_by: The mechanism responsible for provisioning the team relationship.
            Possible values: null for added by a user, "service_account" if added by a service account, and "saml_mapping" if provisioned via SAML mapping.
        :type provisioned_by: str, none_type, optional

        :param provisioned_by_id: UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping.
        :type provisioned_by_id: str, none_type, optional

        :param role: The user's role within the team
        :type role: UserTeamRole, none_type, optional
        """
        if provisioned_by is not unset:
            kwargs["provisioned_by"] = provisioned_by
        if provisioned_by_id is not unset:
            kwargs["provisioned_by_id"] = provisioned_by_id
        if role is not unset:
            kwargs["role"] = role
        super().__init__(kwargs)

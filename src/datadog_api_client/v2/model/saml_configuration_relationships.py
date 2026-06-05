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
    from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles


class SAMLConfigurationRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles

        return {
            "default_roles": (RelationshipToRoles,),
        }

    attribute_map = {
        "default_roles": "default_roles",
    }

    def __init__(self_, default_roles: Union[RelationshipToRoles, UnsetType] = unset, **kwargs):
        """
        Relationships of a SAML configuration.

        :param default_roles: Relationship to roles.
        :type default_roles: RelationshipToRoles, optional
        """
        if default_roles is not unset:
            kwargs["default_roles"] = default_roles
        super().__init__(kwargs)

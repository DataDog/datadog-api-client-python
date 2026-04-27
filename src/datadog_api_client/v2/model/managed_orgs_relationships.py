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
    from datadog_api_client.v2.model.managed_orgs_relationship_to_org import ManagedOrgsRelationshipToOrg
    from datadog_api_client.v2.model.managed_orgs_relationship_to_orgs import ManagedOrgsRelationshipToOrgs


class ManagedOrgsRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.managed_orgs_relationship_to_org import ManagedOrgsRelationshipToOrg
        from datadog_api_client.v2.model.managed_orgs_relationship_to_orgs import ManagedOrgsRelationshipToOrgs

        return {
            "current_org": (ManagedOrgsRelationshipToOrg,),
            "managed_orgs": (ManagedOrgsRelationshipToOrgs,),
        }

    attribute_map = {
        "current_org": "current_org",
        "managed_orgs": "managed_orgs",
    }

    def __init__(
        self_, current_org: ManagedOrgsRelationshipToOrg, managed_orgs: ManagedOrgsRelationshipToOrgs, **kwargs
    ):
        """
        Relationships of the managed organizations resource.

        :param current_org: Relationship to the current organization.
        :type current_org: ManagedOrgsRelationshipToOrg

        :param managed_orgs: Relationship to the managed organizations.
        :type managed_orgs: ManagedOrgsRelationshipToOrgs
        """
        super().__init__(kwargs)

        self_.current_org = current_org
        self_.managed_orgs = managed_orgs

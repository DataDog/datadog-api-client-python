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
    from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients_data import (
        OrgAuthorizedClientRelationshipUserAuthorizedClientsData,
    )
    from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients_links import (
        OrgAuthorizedClientRelationshipUserAuthorizedClientsLinks,
    )


class OrgAuthorizedClientRelationshipUserAuthorizedClients(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients_data import (
            OrgAuthorizedClientRelationshipUserAuthorizedClientsData,
        )
        from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients_links import (
            OrgAuthorizedClientRelationshipUserAuthorizedClientsLinks,
        )

        return {
            "data": ([OrgAuthorizedClientRelationshipUserAuthorizedClientsData],),
            "links": (OrgAuthorizedClientRelationshipUserAuthorizedClientsLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(
        self_,
        data: List[OrgAuthorizedClientRelationshipUserAuthorizedClientsData],
        links: OrgAuthorizedClientRelationshipUserAuthorizedClientsLinks,
        **kwargs,
    ):
        """
        Relationship to the user authorized clients for this org authorized client.

        :param data: List of user authorized client relationship data objects.
        :type data: [OrgAuthorizedClientRelationshipUserAuthorizedClientsData]

        :param links: Links for the user authorized clients relationship.
        :type links: OrgAuthorizedClientRelationshipUserAuthorizedClientsLinks
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links

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
    from datadog_api_client.v2.model.org_authorized_client_relationship_o_auth2_client import (
        OrgAuthorizedClientRelationshipOAuth2Client,
    )
    from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients import (
        OrgAuthorizedClientRelationshipUserAuthorizedClients,
    )


class OrgAuthorizedClientRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_authorized_client_relationship_o_auth2_client import (
            OrgAuthorizedClientRelationshipOAuth2Client,
        )
        from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients import (
            OrgAuthorizedClientRelationshipUserAuthorizedClients,
        )

        return {
            "oauth2_client": (OrgAuthorizedClientRelationshipOAuth2Client,),
            "user_authorized_clients": (OrgAuthorizedClientRelationshipUserAuthorizedClients,),
        }

    attribute_map = {
        "oauth2_client": "oauth2_client",
        "user_authorized_clients": "user_authorized_clients",
    }

    def __init__(
        self_,
        oauth2_client: OrgAuthorizedClientRelationshipOAuth2Client,
        user_authorized_clients: OrgAuthorizedClientRelationshipUserAuthorizedClients,
        **kwargs,
    ):
        """
        Relationships for an org authorized client.

        :param oauth2_client: Relationship to the OAuth2 client for this org authorized client.
        :type oauth2_client: OrgAuthorizedClientRelationshipOAuth2Client

        :param user_authorized_clients: Relationship to the user authorized clients for this org authorized client.
        :type user_authorized_clients: OrgAuthorizedClientRelationshipUserAuthorizedClients
        """
        super().__init__(kwargs)

        self_.oauth2_client = oauth2_client
        self_.user_authorized_clients = user_authorized_clients

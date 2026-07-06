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
    from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients_data_type import (
        OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType,
    )


class OrgAuthorizedClientRelationshipUserAuthorizedClientsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_authorized_client_relationship_user_authorized_clients_data_type import (
            OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType,
        )

        return {
            "id": (str,),
            "type": (OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType, **kwargs):
        """
        Data identifying a user authorized client.

        :param id: The ID of the user authorized client.
        :type id: str

        :param type: User authorized client resource type.
        :type type: OrgAuthorizedClientRelationshipUserAuthorizedClientsDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

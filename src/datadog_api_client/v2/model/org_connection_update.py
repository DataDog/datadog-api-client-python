# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_connection_update_attributes import OrgConnectionUpdateAttributes
    from datadog_api_client.v2.model.org_connection_type import OrgConnectionType


class OrgConnectionUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_update_attributes import OrgConnectionUpdateAttributes
        from datadog_api_client.v2.model.org_connection_type import OrgConnectionType

        return {
            "attributes": (OrgConnectionUpdateAttributes,),
            "id": (UUID,),
            "type": (OrgConnectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OrgConnectionUpdateAttributes, id: UUID, type: OrgConnectionType, **kwargs):
        """
        Org connection update data.

        :param attributes: Attributes for updating an org connection.
        :type attributes: OrgConnectionUpdateAttributes

        :param id: The unique identifier of the org connection.
        :type id: UUID

        :param type: Org connection type.
        :type type: OrgConnectionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type

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
    from datadog_api_client.v2.model.org_authorized_client_update_attributes import OrgAuthorizedClientUpdateAttributes
    from datadog_api_client.v2.model.org_authorized_client_type import OrgAuthorizedClientType


class OrgAuthorizedClientUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_authorized_client_update_attributes import (
            OrgAuthorizedClientUpdateAttributes,
        )
        from datadog_api_client.v2.model.org_authorized_client_type import OrgAuthorizedClientType

        return {
            "attributes": (OrgAuthorizedClientUpdateAttributes,),
            "id": (str,),
            "type": (OrgAuthorizedClientType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: OrgAuthorizedClientType,
        attributes: Union[OrgAuthorizedClientUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating an org authorized client.

        :param attributes: Attributes for updating an org authorized client.
        :type attributes: OrgAuthorizedClientUpdateAttributes, optional

        :param id: The unique identifier of the org authorized client to update.
        :type id: str

        :param type: The resource type for org authorized clients.
        :type type: OrgAuthorizedClientType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

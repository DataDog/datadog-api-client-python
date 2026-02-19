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
    from datadog_api_client.v2.model.change_request_response_attributes import ChangeRequestResponseAttributes
    from datadog_api_client.v2.model.change_request_relationships import ChangeRequestRelationships
    from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType


class ChangeRequestResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_response_attributes import ChangeRequestResponseAttributes
        from datadog_api_client.v2.model.change_request_relationships import ChangeRequestRelationships
        from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType

        return {
            "attributes": (ChangeRequestResponseAttributes,),
            "id": (str,),
            "relationships": (ChangeRequestRelationships,),
            "type": (ChangeRequestResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ChangeRequestResponseAttributes,
        id: str,
        type: ChangeRequestResourceType,
        relationships: Union[ChangeRequestRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a change request response.

        :param attributes: Attributes of a change request response.
        :type attributes: ChangeRequestResponseAttributes

        :param id: The identifier of the change request.
        :type id: str

        :param relationships: Relationships of a change request.
        :type relationships: ChangeRequestRelationships, optional

        :param type: Change request resource type.
        :type type: ChangeRequestResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type

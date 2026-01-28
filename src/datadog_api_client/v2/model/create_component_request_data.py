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
    from datadog_api_client.v2.model.create_component_request_data_attributes import (
        CreateComponentRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_component_request_data_relationships import (
        CreateComponentRequestDataRelationships,
    )
    from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType


class CreateComponentRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_component_request_data_attributes import (
            CreateComponentRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_component_request_data_relationships import (
            CreateComponentRequestDataRelationships,
        )
        from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

        return {
            "attributes": (CreateComponentRequestDataAttributes,),
            "relationships": (CreateComponentRequestDataRelationships,),
            "type": (StatusPagesComponentGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateComponentRequestDataAttributes,
        type: StatusPagesComponentGroupType,
        relationships: Union[CreateComponentRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: The supported attributes for creating a component.
        :type attributes: CreateComponentRequestDataAttributes

        :param relationships: The supported relationships for creating a component.
        :type relationships: CreateComponentRequestDataRelationships, optional

        :param type: Components resource type.
        :type type: StatusPagesComponentGroupType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

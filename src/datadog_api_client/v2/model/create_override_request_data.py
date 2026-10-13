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
    from datadog_api_client.v2.model.create_override_request_attributes import CreateOverrideRequestAttributes
    from datadog_api_client.v2.model.create_override_request_relationships import CreateOverrideRequestRelationships
    from datadog_api_client.v2.model.override_data_type import OverrideDataType


class CreateOverrideRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_override_request_attributes import CreateOverrideRequestAttributes
        from datadog_api_client.v2.model.create_override_request_relationships import CreateOverrideRequestRelationships
        from datadog_api_client.v2.model.override_data_type import OverrideDataType

        return {
            "attributes": (CreateOverrideRequestAttributes,),
            "relationships": (CreateOverrideRequestRelationships,),
            "type": (OverrideDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateOverrideRequestAttributes,
        type: OverrideDataType,
        relationships: Union[CreateOverrideRequestRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for creating an on-call schedule override.

        :param attributes: Attributes for creating an on-call schedule override.
        :type attributes: CreateOverrideRequestAttributes

        :param relationships: Relationships to set when creating an on-call schedule override.
        :type relationships: CreateOverrideRequestRelationships, optional

        :param type: Indicates that the resource is of type 'overrides'.
        :type type: OverrideDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

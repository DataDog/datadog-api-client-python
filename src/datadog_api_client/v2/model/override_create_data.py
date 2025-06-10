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
    from datadog_api_client.v2.model.override_create_data_attributes import OverrideCreateDataAttributes
    from datadog_api_client.v2.model.override_create_data_relationships import OverrideCreateDataRelationships
    from datadog_api_client.v2.model.override_create_data_type import OverrideCreateDataType


class OverrideCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.override_create_data_attributes import OverrideCreateDataAttributes
        from datadog_api_client.v2.model.override_create_data_relationships import OverrideCreateDataRelationships
        from datadog_api_client.v2.model.override_create_data_type import OverrideCreateDataType

        return {
            "attributes": (OverrideCreateDataAttributes,),
            "relationships": (OverrideCreateDataRelationships,),
            "type": (OverrideCreateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OverrideCreateDataAttributes,
        type: OverrideCreateDataType,
        relationships: Union[OverrideCreateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``OverrideCreateData`` object.

        :param attributes: The definition of ``OverrideCreateDataAttributes`` object.
        :type attributes: OverrideCreateDataAttributes

        :param relationships: The definition of ``OverrideCreateDataRelationships`` object.
        :type relationships: OverrideCreateDataRelationships, optional

        :param type: The definition of ``OverrideCreateDataType`` object.
        :type type: OverrideCreateDataType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

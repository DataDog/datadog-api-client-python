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
    from datadog_api_client.v2.model.data_transform_properties import DataTransformProperties
    from datadog_api_client.v2.model.data_transform_type import DataTransformType


class DataTransform(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_transform_properties import DataTransformProperties
        from datadog_api_client.v2.model.data_transform_type import DataTransformType

        return {
            "id": (UUID,),
            "name": (str,),
            "properties": (DataTransformProperties,),
            "type": (DataTransformType,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "properties": "properties",
        "type": "type",
    }

    def __init__(self_, id: UUID, name: str, properties: DataTransformProperties, type: DataTransformType, **kwargs):
        """
        A data transformer, which is custom JavaScript code that executes and transforms data when its inputs change.

        :param id: The ID of the data transformer.
        :type id: UUID

        :param name: A unique identifier for this data transformer. This name is also used to access the transformer's result throughout the app.
        :type name: str

        :param properties: The properties of the data transformer.
        :type properties: DataTransformProperties

        :param type: The data transform type.
        :type type: DataTransformType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.properties = properties
        self_.type = type

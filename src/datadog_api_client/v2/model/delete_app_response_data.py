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
    from datadog_api_client.v2.model.app_definition_type import AppDefinitionType


class DeleteAppResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_definition_type import AppDefinitionType

        return {
            "id": (UUID,),
            "type": (AppDefinitionType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: AppDefinitionType, **kwargs):
        """
        The definition of ``DeleteAppResponseData`` object.

        :param id: The ID of the deleted app.
        :type id: UUID

        :param type: The app definition type.
        :type type: AppDefinitionType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

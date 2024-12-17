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
    from datadog_api_client.v2.model.delete_apps_response_data_items_type import DeleteAppsResponseDataItemsType


class DeleteAppsResponseDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_response_data_items_type import DeleteAppsResponseDataItemsType

        return {
            "id": (str,),
            "type": (DeleteAppsResponseDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: DeleteAppsResponseDataItemsType, **kwargs):
        """
        The definition of ``DeleteAppsResponseDataItems`` object.

        :param id: The ``items`` ``id``.
        :type id: str

        :param type: The definition of ``DeleteAppsResponseDataItemsType`` object.
        :type type: DeleteAppsResponseDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

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
    from datadog_api_client.v2.model.delete_apps_request_data_items_type import DeleteAppsRequestDataItemsType


class DeleteAppsRequestDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_request_data_items_type import DeleteAppsRequestDataItemsType

        return {
            "id": (str,),
            "type": (DeleteAppsRequestDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: DeleteAppsRequestDataItemsType, **kwargs):
        """
        The definition of ``DeleteAppsRequestDataItems`` object.

        :param id: The ``items`` ``id``.
        :type id: str

        :param type: The definition of ``DeleteAppsRequestDataItemsType`` object.
        :type type: DeleteAppsRequestDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
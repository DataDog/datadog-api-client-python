# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.delete_apps_request_data_items import DeleteAppsRequestDataItems


class DeleteAppsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_request_data_items import DeleteAppsRequestDataItems

        return {
            "data": ([DeleteAppsRequestDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[DeleteAppsRequestDataItems], UnsetType] = unset, **kwargs):
        """
        A request object for deleting multiple apps by ID.

        :param data: An array of objects containing the IDs of the apps to delete.
        :type data: [DeleteAppsRequestDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.put_apps_datastore_item_response_data import PutAppsDatastoreItemResponseData


class PutAppsDatastoreItemResponseArray(ModelNormal):
    validations = {
        "data": {
            "max_items": 100,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.put_apps_datastore_item_response_data import PutAppsDatastoreItemResponseData

        return {
            "data": ([PutAppsDatastoreItemResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[PutAppsDatastoreItemResponseData], **kwargs):
        """
        Response after successfully inserting multiple items into a datastore, containing the identifiers of the created items.

        :param data: An array of data objects containing the identifiers of the successfully inserted items.
        :type data: [PutAppsDatastoreItemResponseData]
        """
        super().__init__(kwargs)

        self_.data = data

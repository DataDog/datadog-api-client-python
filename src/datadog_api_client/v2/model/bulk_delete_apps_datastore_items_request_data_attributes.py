# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class BulkDeleteAppsDatastoreItemsRequestDataAttributes(ModelNormal):
    validations = {
        "item_keys": {
            "max_items": 100,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "item_keys": ([str],),
        }

    attribute_map = {
        "item_keys": "item_keys",
    }

    def __init__(self_, item_keys: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes of request data to delete items from a datastore.

        :param item_keys: List of primary keys identifying items to delete from datastore. Up to 100 items can be deleted in a single request.
        :type item_keys: [str], optional
        """
        if item_keys is not unset:
            kwargs["item_keys"] = item_keys
        super().__init__(kwargs)

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DeleteAppsDatastoreItemRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "item_key": (str,),
        }

    attribute_map = {
        "id": "id",
        "item_key": "item_key",
    }

    def __init__(self_, item_key: str, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``DeleteAppsDatastoreItemRequestDataAttributes`` object.

        :param id: The ``item`` ``id``.
        :type id: str, optional

        :param item_key: The ``attributes`` ``item_key``.
        :type item_key: str
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.item_key = item_key

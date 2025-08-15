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


class CreateAppsDatastoreFromImportResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "item_count": (int,),
        }

    attribute_map = {
        "item_count": "item_count",
    }

    def __init__(self_, item_count: Union[int, UnsetType] = unset, **kwargs):
        """
        The definition of ``CreateAppsDatastoreFromImportResponseDataAttributes`` object.

        :param item_count: The ``attributes`` ``item_count``.
        :type item_count: int, optional
        """
        if item_count is not unset:
            kwargs["item_count"] = item_count
        super().__init__(kwargs)

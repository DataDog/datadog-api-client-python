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
    from datadog_api_client.v2.model.put_apps_datastore_item_response_data_type import (
        PutAppsDatastoreItemResponseDataType,
    )


class PutAppsDatastoreItemResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.put_apps_datastore_item_response_data_type import (
            PutAppsDatastoreItemResponseDataType,
        )

        return {
            "id": (str,),
            "type": (PutAppsDatastoreItemResponseDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: PutAppsDatastoreItemResponseDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``PutAppsDatastoreItemResponseData`` object.

        :param id: The ``PutAppsDatastoreItemResponseData`` ``id``.
        :type id: str, optional

        :param type: Items resource type.
        :type type: PutAppsDatastoreItemResponseDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type

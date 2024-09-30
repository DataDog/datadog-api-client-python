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
    from datadog_api_client.v2.model.list_devices_response_metadata_page import ListDevicesResponseMetadataPage


class ListDevicesResponseMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_devices_response_metadata_page import ListDevicesResponseMetadataPage

        return {
            "page": (ListDevicesResponseMetadataPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[ListDevicesResponseMetadataPage, UnsetType] = unset, **kwargs):
        """
        Object describing meta attributes of response.

        :param page: Pagination object.
        :type page: ListDevicesResponseMetadataPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)

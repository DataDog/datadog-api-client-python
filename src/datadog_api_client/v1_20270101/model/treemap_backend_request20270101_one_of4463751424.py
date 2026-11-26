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
    from datadog_api_client.v1_20270101.model.treemap_backend_request_any_of_any_of_item_request_type4453528768 import (
        TreemapBackendRequestAnyOfAnyOfItemRequestType4453528768,
    )
    from datadog_api_client.v1_20270101.model.treemap_backend_request_any_of_any_of_item_response_format4453529088 import (
        TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453529088,
    )
    from datadog_api_client.v1_20270101.model.treemap_request_style import TreemapRequestStyle


class TreemapBackendRequest20270101OneOf4463751424(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.treemap_backend_request_any_of_any_of_item_request_type4453528768 import (
            TreemapBackendRequestAnyOfAnyOfItemRequestType4453528768,
        )
        from datadog_api_client.v1_20270101.model.treemap_backend_request_any_of_any_of_item_response_format4453529088 import (
            TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453529088,
        )
        from datadog_api_client.v1_20270101.model.treemap_request_style import TreemapRequestStyle

        return {
            "ddsql_query": (str,),
            "request_type": (TreemapBackendRequestAnyOfAnyOfItemRequestType4453528768,),
            "response_format": (TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453529088,),
            "style": (TreemapRequestStyle,),
        }

    attribute_map = {
        "ddsql_query": "ddsql_query",
        "request_type": "request_type",
        "response_format": "response_format",
        "style": "style",
    }

    def __init__(
        self_,
        ddsql_query: str,
        request_type: TreemapBackendRequestAnyOfAnyOfItemRequestType4453528768,
        response_format: TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453529088,
        style: Union[TreemapRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: TreemapBackendRequestAnyOfAnyOfItemRequestType4453528768

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453529088

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TreemapRequestStyle, optional
        """
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.ddsql_query = ddsql_query
        self_.request_type = request_type
        self_.response_format = response_format

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
    from datadog_api_client.v2.model.list_apps_response_data_items import ListAppsResponseDataItems
    from datadog_api_client.v2.model.deployment import Deployment
    from datadog_api_client.v2.model.list_apps_response_meta import ListAppsResponseMeta


class ListAppsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_apps_response_data_items import ListAppsResponseDataItems
        from datadog_api_client.v2.model.deployment import Deployment
        from datadog_api_client.v2.model.list_apps_response_meta import ListAppsResponseMeta

        return {
            "data": ([ListAppsResponseDataItems],),
            "included": ([Deployment],),
            "meta": (ListAppsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[ListAppsResponseDataItems], UnsetType] = unset,
        included: Union[List[Deployment], UnsetType] = unset,
        meta: Union[ListAppsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A paginated list of apps matching the specified filters and sorting.

        :param data: An array of app definitions.
        :type data: [ListAppsResponseDataItems], optional

        :param included: Data on the version of the app that was published.
        :type included: [Deployment], optional

        :param meta: Pagination metadata.
        :type meta: ListAppsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

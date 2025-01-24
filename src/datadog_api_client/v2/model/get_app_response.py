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
    from datadog_api_client.v2.model.get_app_response_data import GetAppResponseData
    from datadog_api_client.v2.model.deployment import Deployment
    from datadog_api_client.v2.model.app_meta import AppMeta
    from datadog_api_client.v2.model.app_relationship import AppRelationship


class GetAppResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_app_response_data import GetAppResponseData
        from datadog_api_client.v2.model.deployment import Deployment
        from datadog_api_client.v2.model.app_meta import AppMeta
        from datadog_api_client.v2.model.app_relationship import AppRelationship

        return {
            "data": (GetAppResponseData,),
            "included": ([Deployment],),
            "meta": (AppMeta,),
            "relationship": (AppRelationship,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
        "relationship": "relationship",
    }

    def __init__(
        self_,
        data: Union[GetAppResponseData, UnsetType] = unset,
        included: Union[List[Deployment], UnsetType] = unset,
        meta: Union[AppMeta, UnsetType] = unset,
        relationship: Union[AppRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        The full app definition response object.

        :param data: The data object containing the app definition.
        :type data: GetAppResponseData, optional

        :param included: Data on the version of the app that was published.
        :type included: [Deployment], optional

        :param meta: Metadata of an app.
        :type meta: AppMeta, optional

        :param relationship: The app's publication relationship and custom connections.
        :type relationship: AppRelationship, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        if relationship is not unset:
            kwargs["relationship"] = relationship
        super().__init__(kwargs)

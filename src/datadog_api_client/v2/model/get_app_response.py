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
    from datadog_api_client.v2.model.deployment_included import DeploymentIncluded
    from datadog_api_client.v2.model.app_meta import AppMeta
    from datadog_api_client.v2.model.get_app_response_relationship import GetAppResponseRelationship


class GetAppResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_app_response_data import GetAppResponseData
        from datadog_api_client.v2.model.deployment_included import DeploymentIncluded
        from datadog_api_client.v2.model.app_meta import AppMeta
        from datadog_api_client.v2.model.get_app_response_relationship import GetAppResponseRelationship

        return {
            "data": (GetAppResponseData,),
            "included": ([DeploymentIncluded],),
            "meta": (AppMeta,),
            "relationship": (GetAppResponseRelationship,),
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
        included: Union[List[DeploymentIncluded], UnsetType] = unset,
        meta: Union[AppMeta, UnsetType] = unset,
        relationship: Union[GetAppResponseRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``GetAppResponse`` object.

        :param data: The definition of ``GetAppResponseData`` object.
        :type data: GetAppResponseData, optional

        :param included: The ``GetAppResponse`` ``included``.
        :type included: [DeploymentIncluded], optional

        :param meta: The definition of ``AppMeta`` object.
        :type meta: AppMeta, optional

        :param relationship: The definition of ``GetAppResponseRelationship`` object.
        :type relationship: GetAppResponseRelationship, optional
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

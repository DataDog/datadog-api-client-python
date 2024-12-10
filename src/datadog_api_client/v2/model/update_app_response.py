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
    from datadog_api_client.v2.model.update_app_response_data import UpdateAppResponseData
    from datadog_api_client.v2.model.deployment_included import DeploymentIncluded
    from datadog_api_client.v2.model.app_meta import AppMeta
    from datadog_api_client.v2.model.update_app_response_relationship import UpdateAppResponseRelationship


class UpdateAppResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_response_data import UpdateAppResponseData
        from datadog_api_client.v2.model.deployment_included import DeploymentIncluded
        from datadog_api_client.v2.model.app_meta import AppMeta
        from datadog_api_client.v2.model.update_app_response_relationship import UpdateAppResponseRelationship

        return {
            "data": (UpdateAppResponseData,),
            "included": ([DeploymentIncluded],),
            "meta": (AppMeta,),
            "relationship": (UpdateAppResponseRelationship,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
        "relationship": "relationship",
    }

    def __init__(
        self_,
        data: Union[UpdateAppResponseData, UnsetType] = unset,
        included: Union[List[DeploymentIncluded], UnsetType] = unset,
        meta: Union[AppMeta, UnsetType] = unset,
        relationship: Union[UpdateAppResponseRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateAppResponse`` object.

        :param data: The definition of ``UpdateAppResponseData`` object.
        :type data: UpdateAppResponseData, optional

        :param included: The ``UpdateAppResponse`` ``included``.
        :type included: [DeploymentIncluded], optional

        :param meta: The definition of ``AppMeta`` object.
        :type meta: AppMeta, optional

        :param relationship: The definition of ``UpdateAppResponseRelationship`` object.
        :type relationship: UpdateAppResponseRelationship, optional
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

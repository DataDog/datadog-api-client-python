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
    from datadog_api_client.v2.model.deployment_included import DeploymentIncluded
    from datadog_api_client.v2.model.list_apps_response_meta import ListAppsResponseMeta


class ListAppsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_apps_response_data_items import ListAppsResponseDataItems
        from datadog_api_client.v2.model.deployment_included import DeploymentIncluded
        from datadog_api_client.v2.model.list_apps_response_meta import ListAppsResponseMeta

        return {
            "data": ([ListAppsResponseDataItems],),
            "included": ([DeploymentIncluded],),
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
        included: Union[List[DeploymentIncluded], UnsetType] = unset,
        meta: Union[ListAppsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ListAppsResponse`` object.

        :param data: The ``ListAppsResponse`` ``data``.
        :type data: [ListAppsResponseDataItems], optional

        :param included: The ``ListAppsResponse`` ``included``.
        :type included: [DeploymentIncluded], optional

        :param meta: The definition of ``ListAppsResponseMeta`` object.
        :type meta: ListAppsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

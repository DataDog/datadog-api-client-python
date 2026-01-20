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


class ObservabilityPipelineDatadogLogsDestinationRoute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_key_key": (str,),
            "include": (str,),
            "route_id": (str,),
            "site": (str,),
        }

    attribute_map = {
        "api_key_key": "api_key_key",
        "include": "include",
        "route_id": "route_id",
        "site": "site",
    }

    def __init__(
        self_,
        api_key_key: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        route_id: Union[str, UnsetType] = unset,
        site: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines how the ``datadog_logs`` destination routes matching logs to a Datadog site using a specific API key.

        :param api_key_key: Name of the environment variable or secret that stores the Datadog API key used by this route.
        :type api_key_key: str, optional

        :param include: A Datadog search query that determines which logs are forwarded using this route.
        :type include: str, optional

        :param route_id: Unique identifier for this route within the destination.
        :type route_id: str, optional

        :param site: Datadog site where matching logs are sent (for example, ``us1`` ).
        :type site: str, optional
        """
        if api_key_key is not unset:
            kwargs["api_key_key"] = api_key_key
        if include is not unset:
            kwargs["include"] = include
        if route_id is not unset:
            kwargs["route_id"] = route_id
        if site is not unset:
            kwargs["site"] = site
        super().__init__(kwargs)

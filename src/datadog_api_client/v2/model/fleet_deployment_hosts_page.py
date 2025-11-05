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


class FleetDeploymentHostsPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "current_page": (int,),
            "page_size": (int,),
            "total_hosts": (int,),
            "total_pages": (int,),
        }

    attribute_map = {
        "current_page": "current_page",
        "page_size": "page_size",
        "total_hosts": "total_hosts",
        "total_pages": "total_pages",
    }

    def __init__(
        self_,
        current_page: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        total_hosts: Union[int, UnsetType] = unset,
        total_pages: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination details for the list of hosts in a deployment.

        :param current_page: Current page index (zero-based).
        :type current_page: int, optional

        :param page_size: Number of hosts returned per page.
        :type page_size: int, optional

        :param total_hosts: Total number of hosts in this deployment.
        :type total_hosts: int, optional

        :param total_pages: Total number of pages available.
        :type total_pages: int, optional
        """
        if current_page is not unset:
            kwargs["current_page"] = current_page
        if page_size is not unset:
            kwargs["page_size"] = page_size
        if total_hosts is not unset:
            kwargs["total_hosts"] = total_hosts
        if total_pages is not unset:
            kwargs["total_pages"] = total_pages
        super().__init__(kwargs)

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
    from datadog_api_client.v2.model.list_findings_page import ListFindingsPage


class ListFindingsMeta(ModelNormal):
    validations = {
        "snapshot_timestamp": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_findings_page import ListFindingsPage

        return {
            "page": (ListFindingsPage,),
            "snapshot_timestamp": (int,),
        }

    attribute_map = {
        "page": "page",
        "snapshot_timestamp": "snapshot_timestamp",
    }

    def __init__(
        self_,
        page: Union[ListFindingsPage, UnsetType] = unset,
        snapshot_timestamp: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for pagination.

        :param page: Pagination and findings count information.
        :type page: ListFindingsPage, optional

        :param snapshot_timestamp: The point in time corresponding to the listed findings.
        :type snapshot_timestamp: int, optional
        """
        if page is not unset:
            kwargs["page"] = page
        if snapshot_timestamp is not unset:
            kwargs["snapshot_timestamp"] = snapshot_timestamp
        super().__init__(kwargs)

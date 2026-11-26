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
    from datadog_api_client.v2.model.gcp_project_filter_config_type import GCPProjectFilterConfigType


class GCPProjectFilterConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_project_filter_config_type import GCPProjectFilterConfigType

        return {
            "filters": ([str],),
            "type": (GCPProjectFilterConfigType,),
        }

    attribute_map = {
        "filters": "filters",
        "type": "type",
    }

    def __init__(
        self_,
        filters: Union[List[str], UnsetType] = unset,
        type: Union[GCPProjectFilterConfigType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for filtering the GCP projects that Datadog monitors by project ID or by project label.

        :param filters: List of filters matched against the project field set by ``type``. Filters support the ``*`` and ``?``
            wildcards, and a leading ``!`` makes a filter an exclusion. A project is skipped if it matches any
            exclusion filter. When inclusion filters are set, a project must also match at least one of them.
            For ``project_id`` , each filter is a project ID pattern, such as ``prod-*``. You can set up to 15,000
            filters. For ``project_label`` , each filter is a label in the form ``key:value`` , such as ``env:prod*``.
            You can set up to 100 filters. Keys are matched exactly, and wildcards apply only to values, so
            ``key:*`` matches any value.
        :type filters: [str], optional

        :param type: The GCP project field that the filters are matched against.
        :type type: GCPProjectFilterConfigType, optional
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

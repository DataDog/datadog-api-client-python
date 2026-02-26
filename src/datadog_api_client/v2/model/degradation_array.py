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
    from datadog_api_client.v2.model.degradation_data import DegradationData
    from datadog_api_client.v2.model.degradation_included import DegradationIncluded
    from datadog_api_client.v2.model.pagination_meta import PaginationMeta
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser
    from datadog_api_client.v2.model.status_page_as_included import StatusPageAsIncluded


class DegradationArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_data import DegradationData
        from datadog_api_client.v2.model.degradation_included import DegradationIncluded
        from datadog_api_client.v2.model.pagination_meta import PaginationMeta

        return {
            "data": ([DegradationData],),
            "included": ([DegradationIncluded],),
            "meta": (PaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }
    read_only_vars = {
        "meta",
    }

    def __init__(
        self_,
        data: List[DegradationData],
        included: Union[List[Union[DegradationIncluded, StatusPagesUser, StatusPageAsIncluded]], UnsetType] = unset,
        meta: Union[PaginationMeta, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: [DegradationData]

        :param included: The included related resources of a degradation. Client must explicitly request these resources by name in the ``include`` query parameter.
        :type included: [DegradationIncluded], optional

        :param meta: Response metadata.
        :type meta: PaginationMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

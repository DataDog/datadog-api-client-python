# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.temporary_grant_request_data import TemporaryGrantRequestData
    from datadog_api_client.v2.model.temporary_grant_request_list_meta import TemporaryGrantRequestListMeta


class TemporaryGrantRequestListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_data import TemporaryGrantRequestData
        from datadog_api_client.v2.model.temporary_grant_request_list_meta import TemporaryGrantRequestListMeta

        return {
            "data": ([TemporaryGrantRequestData],),
            "meta": (TemporaryGrantRequestListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[TemporaryGrantRequestData], meta: TemporaryGrantRequestListMeta, **kwargs):
        """
        A page of temporary grant requests, ordered by UUID rather than creation time.

        :param data: Requests visible to the authenticated caller.
        :type data: [TemporaryGrantRequestData]

        :param meta: Pagination metadata.
        :type meta: TemporaryGrantRequestListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta

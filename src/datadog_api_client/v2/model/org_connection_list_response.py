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
    from datadog_api_client.v2.model.org_connection import OrgConnection
    from datadog_api_client.v2.model.org_connection_list_response_meta import OrgConnectionListResponseMeta


class OrgConnectionListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection import OrgConnection
        from datadog_api_client.v2.model.org_connection_list_response_meta import OrgConnectionListResponseMeta

        return {
            "data": ([OrgConnection],),
            "meta": (OrgConnectionListResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[OrgConnection], meta: Union[OrgConnectionListResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a list of org connections.

        :param data: List of org connections.
        :type data: [OrgConnection]

        :param meta: Pagination metadata.
        :type meta: OrgConnectionListResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

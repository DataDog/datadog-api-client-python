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
    from datadog_api_client.v2.model.rum_operation_strong_link_response_data import RUMOperationStrongLinkResponseData
    from datadog_api_client.v2.model.rum_operation_strong_links_list_response_meta import (
        RUMOperationStrongLinksListResponseMeta,
    )


class RUMOperationStrongLinksListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_response_data import (
            RUMOperationStrongLinkResponseData,
        )
        from datadog_api_client.v2.model.rum_operation_strong_links_list_response_meta import (
            RUMOperationStrongLinksListResponseMeta,
        )

        return {
            "data": ([RUMOperationStrongLinkResponseData],),
            "meta": (RUMOperationStrongLinksListResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[RUMOperationStrongLinkResponseData],
        meta: Union[RUMOperationStrongLinksListResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response for a list of RUM operation strong links.

        :param data:
        :type data: [RUMOperationStrongLinkResponseData]

        :param meta: Metadata for a list of RUM operation strong links.
        :type meta: RUMOperationStrongLinksListResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

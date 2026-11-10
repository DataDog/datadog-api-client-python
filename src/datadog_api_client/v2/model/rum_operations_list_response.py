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
    from datadog_api_client.v2.model.rum_operation_response_data import RUMOperationResponseData
    from datadog_api_client.v2.model.rum_operations_list_response_links import RUMOperationsListResponseLinks
    from datadog_api_client.v2.model.rum_operations_list_response_meta import RUMOperationsListResponseMeta


class RUMOperationsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_response_data import RUMOperationResponseData
        from datadog_api_client.v2.model.rum_operations_list_response_links import RUMOperationsListResponseLinks
        from datadog_api_client.v2.model.rum_operations_list_response_meta import RUMOperationsListResponseMeta

        return {
            "data": ([RUMOperationResponseData],),
            "links": (RUMOperationsListResponseLinks,),
            "meta": (RUMOperationsListResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[RUMOperationResponseData],
        links: Union[RUMOperationsListResponseLinks, UnsetType] = unset,
        meta: Union[RUMOperationsListResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response for a list of RUM operations.

        :param data:
        :type data: [RUMOperationResponseData]

        :param links: Pagination links for a list of RUM operations.
        :type links: RUMOperationsListResponseLinks, optional

        :param meta: Metadata for a list of RUM operations.
        :type meta: RUMOperationsListResponseMeta, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

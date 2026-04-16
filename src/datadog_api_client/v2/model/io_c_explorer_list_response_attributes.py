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
    from datadog_api_client.v2.model.io_c_indicator import IoCIndicator
    from datadog_api_client.v2.model.io_c_explorer_list_response_metadata import IoCExplorerListResponseMetadata
    from datadog_api_client.v2.model.io_c_explorer_list_response_paging import IoCExplorerListResponsePaging


class IoCExplorerListResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_indicator import IoCIndicator
        from datadog_api_client.v2.model.io_c_explorer_list_response_metadata import IoCExplorerListResponseMetadata
        from datadog_api_client.v2.model.io_c_explorer_list_response_paging import IoCExplorerListResponsePaging

        return {
            "data": ([IoCIndicator],),
            "metadata": (IoCExplorerListResponseMetadata,),
            "paging": (IoCExplorerListResponsePaging,),
        }

    attribute_map = {
        "data": "data",
        "metadata": "metadata",
        "paging": "paging",
    }

    def __init__(
        self_,
        data: Union[List[IoCIndicator], UnsetType] = unset,
        metadata: Union[IoCExplorerListResponseMetadata, UnsetType] = unset,
        paging: Union[IoCExplorerListResponsePaging, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the IoC Explorer list response.

        :param data: List of indicators of compromise.
        :type data: [IoCIndicator], optional

        :param metadata: Response metadata.
        :type metadata: IoCExplorerListResponseMetadata, optional

        :param paging: Pagination information.
        :type paging: IoCExplorerListResponsePaging, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if paging is not unset:
            kwargs["paging"] = paging
        super().__init__(kwargs)

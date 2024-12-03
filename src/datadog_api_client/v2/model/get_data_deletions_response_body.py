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
    from datadog_api_client.v2.model.data_deletion_response_item import DataDeletionResponseItem
    from datadog_api_client.v2.model.data_deletion_response_meta import DataDeletionResponseMeta


class GetDataDeletionsResponseBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.data_deletion_response_item import DataDeletionResponseItem
        from datadog_api_client.v2.model.data_deletion_response_meta import DataDeletionResponseMeta

        return {
            "data": ([DataDeletionResponseItem],),
            "meta": (DataDeletionResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[DataDeletionResponseItem], UnsetType] = unset,
        meta: Union[DataDeletionResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response from the get data deletion requests endpoint.

        :param data: The list of data deletion requests that matches the query.
        :type data: [DataDeletionResponseItem], optional

        :param meta: The metadata of the data deletion response.
        :type meta: DataDeletionResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

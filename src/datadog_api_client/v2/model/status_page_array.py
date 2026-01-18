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
    from datadog_api_client.v2.model.status_page_data import StatusPageData
    from datadog_api_client.v2.model.status_page_array_included import StatusPageArrayIncluded
    from datadog_api_client.v2.model.status_pages_response_meta import StatusPagesResponseMeta
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser


class StatusPageArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_data import StatusPageData
        from datadog_api_client.v2.model.status_page_array_included import StatusPageArrayIncluded
        from datadog_api_client.v2.model.status_pages_response_meta import StatusPagesResponseMeta

        return {
            "data": ([StatusPageData],),
            "included": ([StatusPageArrayIncluded],),
            "meta": (StatusPagesResponseMeta,),
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
        data: List[StatusPageData],
        included: Union[List[Union[StatusPageArrayIncluded, StatusPagesUser]], UnsetType] = unset,
        meta: Union[StatusPagesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: [StatusPageData]

        :param included: The included related resources of a status page. Client must explicitly request these resources by name in the ``include`` query parameter.
        :type included: [StatusPageArrayIncluded], optional

        :param meta: Response metadata.
        :type meta: StatusPagesResponseMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

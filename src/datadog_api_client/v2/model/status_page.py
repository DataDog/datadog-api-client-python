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
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser


class StatusPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_data import StatusPageData
        from datadog_api_client.v2.model.status_page_array_included import StatusPageArrayIncluded

        return {
            "data": (StatusPageData,),
            "included": ([StatusPageArrayIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[StatusPageData, UnsetType] = unset,
        included: Union[List[Union[StatusPageArrayIncluded, StatusPagesUser]], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: StatusPageData, optional

        :param included:
        :type included: [StatusPageArrayIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

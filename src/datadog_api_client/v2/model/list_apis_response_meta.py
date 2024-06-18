# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_apis_response_meta_pagination import ListAPIsResponseMetaPagination


class ListAPIsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_apis_response_meta_pagination import ListAPIsResponseMetaPagination

        return {
            "pagination": (ListAPIsResponseMetaPagination,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    def __init__(self_, pagination: Union[ListAPIsResponseMetaPagination, UnsetType] = unset, **kwargs):
        """
        Metadata for ``ListAPIsResponse``.

        :param pagination: Pagination metadata information for ``ListAPIsResponse``.
        :type pagination: ListAPIsResponseMetaPagination, optional
        """
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)

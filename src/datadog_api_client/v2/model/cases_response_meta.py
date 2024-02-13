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
    from datadog_api_client.v2.model.cases_response_meta_pagination import CasesResponseMetaPagination


class CasesResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cases_response_meta_pagination import CasesResponseMetaPagination

        return {
            "page": (CasesResponseMetaPagination,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[CasesResponseMetaPagination, UnsetType] = unset, **kwargs):
        """
        Cases response metadata

        :param page: Pagination metadata
        :type page: CasesResponseMetaPagination, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)

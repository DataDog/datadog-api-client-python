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
    from datadog_api_client.v2.model.environments_pagination_meta_page import EnvironmentsPaginationMetaPage


class EnvironmentsPaginationMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.environments_pagination_meta_page import EnvironmentsPaginationMetaPage

        return {
            "page": (EnvironmentsPaginationMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[EnvironmentsPaginationMetaPage, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for environments.

        :param page: Pagination metadata for environments list responses.
        :type page: EnvironmentsPaginationMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)

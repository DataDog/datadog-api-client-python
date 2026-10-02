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
    from datadog_api_client.v2.model.experiments_offset_meta_page import ExperimentsOffsetMetaPage


class ExperimentsOffsetMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_offset_meta_page import ExperimentsOffsetMetaPage

        return {
            "page": (ExperimentsOffsetMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[ExperimentsOffsetMetaPage, UnsetType] = unset, **kwargs):
        """
        Pagination information for a list response.

        :param page: Result counts and offsets for a page of results.
        :type page: ExperimentsOffsetMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)

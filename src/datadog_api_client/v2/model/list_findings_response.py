# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.finding import Finding
    from datadog_api_client.v2.model.list_findings_meta import ListFindingsMeta


class ListFindingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding import Finding
        from datadog_api_client.v2.model.list_findings_meta import ListFindingsMeta

        return {
            "data": ([Finding],),
            "meta": (ListFindingsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[Finding], meta: ListFindingsMeta, **kwargs):
        """
        The expected response schema when listing findings.

        :param data: Array of findings.
        :type data: [Finding]

        :param meta: Metadata for pagination.
        :type meta: ListFindingsMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta

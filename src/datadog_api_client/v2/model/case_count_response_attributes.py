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
    from datadog_api_client.v2.model.case_count_group import CaseCountGroup


class CaseCountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_count_group import CaseCountGroup

        return {
            "groups": ([CaseCountGroup],),
        }

    attribute_map = {
        "groups": "groups",
    }

    def __init__(self_, groups: List[CaseCountGroup], **kwargs):
        """
        Attributes for the count response, including the total count and optional facet breakdowns.

        :param groups: List of facet groups, one per field specified in ``group_bys``.
        :type groups: [CaseCountGroup]
        """
        super().__init__(kwargs)

        self_.groups = groups

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_impact import IssueImpact


class IssueImpactResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact import IssueImpact

        return {
            "data": (IssueImpact,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IssueImpact, **kwargs):
        """
        Response containing the impact of an error tracking issue.

        :param data: The impact of an issue over the requested time window.
        :type data: IssueImpact
        """
        super().__init__(kwargs)

        self_.data = data

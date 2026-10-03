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
    from datadog_api_client.v2.model.case_view import CaseView


class CaseViewResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_view import CaseView

        return {
            "data": (CaseView,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseView, **kwargs):
        """
        Response containing a single work item view.

        :param data: A saved work item view that provides a filtered, reusable list of work items matching a specific query. Views act as persistent dashboards for monitoring work item subsets.
        :type data: CaseView
        """
        super().__init__(kwargs)

        self_.data = data

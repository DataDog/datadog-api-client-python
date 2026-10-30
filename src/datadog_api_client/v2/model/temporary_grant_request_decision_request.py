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
    from datadog_api_client.v2.model.temporary_grant_request_decision_data import TemporaryGrantRequestDecisionData


class TemporaryGrantRequestDecisionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_decision_data import TemporaryGrantRequestDecisionData

        return {
            "data": (TemporaryGrantRequestDecisionData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TemporaryGrantRequestDecisionData, **kwargs):
        """
        Approve or deny a pending request.

        :param data: A decision on a pending request.
        :type data: TemporaryGrantRequestDecisionData
        """
        super().__init__(kwargs)

        self_.data = data

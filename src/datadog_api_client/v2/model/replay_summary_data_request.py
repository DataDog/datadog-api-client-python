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
    from datadog_api_client.v2.model.replay_summary_request_type import ReplaySummaryRequestType


class ReplaySummaryDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_summary_request_type import ReplaySummaryRequestType

        return {
            "type": (ReplaySummaryRequestType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ReplaySummaryRequestType, **kwargs):
        """
        Data object for a RUM replay summary request.

        :param type: RUM replay summary request resource type.
        :type type: ReplaySummaryRequestType
        """
        super().__init__(kwargs)

        self_.type = type

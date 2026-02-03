# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ViewershipHistorySessionDataType(ModelSimple):
    """
    Rum replay session resource type.

    :param value: If omitted defaults to "rum_replay_session". Must be one of ["rum_replay_session"].
    :type value: str
    """

    allowed_values = {
        "rum_replay_session",
    }
    RUM_REPLAY_SESSION: ClassVar["ViewershipHistorySessionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ViewershipHistorySessionDataType.RUM_REPLAY_SESSION = ViewershipHistorySessionDataType("rum_replay_session")

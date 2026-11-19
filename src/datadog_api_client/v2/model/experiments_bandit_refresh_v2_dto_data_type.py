# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditRefreshV2DTODataType(ModelSimple):
    """
    Bandit refresh resource type.

    :param value: If omitted defaults to "bandit-refresh". Must be one of ["bandit-refresh"].
    :type value: str
    """

    allowed_values = {
        "bandit-refresh",
    }
    BANDIT_REFRESH: ClassVar["ExperimentsBanditRefreshV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditRefreshV2DTODataType.BANDIT_REFRESH = ExperimentsBanditRefreshV2DTODataType("bandit-refresh")

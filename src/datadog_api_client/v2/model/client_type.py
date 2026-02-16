# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ClientType(ModelSimple):
    """
    The client type for action filtering.

    :param value: Must be one of ["workflows", "app_builder", "actions_api"].
    :type value: str
    """

    allowed_values = {
        "workflows",
        "app_builder",
        "actions_api",
    }
    WORKFLOWS: ClassVar["ClientType"]
    APP_BUILDER: ClassVar["ClientType"]
    ACTIONS_API: ClassVar["ClientType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ClientType.WORKFLOWS = ClientType("workflows")
ClientType.APP_BUILDER = ClientType("app_builder")
ClientType.ACTIONS_API = ClientType("actions_api")

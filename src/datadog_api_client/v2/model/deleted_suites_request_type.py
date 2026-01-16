# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DeletedSuitesRequestType(ModelSimple):
    """


    :param value: If omitted defaults to "delete_suites_request". Must be one of ["delete_suites_request"].
    :type value: str
    """

    allowed_values = {
        "delete_suites_request",
    }
    DELETE_SUITES_REQUEST: ClassVar["DeletedSuitesRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DeletedSuitesRequestType.DELETE_SUITES_REQUEST = DeletedSuitesRequestType("delete_suites_request")

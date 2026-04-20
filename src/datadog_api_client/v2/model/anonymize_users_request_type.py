# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnonymizeUsersRequestType(ModelSimple):
    """
    Type of the anonymize users request.

    :param value: If omitted defaults to "anonymize_users_request". Must be one of ["anonymize_users_request"].
    :type value: str
    """

    allowed_values = {
        "anonymize_users_request",
    }
    ANONYMIZE_USERS_REQUEST: ClassVar["AnonymizeUsersRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnonymizeUsersRequestType.ANONYMIZE_USERS_REQUEST = AnonymizeUsersRequestType("anonymize_users_request")

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateDataDeletionRequestBodyDataType(ModelSimple):
    """
    The deletion request type.

    :param value: If omitted defaults to "create_deletion_req". Must be one of ["create_deletion_req"].
    :type value: str
    """

    allowed_values = {
        "create_deletion_req",
    }
    CREATE_DELETION_REQ: ClassVar["CreateDataDeletionRequestBodyDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateDataDeletionRequestBodyDataType.CREATE_DELETION_REQ = CreateDataDeletionRequestBodyDataType("create_deletion_req")

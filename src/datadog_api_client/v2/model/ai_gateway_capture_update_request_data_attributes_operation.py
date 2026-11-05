# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCaptureUpdateRequestDataAttributesOperation(ModelSimple):
    """
    Proposed operation for preview. Write endpoints infer it from the HTTP method.

    :param value: Must be one of ["create", "replace", "delete"].
    :type value: str
    """

    allowed_values = {
        "create",
        "replace",
        "delete",
    }
    CREATE: ClassVar["AiGatewayCaptureUpdateRequestDataAttributesOperation"]
    REPLACE: ClassVar["AiGatewayCaptureUpdateRequestDataAttributesOperation"]
    DELETE: ClassVar["AiGatewayCaptureUpdateRequestDataAttributesOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCaptureUpdateRequestDataAttributesOperation.CREATE = AiGatewayCaptureUpdateRequestDataAttributesOperation(
    "create"
)
AiGatewayCaptureUpdateRequestDataAttributesOperation.REPLACE = AiGatewayCaptureUpdateRequestDataAttributesOperation(
    "replace"
)
AiGatewayCaptureUpdateRequestDataAttributesOperation.DELETE = AiGatewayCaptureUpdateRequestDataAttributesOperation(
    "delete"
)

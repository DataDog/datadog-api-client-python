# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsAssertionJSONSchemaMetaSchema(ModelSimple):
    """
    The JSON Schema meta-schema version used in the assertion.

    :param value: Must be one of ["draft-07", "draft-06"].
    :type value: str
    """

    allowed_values = {
        "draft-07",
        "draft-06",
    }
    DRAFT_07: ClassVar["SyntheticsAssertionJSONSchemaMetaSchema"]
    DRAFT_06: ClassVar["SyntheticsAssertionJSONSchemaMetaSchema"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsAssertionJSONSchemaMetaSchema.DRAFT_07 = SyntheticsAssertionJSONSchemaMetaSchema("draft-07")
SyntheticsAssertionJSONSchemaMetaSchema.DRAFT_06 = SyntheticsAssertionJSONSchemaMetaSchema("draft-06")

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DataAttributesRulesItemsIfTagExists(ModelSimple):
    """
    The behavior when the tag already exists.

    :param value: Must be one of ["append", "do_not_apply", "replace"].
    :type value: str
    """

    allowed_values = {
        "append",
        "do_not_apply",
        "replace",
    }
    APPEND: ClassVar["DataAttributesRulesItemsIfTagExists"]
    DO_NOT_APPLY: ClassVar["DataAttributesRulesItemsIfTagExists"]
    REPLACE: ClassVar["DataAttributesRulesItemsIfTagExists"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DataAttributesRulesItemsIfTagExists.APPEND = DataAttributesRulesItemsIfTagExists("append")
DataAttributesRulesItemsIfTagExists.DO_NOT_APPLY = DataAttributesRulesItemsIfTagExists("do_not_apply")
DataAttributesRulesItemsIfTagExists.REPLACE = DataAttributesRulesItemsIfTagExists("replace")

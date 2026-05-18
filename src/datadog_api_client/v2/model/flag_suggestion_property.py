# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlagSuggestionProperty(ModelSimple):
    """
    The flag property being changed.

    :param value: Must be one of ["FLAG", "FLAG_NAME", "FLAG_DESCRIPTION", "JSON_SCHEMA", "DISTRIBUTION_CHANNEL", "VARIANT", "VARIANT_NAME", "VARIANT_VALUE", "ALLOCATIONS", "ROLLOUT", "ENVIRONMENT_STATUS", "DEFAULT_VARIANT", "OVERRIDE_VARIANT"].
    :type value: str
    """

    allowed_values = {
        "FLAG",
        "FLAG_NAME",
        "FLAG_DESCRIPTION",
        "JSON_SCHEMA",
        "DISTRIBUTION_CHANNEL",
        "VARIANT",
        "VARIANT_NAME",
        "VARIANT_VALUE",
        "ALLOCATIONS",
        "ROLLOUT",
        "ENVIRONMENT_STATUS",
        "DEFAULT_VARIANT",
        "OVERRIDE_VARIANT",
    }
    FLAG: ClassVar["FlagSuggestionProperty"]
    FLAG_NAME: ClassVar["FlagSuggestionProperty"]
    FLAG_DESCRIPTION: ClassVar["FlagSuggestionProperty"]
    JSON_SCHEMA: ClassVar["FlagSuggestionProperty"]
    DISTRIBUTION_CHANNEL: ClassVar["FlagSuggestionProperty"]
    VARIANT: ClassVar["FlagSuggestionProperty"]
    VARIANT_NAME: ClassVar["FlagSuggestionProperty"]
    VARIANT_VALUE: ClassVar["FlagSuggestionProperty"]
    ALLOCATIONS: ClassVar["FlagSuggestionProperty"]
    ROLLOUT: ClassVar["FlagSuggestionProperty"]
    ENVIRONMENT_STATUS: ClassVar["FlagSuggestionProperty"]
    DEFAULT_VARIANT: ClassVar["FlagSuggestionProperty"]
    OVERRIDE_VARIANT: ClassVar["FlagSuggestionProperty"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlagSuggestionProperty.FLAG = FlagSuggestionProperty("FLAG")
FlagSuggestionProperty.FLAG_NAME = FlagSuggestionProperty("FLAG_NAME")
FlagSuggestionProperty.FLAG_DESCRIPTION = FlagSuggestionProperty("FLAG_DESCRIPTION")
FlagSuggestionProperty.JSON_SCHEMA = FlagSuggestionProperty("JSON_SCHEMA")
FlagSuggestionProperty.DISTRIBUTION_CHANNEL = FlagSuggestionProperty("DISTRIBUTION_CHANNEL")
FlagSuggestionProperty.VARIANT = FlagSuggestionProperty("VARIANT")
FlagSuggestionProperty.VARIANT_NAME = FlagSuggestionProperty("VARIANT_NAME")
FlagSuggestionProperty.VARIANT_VALUE = FlagSuggestionProperty("VARIANT_VALUE")
FlagSuggestionProperty.ALLOCATIONS = FlagSuggestionProperty("ALLOCATIONS")
FlagSuggestionProperty.ROLLOUT = FlagSuggestionProperty("ROLLOUT")
FlagSuggestionProperty.ENVIRONMENT_STATUS = FlagSuggestionProperty("ENVIRONMENT_STATUS")
FlagSuggestionProperty.DEFAULT_VARIANT = FlagSuggestionProperty("DEFAULT_VARIANT")
FlagSuggestionProperty.OVERRIDE_VARIANT = FlagSuggestionProperty("OVERRIDE_VARIANT")

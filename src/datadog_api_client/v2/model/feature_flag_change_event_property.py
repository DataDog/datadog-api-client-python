# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagChangeEventProperty(ModelSimple):
    """
    The part of the feature flag the change applies to.

    :param value: Must be one of ["FLAG", "FLAG_NAME", "FLAG_DESCRIPTION", "JSON_SCHEMA", "DISTRIBUTION_CHANNEL", "REQUIRE_APPROVAL", "VARIANT", "VARIANT_NAME", "VARIANT_VALUE", "ALLOCATIONS", "ROLLOUT", "ENVIRONMENT_STATUS", "DEFAULT_VARIANT", "OVERRIDE_VARIANT", "STALENESS_STATUS", "SAVED_FILTER"].
    :type value: str
    """

    allowed_values = {
        "FLAG",
        "FLAG_NAME",
        "FLAG_DESCRIPTION",
        "JSON_SCHEMA",
        "DISTRIBUTION_CHANNEL",
        "REQUIRE_APPROVAL",
        "VARIANT",
        "VARIANT_NAME",
        "VARIANT_VALUE",
        "ALLOCATIONS",
        "ROLLOUT",
        "ENVIRONMENT_STATUS",
        "DEFAULT_VARIANT",
        "OVERRIDE_VARIANT",
        "STALENESS_STATUS",
        "SAVED_FILTER",
    }
    FLAG: ClassVar["FeatureFlagChangeEventProperty"]
    FLAG_NAME: ClassVar["FeatureFlagChangeEventProperty"]
    FLAG_DESCRIPTION: ClassVar["FeatureFlagChangeEventProperty"]
    JSON_SCHEMA: ClassVar["FeatureFlagChangeEventProperty"]
    DISTRIBUTION_CHANNEL: ClassVar["FeatureFlagChangeEventProperty"]
    REQUIRE_APPROVAL: ClassVar["FeatureFlagChangeEventProperty"]
    VARIANT: ClassVar["FeatureFlagChangeEventProperty"]
    VARIANT_NAME: ClassVar["FeatureFlagChangeEventProperty"]
    VARIANT_VALUE: ClassVar["FeatureFlagChangeEventProperty"]
    ALLOCATIONS: ClassVar["FeatureFlagChangeEventProperty"]
    ROLLOUT: ClassVar["FeatureFlagChangeEventProperty"]
    ENVIRONMENT_STATUS: ClassVar["FeatureFlagChangeEventProperty"]
    DEFAULT_VARIANT: ClassVar["FeatureFlagChangeEventProperty"]
    OVERRIDE_VARIANT: ClassVar["FeatureFlagChangeEventProperty"]
    STALENESS_STATUS: ClassVar["FeatureFlagChangeEventProperty"]
    SAVED_FILTER: ClassVar["FeatureFlagChangeEventProperty"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagChangeEventProperty.FLAG = FeatureFlagChangeEventProperty("FLAG")
FeatureFlagChangeEventProperty.FLAG_NAME = FeatureFlagChangeEventProperty("FLAG_NAME")
FeatureFlagChangeEventProperty.FLAG_DESCRIPTION = FeatureFlagChangeEventProperty("FLAG_DESCRIPTION")
FeatureFlagChangeEventProperty.JSON_SCHEMA = FeatureFlagChangeEventProperty("JSON_SCHEMA")
FeatureFlagChangeEventProperty.DISTRIBUTION_CHANNEL = FeatureFlagChangeEventProperty("DISTRIBUTION_CHANNEL")
FeatureFlagChangeEventProperty.REQUIRE_APPROVAL = FeatureFlagChangeEventProperty("REQUIRE_APPROVAL")
FeatureFlagChangeEventProperty.VARIANT = FeatureFlagChangeEventProperty("VARIANT")
FeatureFlagChangeEventProperty.VARIANT_NAME = FeatureFlagChangeEventProperty("VARIANT_NAME")
FeatureFlagChangeEventProperty.VARIANT_VALUE = FeatureFlagChangeEventProperty("VARIANT_VALUE")
FeatureFlagChangeEventProperty.ALLOCATIONS = FeatureFlagChangeEventProperty("ALLOCATIONS")
FeatureFlagChangeEventProperty.ROLLOUT = FeatureFlagChangeEventProperty("ROLLOUT")
FeatureFlagChangeEventProperty.ENVIRONMENT_STATUS = FeatureFlagChangeEventProperty("ENVIRONMENT_STATUS")
FeatureFlagChangeEventProperty.DEFAULT_VARIANT = FeatureFlagChangeEventProperty("DEFAULT_VARIANT")
FeatureFlagChangeEventProperty.OVERRIDE_VARIANT = FeatureFlagChangeEventProperty("OVERRIDE_VARIANT")
FeatureFlagChangeEventProperty.STALENESS_STATUS = FeatureFlagChangeEventProperty("STALENESS_STATUS")
FeatureFlagChangeEventProperty.SAVED_FILTER = FeatureFlagChangeEventProperty("SAVED_FILTER")

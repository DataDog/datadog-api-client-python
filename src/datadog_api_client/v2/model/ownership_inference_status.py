# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipInferenceStatus(ModelSimple):
    """
    The lifecycle status of an ownership inference.

    :param value: Must be one of ["suggested", "persisted", "overridden", "failed", "unknown"].
    :type value: str
    """

    allowed_values = {
        "suggested",
        "persisted",
        "overridden",
        "failed",
        "unknown",
    }
    SUGGESTED: ClassVar["OwnershipInferenceStatus"]
    PERSISTED: ClassVar["OwnershipInferenceStatus"]
    OVERRIDDEN: ClassVar["OwnershipInferenceStatus"]
    FAILED: ClassVar["OwnershipInferenceStatus"]
    UNKNOWN: ClassVar["OwnershipInferenceStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipInferenceStatus.SUGGESTED = OwnershipInferenceStatus("suggested")
OwnershipInferenceStatus.PERSISTED = OwnershipInferenceStatus("persisted")
OwnershipInferenceStatus.OVERRIDDEN = OwnershipInferenceStatus("overridden")
OwnershipInferenceStatus.FAILED = OwnershipInferenceStatus("failed")
OwnershipInferenceStatus.UNKNOWN = OwnershipInferenceStatus("unknown")

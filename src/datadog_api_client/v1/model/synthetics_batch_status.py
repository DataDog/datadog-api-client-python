# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBatchStatus(ModelSimple):
    """
    Determines whether the batch has passed, failed, or is in progress.

    :param value: Must be one of ["passed", "skipped", "failed"].
    :type value: str
    """

    allowed_values = {
        "passed",
        "skipped",
        "failed",
    }
    PASSED: ClassVar["SyntheticsBatchStatus"]
    SKIPPED: ClassVar["SyntheticsBatchStatus"]
    FAILED: ClassVar["SyntheticsBatchStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBatchStatus.PASSED = SyntheticsBatchStatus("passed")
SyntheticsBatchStatus.SKIPPED = SyntheticsBatchStatus("skipped")
SyntheticsBatchStatus.FAILED = SyntheticsBatchStatus("failed")

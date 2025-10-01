# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlakyTestsSearchSort(ModelSimple):
    """
    Parameter for sorting flaky test results. The default sort is by ascending Fully Qualified Name (FQN). The FQN is the concatenation of the test module, suite, and name.

    :param value: Must be one of ["fqn", "-fqn", "first_flaked", "-first_flaked", "last_flaked", "-last_flaked", "failure_rate", "-failure_rate", "pipelines_failed", "-pipelines_failed", "pipelines_duration_lost", "-pipelines_duration_lost"].
    :type value: str
    """

    allowed_values = {
        "fqn",
        "-fqn",
        "first_flaked",
        "-first_flaked",
        "last_flaked",
        "-last_flaked",
        "failure_rate",
        "-failure_rate",
        "pipelines_failed",
        "-pipelines_failed",
        "pipelines_duration_lost",
        "-pipelines_duration_lost",
    }
    FQN_ASCENDING: ClassVar["FlakyTestsSearchSort"]
    FQN_DESCENDING: ClassVar["FlakyTestsSearchSort"]
    FIRST_FLAKED_ASCENDING: ClassVar["FlakyTestsSearchSort"]
    FIRST_FLAKED_DESCENDING: ClassVar["FlakyTestsSearchSort"]
    LAST_FLAKED_ASCENDING: ClassVar["FlakyTestsSearchSort"]
    LAST_FLAKED_DESCENDING: ClassVar["FlakyTestsSearchSort"]
    FAILURE_RATE_ASCENDING: ClassVar["FlakyTestsSearchSort"]
    FAILURE_RATE_DESCENDING: ClassVar["FlakyTestsSearchSort"]
    PIPELINES_FAILED_ASCENDING: ClassVar["FlakyTestsSearchSort"]
    PIPELINES_FAILED_DESCENDING: ClassVar["FlakyTestsSearchSort"]
    PIPELINES_DURATION_LOST_ASCENDING: ClassVar["FlakyTestsSearchSort"]
    PIPELINES_DURATION_LOST_DESCENDING: ClassVar["FlakyTestsSearchSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlakyTestsSearchSort.FQN_ASCENDING = FlakyTestsSearchSort("fqn")
FlakyTestsSearchSort.FQN_DESCENDING = FlakyTestsSearchSort("-fqn")
FlakyTestsSearchSort.FIRST_FLAKED_ASCENDING = FlakyTestsSearchSort("first_flaked")
FlakyTestsSearchSort.FIRST_FLAKED_DESCENDING = FlakyTestsSearchSort("-first_flaked")
FlakyTestsSearchSort.LAST_FLAKED_ASCENDING = FlakyTestsSearchSort("last_flaked")
FlakyTestsSearchSort.LAST_FLAKED_DESCENDING = FlakyTestsSearchSort("-last_flaked")
FlakyTestsSearchSort.FAILURE_RATE_ASCENDING = FlakyTestsSearchSort("failure_rate")
FlakyTestsSearchSort.FAILURE_RATE_DESCENDING = FlakyTestsSearchSort("-failure_rate")
FlakyTestsSearchSort.PIPELINES_FAILED_ASCENDING = FlakyTestsSearchSort("pipelines_failed")
FlakyTestsSearchSort.PIPELINES_FAILED_DESCENDING = FlakyTestsSearchSort("-pipelines_failed")
FlakyTestsSearchSort.PIPELINES_DURATION_LOST_ASCENDING = FlakyTestsSearchSort("pipelines_duration_lost")
FlakyTestsSearchSort.PIPELINES_DURATION_LOST_DESCENDING = FlakyTestsSearchSort("-pipelines_duration_lost")

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.update_flaky_tests_response_result import UpdateFlakyTestsResponseResult


class UpdateFlakyTestsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_flaky_tests_response_result import UpdateFlakyTestsResponseResult

        return {
            "has_errors": (bool,),
            "results": ([UpdateFlakyTestsResponseResult],),
        }

    attribute_map = {
        "has_errors": "has_errors",
        "results": "results",
    }

    def __init__(self_, has_errors: bool, results: List[UpdateFlakyTestsResponseResult], **kwargs):
        """
        Attributes for the update flaky test state response.

        :param has_errors: ``True`` if any errors occurred during the update operations. ``False`` if all tests succeeded to be updated.
        :type has_errors: bool

        :param results: Results of the update operation for each test.
        :type results: [UpdateFlakyTestsResponseResult]
        """
        super().__init__(kwargs)

        self_.has_errors = has_errors
        self_.results = results

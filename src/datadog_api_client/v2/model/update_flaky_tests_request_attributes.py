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
    from datadog_api_client.v2.model.update_flaky_tests_request_test import UpdateFlakyTestsRequestTest


class UpdateFlakyTestsRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_flaky_tests_request_test import UpdateFlakyTestsRequestTest

        return {
            "tests": ([UpdateFlakyTestsRequestTest],),
        }

    attribute_map = {
        "tests": "tests",
    }

    def __init__(self_, tests: List[UpdateFlakyTestsRequestTest], **kwargs):
        """
        Attributes for updating flaky test states.

        :param tests: List of flaky tests to update.
        :type tests: [UpdateFlakyTestsRequestTest]
        """
        super().__init__(kwargs)

        self_.tests = tests

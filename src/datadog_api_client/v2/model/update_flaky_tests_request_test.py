# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.update_flaky_tests_request_test_new_state import (
        UpdateFlakyTestsRequestTestNewState,
    )


class UpdateFlakyTestsRequestTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_flaky_tests_request_test_new_state import (
            UpdateFlakyTestsRequestTestNewState,
        )

        return {
            "id": (str,),
            "new_state": (UpdateFlakyTestsRequestTestNewState,),
        }

    attribute_map = {
        "id": "id",
        "new_state": "new_state",
    }

    def __init__(self_, id: str, new_state: UpdateFlakyTestsRequestTestNewState, **kwargs):
        """
        Details of what tests to update and their new attributes.

        :param id: The ID of the flaky test. This is the same ID returned by the Search flaky tests endpoint and corresponds to the test_fingerprint_fqn field in test run events.
        :type id: str

        :param new_state: The new state to set for the flaky test.
        :type new_state: UpdateFlakyTestsRequestTestNewState
        """
        super().__init__(kwargs)

        self_.id = id
        self_.new_state = new_state

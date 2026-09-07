# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DemBatchGetJourneysAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "test_suite_ids": ([str],),
        }

    attribute_map = {
        "test_suite_ids": "test_suite_ids",
    }

    def __init__(self_, test_suite_ids: List[str], **kwargs):
        """
        Attributes for a batch get journeys request.

        :param test_suite_ids: List of test suite IDs.
        :type test_suite_ids: [str]
        """
        super().__init__(kwargs)

        self_.test_suite_ids = test_suite_ids

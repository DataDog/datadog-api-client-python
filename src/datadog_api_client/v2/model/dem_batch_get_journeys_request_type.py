# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DemBatchGetJourneysRequestType(ModelSimple):
    """
    The resource type for a request to retrieve DEM journeys by test suite IDs.

    :param value: If omitted defaults to "batch_get_journeys_by_test_suite_ids_request". Must be one of ["batch_get_journeys_by_test_suite_ids_request"].
    :type value: str
    """

    allowed_values = {
        "batch_get_journeys_by_test_suite_ids_request",
    }
    BATCH_GET_JOURNEYS_BY_TEST_SUITE_IDS_REQUEST: ClassVar["DemBatchGetJourneysRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DemBatchGetJourneysRequestType.BATCH_GET_JOURNEYS_BY_TEST_SUITE_IDS_REQUEST = DemBatchGetJourneysRequestType(
    "batch_get_journeys_by_test_suite_ids_request"
)

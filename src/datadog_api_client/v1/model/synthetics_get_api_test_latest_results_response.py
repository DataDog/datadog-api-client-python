# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsGetAPITestLatestResultsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_api_test_result_short import SyntheticsAPITestResultShort

        return {
            "last_timestamp_fetched": (int,),
            "results": ([SyntheticsAPITestResultShort],),
        }

    attribute_map = {
        "last_timestamp_fetched": "last_timestamp_fetched",
        "results": "results",
    }

    def __init__(self, *args, **kwargs):
        """
        Object with the latest Synthetic API test run.

        :param last_timestamp_fetched: Timestamp of the latest API test run.
        :type last_timestamp_fetched: int, optional

        :param results: Result of the latest API test run.
        :type results: [SyntheticsAPITestResultShort], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsGetAPITestLatestResultsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

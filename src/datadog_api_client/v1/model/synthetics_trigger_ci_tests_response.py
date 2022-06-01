# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SyntheticsTriggerCITestsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_trigger_ci_test_location import SyntheticsTriggerCITestLocation
        from datadog_api_client.v1.model.synthetics_trigger_ci_test_run_result import SyntheticsTriggerCITestRunResult

        return {
            "batch_id": (str, none_type),
            "locations": ([SyntheticsTriggerCITestLocation],),
            "results": ([SyntheticsTriggerCITestRunResult],),
            "triggered_check_ids": ([str],),
        }

    attribute_map = {
        "batch_id": "batch_id",
        "locations": "locations",
        "results": "results",
        "triggered_check_ids": "triggered_check_ids",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing information about the tests triggered.

        :param batch_id: The public ID of the batch triggered.
        :type batch_id: str, none_type, optional

        :param locations: List of Synthetics locations.
        :type locations: [SyntheticsTriggerCITestLocation], optional

        :param results: Information about the tests runs.
        :type results: [SyntheticsTriggerCITestRunResult], optional

        :param triggered_check_ids: The public IDs of the Synthetics test triggered.
        :type triggered_check_ids: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerCITestsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

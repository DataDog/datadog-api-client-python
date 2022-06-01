# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsAPITestResultShortResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_timing import SyntheticsTiming

        return {
            "passed": (bool,),
            "timings": (SyntheticsTiming,),
        }

    attribute_map = {
        "passed": "passed",
        "timings": "timings",
    }

    def __init__(self, *args, **kwargs):
        """
        Result of the last API test run.

        :param passed: Describes if the test run has passed or failed.
        :type passed: bool, optional

        :param timings: Object containing all metrics and their values collected for a Synthetic API test.
            Learn more about those metrics in `Synthetics documentation <https://docs.datadoghq.com/synthetics/#metrics>`_.
        :type timings: SyntheticsTiming, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITestResultShortResult, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

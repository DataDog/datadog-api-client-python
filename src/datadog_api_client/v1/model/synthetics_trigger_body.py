# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTriggerBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_trigger_test import SyntheticsTriggerTest

        return {
            "tests": ([SyntheticsTriggerTest],),
        }

    attribute_map = {
        "tests": "tests",
    }

    def __init__(self, tests, *args, **kwargs):
        """
        Object describing the synthetics tests to trigger.

        :param tests: Individual synthetics test.
        :type tests: [SyntheticsTriggerTest]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.tests = tests

    @classmethod
    def _from_openapi_data(cls, tests, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerBody, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.tests = tests
        return self

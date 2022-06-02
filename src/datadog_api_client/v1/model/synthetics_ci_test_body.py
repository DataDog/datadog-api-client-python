# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsCITestBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ci_test import SyntheticsCITest

        return {
            "tests": ([SyntheticsCITest],),
        }

    attribute_map = {
        "tests": "tests",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the synthetics tests to trigger.

        :param tests: Individual synthetics test.
        :type tests: [SyntheticsCITest], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsCITestBody, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

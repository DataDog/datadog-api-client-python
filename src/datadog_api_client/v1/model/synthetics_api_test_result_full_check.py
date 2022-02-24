# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_test_config import SyntheticsTestConfig

    globals()["SyntheticsTestConfig"] = SyntheticsTestConfig


class SyntheticsAPITestResultFullCheck(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "config": (SyntheticsTestConfig,),
        }

    attribute_map = {
        "config": "config",
    }

    read_only_vars = {}

    def __init__(self, config, *args, **kwargs):
        """
        Object describing the API test configuration.

        :param config: Configuration object for a Synthetic test.
        :type config: SyntheticsTestConfig
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.config = config

    @classmethod
    def _from_openapi_data(cls, config, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITestResultFullCheck, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.config = config
        return self

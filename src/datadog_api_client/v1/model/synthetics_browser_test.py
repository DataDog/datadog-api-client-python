# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_browser_test_config import SyntheticsBrowserTestConfig
    from datadog_api_client.v1.model.synthetics_browser_test_type import SyntheticsBrowserTestType
    from datadog_api_client.v1.model.synthetics_step import SyntheticsStep
    from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
    from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

    globals()["SyntheticsBrowserTestConfig"] = SyntheticsBrowserTestConfig
    globals()["SyntheticsBrowserTestType"] = SyntheticsBrowserTestType
    globals()["SyntheticsStep"] = SyntheticsStep
    globals()["SyntheticsTestOptions"] = SyntheticsTestOptions
    globals()["SyntheticsTestPauseStatus"] = SyntheticsTestPauseStatus


class SyntheticsBrowserTest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "config": (SyntheticsBrowserTestConfig,),
            "locations": ([str],),
            "message": (str,),
            "monitor_id": (int,),
            "name": (str,),
            "options": (SyntheticsTestOptions,),
            "public_id": (str,),
            "status": (SyntheticsTestPauseStatus,),
            "steps": ([SyntheticsStep],),
            "tags": ([str],),
            "type": (SyntheticsBrowserTestType,),
        }

    attribute_map = {
        "message": "message",
        "config": "config",
        "locations": "locations",
        "monitor_id": "monitor_id",
        "name": "name",
        "options": "options",
        "public_id": "public_id",
        "status": "status",
        "steps": "steps",
        "tags": "tags",
        "type": "type",
    }

    read_only_vars = {
        "monitor_id",
        "public_id",
    }

    def __init__(self, message, *args, **kwargs):
        """SyntheticsBrowserTest - a model defined in OpenAPI

        Args:
            message (str): Notification message associated with the test. Message can either be text or an empty string.

        Keyword Args:
            config (SyntheticsBrowserTestConfig): [optional]
            locations ([str]): [optional] Array of locations used to run the test.
            monitor_id (int): [optional] The associated monitor ID.
            name (str): [optional] Name of the test.
            options (SyntheticsTestOptions): [optional]
            public_id (str): [optional] The public ID of the test.
            status (SyntheticsTestPauseStatus): [optional]
            steps ([SyntheticsStep]): [optional] The steps of the test.
            tags ([str]): [optional] Array of tags attached to the test.
            type (SyntheticsBrowserTestType): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.message = message

    @classmethod
    def _from_openapi_data(cls, message, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.message = message
        return self

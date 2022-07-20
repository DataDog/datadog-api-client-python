# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBrowserTestResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_device import SyntheticsDevice
        from datadog_api_client.v1.model.synthetics_browser_test_result_failure import (
            SyntheticsBrowserTestResultFailure,
        )
        from datadog_api_client.v1.model.synthetics_step_detail import SyntheticsStepDetail

        return {
            "browser_type": (str,),
            "browser_version": (str,),
            "device": (SyntheticsDevice,),
            "duration": (float,),
            "error": (str,),
            "failure": (SyntheticsBrowserTestResultFailure,),
            "passed": (bool,),
            "received_email_count": (int,),
            "start_url": (str,),
            "step_details": ([SyntheticsStepDetail],),
            "thumbnails_bucket_key": (bool,),
            "time_to_interactive": (float,),
        }

    attribute_map = {
        "browser_type": "browserType",
        "browser_version": "browserVersion",
        "device": "device",
        "duration": "duration",
        "error": "error",
        "failure": "failure",
        "passed": "passed",
        "received_email_count": "receivedEmailCount",
        "start_url": "startUrl",
        "step_details": "stepDetails",
        "thumbnails_bucket_key": "thumbnailsBucketKey",
        "time_to_interactive": "timeToInteractive",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing results for your Synthetic browser test.

        :param browser_type: Type of browser device used for the browser test.
        :type browser_type: str, optional

        :param browser_version: Browser version used for the browser test.
        :type browser_version: str, optional

        :param device: Object describing the device used to perform the Synthetic test.
        :type device: SyntheticsDevice, optional

        :param duration: Global duration in second of the browser test.
        :type duration: float, optional

        :param error: Error returned for the browser test.
        :type error: str, optional

        :param failure: The browser test failure details.
        :type failure: SyntheticsBrowserTestResultFailure, optional

        :param passed: Whether or not the browser test was conducted.
        :type passed: bool, optional

        :param received_email_count: The amount of email received during the browser test.
        :type received_email_count: int, optional

        :param start_url: Starting URL for the browser test.
        :type start_url: str, optional

        :param step_details: Array containing the different browser test steps.
        :type step_details: [SyntheticsStepDetail], optional

        :param thumbnails_bucket_key: Whether or not a thumbnail is associated with the browser test.
        :type thumbnails_bucket_key: bool, optional

        :param time_to_interactive: Time in second to wait before the browser test starts after
            reaching the start URL.
        :type time_to_interactive: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTestResultData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
)


class SyntheticsStepDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_browser_error import SyntheticsBrowserError
        from datadog_api_client.v1.model.synthetics_check_type import SyntheticsCheckType
        from datadog_api_client.v1.model.synthetics_playing_tab import SyntheticsPlayingTab
        from datadog_api_client.v1.model.synthetics_step_detail import SyntheticsStepDetail
        from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType
        from datadog_api_client.v1.model.synthetics_core_web_vitals import SyntheticsCoreWebVitals
        from datadog_api_client.v1.model.synthetics_step_detail_warning import SyntheticsStepDetailWarning

        return {
            "browser_errors": ([SyntheticsBrowserError],),
            "check_type": (SyntheticsCheckType,),
            "description": (str,),
            "duration": (float,),
            "error": (str,),
            "playing_tab": (SyntheticsPlayingTab,),
            "screenshot_bucket_key": (bool,),
            "skipped": (bool,),
            "snapshot_bucket_key": (bool,),
            "step_id": (int,),
            "sub_test_step_details": ([SyntheticsStepDetail],),
            "time_to_interactive": (float,),
            "type": (SyntheticsStepType,),
            "url": (str,),
            "value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
            "vitals_metrics": ([SyntheticsCoreWebVitals],),
            "warnings": ([SyntheticsStepDetailWarning],),
        }

    attribute_map = {
        "browser_errors": "browserErrors",
        "check_type": "checkType",
        "description": "description",
        "duration": "duration",
        "error": "error",
        "playing_tab": "playingTab",
        "screenshot_bucket_key": "screenshotBucketKey",
        "skipped": "skipped",
        "snapshot_bucket_key": "snapshotBucketKey",
        "step_id": "stepId",
        "sub_test_step_details": "subTestStepDetails",
        "time_to_interactive": "timeToInteractive",
        "type": "type",
        "url": "url",
        "value": "value",
        "vitals_metrics": "vitalsMetrics",
        "warnings": "warnings",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing a step for a Synthetic test.

        :param browser_errors: Array of errors collected for a browser test.
        :type browser_errors: [SyntheticsBrowserError], optional

        :param check_type: Type of assertion to apply in an API test.
        :type check_type: SyntheticsCheckType, optional

        :param description: Description of the test.
        :type description: str, optional

        :param duration: Total duration in millisecond of the test.
        :type duration: float, optional

        :param error: Error returned by the test.
        :type error: str, optional

        :param playing_tab: Navigate between different tabs for your browser test.
        :type playing_tab: SyntheticsPlayingTab, optional

        :param screenshot_bucket_key: Whether or not screenshots where collected by the test.
        :type screenshot_bucket_key: bool, optional

        :param skipped: Whether or not to skip this step.
        :type skipped: bool, optional

        :param snapshot_bucket_key: Whether or not snapshots where collected by the test.
        :type snapshot_bucket_key: bool, optional

        :param step_id: The step ID.
        :type step_id: int, optional

        :param sub_test_step_details: If this steps include a sub-test.
            `Subtests documentation <https://docs.datadoghq.com/synthetics/browser_tests/advanced_options/#subtests>`_.
        :type sub_test_step_details: [SyntheticsStepDetail], optional

        :param time_to_interactive: Time before starting the step.
        :type time_to_interactive: float, optional

        :param type: Step type used in your Synthetic test.
        :type type: SyntheticsStepType, optional

        :param url: URL to perform the step against.
        :type url: str, optional

        :param value: Value for the step.
        :type value: bool, date, datetime, dict, float, int, list, str, none_type, optional

        :param vitals_metrics: Array of Core Web Vitals metrics for the step.
        :type vitals_metrics: [SyntheticsCoreWebVitals], optional

        :param warnings: Warning collected that didn't failed the step.
        :type warnings: [SyntheticsStepDetailWarning], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsStepDetail, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultBucketKeys(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "after_step_screenshot": (str,),
            "after_turn_screenshot": (str,),
            "artifacts": (str,),
            "before_step_screenshot": (str,),
            "before_turn_screenshot": (str,),
            "crash_report": (str,),
            "device_logs": (str,),
            "email_messages": ([str],),
            "screenshot": (str,),
            "snapshot": (str,),
            "source": (str,),
        }

    attribute_map = {
        "after_step_screenshot": "after_step_screenshot",
        "after_turn_screenshot": "after_turn_screenshot",
        "artifacts": "artifacts",
        "before_step_screenshot": "before_step_screenshot",
        "before_turn_screenshot": "before_turn_screenshot",
        "crash_report": "crash_report",
        "device_logs": "device_logs",
        "email_messages": "email_messages",
        "screenshot": "screenshot",
        "snapshot": "snapshot",
        "source": "source",
    }

    def __init__(
        self_,
        after_step_screenshot: Union[str, UnsetType] = unset,
        after_turn_screenshot: Union[str, UnsetType] = unset,
        artifacts: Union[str, UnsetType] = unset,
        before_step_screenshot: Union[str, UnsetType] = unset,
        before_turn_screenshot: Union[str, UnsetType] = unset,
        crash_report: Union[str, UnsetType] = unset,
        device_logs: Union[str, UnsetType] = unset,
        email_messages: Union[List[str], UnsetType] = unset,
        screenshot: Union[str, UnsetType] = unset,
        snapshot: Union[str, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Storage bucket keys for artifacts produced during a step or test.

        :param after_step_screenshot: Key for the screenshot captured after the step (goal-based tests).
        :type after_step_screenshot: str, optional

        :param after_turn_screenshot: Key for the screenshot captured after the turn (goal-based tests).
        :type after_turn_screenshot: str, optional

        :param artifacts: Key for miscellaneous artifacts.
        :type artifacts: str, optional

        :param before_step_screenshot: Key for the screenshot captured before the step (goal-based tests).
        :type before_step_screenshot: str, optional

        :param before_turn_screenshot: Key for the screenshot captured before the turn (goal-based tests).
        :type before_turn_screenshot: str, optional

        :param crash_report: Key for a captured crash report.
        :type crash_report: str, optional

        :param device_logs: Key for captured device logs.
        :type device_logs: str, optional

        :param email_messages: Keys for email message payloads captured by the step.
        :type email_messages: [str], optional

        :param screenshot: Key for the captured screenshot.
        :type screenshot: str, optional

        :param snapshot: Key for the captured DOM snapshot.
        :type snapshot: str, optional

        :param source: Key for the page source or element source.
        :type source: str, optional
        """
        if after_step_screenshot is not unset:
            kwargs["after_step_screenshot"] = after_step_screenshot
        if after_turn_screenshot is not unset:
            kwargs["after_turn_screenshot"] = after_turn_screenshot
        if artifacts is not unset:
            kwargs["artifacts"] = artifacts
        if before_step_screenshot is not unset:
            kwargs["before_step_screenshot"] = before_step_screenshot
        if before_turn_screenshot is not unset:
            kwargs["before_turn_screenshot"] = before_turn_screenshot
        if crash_report is not unset:
            kwargs["crash_report"] = crash_report
        if device_logs is not unset:
            kwargs["device_logs"] = device_logs
        if email_messages is not unset:
            kwargs["email_messages"] = email_messages
        if screenshot is not unset:
            kwargs["screenshot"] = screenshot
        if snapshot is not unset:
            kwargs["snapshot"] = snapshot
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)

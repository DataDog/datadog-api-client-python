# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class FlakyTestRunMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "duration_ms": (int, none_type),
            "error_message": (str, none_type),
            "error_stack": (str, none_type),
            "source_end": (int, none_type),
            "source_file": (str, none_type),
            "source_start": (int, none_type),
        }

    attribute_map = {
        "duration_ms": "duration_ms",
        "error_message": "error_message",
        "error_stack": "error_stack",
        "source_end": "source_end",
        "source_file": "source_file",
        "source_start": "source_start",
    }

    def __init__(
        self_,
        duration_ms: Union[int, none_type, UnsetType] = unset,
        error_message: Union[str, none_type, UnsetType] = unset,
        error_stack: Union[str, none_type, UnsetType] = unset,
        source_end: Union[int, none_type, UnsetType] = unset,
        source_file: Union[str, none_type, UnsetType] = unset,
        source_start: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the latest failed test run of the flaky test.

        :param duration_ms: The duration of the test run in milliseconds.
        :type duration_ms: int, none_type, optional

        :param error_message: The error message from the test failure.
        :type error_message: str, none_type, optional

        :param error_stack: The stack trace from the test failure.
        :type error_stack: str, none_type, optional

        :param source_end: The line number where the test ends in the source file.
        :type source_end: int, none_type, optional

        :param source_file: The source file where the test is defined.
        :type source_file: str, none_type, optional

        :param source_start: The line number where the test starts in the source file.
        :type source_start: int, none_type, optional
        """
        if duration_ms is not unset:
            kwargs["duration_ms"] = duration_ms
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if error_stack is not unset:
            kwargs["error_stack"] = error_stack
        if source_end is not unset:
            kwargs["source_end"] = source_end
        if source_file is not unset:
            kwargs["source_file"] = source_file
        if source_start is not unset:
            kwargs["source_start"] = source_start
        super().__init__(kwargs)

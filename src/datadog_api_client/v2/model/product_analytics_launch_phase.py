# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsLaunchPhase(ModelSimple):
    """
    Lifecycle phase of a launch. A new launch starts in `plan` or `setup`, and defaults to `plan`.
        Allowed changes: `plan` to `setup`, `setup` to `ready`, `ready` to `setup` or `launched`, and `launched` to
        `ready`.

    :param value: Must be one of ["plan", "setup", "ready", "launched"].
    :type value: str
    """

    allowed_values = {
        "plan",
        "setup",
        "ready",
        "launched",
    }
    PLAN: ClassVar["ProductAnalyticsLaunchPhase"]
    SETUP: ClassVar["ProductAnalyticsLaunchPhase"]
    READY: ClassVar["ProductAnalyticsLaunchPhase"]
    LAUNCHED: ClassVar["ProductAnalyticsLaunchPhase"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsLaunchPhase.PLAN = ProductAnalyticsLaunchPhase("plan")
ProductAnalyticsLaunchPhase.SETUP = ProductAnalyticsLaunchPhase("setup")
ProductAnalyticsLaunchPhase.READY = ProductAnalyticsLaunchPhase("ready")
ProductAnalyticsLaunchPhase.LAUNCHED = ProductAnalyticsLaunchPhase("launched")

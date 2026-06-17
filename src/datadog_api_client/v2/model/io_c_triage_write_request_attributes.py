# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.io_c_triage_state import IoCTriageState


class IoCTriageWriteRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_triage_state import IoCTriageState

        return {
            "indicator": (str,),
            "triage_state": (IoCTriageState,),
        }

    attribute_map = {
        "indicator": "indicator",
        "triage_state": "triage_state",
    }

    def __init__(self_, indicator: str, triage_state: IoCTriageState, **kwargs):
        """
        Attributes for setting an indicator's triage state.

        :param indicator: The indicator value to triage (for example, an IP address or domain).
        :type indicator: str

        :param triage_state: Current triage state of the indicator.
        :type triage_state: IoCTriageState
        """
        super().__init__(kwargs)

        self_.indicator = indicator
        self_.triage_state = triage_state

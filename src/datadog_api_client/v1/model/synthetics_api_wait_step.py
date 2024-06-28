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
    from datadog_api_client.v1.model.synthetics_api_wait_step_subtype import SyntheticsAPIWaitStepSubtype


class SyntheticsAPIWaitStep(ModelNormal):
    validations = {
        "value": {
            "inclusive_maximum": 180,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_api_wait_step_subtype import SyntheticsAPIWaitStepSubtype

        return {
            "name": (str,),
            "subtype": (SyntheticsAPIWaitStepSubtype,),
            "value": (int,),
        }

    attribute_map = {
        "name": "name",
        "subtype": "subtype",
        "value": "value",
    }

    def __init__(self_, name: str, subtype: SyntheticsAPIWaitStepSubtype, value: int, **kwargs):
        """
        The Wait step used in a Synthetic multi-step API test.

        :param name: The name of the step.
        :type name: str

        :param subtype: The subtype of the Synthetic multi-step API wait step.
        :type subtype: SyntheticsAPIWaitStepSubtype

        :param value: The time to wait in seconds. Minimum value: 0. Maximum value: 180.
        :type value: int
        """
        super().__init__(kwargs)

        self_.name = name
        self_.subtype = subtype
        self_.value = value

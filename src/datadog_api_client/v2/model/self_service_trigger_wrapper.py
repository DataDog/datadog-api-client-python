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


class SelfServiceTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "self_service_trigger": (dict,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "self_service_trigger": "selfServiceTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(self_, self_service_trigger: dict, start_step_names: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Schema for a Self Service-based trigger.

        :param self_service_trigger: Trigger a workflow from Self Service.
        :type self_service_trigger: dict

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.self_service_trigger = self_service_trigger

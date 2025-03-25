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


class DatabaseMonitoringTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "database_monitoring_trigger": (dict,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "database_monitoring_trigger": "databaseMonitoringTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(
        self_, database_monitoring_trigger: dict, start_step_names: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Schema for a Database Monitoring-based trigger.

        :param database_monitoring_trigger: Trigger a workflow from Database Monitoring.
        :type database_monitoring_trigger: dict

        :param start_step_names: A list of steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.database_monitoring_trigger = database_monitoring_trigger

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageFargateHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "apm_fargate_count": (int,),
            "avg_profiled_fargate_tasks": (int,),
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
            "tasks_count": (int,),
        }

    attribute_map = {
        "apm_fargate_count": "apm_fargate_count",
        "avg_profiled_fargate_tasks": "avg_profiled_fargate_tasks",
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
        "tasks_count": "tasks_count",
    }

    def __init__(self_, *args, **kwargs):
        """
        Number of Fargate tasks run and hourly usage.

        :param apm_fargate_count: The high-water mark of APM ECS Fargate tasks during the given hour.
        :type apm_fargate_count: int, optional

        :param avg_profiled_fargate_tasks: The average profiled task count for Fargate Profiling.
        :type avg_profiled_fargate_tasks: int, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param tasks_count: The number of Fargate tasks run.
        :type tasks_count: int, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

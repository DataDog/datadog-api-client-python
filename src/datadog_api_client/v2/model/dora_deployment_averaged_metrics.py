# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DORADeploymentAveragedMetrics(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "change_lead_time": (int,),
            "merge_time": (int,),
            "review_time": (int,),
            "time_to_deploy": (int,),
            "time_to_pr_ready": (int,),
        }

    attribute_map = {
        "change_lead_time": "change_lead_time",
        "merge_time": "merge_time",
        "review_time": "review_time",
        "time_to_deploy": "time_to_deploy",
        "time_to_pr_ready": "time_to_pr_ready",
    }

    def __init__(
        self_,
        change_lead_time: Union[int, UnsetType] = unset,
        merge_time: Union[int, UnsetType] = unset,
        review_time: Union[int, UnsetType] = unset,
        time_to_deploy: Union[int, UnsetType] = unset,
        time_to_pr_ready: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Averaged DORA and delivery metrics computed across the commits and pull requests included in the deployment.

        :param change_lead_time: The averaged change lead time, in seconds.
        :type change_lead_time: int, optional

        :param merge_time: The averaged merge time, in seconds.
        :type merge_time: int, optional

        :param review_time: The averaged review time, in seconds.
        :type review_time: int, optional

        :param time_to_deploy: The averaged time to deploy, in seconds.
        :type time_to_deploy: int, optional

        :param time_to_pr_ready: The averaged time until the pull request was ready for review, in seconds.
        :type time_to_pr_ready: int, optional
        """
        if change_lead_time is not unset:
            kwargs["change_lead_time"] = change_lead_time
        if merge_time is not unset:
            kwargs["merge_time"] = merge_time
        if review_time is not unset:
            kwargs["review_time"] = review_time
        if time_to_deploy is not unset:
            kwargs["time_to_deploy"] = time_to_deploy
        if time_to_pr_ready is not unset:
            kwargs["time_to_pr_ready"] = time_to_pr_ready
        super().__init__(kwargs)

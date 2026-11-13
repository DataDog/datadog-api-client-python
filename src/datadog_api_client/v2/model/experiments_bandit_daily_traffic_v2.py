# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


class ExperimentsBanditDailyTrafficV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cumulative_new_subjects": (int,),
            "cumulative_observations": (int,),
            "date": (datetime,),
            "feature_flag_variant_id": (UUID,),
            "new_subjects": (int,),
            "observations": (int,),
            "variant_key": (str, none_type),
        }

    attribute_map = {
        "cumulative_new_subjects": "cumulative_new_subjects",
        "cumulative_observations": "cumulative_observations",
        "date": "date",
        "feature_flag_variant_id": "feature_flag_variant_id",
        "new_subjects": "new_subjects",
        "observations": "observations",
        "variant_key": "variant_key",
    }

    def __init__(
        self_,
        cumulative_new_subjects: int,
        cumulative_observations: int,
        date: datetime,
        feature_flag_variant_id: UUID,
        new_subjects: int,
        observations: int,
        variant_key: Union[str, none_type],
        **kwargs,
    ):
        """
        An arm's observations and new subjects on one UTC day.

        :param cumulative_new_subjects: The arm's new subjects from the bandit's start through this day, including days before the requested range.
        :type cumulative_new_subjects: int

        :param cumulative_observations: The arm's observations from the bandit's start through this day, including days before the requested range.
        :type cumulative_observations: int

        :param date: A UTC date as YYYY-MM-DD.
        :type date: datetime

        :param feature_flag_variant_id: The arm's variant ID on the flag.
        :type feature_flag_variant_id: UUID

        :param new_subjects: Subjects whose first valid observation is on this day and arm.
        :type new_subjects: int

        :param observations: The arm's valid observations on this day.
        :type observations: int

        :param variant_key: The arm's variant key.
        :type variant_key: str, none_type
        """
        super().__init__(kwargs)

        self_.cumulative_new_subjects = cumulative_new_subjects
        self_.cumulative_observations = cumulative_observations
        self_.date = date
        self_.feature_flag_variant_id = feature_flag_variant_id
        self_.new_subjects = new_subjects
        self_.observations = observations
        self_.variant_key = variant_key

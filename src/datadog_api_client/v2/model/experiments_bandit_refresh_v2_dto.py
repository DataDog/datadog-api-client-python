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
    from datadog_api_client.v2.model.experiments_bandit_refresh_v2_dto_data import ExperimentsBanditRefreshV2DTOData


class ExperimentsBanditRefreshV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_refresh_v2_dto_data import ExperimentsBanditRefreshV2DTOData

        return {
            "data": (ExperimentsBanditRefreshV2DTOData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsBanditRefreshV2DTOData, **kwargs):
        """
        Response acknowledging a refresh that has started.

        :param data: The refresh that started.
        :type data: ExperimentsBanditRefreshV2DTOData
        """
        super().__init__(kwargs)

        self_.data = data

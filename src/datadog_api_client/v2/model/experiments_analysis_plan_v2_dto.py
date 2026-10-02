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
    from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto_data import ExperimentsAnalysisPlanV2DTOData


class ExperimentsAnalysisPlanV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto_data import ExperimentsAnalysisPlanV2DTOData

        return {
            "data": (ExperimentsAnalysisPlanV2DTOData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsAnalysisPlanV2DTOData, **kwargs):
        """
        Response containing the analysis settings for an experiment.

        :param data: Analysis plan resource with its identifier and settings.
        :type data: ExperimentsAnalysisPlanV2DTOData
        """
        super().__init__(kwargs)

        self_.data = data

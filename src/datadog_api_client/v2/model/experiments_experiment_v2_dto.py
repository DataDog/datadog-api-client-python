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
    from datadog_api_client.v2.model.experiments_experiment_v2_dto_data import ExperimentsExperimentV2DTOData


class ExperimentsExperimentV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_v2_dto_data import ExperimentsExperimentV2DTOData

        return {
            "data": (ExperimentsExperimentV2DTOData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsExperimentV2DTOData, **kwargs):
        """
        Response containing an experiment and its configuration.

        :param data: Experiment resource with its identifier and configuration.
        :type data: ExperimentsExperimentV2DTOData
        """
        super().__init__(kwargs)

        self_.data = data

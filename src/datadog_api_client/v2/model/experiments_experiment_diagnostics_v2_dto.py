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
    from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data import (
        ExperimentsExperimentDiagnosticsV2DTOData,
    )


class ExperimentsExperimentDiagnosticsV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto_data import (
            ExperimentsExperimentDiagnosticsV2DTOData,
        )

        return {
            "data": (ExperimentsExperimentDiagnosticsV2DTOData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsExperimentDiagnosticsV2DTOData, **kwargs):
        """
        Response containing the diagnostic checks for an experiment.

        :param data: Experiment diagnostics resource with its identifier and check results.
        :type data: ExperimentsExperimentDiagnosticsV2DTOData
        """
        super().__init__(kwargs)

        self_.data = data

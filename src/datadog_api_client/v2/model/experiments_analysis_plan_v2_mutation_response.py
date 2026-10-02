# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto_data import ExperimentsAnalysisPlanV2DTOData
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_meta_dto import ExperimentsPatchExperimentV2MetaDTO


class ExperimentsAnalysisPlanV2MutationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto_data import ExperimentsAnalysisPlanV2DTOData
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_meta_dto import (
            ExperimentsPatchExperimentV2MetaDTO,
        )

        return {
            "data": (ExperimentsAnalysisPlanV2DTOData,),
            "meta": (ExperimentsPatchExperimentV2MetaDTO,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: ExperimentsAnalysisPlanV2DTOData,
        meta: Union[ExperimentsPatchExperimentV2MetaDTO, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing the saved analysis plan and result refresh information.

        :param data: Analysis plan resource with its identifier and settings.
        :type data: ExperimentsAnalysisPlanV2DTOData

        :param meta: Refresh requirements and warnings returned by an experiment update.
        :type meta: ExperimentsPatchExperimentV2MetaDTO, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_data import (
        ExperimentsRefreshExperimentResultsV2DTOData,
    )
    from datadog_api_client.v2.model.experiments_refresh_experiment_results_batch_meta_v2_dto import (
        ExperimentsRefreshExperimentResultsBatchMetaV2DTO,
    )


class ExperimentsRefreshExperimentResultsV2DTOArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_data import (
            ExperimentsRefreshExperimentResultsV2DTOData,
        )
        from datadog_api_client.v2.model.experiments_refresh_experiment_results_batch_meta_v2_dto import (
            ExperimentsRefreshExperimentResultsBatchMetaV2DTO,
        )

        return {
            "data": ([ExperimentsRefreshExperimentResultsV2DTOData],),
            "meta": (ExperimentsRefreshExperimentResultsBatchMetaV2DTO,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ExperimentsRefreshExperimentResultsV2DTOData],
        meta: Union[ExperimentsRefreshExperimentResultsBatchMetaV2DTO, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of experiment refresh result resources.

        :param data: Resources returned in this response.
        :type data: [ExperimentsRefreshExperimentResultsV2DTOData]

        :param meta: Summary of refresh outcomes across the organization's experiments.
        :type meta: ExperimentsRefreshExperimentResultsBatchMetaV2DTO, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

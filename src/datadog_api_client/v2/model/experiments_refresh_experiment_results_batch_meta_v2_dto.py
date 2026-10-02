# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_refresh_experiment_results_batch_meta_v2_dto_results_items import (
        ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItems,
    )


class ExperimentsRefreshExperimentResultsBatchMetaV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_refresh_experiment_results_batch_meta_v2_dto_results_items import (
            ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItems,
        )

        return {
            "experiments_updated": (int,),
            "results": ([ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItems, none_type],),
        }

    attribute_map = {
        "experiments_updated": "experiments_updated",
        "results": "results",
    }

    def __init__(
        self_,
        experiments_updated: Union[int, UnsetType] = unset,
        results: Union[List[ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of refresh outcomes across the organization's experiments.

        :param experiments_updated: Number of experiments updated by the refresh request.
        :type experiments_updated: int, optional

        :param results: Refresh outcome reported for each experiment.
        :type results: [ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItems, none_type], optional
        """
        if experiments_updated is not unset:
            kwargs["experiments_updated"] = experiments_updated
        if results is not unset:
            kwargs["results"] = results
        super().__init__(kwargs)

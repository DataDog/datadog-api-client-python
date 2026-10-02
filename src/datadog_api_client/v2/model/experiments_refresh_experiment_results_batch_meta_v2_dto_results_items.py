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
    from datadog_api_client.v2.model.experiments_refresh_experiment_results_batch_meta_v2_dto_results_items_outcome import (
        ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome,
    )


class ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItems(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_refresh_experiment_results_batch_meta_v2_dto_results_items_outcome import (
            ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome,
        )

        return {
            "experiment_id": (str,),
            "outcome": (ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome,),
        }

    attribute_map = {
        "experiment_id": "experiment_id",
        "outcome": "outcome",
    }

    def __init__(
        self_,
        experiment_id: Union[str, UnsetType] = unset,
        outcome: Union[ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome, UnsetType] = unset,
        **kwargs,
    ):
        """
        Refresh outcome for one experiment.

        :param experiment_id: ID of the experiment associated with this result.
        :type experiment_id: str, optional

        :param outcome: Outcome of attempting to refresh one experiment.
        :type outcome: ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome, optional
        """
        if experiment_id is not unset:
            kwargs["experiment_id"] = experiment_id
        if outcome is not unset:
            kwargs["outcome"] = outcome
        super().__init__(kwargs)

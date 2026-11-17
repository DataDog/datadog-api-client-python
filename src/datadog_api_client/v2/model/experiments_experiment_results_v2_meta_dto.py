# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_evsi_context import ExperimentsEVSIContext


class ExperimentsExperimentResultsV2MetaDTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_evsi_context import ExperimentsEVSIContext

        return {
            "evsi_context": (ExperimentsEVSIContext,),
            "is_stale": (bool,),
            "result_run_id": (UUID,),
            "results_last_updated": (datetime, none_type),
            "stale_reasons": ([str],),
        }

    attribute_map = {
        "evsi_context": "evsi_context",
        "is_stale": "is_stale",
        "result_run_id": "result_run_id",
        "results_last_updated": "results_last_updated",
        "stale_reasons": "stale_reasons",
    }

    def __init__(
        self_,
        result_run_id: UUID,
        evsi_context: Union[ExperimentsEVSIContext, UnsetType] = unset,
        is_stale: Union[bool, UnsetType] = unset,
        results_last_updated: Union[datetime, none_type, UnsetType] = unset,
        stale_reasons: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Selected experiment result run, its recorded EVSI forecast, and results freshness.

        :param evsi_context: Forecast horizon and traffic counts used to calculate expected value of sample information (EVSI) for result_run_id. Assumes traffic continues at the rate observed during the lookback window. Omitted if the forecast was not recorded or could not be loaded.
        :type evsi_context: ExperimentsEVSIContext, optional

        :param is_stale: Whether the saved results require a refresh or their freshness cannot be confirmed. See stale_reasons for
            details.
        :type is_stale: bool, optional

        :param result_run_id: ID of the successful experiment run that produced these results.
        :type result_run_id: UUID

        :param results_last_updated: Time when the experiment results were last updated.
        :type results_last_updated: datetime, none_type, optional

        :param stale_reasons: Reasons the saved experiment results are stale.
        :type stale_reasons: [str], optional
        """
        if evsi_context is not unset:
            kwargs["evsi_context"] = evsi_context
        if is_stale is not unset:
            kwargs["is_stale"] = is_stale
        if results_last_updated is not unset:
            kwargs["results_last_updated"] = results_last_updated
        if stale_reasons is not unset:
            kwargs["stale_reasons"] = stale_reasons
        super().__init__(kwargs)

        self_.result_run_id = result_run_id

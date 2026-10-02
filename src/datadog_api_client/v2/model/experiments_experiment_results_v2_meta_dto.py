# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class ExperimentsExperimentResultsV2MetaDTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_stale": (bool,),
            "results_last_updated": (datetime, none_type),
            "stale_reasons": ([str],),
        }

    attribute_map = {
        "is_stale": "is_stale",
        "results_last_updated": "results_last_updated",
        "stale_reasons": "stale_reasons",
    }

    def __init__(
        self_,
        is_stale: Union[bool, UnsetType] = unset,
        results_last_updated: Union[datetime, none_type, UnsetType] = unset,
        stale_reasons: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about when experiment results were updated and whether they are stale.

        :param is_stale: Whether the saved results require a refresh or their freshness cannot be confirmed. See stale_reasons for
            details.
        :type is_stale: bool, optional

        :param results_last_updated: Time when the experiment results were last updated.
        :type results_last_updated: datetime, none_type, optional

        :param stale_reasons: Reasons the saved experiment results are stale.
        :type stale_reasons: [str], optional
        """
        if is_stale is not unset:
            kwargs["is_stale"] = is_stale
        if results_last_updated is not unset:
            kwargs["results_last_updated"] = results_last_updated
        if stale_reasons is not unset:
            kwargs["stale_reasons"] = stale_reasons
        super().__init__(kwargs)

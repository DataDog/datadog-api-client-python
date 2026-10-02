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
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data import ExperimentsVariantResultsV2DTOData
    from datadog_api_client.v2.model.experiments_experiment_results_v2_meta_dto import (
        ExperimentsExperimentResultsV2MetaDTO,
    )


class ExperimentsVariantResultsV2DTOArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data import (
            ExperimentsVariantResultsV2DTOData,
        )
        from datadog_api_client.v2.model.experiments_experiment_results_v2_meta_dto import (
            ExperimentsExperimentResultsV2MetaDTO,
        )

        return {
            "data": ([ExperimentsVariantResultsV2DTOData],),
            "meta": (ExperimentsExperimentResultsV2MetaDTO,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ExperimentsVariantResultsV2DTOData],
        meta: Union[ExperimentsExperimentResultsV2MetaDTO, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of variant result resources.

        :param data: Resources returned in this response.
        :type data: [ExperimentsVariantResultsV2DTOData]

        :param meta: Information about when experiment results were updated and whether they are stale.
        :type meta: ExperimentsExperimentResultsV2MetaDTO, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data

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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_data_attributes import (
        ExperimentsRefreshExperimentResultsV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_data_type import (
        ExperimentsRefreshExperimentResultsV2DTODataType,
    )


class ExperimentsRefreshExperimentResultsV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_data_attributes import (
            ExperimentsRefreshExperimentResultsV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_data_type import (
            ExperimentsRefreshExperimentResultsV2DTODataType,
        )

        return {
            "attributes": (ExperimentsRefreshExperimentResultsV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsRefreshExperimentResultsV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsRefreshExperimentResultsV2DTODataType,
        attributes: Union[ExperimentsRefreshExperimentResultsV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the experiment refresh result identity and fields.

        :param attributes: Details of the experiment refresh result.
        :type attributes: ExperimentsRefreshExperimentResultsV2DTODataAttributes, optional

        :param id: ID of the experiment whose results were refreshed.
        :type id: UUID

        :param type: Experiment results refresh resource type.
        :type type: ExperimentsRefreshExperimentResultsV2DTODataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

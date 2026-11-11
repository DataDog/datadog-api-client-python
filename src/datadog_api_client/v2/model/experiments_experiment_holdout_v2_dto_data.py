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
    from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes import (
        ExperimentsExperimentHoldoutV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_type import (
        ExperimentsExperimentHoldoutV2DTODataType,
    )


class ExperimentsExperimentHoldoutV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_attributes import (
            ExperimentsExperimentHoldoutV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_experiment_holdout_v2_dto_data_type import (
            ExperimentsExperimentHoldoutV2DTODataType,
        )

        return {
            "attributes": (ExperimentsExperimentHoldoutV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsExperimentHoldoutV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsExperimentHoldoutV2DTODataType,
        attributes: Union[ExperimentsExperimentHoldoutV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A holdout the experiment is attached to.

        :param attributes: Attributes of a holdout that the experiment is attached to.
        :type attributes: ExperimentsExperimentHoldoutV2DTODataAttributes, optional

        :param id: Identifier of the holdout.
        :type id: UUID

        :param type: Experiment holdout resource type.
        :type type: ExperimentsExperimentHoldoutV2DTODataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

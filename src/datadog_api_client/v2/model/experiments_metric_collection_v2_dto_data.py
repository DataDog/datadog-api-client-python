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
    from datadog_api_client.v2.model.experiments_metric_collection_v2_dto_data_attributes import (
        ExperimentsMetricCollectionV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
        ExperimentsPatchMetricCollectionV2RequestDataType,
    )


class ExperimentsMetricCollectionV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_collection_v2_dto_data_attributes import (
            ExperimentsMetricCollectionV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
            ExperimentsPatchMetricCollectionV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsMetricCollectionV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsPatchMetricCollectionV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsPatchMetricCollectionV2RequestDataType,
        attributes: Union[ExperimentsMetricCollectionV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the metric collection identity and fields.

        :param attributes: Details of the metric collection.
        :type attributes: ExperimentsMetricCollectionV2DTODataAttributes, optional

        :param id: ID of the metric collection.
        :type id: UUID

        :param type: Metric collections resource type.
        :type type: ExperimentsPatchMetricCollectionV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

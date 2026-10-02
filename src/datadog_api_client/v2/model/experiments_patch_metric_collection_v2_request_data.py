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
    from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_attributes import (
        ExperimentsPatchMetricCollectionV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
        ExperimentsPatchMetricCollectionV2RequestDataType,
    )


class ExperimentsPatchMetricCollectionV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_attributes import (
            ExperimentsPatchMetricCollectionV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
            ExperimentsPatchMetricCollectionV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsPatchMetricCollectionV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsPatchMetricCollectionV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ExperimentsPatchMetricCollectionV2RequestDataType,
        attributes: Union[ExperimentsPatchMetricCollectionV2RequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the metric collection identity and fields.

        :param attributes: Fields supplied to update the metric collection.
        :type attributes: ExperimentsPatchMetricCollectionV2RequestDataAttributes, optional

        :param id: ID of the metric collection.
        :type id: str, optional

        :param type: Metric collections resource type.
        :type type: ExperimentsPatchMetricCollectionV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type

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
    from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes import (
        ExperimentsCreateMetricCollectionV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
        ExperimentsPatchMetricCollectionV2RequestDataType,
    )


class ExperimentsCreateMetricCollectionV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes import (
            ExperimentsCreateMetricCollectionV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request_data_type import (
            ExperimentsPatchMetricCollectionV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsCreateMetricCollectionV2RequestDataAttributes,),
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
        attributes: ExperimentsCreateMetricCollectionV2RequestDataAttributes,
        type: ExperimentsPatchMetricCollectionV2RequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metric collection resource to create.

        :param attributes: Name, description, and metric selection for the new collection.
        :type attributes: ExperimentsCreateMetricCollectionV2RequestDataAttributes

        :param id: Optional JSON:API resource identifier field.
        :type id: str, optional

        :param type: Metric collections resource type.
        :type type: ExperimentsPatchMetricCollectionV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

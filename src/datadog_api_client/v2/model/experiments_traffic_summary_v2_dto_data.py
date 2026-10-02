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
    from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto_data_attributes import (
        ExperimentsTrafficSummaryV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto_data_type import (
        ExperimentsTrafficSummaryV2DTODataType,
    )


class ExperimentsTrafficSummaryV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto_data_attributes import (
            ExperimentsTrafficSummaryV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto_data_type import (
            ExperimentsTrafficSummaryV2DTODataType,
        )

        return {
            "attributes": (ExperimentsTrafficSummaryV2DTODataAttributes,),
            "id": (str,),
            "type": (ExperimentsTrafficSummaryV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ExperimentsTrafficSummaryV2DTODataType,
        attributes: Union[ExperimentsTrafficSummaryV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the experiment traffic summary identity and fields.

        :param attributes: Details of the experiment traffic summary.
        :type attributes: ExperimentsTrafficSummaryV2DTODataAttributes, optional

        :param id: Identifier of this traffic summary.
        :type id: str

        :param type: Traffic summary resource type.
        :type type: ExperimentsTrafficSummaryV2DTODataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

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
    from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_attributes import (
        ExperimentsSubjectTypeV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_type import (
        ExperimentsSubjectTypeV2DTODataType,
    )


class ExperimentsSubjectTypeV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_attributes import (
            ExperimentsSubjectTypeV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_type import (
            ExperimentsSubjectTypeV2DTODataType,
        )

        return {
            "attributes": (ExperimentsSubjectTypeV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsSubjectTypeV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsSubjectTypeV2DTODataType,
        attributes: Union[ExperimentsSubjectTypeV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the subject type identity and fields.

        :param attributes: Details of the subject type.
        :type attributes: ExperimentsSubjectTypeV2DTODataAttributes, optional

        :param id: ID of the subject type.
        :type id: UUID

        :param type: Subject types resource type.
        :type type: ExperimentsSubjectTypeV2DTODataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

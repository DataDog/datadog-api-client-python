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
    from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request_data_attributes import (
        ExperimentsPatchSubjectTypeV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_type import (
        ExperimentsSubjectTypeV2DTODataType,
    )


class ExperimentsPatchSubjectTypeV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request_data_attributes import (
            ExperimentsPatchSubjectTypeV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_subject_type_v2_dto_data_type import (
            ExperimentsSubjectTypeV2DTODataType,
        )

        return {
            "attributes": (ExperimentsPatchSubjectTypeV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsSubjectTypeV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsPatchSubjectTypeV2RequestDataAttributes,
        type: ExperimentsSubjectTypeV2DTODataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the subject type identity and fields.

        :param attributes: Fields supplied to update the subject type.
        :type attributes: ExperimentsPatchSubjectTypeV2RequestDataAttributes

        :param id: ID of the subject type.
        :type id: str, optional

        :param type: Subject types resource type.
        :type type: ExperimentsSubjectTypeV2DTODataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.commitments_savings_scalar_response_attributes import (
        CommitmentsSavingsScalarResponseAttributes,
    )
    from datadog_api_client.v2.model.scalar_formula_response_type import ScalarFormulaResponseType


class CommitmentsSavingsScalarResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_savings_scalar_response_attributes import (
            CommitmentsSavingsScalarResponseAttributes,
        )
        from datadog_api_client.v2.model.scalar_formula_response_type import ScalarFormulaResponseType

        return {
            "attributes": (CommitmentsSavingsScalarResponseAttributes,),
            "id": (str,),
            "type": (ScalarFormulaResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CommitmentsSavingsScalarResponseAttributes,
        id: str,
        type: ScalarFormulaResponseType,
        **kwargs,
    ):
        """
        The scalar savings resource.

        :param attributes: Attributes of a scalar savings response.
        :type attributes: CommitmentsSavingsScalarResponseAttributes

        :param id: The identifier of the scalar savings response.
        :type id: str

        :param type: The type of the resource. The value should always be scalar_response.
        :type type: ScalarFormulaResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type

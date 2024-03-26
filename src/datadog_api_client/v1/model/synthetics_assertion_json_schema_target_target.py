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
    from datadog_api_client.v1.model.synthetics_assertion_json_schema_meta_schema import (
        SyntheticsAssertionJSONSchemaMetaSchema,
    )


class SyntheticsAssertionJSONSchemaTargetTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_json_schema_meta_schema import (
            SyntheticsAssertionJSONSchemaMetaSchema,
        )

        return {
            "json_schema": (str,),
            "meta_schema": (SyntheticsAssertionJSONSchemaMetaSchema,),
        }

    attribute_map = {
        "json_schema": "jsonSchema",
        "meta_schema": "metaSchema",
    }

    def __init__(
        self_,
        json_schema: Union[str, UnsetType] = unset,
        meta_schema: Union[SyntheticsAssertionJSONSchemaMetaSchema, UnsetType] = unset,
        **kwargs,
    ):
        """
        Composed target for ``validatesJSONSchema`` operator.

        :param json_schema: The JSON Schema to assert.
        :type json_schema: str, optional

        :param meta_schema: The JSON Schema meta-schema version used in the assertion.
        :type meta_schema: SyntheticsAssertionJSONSchemaMetaSchema, optional
        """
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        if meta_schema is not unset:
            kwargs["meta_schema"] = meta_schema
        super().__init__(kwargs)

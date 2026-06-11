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
    from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
    from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition
    from datadog_api_client.v2.model.upsert_and_publish_form_version_upsert_params import (
        UpsertAndPublishFormVersionUpsertParams,
    )


class UpsertAndPublishFormVersionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
        from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition
        from datadog_api_client.v2.model.upsert_and_publish_form_version_upsert_params import (
            UpsertAndPublishFormVersionUpsertParams,
        )

        return {
            "data_definition": (FormDataDefinition,),
            "ui_definition": (FormUiDefinition,),
            "upsert_params": (UpsertAndPublishFormVersionUpsertParams,),
        }

    attribute_map = {
        "data_definition": "data_definition",
        "ui_definition": "ui_definition",
        "upsert_params": "upsert_params",
    }

    def __init__(
        self_,
        data_definition: FormDataDefinition,
        ui_definition: FormUiDefinition,
        upsert_params: UpsertAndPublishFormVersionUpsertParams,
        **kwargs,
    ):
        """
        The attributes for upserting and publishing a form version.

        :param data_definition: A JSON Schema definition that describes the form's data fields.
        :type data_definition: FormDataDefinition

        :param ui_definition: UI configuration for rendering form fields, including widget overrides, field ordering, and themes.
        :type ui_definition: FormUiDefinition

        :param upsert_params: Concurrency control parameters for the upsert and publish operation.
        :type upsert_params: UpsertAndPublishFormVersionUpsertParams
        """
        super().__init__(kwargs)

        self_.data_definition = data_definition
        self_.ui_definition = ui_definition
        self_.upsert_params = upsert_params

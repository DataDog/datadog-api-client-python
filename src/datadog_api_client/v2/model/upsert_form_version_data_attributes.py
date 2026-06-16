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
    from datadog_api_client.v2.model.form_version_state import FormVersionState
    from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition
    from datadog_api_client.v2.model.upsert_form_version_upsert_params import UpsertFormVersionUpsertParams


class UpsertFormVersionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
        from datadog_api_client.v2.model.form_version_state import FormVersionState
        from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition
        from datadog_api_client.v2.model.upsert_form_version_upsert_params import UpsertFormVersionUpsertParams

        return {
            "data_definition": (FormDataDefinition,),
            "state": (FormVersionState,),
            "ui_definition": (FormUiDefinition,),
            "upsert_params": (UpsertFormVersionUpsertParams,),
        }

    attribute_map = {
        "data_definition": "data_definition",
        "state": "state",
        "ui_definition": "ui_definition",
        "upsert_params": "upsert_params",
    }

    def __init__(
        self_,
        data_definition: FormDataDefinition,
        state: FormVersionState,
        ui_definition: FormUiDefinition,
        upsert_params: UpsertFormVersionUpsertParams,
        **kwargs,
    ):
        """
        The attributes for creating or updating a form version.

        :param data_definition: A JSON Schema definition that describes the form's data fields.
        :type data_definition: FormDataDefinition

        :param state: The state of a form version.
        :type state: FormVersionState

        :param ui_definition: UI configuration for rendering form fields, including widget overrides, field ordering, and themes.
        :type ui_definition: FormUiDefinition

        :param upsert_params: Concurrency control parameters for the form version upsert operation.
        :type upsert_params: UpsertFormVersionUpsertParams
        """
        super().__init__(kwargs)

        self_.data_definition = data_definition
        self_.state = state
        self_.ui_definition = ui_definition
        self_.upsert_params = upsert_params

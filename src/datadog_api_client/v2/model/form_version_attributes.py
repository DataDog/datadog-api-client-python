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
    from datadog_api_client.v2.model.form_version_state import FormVersionState
    from datadog_api_client.v2.model.form_version_upsert_params import FormVersionUpsertParams


class FormVersionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_version_state import FormVersionState
        from datadog_api_client.v2.model.form_version_upsert_params import FormVersionUpsertParams

        return {
            "data_definition": (dict,),
            "state": (FormVersionState,),
            "ui_definition": (dict,),
            "upsert_params": (FormVersionUpsertParams,),
        }

    attribute_map = {
        "data_definition": "data_definition",
        "state": "state",
        "ui_definition": "ui_definition",
        "upsert_params": "upsert_params",
    }

    def __init__(
        self_,
        data_definition: dict,
        ui_definition: dict,
        upsert_params: FormVersionUpsertParams,
        state: Union[FormVersionState, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data_definition: The data definition for the form.
        :type data_definition: dict

        :param state: The state of the form version.
        :type state: FormVersionState, optional

        :param ui_definition: The UI definition for the form.
        :type ui_definition: dict

        :param upsert_params: Parameters for upserting a form version.
        :type upsert_params: FormVersionUpsertParams
        """
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)

        self_.data_definition = data_definition
        self_.ui_definition = ui_definition
        self_.upsert_params = upsert_params

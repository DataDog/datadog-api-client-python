# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
    from datadog_api_client.v2.model.form_version_state import FormVersionState
    from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition


class FormVersionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
        from datadog_api_client.v2.model.form_version_state import FormVersionState
        from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition

        return {
            "created_at": (datetime,),
            "data_definition": (FormDataDefinition,),
            "definition_signature": (str,),
            "etag": (str, none_type),
            "has_ever_been_published": (bool,),
            "id": (str,),
            "modified_at": (datetime,),
            "state": (FormVersionState,),
            "ui_definition": (FormUiDefinition,),
            "user_id": (int,),
            "user_uuid": (UUID,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "data_definition": "data_definition",
        "definition_signature": "definition_signature",
        "etag": "etag",
        "has_ever_been_published": "has_ever_been_published",
        "id": "id",
        "modified_at": "modified_at",
        "state": "state",
        "ui_definition": "ui_definition",
        "user_id": "user_id",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        data_definition: FormDataDefinition,
        definition_signature: str,
        etag: Union[str, none_type],
        modified_at: datetime,
        state: FormVersionState,
        ui_definition: FormUiDefinition,
        user_id: int,
        user_uuid: UUID,
        version: int,
        has_ever_been_published: Union[bool, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a form version.

        :param created_at: The time at which the version was created.
        :type created_at: datetime

        :param data_definition: A JSON Schema definition that describes the form's data fields.
        :type data_definition: FormDataDefinition

        :param definition_signature: The signature of the version definition.
        :type definition_signature: str

        :param etag: The ETag for optimistic concurrency control.
        :type etag: str, none_type

        :param has_ever_been_published: Whether this version number has ever appeared in the form's publication history.
        :type has_ever_been_published: bool, optional

        :param id: The ID of the form version.
        :type id: str, optional

        :param modified_at: The time at which the version was last modified.
        :type modified_at: datetime

        :param state: The state of a form version.
        :type state: FormVersionState

        :param ui_definition: UI configuration for rendering form fields, including widget overrides, field ordering, and themes.
        :type ui_definition: FormUiDefinition

        :param user_id: The ID of the user who created this version.
        :type user_id: int

        :param user_uuid: The UUID of the user who created this version.
        :type user_uuid: UUID

        :param version: The sequential version number.
        :type version: int
        """
        if has_ever_been_published is not unset:
            kwargs["has_ever_been_published"] = has_ever_been_published
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.data_definition = data_definition
        self_.definition_signature = definition_signature
        self_.etag = etag
        self_.modified_at = modified_at
        self_.state = state
        self_.ui_definition = ui_definition
        self_.user_id = user_id
        self_.user_uuid = user_uuid
        self_.version = version

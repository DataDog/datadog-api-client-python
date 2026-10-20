# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class PatchSavedFilterForbiddenResponse(ModelComposed):
    def __init__(self, **kwargs):
        """
        An authentication or permission error, or a resource listing consumer flags that the caller cannot edit.

        :param errors: The authorization error messages.
        :type errors: [str]

        :param data: The caller lacks edit permission on one or more feature flags that reference this saved filter.
        :type data: SavedFilterPermissionDeniedData
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.saved_filter_api_error_response import SavedFilterAPIErrorResponse
        from datadog_api_client.v2.model.saved_filter_jsonapi_error_response import SavedFilterJSONAPIErrorResponse
        from datadog_api_client.v2.model.saved_filter_permission_denied_response import (
            SavedFilterPermissionDeniedResponse,
        )

        return {
            "oneOf": [
                SavedFilterAPIErrorResponse,
                SavedFilterJSONAPIErrorResponse,
                SavedFilterPermissionDeniedResponse,
            ],
        }

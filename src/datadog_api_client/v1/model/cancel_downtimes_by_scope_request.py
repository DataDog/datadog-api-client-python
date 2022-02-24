# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class CancelDowntimesByScopeRequest(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "scope": (str,),
        }

    attribute_map = {
        "scope": "scope",
    }

    read_only_vars = {}

    def __init__(self, scope, *args, **kwargs):
        """
        Cancel downtimes according to scope.

        :param scope: The scope(s) to which the downtime applies. For example, `host:app2`.
            Provide multiple scopes as a comma-separated list like `env:dev,env:prod`.
            The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
        :type scope: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.scope = scope

    @classmethod
    def _from_openapi_data(cls, scope, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CancelDowntimesByScopeRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.scope = scope
        return self

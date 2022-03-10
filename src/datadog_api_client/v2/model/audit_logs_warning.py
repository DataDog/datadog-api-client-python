# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuditLogsWarning(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "detail": (str,),
            "title": (str,),
        }

    attribute_map = {
        "code": "code",
        "detail": "detail",
        "title": "title",
    }

    def __init__(self, *args, **kwargs):
        """
        Warning message indicating something that went wrong with the query.

        :param code: Unique code for this type of warning.
        :type code: str, optional

        :param detail: Detailed explanation of this specific warning.
        :type detail: str, optional

        :param title: Short human-readable summary of the warning.
        :type title: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuditLogsWarning, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

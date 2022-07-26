# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class AccessRole(ModelSimple):
    """
    The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user).

    :param value: If omitted defaults to "st". Must be one of ["st", "adm", "ro", "ERROR"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "STANDARD": "st",
            "ADMIN": "adm",
            "READ_ONLY": "ro",
            "ERROR": "ERROR",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

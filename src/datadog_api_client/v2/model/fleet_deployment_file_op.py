# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetDeploymentFileOp(ModelSimple):
    """
    Type of file operation to perform on the target configuration file.
        - `merge-patch`: Merges the provided patch data with the existing configuration file.
          Creates the file if it doesn't exist.
        - `delete`: Removes the specified configuration file from the target hosts.

    :param value: Must be one of ["merge-patch", "delete"].
    :type value: str
    """

    allowed_values = {
        "merge-patch",
        "delete",
    }
    MERGE_PATCH: ClassVar["FleetDeploymentFileOp"]
    DELETE: ClassVar["FleetDeploymentFileOp"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetDeploymentFileOp.MERGE_PATCH = FleetDeploymentFileOp("merge-patch")
FleetDeploymentFileOp.DELETE = FleetDeploymentFileOp("delete")

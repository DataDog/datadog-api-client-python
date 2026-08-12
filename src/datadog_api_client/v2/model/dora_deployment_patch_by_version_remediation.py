# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DORADeploymentPatchByVersionRemediation(ModelComposed):
    def __init__(self, **kwargs):
        """
        Remediation details for the deployment. Optional, but required to calculate failed deployment recovery time. Specify either ``id`` or ``version`` to identify the remediation deployment, but not both.

        :param id: The ID of the remediation deployment.
        :type id: str

        :param type: The type of remediation action taken. Required when the failed deployment must be linked to a remediation deployment.
        :type type: DORADeploymentPatchRemediationType

        :param version: The version of the remediation deployment.
        :type version: str
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
        from datadog_api_client.v2.model.dora_deployment_patch_by_version_remediation_by_id import (
            DORADeploymentPatchByVersionRemediationByID,
        )
        from datadog_api_client.v2.model.dora_deployment_patch_by_version_remediation_by_version import (
            DORADeploymentPatchByVersionRemediationByVersion,
        )

        return {
            "oneOf": [
                DORADeploymentPatchByVersionRemediationByID,
                DORADeploymentPatchByVersionRemediationByVersion,
            ],
        }

#!/usr/bin/env python
"""
file: v3
author: adh
created_at: 9/20/23 2:30 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcDecisionPointValue
from ssvc.dp_groups.base import SsvcDecisionPointGroup
from ssvc.decision_points.cvss.attack_complexity import (
    ATTACK_COMPLEXITY_1,
)
from ssvc.decision_points.cvss.attack_vector import ATTACK_VECTOR_1
from ssvc.decision_points.cvss.availability_impact import (
    AVAILABILITY_IMPACT_2,
)
from ssvc.decision_points.cvss.availability_requirement import (
    AVAILABILITY_REQUIREMENT_1,
)
from ssvc.decision_points.cvss.confidentiality_impact import (
    CONFIDENTIALITY_IMPACT_2,
)
from ssvc.decision_points.cvss.confidentiality_requirement import (
    CONFIDENTIALITY_REQUIREMENT_1,
)
from ssvc.decision_points.cvss.exploitability import (
    EXPLOIT_CODE_MATURITY_1_1_1,
)
from ssvc.decision_points.cvss.integrity_impact import (
    INTEGRITY_IMPACT_2,
)
from ssvc.decision_points.cvss.integrity_requirement import (
    INTEGRITY_REQUIREMENT_1,
)
from ssvc.decision_points.cvss.privileges_required import (
    PRIVILEGES_REQUIRED_1,
)
from ssvc.decision_points.cvss.remediation_level import (
    REMEDIATION_LEVEL_1_1,
)
from ssvc.decision_points.cvss.report_confidence import (
    REPORT_CONFIDENCE_2,
)
from ssvc.decision_points.cvss.scope import SCOPE_1 as SCOPE
from ssvc.decision_points.cvss.user_interaction import (
    USER_INTERACTION_1,
)


def _modify(obj):
    """
    Prepends "Modified " to the name and "M" to the key of the given object. Also adds a value of "Not Defined" to the
    values list.
    :param obj: the object to modify
    :return: the object
    """
    o = deepcopy(obj)
    o.name = "Modified " + o.name
    o.key = "M" + o.key
    nd = SsvcDecisionPointValue(
        name="Not Defined", key="ND", description="Ignore this value"
    )
    values = list(o.values)
    values.append(nd)
    o.values = tuple(values)
    return o


MODIFIED_ATTACK_VECTOR = _modify(ATTACK_VECTOR_1)
MODIFIED_ATTACK_COMPLEXITY = _modify(ATTACK_COMPLEXITY_1)
MODIFIED_PRIVILEGES_REQUIRED = _modify(PRIVILEGES_REQUIRED_1)
MODIFIED_USER_INTERACTION = _modify(USER_INTERACTION_1)
MODIFIED_SCOPE = _modify(SCOPE)
MODIFIED_CONFIDENTIALITY_IMPACT = _modify(CONFIDENTIALITY_IMPACT_2)
MODIFIED_INTEGRITY_IMPACT = _modify(INTEGRITY_IMPACT_2)
MODIFIED_AVAILABILITY_IMPACT = _modify(AVAILABILITY_IMPACT_2)


CVSSv3 = SsvcDecisionPointGroup(
    name="CVSS Version 3",
    description="The Common Vulnerability Scoring System (CVSS) is a free and open industry standard for assessing the severity of computer system security vulnerabilities. CVSS attempts to assign severity scores to vulnerabilities, allowing responders to prioritize responses and resources according to threat. Scores are calculated based on a formula that depends on several metrics that approximate ease of exploit and the impact of exploit. Scores range from 0 to 10, with 10 being the most severe.",
    version="3.0",
    decision_points=[
        ATTACK_VECTOR_1,
        ATTACK_COMPLEXITY_1,
        PRIVILEGES_REQUIRED_1,
        USER_INTERACTION_1,
        SCOPE,
        CONFIDENTIALITY_IMPACT_2,
        INTEGRITY_IMPACT_2,
        AVAILABILITY_IMPACT_2,
        EXPLOIT_CODE_MATURITY_1_1_1,
        REMEDIATION_LEVEL_1_1,
        REPORT_CONFIDENCE_2,
        CONFIDENTIALITY_REQUIREMENT_1,
        INTEGRITY_REQUIREMENT_1,
        AVAILABILITY_REQUIREMENT_1,
        MODIFIED_ATTACK_VECTOR,
        MODIFIED_ATTACK_COMPLEXITY,
        MODIFIED_PRIVILEGES_REQUIRED,
        MODIFIED_USER_INTERACTION,
        MODIFIED_SCOPE,
        MODIFIED_CONFIDENTIALITY_IMPACT,
        MODIFIED_INTEGRITY_IMPACT,
        MODIFIED_AVAILABILITY_IMPACT,
    ],
)


def main():
    print(CVSSv3.to_json(indent=2))


if __name__ == "__main__":
    main()
